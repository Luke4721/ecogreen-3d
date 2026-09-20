import * as THREE from 'three';

// --- 1. Lenis Smooth Scrolling Setup ---
const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smooth: true
});

lenis.on('scroll', ScrollTrigger.update);

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);

// --- 2. Counters & Reveals Animation ---
const counters = document.querySelectorAll('.counter-val');
const counterObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const el = entry.target;
            const target = parseFloat(el.getAttribute('data-target'));
            const suffix = el.getAttribute('data-suffix') || '';
            const duration = 2000;
            let startTime = null;
            const animateCounter = (currentTime) => {
                if (!startTime) startTime = currentTime;
                const progress = Math.min((currentTime - startTime) / duration, 1);
                const ease = 1 - Math.pow(1 - progress, 4);
                const current = (target * ease);
                el.innerText = (current % 1 !== 0 ? current.toFixed(1) : Math.floor(current)) + suffix;
                
                if (progress < 1) requestAnimationFrame(animateCounter);
                else el.innerText = target + suffix;
            };
            requestAnimationFrame(animateCounter);
            obs.unobserve(el);
        }
    });
});
counters.forEach(c => counterObserver.observe(c));

const revealElements = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });
revealElements.forEach(el => revealObserver.observe(el));

// --- 3. Three.js Voxel Palm Tree System ---
const canvas = document.getElementById('webgl-canvas');
const isMobile = window.innerWidth < 768;
const DPR = isMobile ? 1 : Math.min(window.devicePixelRatio, 1.5);

const scene = new THREE.Scene();
scene.background = new THREE.Color('#0B1F18');
// Subtle fog for depth
scene.fog = new THREE.FogExp2(0x0B1F18, 0.004);

const camera = new THREE.PerspectiveCamera(40, window.innerWidth / window.innerHeight, 0.1, 500);
camera.position.set(0, 24, 75);

const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: !isMobile, powerPreference: 'high-performance' });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(DPR);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

// Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.2);
scene.add(ambientLight);

const keyLight = new THREE.DirectionalLight(0x10B981, 1.8);
keyLight.position.set(30, 80, 40);
keyLight.castShadow = true;
keyLight.shadow.mapSize.width = 1024;
keyLight.shadow.mapSize.height = 1024;
keyLight.shadow.bias = -0.001;
scene.add(keyLight);

const fillLight = new THREE.DirectionalLight(0x064E3B, 1.0);
fillLight.position.set(-30, 20, -30);
scene.add(fillLight);

// Simplex Noise
class SimplexNoise {
    constructor() {
        this.p = new Uint8Array(512);
        for (let i = 0; i < 512; i++) this.p[i] = Math.floor(Math.random() * 256);
        this.g = [[1,1],[-1,1],[1,-1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1]];
    }
    noise2D(x, y) {
        const F2 = 0.5 * (Math.sqrt(3) - 1), G2 = (3 - Math.sqrt(3)) / 6;
        const s = (x + y) * F2;
        const i = Math.floor(x + s), j = Math.floor(y + s);
        const t = (i + j) * G2;
        const x0 = x - (i - t), y0 = y - (j - t);
        let i1, j1; if (x0 > y0) { i1 = 1; j1 = 0; } else { i1 = 0; j1 = 1; }
        const x1 = x0 - i1 + G2, y1 = y0 - j1 + G2;
        const x2 = x0 - 1 + 2 * G2, y2 = y0 - 1 + 2 * G2;
        const ii = i & 255, jj = j & 255;
        const gi = (a) => this.g[this.p[a] & 7];
        let n0 = 0, n1 = 0, n2 = 0;
        let tt = 0.5 - x0 * x0 - y0 * y0;
        if (tt > 0) { tt *= tt; const gg = gi(ii + this.p[jj]); n0 = tt * tt * (gg[0] * x0 + gg[1] * y0); }
        tt = 0.5 - x1 * x1 - y1 * y1;
        if (tt > 0) { tt *= tt; const gg = gi(ii + i1 + this.p[jj + j1]); n1 = tt * tt * (gg[0] * x1 + gg[1] * y1); }
        tt = 0.5 - x2 * x2 - y2 * y2;
        if (tt > 0) { tt *= tt; const gg = gi(ii + 1 + this.p[jj + 1]); n2 = tt * tt * (gg[0] * x2 + gg[1] * y2); }
        return 70 * (n0 + n1 + n2);
    }
}
const noise = new SimplexNoise();
function fbm(x, y, octaves = 4) {
    let v = 0, a = 0.5, f = 1;
    for(let i=0; i<octaves; i++) {
        v += a * noise.noise2D(x * f, y * f);
        f *= 2; a *= 0.5;
    }
    return v;
}

