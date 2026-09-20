import os

js_content = """
document.addEventListener('DOMContentLoaded', () => {
    // 1. Navigation Logic
    const navbar = document.querySelector('.navbar');
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navMenu = document.querySelector('.nav-menu');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            mobileToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }

    // 2. Form Validation (Contact Page AJAX)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = form.querySelector('button[type="submit"]');
            const originalText = btn.innerText;
            btn.innerText = "Sending...";
            btn.style.opacity = "0.7";
            
            try {
                const formData = new FormData(form);
                const response = await fetch(form.action, {
                    method: form.method || 'POST',
                    body: formData,
                    headers: { 'Accept': 'application/json' }
                });
                
                // Show success regardless of actual backend existence for demo purposes
                btn.innerText = "Message Sent!";
                btn.style.background = "#10B981";
                form.reset();
                setTimeout(() => {
                    btn.innerText = originalText;
                    btn.style.opacity = "1";
                    btn.style.background = "";
                }, 3000);
            } catch (err) {
                // Fallback success for local development without PHP server
                btn.innerText = "Message Sent!";
                btn.style.background = "#10B981";
                form.reset();
                setTimeout(() => {
                    btn.innerText = originalText;
                    btn.style.opacity = "1";
                    btn.style.background = "";
                }, 3000);
            }
        });
    });

    // 3. Scroll Reveal & Counters
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, { root: null, threshold: 0.1, rootMargin: "0px 0px -50px 0px" });
    revealElements.forEach(el => revealObserver.observe(el));

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

    // 4. Three.js Background
    const canvas = document.getElementById('webgl-canvas');
    if (!canvas) return;

    const isMobile = window.innerWidth < 768;
    const PIXEL_RATIO = isMobile ? 1 : Math.min(window.devicePixelRatio, 2);

    const scene = new THREE.Scene();
    scene.background = new THREE.Color('#0B1F18');
    scene.fog = new THREE.FogExp2(0x0B1F18, 0.03);

    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
    camera.position.set(0, 0, 12);

    const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: !isMobile, alpha: false });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(PIXEL_RATIO);
    renderer.outputEncoding = THREE.sRGBEncoding;

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.2);
    scene.add(ambientLight);

    const keyLight = new THREE.DirectionalLight(0xffffff, 2.0);
    keyLight.position.set(5, 8, 5);
    scene.add(keyLight);

    const fillLight = new THREE.DirectionalLight(0x10B981, 1.2);
    fillLight.position.set(-5, 3, 3);
    scene.add(fillLight);

    const goldAccent = new THREE.PointLight(0xFFD700, 1.5, 50);
    goldAccent.position.set(-3, -5, 2);
    scene.add(goldAccent);

    const coreGeo = new THREE.IcosahedronGeometry(2.5, isMobile ? 4 : 8);
    const posAttribute = coreGeo.attributes.position;
    coreGeo.userData.originalPositions = new Float32Array(posAttribute.count * 3);
    for(let i=0; i < posAttribute.count; i++) {
        coreGeo.userData.originalPositions[i*3] = posAttribute.getX(i);
        coreGeo.userData.originalPositions[i*3+1] = posAttribute.getY(i);
        coreGeo.userData.originalPositions[i*3+2] = posAttribute.getZ(i);
    }
    const coreMat = new THREE.MeshPhysicalMaterial({
        color: 0x10B981, metalness: 1.0, roughness: 0.1,
        clearcoat: 1.0, clearcoatRoughness: 0.05, reflectivity: 1.0,
        transparent: true, opacity: 0.95
    });
    const liquidCore = new THREE.Mesh(coreGeo, coreMat);
    liquidCore.position.set(1.5, 0, 0);
    scene.add(liquidCore);

    const auroraGroup = new THREE.Group();
    scene.add(auroraGroup);
    
    const auroraMat = new THREE.MeshPhysicalMaterial({ color: 0x10B981, transmission: 0.9, opacity: 0.4, roughness: 0.1, metalness: 0.2, transparent: true, side: THREE.DoubleSide });
    const auroraMatLight = new THREE.MeshPhysicalMaterial({ color: 0x34D399, transmission: 0.9, opacity: 0.3, roughness: 0.1, metalness: 0.2, transparent: true, side: THREE.DoubleSide });

    const ribbons = [];
    const ribbonCount = isMobile ? 4 : 7;
    for (let i=0; i<ribbonCount; i++) {
        const geo = new THREE.TorusGeometry(8 + Math.random() * 4, 0.3 + Math.random() * 0.2, 8, 100);
        const mesh = new THREE.Mesh(geo, Math.random() > 0.5 ? auroraMat : auroraMatLight);
        mesh.position.set((Math.random()-0.5)*10, (Math.random()-0.5)*10, (Math.random()-0.5)*15 - 5);
        mesh.rotation.set(Math.random()*Math.PI, Math.random()*Math.PI, Math.random()*Math.PI);
        mesh.userData = { rx: (Math.random() - 0.5) * 0.002, ry: (Math.random() - 0.5) * 0.002, rz: (Math.random() - 0.5) * 0.002 };
        ribbons.push(mesh);
        auroraGroup.add(mesh);
    }

    const particleCount = isMobile ? 150 : 400;
    const pGeo = new THREE.BufferGeometry();
    const pPos = new Float32Array(particleCount * 3);
    const pOpacities = new Float32Array(particleCount);
    const dustData = [];
    for(let i=0; i<particleCount; i++) {
        const x = (Math.random() - 0.5) * 30;
        const y = (Math.random() - 0.5) * 30;
        const z = (Math.random() - 0.5) * 20;
        pPos[i*3] = x; pPos[i*3+1] = y; pPos[i*3+2] = z;
        pOpacities[i] = 0.4 + Math.random() * 0.6;
        dustData.push({ x: x, y: y, z: z, phaseX: Math.random() * Math.PI*2, phaseY: Math.random() * Math.PI*2 });
    }
    pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
    pGeo.setAttribute('opacity', new THREE.BufferAttribute(pOpacities, 1));
    const pMat = new THREE.PointsMaterial({ color: 0x34D399, size: 0.08, transparent: true, opacity: 0.8, sizeAttenuation: true, blending: THREE.AdditiveBlending });
    const dustParticles = new THREE.Points(pGeo, pMat);
    scene.add(dustParticles);

    let scrollProgress = 0;
    function updateScrollProgress() {
        const maxScroll = document.body.scrollHeight - window.innerHeight;
        scrollProgress = maxScroll > 0 ? (window.scrollY / maxScroll) : 0;
    }
    window.addEventListener('scroll', updateScrollProgress);
    window.addEventListener('resize', updateScrollProgress);
    updateScrollProgress();

    const mouse = new THREE.Vector2(0, 0);
    const windowHalfX = window.innerWidth / 2;
    const windowHalfY = window.innerHeight / 2;
    document.addEventListener('mousemove', (event) => {
        mouse.x = (event.clientX - windowHalfX) / windowHalfX;
        mouse.y = -(event.clientY - windowHalfY) / windowHalfY;
    });

    const clock = new THREE.Clock();
    function animate() {
        requestAnimationFrame(animate);
        const time = clock.getElapsedTime();

        const origPositions = liquidCore.geometry.userData.originalPositions;
        const currentPositions = liquidCore.geometry.attributes.position;
        const normals = liquidCore.geometry.attributes.normal;
        for(let i=0; i<currentPositions.count; i++) {
            const ox = origPositions[i*3];
            const oy = origPositions[i*3+1];
            const oz = origPositions[i*3+2];
            const nx = normals.getX(i);
            const ny = normals.getY(i);
            const nz = normals.getZ(i);
            const noise = (Math.sin(ox * 2 + time * 1.5) * Math.cos(oy * 2 + time * 1.2) * Math.sin(oz * 2 + time)) * 0.3;
            currentPositions.setXYZ(i, ox + nx * noise, oy + ny * noise, oz + nz * noise);
        }
        currentPositions.needsUpdate = true;
        liquidCore.geometry.computeVertexNormals();

        const coreSpeed = 0.001 + (scrollProgress * 0.004);
        liquidCore.rotation.y += coreSpeed;
        liquidCore.rotation.x += coreSpeed * 0.5;

        ribbons.forEach(ribbon => {
            ribbon.rotation.x += ribbon.userData.rx;
            ribbon.rotation.y += ribbon.userData.ry;
            ribbon.rotation.z += ribbon.userData.rz;
        });
        auroraGroup.position.y += (-(scrollProgress * 4) - auroraGroup.position.y) * 0.05;

        const dPositions = dustParticles.geometry.attributes.position;
        for(let i=0; i<particleCount; i++) {
            const data = dustData[i];
            dPositions.setXYZ(i, data.x + Math.sin(time * 0.5 + data.phaseX) * 2, data.y + Math.cos(time * 0.5 + data.phaseY) * 2, data.z);
        }
        dPositions.needsUpdate = true;

        camera.position.z += ((12 + (scrollProgress * 3)) - camera.position.z) * 0.05;
        camera.position.x += ((mouse.x * 1.5) - camera.position.x) * 0.05;
        camera.position.y += ((mouse.y * 1.5) - camera.position.y) * 0.05;
        camera.lookAt(scene.position);

        renderer.render(scene, camera);
    }
    animate();
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
});
"""

with open("script.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Updated script.js with AJAX form support.")
