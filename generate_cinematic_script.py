script_content = """document.addEventListener('DOMContentLoaded', () => {
    /* ═══════════════════════════════════════════════════════════════════════════
       1. INTERSECTION OBSERVER (Scroll Animations)
       ═══════════════════════════════════════════════════════════════════════════ */
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, {
        root: null,
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    });

    revealElements.forEach(el => revealObserver.observe(el));


    /* ═══════════════════════════════════════════════════════════════════════════
       2. THREE.JS PREMIUM BACKGROUND (CINEMATIC SCROLL)
       ═══════════════════════════════════════════════════════════════════════════ */
    const canvas = document.getElementById('webgl-canvas');
    if (!canvas) return;

    // Determine environment constraints
    const isMobile = window.innerWidth < 768;
    const PIXEL_RATIO = isMobile ? 1 : Math.min(window.devicePixelRatio, 2);

    // Scene Setup
    const scene = new THREE.Scene();
    scene.background = new THREE.Color('#FAFAF9'); 

    // Camera
    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
    camera.position.z = 8; // initial close-up

    // Renderer
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: !isMobile, alpha: false });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(PIXEL_RATIO);
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xe0f2f1, 0.5); 
    scene.add(ambientLight);

    const keyLight = new THREE.DirectionalLight(0xffffff, 1.5);
    keyLight.position.set(10, 10, 10);
    keyLight.castShadow = true;
    scene.add(keyLight);
    
    const fillLight = new THREE.DirectionalLight(0xffffff, 0.8);
    fillLight.position.set(-10, 5, 5);
    scene.add(fillLight);

    const rimLight = new THREE.DirectionalLight(0xffffff, 0.6);
    rimLight.position.set(0, 5, -10);
    scene.add(rimLight);

    // Premium Materials
    const glassMaterial = new THREE.MeshPhysicalMaterial({
        color: 0xe0f2f1, metalness: 0.1, roughness: 0.1,
        transmission: 0.9, thickness: 1.5, clearcoat: 1.0,
        clearcoatRoughness: 0.1, transparent: true
    });

    const emeraldMaterial = new THREE.MeshPhysicalMaterial({
        color: 0x10B981, metalness: 1.0, roughness: 0.2,
        clearcoat: 0.5, emissive: 0x10B981, emissiveIntensity: 0.2
    });

    const copperMaterial = new THREE.MeshPhysicalMaterial({
        color: 0xB87333, metalness: 1.0, roughness: 0.1, clearcoat: 0.5
    });

    const goldMaterial = new THREE.MeshPhysicalMaterial({
        color: 0xFFD700, metalness: 1.0, roughness: 0.2,
    });

    const darkMetalMaterial = new THREE.MeshPhysicalMaterial({
        color: 0x222222, metalness: 0.9, roughness: 0.4,
        emissive: 0x10B981, emissiveIntensity: 0.1
    });

    const brushedMetalMaterial = new THREE.MeshPhysicalMaterial({
        color: 0x888888, metalness: 0.8, roughness: 0.5,
    });

    const aluminumMaterial = new THREE.MeshPhysicalMaterial({
        color: 0xC0C0C0, metalness: 0.9, roughness: 0.2,
    });
    
    const lithiumMaterial = new THREE.MeshPhysicalMaterial({
        color: 0x10B981, metalness: 0.8, roughness: 0.15,
    });
    
    const whiteMaterial = new THREE.MeshPhysicalMaterial({
        color: 0xffffff, metalness: 0.1, roughness: 0.8,
    });

    function setShadows(object) {
        object.traverse((child) => {
            if (child.isMesh) {
                child.castShadow = true;
                child.receiveShadow = true;
            }
        });
    }

    function createEWasteObject(type) {
        const group = new THREE.Group();
        // ... (Include same geometry creation code as before)
        if (type === 'circuit_board') {
            const baseGeo = new THREE.BoxGeometry(2.5, 0.15, 1.8);
            const base = new THREE.Mesh(baseGeo, glassMaterial);
            group.add(base);
            const chipGeo = new THREE.BoxGeometry(0.4, 0.2, 0.4);
            [[-0.6, 0.075, -0.4], [0.5, 0.075, -0.5], [0.8, 0.075, 0.3], [-0.3, 0.075, 0.5]].forEach(pos => {
                const chip = new THREE.Mesh(chipGeo, copperMaterial);
                chip.position.set(...pos); group.add(chip);
            });
            const capGeo = new THREE.CylinderGeometry(0.08, 0.08, 0.15, 16);
            for(let i=0; i<6; i++) {
                const cap = new THREE.Mesh(capGeo, aluminumMaterial);
                cap.position.set((Math.random()-0.5)*2, 0.1, (Math.random()-0.5)*1.4);
                group.add(cap);
            }
            const pinGeo = new THREE.CylinderGeometry(0.02, 0.02, 0.2, 8);
            for (let i = -1; i <= 1; i += 0.2) {
                const pin = new THREE.Mesh(pinGeo, goldMaterial);
                pin.position.set(i, 0, -0.9); group.add(pin);
            }
            const traceGeo = new THREE.BoxGeometry(1.5, 0.02, 0.05);
            const trace = new THREE.Mesh(traceGeo, copperMaterial);
            trace.position.set(0, 0.08, 0); trace.rotation.y = Math.PI / 4;
            group.add(trace);
        } else if (type === 'battery') {
            const batGeo = new THREE.CylinderGeometry(0.8, 0.8, 2.5, 32);
            const battery = new THREE.Mesh(batGeo, emeraldMaterial);
            battery.rotation.x = Math.PI / 2; group.add(battery);
            const capGeo = new THREE.CylinderGeometry(0.82, 0.82, 0.2, 32);
            const cap = new THREE.Mesh(capGeo, darkMetalMaterial);
            cap.rotation.x = Math.PI / 2; cap.position.z = 1.25; group.add(cap);
            const bottomGeo = new THREE.CylinderGeometry(0.6, 0.6, 0.1, 32);
            const bottom = new THREE.Mesh(bottomGeo, copperMaterial);
            bottom.rotation.x = Math.PI / 2; bottom.position.z = -1.3; group.add(bottom);
            const labelGeo = new THREE.TorusGeometry(0.81, 0.1, 16, 64);
            const label = new THREE.Mesh(labelGeo, whiteMaterial); group.add(label);
            const terminalGeo = new THREE.CylinderGeometry(0.2, 0.2, 0.1, 16);
            const terminal = new THREE.Mesh(terminalGeo, aluminumMaterial);
            terminal.rotation.x = Math.PI / 2; terminal.position.z = 1.4; group.add(terminal);
        } else if (type === 'chip') {
            const dieGeo = new THREE.BoxGeometry(1.2, 0.05, 1.2);
            const die = new THREE.Mesh(dieGeo, darkMetalMaterial); group.add(die);
            const spreaderGeo = new THREE.BoxGeometry(1.4, 0.1, 1.4);
            const spreader = new THREE.Mesh(spreaderGeo, brushedMetalMaterial);
            spreader.position.y = 0.05; group.add(spreader);
            const pinGeo = new THREE.CylinderGeometry(0.02, 0.02, 0.1, 8);
            for (let x = -0.5; x <= 0.5; x += 0.15) {
                for (let z = -0.5; z <= 0.5; z += 0.15) {
                    const pin = new THREE.Mesh(pinGeo, goldMaterial);
                    pin.position.set(x, -0.05, z); group.add(pin);
                }
            }
            const markerGeo = new THREE.SphereGeometry(0.04, 8, 8);
            [[-0.6, 0.1, -0.6], [0.6, 0.1, -0.6], [-0.6, 0.1, 0.6], [0.6, 0.1, 0.6]].forEach(pos => {
                const marker = new THREE.Mesh(markerGeo, goldMaterial);
                marker.position.set(...pos); group.add(marker);
            });
        } else if (type === 'bin') {
            const wallGeo1 = new THREE.BoxGeometry(2, 2.5, 0.1);
            const wall1 = new THREE.Mesh(wallGeo1, glassMaterial); wall1.position.set(0, 0, 0.75); group.add(wall1);
            const wall2 = new THREE.Mesh(wallGeo1, glassMaterial); wall2.position.set(0, 0, -0.75); group.add(wall2);
            const wallGeo2 = new THREE.BoxGeometry(0.1, 2.5, 1.4);
            const wall3 = new THREE.Mesh(wallGeo2, glassMaterial); wall3.position.set(0.95, 0, 0); group.add(wall3);
            const wall4 = new THREE.Mesh(wallGeo2, glassMaterial); wall4.position.set(-0.95, 0, 0); group.add(wall4);
            const floorGeo = new THREE.BoxGeometry(2, 0.1, 1.5);
            const floor = new THREE.Mesh(floorGeo, glassMaterial); floor.position.set(0, -1.2, 0); group.add(floor);
            for(let i=0; i<8; i++) {
                const part = new THREE.Mesh(new THREE.BoxGeometry(0.3,0.3,0.3), darkMetalMaterial);
                part.position.set((Math.random()-0.5)*1.5, -0.8 + Math.random(), (Math.random()-0.5)*1.2);
                part.rotation.set(Math.random(), Math.random(), Math.random()); group.add(part);
            }
        } else if (type === 'ingot_copper') {
            const geo = new THREE.CylinderGeometry(0.4, 0.6, 1.5, 4);
            const mesh = new THREE.Mesh(geo, copperMaterial);
            mesh.rotation.x = Math.PI / 2; mesh.rotation.z = Math.PI / 4; group.add(mesh);
        } else if (type === 'ingot_aluminum') {
            const geo = new THREE.CylinderGeometry(0.8, 0.8, 0.4, 32);
            const mesh = new THREE.Mesh(geo, aluminumMaterial); group.add(mesh);
        } else if (type === 'ingot_lithium') {
            const geo = new THREE.BoxGeometry(0.8, 0.8, 0.8);
            const mesh = new THREE.Mesh(geo, lithiumMaterial); group.add(mesh);
        } else if (type === 'cluster') {
            const r1 = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.1, 0.6, 16), whiteMaterial);
            r1.position.set(-0.5, 0, 0); r1.rotation.z = Math.PI/4; group.add(r1);
            const c1 = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 0.8, 16), aluminumMaterial);
            c1.position.set(0.4, 0.2, -0.3); group.add(c1);
            const led = new THREE.Mesh(new THREE.SphereGeometry(0.15, 16, 16), emeraldMaterial);
            led.position.set(0, -0.2, 0.4); group.add(led);
            const conn = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.2, 0.3), darkMetalMaterial);
            conn.position.set(0.2, -0.4, -0.2); group.add(conn);
        }
        setShadows(group);
        return group;
    }

    const shapesGroup = new THREE.Group();
    scene.add(shapesGroup);

    const meshes = [];
    
    // Configurations for the 4 cinematic sections
    // sec1: Hero (0-25%), sec2: Services (25-50%), sec3: Impact (50-75%), sec4: Contact (75-100%)
    const configs = {
        'circuit_board': {
            sec1: {x: -3, y: 1, z: 0, scale: 1},
            sec2: {x: -6, y: 4, z: -5, scale: 0.5},
            sec3: {x: -8, y: -4, z: -8, scale: 0.5},
            sec4: {x: 0, y: 3, z: 0, scale: 1} // Top of recycling symbol
        },
        'chip': {
            sec1: {x: 3, y: -2, z: 1, scale: 1},
            sec2: {x: -4, y: -4, z: -3, scale: 0.5},
            sec3: {x: -6, y: 5, z: -6, scale: 0.5},
            sec4: {x: 2.5, y: -1.5, z: 0, scale: 1} // Bottom right
        },
        'battery': {
            sec1: {x: 0, y: 3, z: -2, scale: 1},
            sec2: {x: 5, y: 3, z: -2, scale: 0.5},
            sec3: {x: 6, y: -4, z: -5, scale: 0.5},
            sec4: {x: -2.5, y: -1.5, z: 0, scale: 1} // Bottom left
        },
        'bin': {
            sec1: {x: -12, y: -8, z: -15, scale: 0.1}, // Hidden
            sec2: {x: 0, y: -1, z: 1, scale: 1},
            sec3: {x: -7, y: -2, z: -4, scale: 0.8},
            sec4: {x: 0, y: 0, z: -8, scale: 0.5} // Background center
        },
        'cluster': {
            sec1: {x: 12, y: 8, z: -15, scale: 0.1}, // Hidden
            sec2: {x: 4, y: -2, z: 2, scale: 1},
            sec3: {x: 8, y: 2, z: -4, scale: 0.8},
            sec4: {x: 0, y: 0, z: 0, scale: 0} // Hidden
        },
        'ingot_copper': {
            sec1: {x: 15, y: 0, z: -15, scale: 0.1},
            sec2: {x: -3, y: 1, z: -2, scale: 0.8},
            sec3: {x: -3, y: 0, z: 3, scale: 1.5}, // Hero size
            sec4: {x: 1.5, y: 1.5, z: -2, scale: 1}
        },
        'ingot_aluminum': {
            sec1: {x: 0, y: 15, z: -15, scale: 0.1},
            sec2: {x: 0, y: 2, z: -2, scale: 0.8},
            sec3: {x: 0, y: -1, z: 4, scale: 1.5}, // Hero size
            sec4: {x: -1.5, y: 1.5, z: -2, scale: 1}
        },
        'ingot_lithium': {
            sec1: {x: -15, y: -5, z: -15, scale: 0.1},
            sec2: {x: 3, y: 1, z: -2, scale: 0.8},
            sec3: {x: 3, y: 0, z: 3, scale: 1.5}, // Hero size
            sec4: {x: 0, y: -2, z: -2, scale: 1}
        }
    };

    const objectTypes = Object.keys(configs);
    const activeTypes = isMobile ? ['circuit_board', 'battery', 'ingot_copper', 'bin'] : objectTypes;

    activeTypes.forEach((type) => {
        const meshGroup = createEWasteObject(type);
        const wrapper = new THREE.Group();
        wrapper.add(meshGroup);
        
        wrapper.userData = {
            type: type,
            floatSpeed: 0.001 + Math.random() * 0.001,
            wobbleSpeedX: 0.002 + Math.random() * 0.002,
            wobbleSpeedZ: 0.002 + Math.random() * 0.002,
            targetScale: 1,
            hoverScale: 1,
            isHovered: false
        };

        meshes.push(wrapper);
        shapesGroup.add(wrapper);
    });

    /* ═══════════════════════════════════════════════════════════════════════════
       3. INTERACTION & SCROLL NARRATIVE
       ═══════════════════════════════════════════════════════════════════════════ */
    let scrollProgress = 0;
    
    function updateScrollProgress() {
        const maxScroll = document.body.scrollHeight - window.innerHeight;
        if (maxScroll > 0) {
            scrollProgress = window.scrollY / maxScroll;
        } else {
            scrollProgress = 0;
        }
    }
    window.addEventListener('scroll', updateScrollProgress);
    window.addEventListener('resize', updateScrollProgress);
    updateScrollProgress(); // Initial call

    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();
    let mouseX = 0, mouseY = 0;
    const windowHalfX = window.innerWidth / 2;
    const windowHalfY = window.innerHeight / 2;

    document.addEventListener('mousemove', (event) => {
        mouseX = (event.clientX - windowHalfX) * 0.0005;
        mouseY = (event.clientY - windowHalfY) * 0.0005;
        mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
    });

    const clock = new THREE.Clock();

    function interpolate(val1, val2, factor) {
        return val1 + (val2 - val1) * factor;
    }

    function animate() {
        requestAnimationFrame(animate);
        const elapsedTime = clock.getElapsedTime();

        // Map scrollProgress (0 to 1) to sections
        // 0-0.25 -> Sec1 to Sec2
        // 0.25-0.5 -> Sec2 to Sec3
        // 0.5-0.75 -> Sec3 to Sec4
        // 0.75-1.0 -> Sec4 hold
        let currentSection, nextSection, factor;
        if (scrollProgress < 0.25) {
            currentSection = 'sec1'; nextSection = 'sec2'; factor = scrollProgress / 0.25;
        } else if (scrollProgress < 0.5) {
            currentSection = 'sec2'; nextSection = 'sec3'; factor = (scrollProgress - 0.25) / 0.25;
        } else if (scrollProgress < 0.75) {
            currentSection = 'sec3'; nextSection = 'sec4'; factor = (scrollProgress - 0.5) / 0.25;
        } else {
            currentSection = 'sec4'; nextSection = 'sec4'; factor = 1;
        }
        
        // Easing factor for smoother transitions
        const easedFactor = factor * factor * (3 - 2 * factor); // Smoothstep

        // --- Camera & Lighting orchestration ---
        const cameraZTargets = { sec1: 8, sec2: 10, sec3: 9, sec4: 12 };
        const camZ = interpolate(cameraZTargets[currentSection], cameraZTargets[nextSection], easedFactor);
        camera.position.z += (camZ - camera.position.z) * 0.1;

        const keyIntensities = { sec1: 1.5, sec2: 1.2, sec3: 0.8, sec4: 1.0 };
        const rimIntensities = { sec1: 0.6, sec2: 0.8, sec3: 1.5, sec4: 0.5 };
        keyLight.intensity = interpolate(keyIntensities[currentSection], keyIntensities[nextSection], easedFactor);
        rimLight.intensity = interpolate(rimIntensities[currentSection], rimIntensities[nextSection], easedFactor);

        // --- Hover Effects ---
        raycaster.setFromCamera(mouse, camera);
        meshes.forEach(w => { w.userData.isHovered = false; w.userData.hoverScale = 1.0; });
        const allIntersectables = [];
        meshes.forEach(w => {
            w.children[0].traverse((child) => {
                if (child.isMesh) { child.userData.parentWrapper = w; allIntersectables.push(child); }
            });
        });
        const intersects = raycaster.intersectObjects(allIntersectables, false);
        if (intersects.length > 0) {
            const hovered = intersects[0].object.userData.parentWrapper;
            if (hovered) { hovered.userData.isHovered = true; hovered.userData.hoverScale = 1.1; }
        }

        // --- Object Orchestration ---
        meshes.forEach((wrapper) => {
            const type = wrapper.userData.type;
            const t1 = configs[type][currentSection];
            const t2 = configs[type][nextSection];

            // Interpolate position & scale
            const targetX = interpolate(t1.x, t2.x, easedFactor);
            const targetY = interpolate(t1.y, t2.y, easedFactor);
            const targetZ = interpolate(t1.z, t2.z, easedFactor);
            const targetScale = interpolate(t1.scale, t2.scale, easedFactor) * wrapper.userData.hoverScale;

            wrapper.position.x += (targetX - wrapper.position.x) * 0.05;
            // Float effect layered on top of structural Y position
            const floatY = Math.sin(elapsedTime * wrapper.userData.floatSpeed * 1000) * 0.5;
            wrapper.position.y += ((targetY + floatY) - wrapper.position.y) * 0.05;
            wrapper.position.z += (targetZ - wrapper.position.z) * 0.05;
            
            wrapper.scale.lerp(new THREE.Vector3(targetScale, targetScale, targetScale), 0.1);

            // Circular rotation for Sec4, otherwise normal rotation
            const rotSpeed = wrapper.userData.isHovered ? 0.015 : 0.005;
            wrapper.rotation.y += rotSpeed;
            wrapper.rotation.x += Math.sin(elapsedTime * wrapper.userData.wobbleSpeedX * 1000) * 0.002;
            wrapper.rotation.z += Math.cos(elapsedTime * wrapper.userData.wobbleSpeedZ * 1000) * 0.002;
        });

        // Parallax and Scene rotation
        const parallaxTargetX = mouseX * 0.5;
        const parallaxTargetY = mouseY * 0.5;
        camera.position.x += (parallaxTargetX - camera.position.x) * 0.05;
        camera.position.y += (-parallaxTargetY - camera.position.y) * 0.05;
        
        // Scene rotation based on scroll (max Pi/2 rotation overall)
        const sceneTargetRotY = scrollProgress * Math.PI * 0.5;
        shapesGroup.rotation.y += (sceneTargetRotY - shapesGroup.rotation.y) * 0.05;

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
    f.write(script_content)

print("Updated script.js successfully!")