// Generate Palm Tree Structure (Ported from oxigen.sa)
function buildEmblemPalm(res) {
  res = Math.max(20, res | 0);
  const HEIGHT = 15, vs = HEIGHT / res;
  const frondCount = 17, fanSpread = 360, frondLen = 100, frondCurl = 30, serration = 60, pack = 78;
  const voxSet = new Set(), vox = [];
  const vkey = (i, j, k) => i + '|' + j + '|' + k;
  function addVox(i, j, k) { const kk = vkey(i, j, k); if (!voxSet.has(kk)) { voxSet.add(kk); vox.push([i, j, k]); } }
  function addP(x, y, z) { addVox(Math.round(x / vs), Math.round(y / vs), Math.round(z / vs)); }
  function ball(x, y, z, rW) {
    const r = Math.round(rW / vs), ci = Math.round(x / vs), cj = Math.round(y / vs), ck = Math.round(z / vs);
    for (let i = -r; i <= r; i++) for (let j = -r; j <= r; j++) for (let k = -r; k <= r; k++)
      if (i * i + j * j + k * k <= r * r + 0.6) addVox(ci + i, cj + j, ck + k);
  }
  function seg(ax, ay, az, bx, by, bz) {
    const dx = bx - ax, dy = by - ay, dz = bz - az, L = Math.hypot(dx, dy, dz), n = Math.max(1, Math.ceil(L / (vs * 0.7)));
    for (let s = 0; s <= n; s++) { const t = s / n; addP(ax + dx * t, ay + dy * t, az + dz * t); }
  }
  const cy = 3.9, crossY = -2.4;
  // trunk: round 3D column, gently tapered
  const trunkTop = cy - 0.25, trunkBot = crossY - 0.2;
  for (let y = trunkBot; y <= trunkTop; y += vs * 0.85) {
    const tt = (y - trunkBot) / (trunkTop - trunkBot);
    const rad = 0.50 - 0.16 * tt;
    const ri = Math.ceil(rad / vs), cj = Math.round(y / vs);
    for (let i = -ri; i <= ri; i++) for (let k = -ri; k <= ri; k++) {
      const xx = i * vs, zz = k * vs; if (xx * xx + zz * zz <= rad * rad) addVox(i, cj, k);
    }
  }
  // crown hub
  ball(0, cy, 0, 0.42);
  // fronds
  const spread = fanSpread * Math.PI / 180;
  const full = spread >= 2 * Math.PI - 0.02;
  const baseLen = 4.0 * (frondLen / 100);
  const bendK = 0.55 + 0.9 * (frondCurl / 100);
  const serr = serration / 100;
  const tiers = [
    { a0: 90, bend: 54, lenK: 0.84, nK: 0.42 },
    { a0: 85, bend: 70, lenK: 0.98, nK: 0.60 },
    { a0: 78, bend: 82, lenK: 1.10, nK: 0.80 },
    { a0: 68, bend: 88, lenK: 1.18, nK: 0.92 },
    { a0: 56, bend: 90, lenK: 1.22, nK: 1.00 },
    { a0: 43, bend: 88, lenK: 1.18, nK: 0.96 },
    { a0: 30, bend: 84, lenK: 1.12, nK: 0.90 }
  ];
  const leafGap = Math.max(1, Math.round(1 + serr * 2));
  const VSTRETCH = 1.55;
  let cseed = 98765; const crnd = () => { cseed = (cseed * 1103515245 + 12345) & 0x7fffffff; return cseed / 0x7fffffff; };
  function frond(az, a0deg, bendDeg, len, bx, by, bz, wK, upK, fwd) {
    const ox = Math.sin(az), oz = Math.cos(az);
    const sx = oz, sz = -ox;
    const a0 = a0deg * Math.PI / 180, bend = bendDeg * Math.PI / 180 * bendK;
    const steps = Math.max(8, Math.ceil(len / vs));
    const dl = len / steps;
    const sPhase = (crnd() * leafGap) | 0;
    let hx = 0, vy = 0;
    for (let s = 0; s <= steps; s++) {
      const t = s / steps;
      const a = a0 - bend * Math.pow(t, 1.35);
      if (s > 0) { hx += Math.cos(a) * dl; vy += Math.sin(a) * dl * VSTRETCH; }
      const px = bx + ox * hx, py = by + vy, pz = bz + oz * hx;
      addP(px, py, pz);
      addP(px, py - vs, pz);
      const wmax = len * wK;
      const w = Math.max(0, Math.sin(Math.pow(t, 0.78) * Math.PI)) * wmax * (0.6 + 0.4 * (1 - t));
      if (w <= vs) continue;
      const doLeaf = serr <= 0 || (s + sPhase) % leafGap === 0;
      if (doLeaf) {
        for (let side = -1; side <= 1; side += 2) {
          const ex = px + sx * side * w + ox * w * fwd, ez = pz + sz * side * w + oz * w * fwd, ey = py + w * upK;
          seg(px, py, pz, ex, ey, ez);
        }
      }
    }
  }
  tiers.forEach((ti, idx) => {
    const n = Math.max(3, Math.round(frondCount * ti.nK));
    const azStep = (full ? 2 * Math.PI : spread) / n;
    for (let i = 0; i < n; i++) {
      let az0 = full ? 2 * Math.PI * (i / n) + idx * 0.5
                     : (n === 1 ? 0 : spread * (i / (n - 1)) - spread / 2) + idx * 0.18;
      const az = az0 + (crnd() - 0.5) * azStep * 1.1;
      const a0 = ti.a0 + (crnd() - 0.5) * 18;
      const bend = ti.bend + (crnd() - 0.5) * 26;
      const len = baseLen * ti.lenK * (0.80 + crnd() * 0.42);
      const bx = (crnd() - 0.5) * 0.7, bz = (crnd() - 0.5) * 0.7, by = cy + (crnd() - 0.5) * 0.7;
      const wK = 0.20 + crnd() * 0.06;
      const upK = 0.26 + crnd() * 0.14, fwd = 0.34 + crnd() * 0.16;
      frond(az, a0, bend, len, bx, by, bz, wK, upK, fwd);
    }
  });

  // local → world
  let minX = 1e9, maxX = -1e9, minY = 1e9, maxY = -1e9, minZ = 1e9, maxZ = -1e9;
  for (const v of vox) {
    const x = v[0] * vs, y = v[1] * vs, z = v[2] * vs;
    if (x < minX) minX = x; if (x > maxX) maxX = x;
    if (y < minY) minY = y; if (y > maxY) maxY = y;
    if (z < minZ) minZ = z; if (z > maxZ) maxZ = z;
  }
  const localH = (maxY - minY) || 1;
  const TARGET_H = 48; // palm height
  const BASE_Y = -1.5; // root the trunk slightly into the sand
  const scale = TARGET_H / localH;
  const cX = (minX + maxX) / 2, cZ = (minZ + maxZ) / 2;
  const localCube = vs * (pack / 100) * 0.96;

  const positions = [];
  for (const v of vox) {
    positions.push((v[0] * vs - cX) * scale, (v[1] * vs - minY) * scale + BASE_Y, (v[2] * vs - cZ) * scale);
  }
  return { positions, cubeSize: localCube * scale };
}

// Generate Data
const res = isMobile ? 60 : 110; 
const palmData = buildEmblemPalm(res);
const treeVoxels = palmData.positions.length / 3;

const allVoxels = [];

// Ground Generation (Desert floor style)
const groundCell = palmData.cubeSize * 2.0; 
const gridRadius = 140;

for (let x = -gridRadius; x <= gridRadius; x += groundCell) {
    for (let z = -gridRadius; z <= gridRadius; z += groundCell) {
        const d = Math.hypot(x, z);
        
        // Skip the very center where the trunk goes
        if (d < 5) continue;

        // Base terrain height with noise
        let h = fbm(x * 0.012, z * 0.012, 4) * 9.0;
        h += fbm(x * 0.045 + 10, z * 0.045 - 7, 3) * 2.2;
        
        // Quantize height to match the voxel style
        h = Math.floor(h / groundCell) * groundCell;
        
        // Push the top ground layer
        allVoxels.push({ x: x, y: h, z: z, type: 'ground' });
        
        // We only add inner layers if they would be visible (near center or edges), 
        // to save performance. A simplified ground looks great.
        if (Math.random() > 0.5) {
            allVoxels.push({ x: x, y: h - groundCell, z: z, type: 'ground_deep' });
        }
    }
}

// Add the tree voxels
for (let i = 0; i < treeVoxels; i++) {
    allVoxels.push({
        x: palmData.positions[i * 3],
        y: palmData.positions[i * 3 + 1],
        z: palmData.positions[i * 3 + 2],
        type: 'tree'
    });
}

// Create InstancedMesh
const boxGeo = new THREE.BoxGeometry(palmData.cubeSize, palmData.cubeSize, palmData.cubeSize);
const voxelMat = new THREE.MeshStandardMaterial({
    color: 0xffffff, // We use instance colors
    roughness: 0.9,
    metalness: 0.1
});

const instancedMesh = new THREE.InstancedMesh(boxGeo, voxelMat, allVoxels.length);
instancedMesh.castShadow = true;
instancedMesh.receiveShadow = true;

const dummy = new THREE.Object3D();
const colors = new Float32Array(allVoxels.length * 3);
const colorObj = new THREE.Color();

for(let i=0; i<allVoxels.length; i++) {
    const v = allVoxels[i];
    
    // The ground cells are larger, so scale them up relative to tree cells
    if (v.type.includes('ground')) {
        dummy.scale.setScalar(2.0); 
    } else {
        dummy.scale.setScalar(1.0);
    }
    
    dummy.position.set(v.x, v.y, v.z);
    dummy.updateMatrix();
    instancedMesh.setMatrixAt(i, dummy.matrix);
    
    // Assign Colors based on type
    if (v.type === 'tree') {
        colorObj.setHex(0x10B981); // Emerald green for tree
    } else if (v.type === 'ground') {
        colorObj.setHex(0x064E3B); // Darker green for ground
    } else {
        colorObj.setHex(0x022c22); // Deepest green for ground base
    }
    
    colors[i*3] = colorObj.r;
    colors[i*3+1] = colorObj.g;
    colors[i*3+2] = colorObj.b;
}
instancedMesh.instanceColor = new THREE.InstancedBufferAttribute(colors, 3);
scene.add(instancedMesh);

// Custom Vertex Shader for Voxel Interaction & Animation
const uniforms = {
    uTime: { value: 0 },
    uCursor: { value: new THREE.Vector2(9999, 9999) },
    uCursorStr: { value: 0 },
    uSwayAmp: { value: 1.0 },
    uWindDir: { value: new THREE.Vector2(1.0, 0.3) },
    uWindFreq: { value: 0.7 }
};

voxelMat.onBeforeCompile = (shader) => {
    shader.uniforms.uTime = uniforms.uTime;
    shader.uniforms.uCursor = uniforms.uCursor;
    shader.uniforms.uCursorStr = uniforms.uCursorStr;
    shader.uniforms.uSwayAmp = uniforms.uSwayAmp;
    shader.uniforms.uWindDir = uniforms.uWindDir;
    shader.uniforms.uWindFreq = uniforms.uWindFreq;

    shader.vertexShader = `
        uniform float uTime;
        uniform vec2 uCursor;
        uniform float uCursorStr;
        uniform float uSwayAmp;
        uniform vec2 uWindDir;
        uniform float uWindFreq;
        ${shader.vertexShader}
    `.replace(
        '#include <project_vertex>',
        `
        #ifdef USE_INSTANCING
            vec3 iPos = instanceMatrix[3].xyz;
            
            // Tree wind sway (only affects tree height > 18)
            float crown = smoothstep(18.0, 46.0, iPos.y);
            float reach = length(iPos.xz);
            float ph = uTime * uWindFreq + iPos.y * 0.12 + reach * 0.08;
            float gust = 0.72 + 0.28 * sin(uTime * 0.37);
            float sway = sin(ph) * uSwayAmp * crown * (0.35 + reach * 0.05) * gust;
            
            transformed.x += sway * uWindDir.x;
            transformed.z += sway * uWindDir.y;
            transformed.y += abs(sin(ph)) * uSwayAmp * crown * reach * 0.012;
            
            // Cursor wake displacement (scattering slightly)
            if (uCursorStr > 0.0) {
                float dist = distance(iPos.xz, uCursor);
                float radius = 18.0;
                float gate = 1.0 - smoothstep(6.0, 16.0, iPos.y); // Ground + lower trunk only
                if (dist < radius) {
                    float pool = smoothstep(radius, 0.0, dist);
                    pool *= pool; 
                    float wake = pool * uCursorStr * 1.8 * gate;
                    wake += sin(dist * 0.5 - uTime * 2.6) * pool * uCursorStr * 0.22 * gate;
                    transformed.y += wake;
                }
            }
        #endif
        #include <project_vertex>
        `
    );
};

// Pointer Interaction
const pointer = new THREE.Vector2();
const raycaster = new THREE.Raycaster();
const groundPlane = new THREE.Plane(new THREE.Vector3(0, 1, 0), 0);
const hitPoint = new THREE.Vector3();
let pointerActive = false;
let targetCursorStr = 0;

const onPointerMove = (e) => {
    let clientX = e.clientX;
    let clientY = e.clientY;
    if (e.touches && e.touches.length > 0) {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
    }
    pointer.x = (clientX / window.innerWidth) * 2 - 1;
    pointer.y = -(clientY / window.innerHeight) * 2 + 1;
    pointerActive = true;
};

if (!isMobile) {
    window.addEventListener('pointermove', onPointerMove, { passive: true });
    window.addEventListener('pointerout', () => pointerActive = false);
} else {
    window.addEventListener('touchmove', onPointerMove, { passive: true });
    window.addEventListener('touchend', () => pointerActive = false);
}

// Initial Camera Animation (Orbiting slowly)
const cameraProxy = { angle: 0, height: 24, radius: 100 };

// Link scroll position to camera orbit like oxigen.sa
gsap.to(cameraProxy, {
    angle: Math.PI * 0.35, 
    height: 40,           
    radius: 55,           
    ease: "none",
    scrollTrigger: {
        trigger: "body",
        start: "top top",
        end: "bottom bottom",
        scrub: 1.0
    }
});

const clock = new THREE.Clock();

function animate() {
    requestAnimationFrame(animate);
    
    const time = clock.getElapsedTime();
    uniforms.uTime.value = time;

    // Update cursor interaction
    if (pointerActive) {
        raycaster.setFromCamera(pointer, camera);
        if (raycaster.ray.intersectPlane(groundPlane, hitPoint)) {
            uniforms.uCursor.value.lerp(new THREE.Vector2(hitPoint.x, hitPoint.z), 0.2);
            targetCursorStr = 1.0;
        }
    } else {
        targetCursorStr = 0.0;
    }
    uniforms.uCursorStr.value += (targetCursorStr - uniforms.uCursorStr.value) * 0.1;

    // Apply Camera Proxy to real camera
    camera.position.x = Math.sin(cameraProxy.angle) * cameraProxy.radius;
    camera.position.z = Math.cos(cameraProxy.angle) * cameraProxy.radius;
    camera.position.y = cameraProxy.height;
    
    // Look at center of tree
    camera.lookAt(0, 22, 0);

    renderer.render(scene, camera);
}
animate();

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
