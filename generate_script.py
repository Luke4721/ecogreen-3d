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
       2. THREE.JS PREMIUM BACKGROUND
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
    camera.position.z = 12;

    // Renderer
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: !isMobile, alpha: false });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(PIXEL_RATIO);
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xe0f2f1, 0.5); // Soft green tint
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
        color: 0xe0f2f1,
        metalness: 0.1,
        roughness: 0.1,
        transmission: 0.9, 
        thickness: 1.5,
        clearcoat: 1.0,
        clearcoatRoughness: 0.1,
        transparent: true
    });

    const emeraldMaterial = new THREE.MeshPhysicalMaterial({
        color: 0x10B981, 
        metalness: 1.0,
        roughness: 0.2,
        clearcoat: 0.5,
        emissive: 0x10B981,
        emissiveIntensity: 0.2
    });

    const copperMaterial = new THREE.MeshPhysicalMaterial({
        color: 0xB87333,
        metalness: 1.0,
        roughness: 0.1,
        clearcoat: 0.5
    });

    const goldMaterial = new THREE.MeshPhysicalMaterial({
        color: 0xFFD700,
        metalness: 1.0,
        roughness: 0.2,
    });

    const darkMetalMaterial = new THREE.MeshPhysicalMaterial({
        color: 0x222222,
        metalness: 0.9,
        roughness: 0.4,
        emissive: 0x10B981,
        emissiveIntensity: 0.1
    });

    const brushedMetalMaterial = new THREE.MeshPhysicalMaterial({
        color: 0x888888,
        metalness: 0.8,
        roughness: 0.5,
    });

    const aluminumMaterial = new THREE.MeshPhysicalMaterial({
        color: 0xC0C0C0,
        metalness: 0.9,
        roughness: 0.2,
    });
    
    const lithiumMaterial = new THREE.MeshPhysicalMaterial({
        color: 0x10B981,
        metalness: 0.8,
        roughness: 0.15,
    });
    
    const whiteMaterial = new THREE.MeshPhysicalMaterial({
        color: 0xffffff,
        metalness: 0.1,
        roughness: 0.8,
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
        
        if (type === 'circuit_board') {
            const baseGeo = new THREE.BoxGeometry(2.5, 0.15, 1.8);
            const base = new THREE.Mesh(baseGeo, glassMaterial);
            group.add(base);
            
            // Large chips
            const chipGeo = new THREE.BoxGeometry(0.4, 0.2, 0.4);
            const chipPositions = [
                [-0.6, 0.075, -0.4], [0.5, 0.075, -0.5], 
                [0.8, 0.075, 0.3], [-0.3, 0.075, 0.5]
            ];
            chipPositions.forEach(pos => {
                const chip = new THREE.Mesh(chipGeo, copperMaterial);
                chip.position.set(...pos);
                group.add(chip);
            });

            // Small capacitors
            const capGeo = new THREE.CylinderGeometry(0.08, 0.08, 0.15, 16);
            for(let i=0; i<6; i++) {
                const cap = new THREE.Mesh(capGeo, aluminumMaterial);
                cap.position.set((Math.random()-0.5)*2, 0.1, (Math.random()-0.5)*1.4);
                group.add(cap);
            }

            // Connector pins
            const pinGeo = new THREE.CylinderGeometry(0.02, 0.02, 0.2, 8);
            for (let i = -1; i <= 1; i += 0.2) {
                const pin = new THREE.Mesh(pinGeo, goldMaterial);
                pin.position.set(i, 0, -0.9);
                group.add(pin);
            }

            // Traces (Thin boxes)
            const traceGeo = new THREE.BoxGeometry(1.5, 0.02, 0.05);
            const trace = new THREE.Mesh(traceGeo, copperMaterial);
            trace.position.set(0, 0.08, 0);
            trace.rotation.y = Math.PI / 4;
            group.add(trace);
            
        } else if (type === 'battery') {
            const batGeo = new THREE.CylinderGeometry(0.8, 0.8, 2.5, 32);
            const battery = new THREE.Mesh(batGeo, emeraldMaterial);
            battery.rotation.x = Math.PI / 2;
            group.add(battery);
            
            const capGeo = new THREE.CylinderGeometry(0.82, 0.82, 0.2, 32);
            const cap = new THREE.Mesh(capGeo, darkMetalMaterial);
            cap.rotation.x = Math.PI / 2;
            cap.position.z = 1.25;
            group.add(cap);

            const bottomGeo = new THREE.CylinderGeometry(0.6, 0.6, 0.1, 32);
            const bottom = new THREE.Mesh(bottomGeo, copperMaterial);
            bottom.rotation.x = Math.PI / 2;
            bottom.position.z = -1.3;
            group.add(bottom);
            
            const labelGeo = new THREE.TorusGeometry(0.81, 0.1, 16, 64);
            const label = new THREE.Mesh(labelGeo, whiteMaterial);
            group.add(label);

            const terminalGeo = new THREE.CylinderGeometry(0.2, 0.2, 0.1, 16);
            const terminal = new THREE.Mesh(terminalGeo, aluminumMaterial);
            terminal.rotation.x = Math.PI / 2;
            terminal.position.z = 1.4;
            group.add(terminal);
            
        } else if (type === 'chip') {
            const dieGeo = new THREE.BoxGeometry(1.2, 0.05, 1.2);
            const die = new THREE.Mesh(dieGeo, darkMetalMaterial);
            group.add(die);
            
            const spreaderGeo = new THREE.BoxGeometry(1.4, 0.1, 1.4);
            const spreader = new THREE.Mesh(spreaderGeo, brushedMetalMaterial);
            spreader.position.y = 0.05;
            group.add(spreader);
            
            // Pins
            const pinGeo = new THREE.CylinderGeometry(0.02, 0.02, 0.1, 8);
            for (let x = -0.5; x <= 0.5; x += 0.15) {
                for (let z = -0.5; z <= 0.5; z += 0.15) {
                    const pin = new THREE.Mesh(pinGeo, goldMaterial);
                    pin.position.set(x, -0.05, z);
                    group.add(pin);
                }
            }

            // Corner markers
            const markerGeo = new THREE.SphereGeometry(0.04, 8, 8);
            [
                [-0.6, 0.1, -0.6], [0.6, 0.1, -0.6], 
                [-0.6, 0.1, 0.6], [0.6, 0.1, 0.6]
            ].forEach(pos => {
                const marker = new THREE.Mesh(markerGeo, goldMaterial);
                marker.position.set(...pos);
                group.add(marker);
            });
            
        } else if (type === 'bin') {
            // E-Waste Bin
            const wallGeo1 = new THREE.BoxGeometry(2, 2.5, 0.1);
            const wall1 = new THREE.Mesh(wallGeo1, glassMaterial);
            wall1.position.set(0, 0, 0.75);
            group.add(wall1);
            
            const wall2 = new THREE.Mesh(wallGeo1, glassMaterial);
            wall2.position.set(0, 0, -0.75);
            group.add(wall2);

            const wallGeo2 = new THREE.BoxGeometry(0.1, 2.5, 1.4);
            const wall3 = new THREE.Mesh(wallGeo2, glassMaterial);
            wall3.position.set(0.95, 0, 0);
            group.add(wall3);

            const wall4 = new THREE.Mesh(wallGeo2, glassMaterial);
            wall4.position.set(-0.95, 0, 0);
            group.add(wall4);

            const floorGeo = new THREE.BoxGeometry(2, 0.1, 1.5);
            const floor = new THREE.Mesh(floorGeo, glassMaterial);
            floor.position.set(0, -1.2, 0);
            group.add(floor);

            // Fill with small parts
            for(let i=0; i<8; i++) {
                const part = new THREE.Mesh(new THREE.BoxGeometry(0.3,0.3,0.3), darkMetalMaterial);
                part.position.set((Math.random()-0.5)*1.5, -0.8 + Math.random(), (Math.random()-0.5)*1.2);
                part.rotation.set(Math.random(), Math.random(), Math.random());
                group.add(part);
            }
            
        } else if (type === 'ingot_copper') {
            const geo = new THREE.CylinderGeometry(0.4, 0.6, 1.5, 4);
            const mesh = new THREE.Mesh(geo, copperMaterial);
            mesh.rotation.x = Math.PI / 2;
            mesh.rotation.z = Math.PI / 4;
            group.add(mesh);
        } else if (type === 'ingot_aluminum') {
            const geo = new THREE.CylinderGeometry(0.8, 0.8, 0.4, 32);
            const mesh = new THREE.Mesh(geo, aluminumMaterial);
            group.add(mesh);
        } else if (type === 'ingot_lithium') {
            const geo = new THREE.BoxGeometry(0.8, 0.8, 0.8);
            const mesh = new THREE.Mesh(geo, lithiumMaterial);
            group.add(mesh);
        } else if (type === 'cluster') {
            // Component Cluster
            const resistorGeo = new THREE.CylinderGeometry(0.1, 0.1, 0.6, 16);
            const r1 = new THREE.Mesh(resistorGeo, whiteMaterial);
            r1.position.set(-0.5, 0, 0);
            r1.rotation.z = Math.PI/4;
            group.add(r1);

            const capGeo = new THREE.CylinderGeometry(0.2, 0.2, 0.8, 16);
            const c1 = new THREE.Mesh(capGeo, aluminumMaterial);
            c1.position.set(0.4, 0.2, -0.3);
            group.add(c1);

            const ledGeo = new THREE.SphereGeometry(0.15, 16, 16);
            const led = new THREE.Mesh(ledGeo, emeraldMaterial);
            led.position.set(0, -0.2, 0.4);
            group.add(led);

            const connGeo = new THREE.BoxGeometry(0.8, 0.2, 0.3);
            const conn = new THREE.Mesh(connGeo, darkMetalMaterial);
            conn.position.set(0.2, -0.4, -0.2);
            group.add(conn);
        }
        
        setShadows(group);
        return group;
    }

    // Group to hold all shapes for global scroll rotation
    const shapesGroup = new THREE.Group();
    scene.add(shapesGroup);

    // Instantiate Shapes
    const meshes = [];
    
    // Total 8 distinct objects specified
    const objectTypes = [
        'circuit_board', 
        'chip', 
        'battery', 
        'ingot_copper', 
        'ingot_aluminum',
        'ingot_lithium',
        'bin', 
        'cluster'
    ];
    
    const mobileObjectTypes = ['circuit_board', 'battery', 'ingot_copper', 'bin'];
    const activeTypes = isMobile ? mobileObjectTypes : objectTypes;
    
    // Strategic positions
    const positions = {
        'circuit_board': { x: -4, y: 1, z: -1 },
        'chip': { x: -3, y: -4, z: -2 },
        'battery': { x: 5, y: -2, z: 1 },
        'ingot_copper': { x: 3, y: -5, z: 0 },
        'ingot_aluminum': { x: 6, y: 0, z: 2 },
        'ingot_lithium': { x: -6, y: -1, z: 1 },
        'bin': { x: -5, y: 4, z: 3 },
        'cluster': { x: 5, y: 4, z: 4 }
    };

    activeTypes.forEach((type, i) => {
        const meshGroup = createEWasteObject(type);
        
        if (positions[type]) {
            meshGroup.position.set(positions[type].x, positions[type].y, positions[type].z);
        } else {
            meshGroup.position.set((Math.random() - 0.5) * 16, (Math.random() - 0.5) * 10, 2 + Math.random()*2);
        }
        
        // Wrap in another group for hover scaling without affecting base rotation logic
        const wrapper = new THREE.Group();
        wrapper.add(meshGroup);
        wrapper.position.copy(meshGroup.position);
        meshGroup.position.set(0,0,0);
        
        // Random initial rotation
        wrapper.rotation.x = Math.random() * Math.PI * 2;
        wrapper.rotation.y = Math.random() * Math.PI * 2;

        wrapper.userData = {
            floatSpeed: 0.001 + Math.random() * 0.001,
            rotSpeedY: 0.005, // base Y rotation
            wobbleSpeedX: 0.002 + Math.random() * 0.002,
            wobbleSpeedZ: 0.002 + Math.random() * 0.002,
            initialY: wrapper.position.y,
            targetScale: 1,
            currentScale: 1,
            isHovered: false
        };

        meshes.push(wrapper);
        shapesGroup.add(wrapper);
    });

    /* ═══════════════════════════════════════════════════════════════════════════
       3. INTERACTION & ANIMATION LOOP
       ═══════════════════════════════════════════════════════════════════════════ */
    
    // Mouse Parallax & Raycasting
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();
    let mouseX = 0;
    let mouseY = 0;
    let targetX = 0;
    let targetY = 0;
    const windowHalfX = window.innerWidth / 2;
    const windowHalfY = window.innerHeight / 2;

    document.addEventListener('mousemove', (event) => {
        // For parallax
        mouseX = (event.clientX - windowHalfX) * 0.0005;
        mouseY = (event.clientY - windowHalfY) * 0.0005;
        
        // For raycasting
        mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
    });

    // Scroll Rotation
    let scrollY = 0;
    document.addEventListener('scroll', () => {
        scrollY = window.scrollY;
    });

    // Main Render Loop
    const clock = new THREE.Clock();

    function animate() {
        requestAnimationFrame(animate);
        const elapsedTime = clock.getElapsedTime();

        // Raycasting for hover effects
        raycaster.setFromCamera(mouse, camera);
        
        // Reset hover state
        meshes.forEach(wrapper => {
            wrapper.userData.isHovered = false;
            wrapper.userData.targetScale = 1.0;
        });

        // Find intersections with the children of the wrappers
        const allIntersectables = [];
        meshes.forEach(w => {
            w.children[0].traverse((child) => {
                if (child.isMesh) {
                    child.userData.parentWrapper = w;
                    allIntersectables.push(child);
                }
            });
        });

        const intersects = raycaster.intersectObjects(allIntersectables, false);
        if (intersects.length > 0) {
            const hoveredWrapper = intersects[0].object.userData.parentWrapper;
            if (hoveredWrapper) {
                hoveredWrapper.userData.isHovered = true;
                hoveredWrapper.userData.targetScale = 1.1;
            }
        }

        // 1. Idle float + rotation for individual meshes
        meshes.forEach((wrapper) => {
            // Scale lerp
            wrapper.userData.currentScale += (wrapper.userData.targetScale - wrapper.userData.currentScale) * 0.1;
            wrapper.scale.setScalar(wrapper.userData.currentScale);

            // Rotation
            const rotMultiplier = wrapper.userData.isHovered ? 3 : 1;
            wrapper.rotation.y += wrapper.userData.rotSpeedY * rotMultiplier;
            wrapper.rotation.x += Math.sin(elapsedTime * wrapper.userData.wobbleSpeedX * 1000) * 0.002;
            wrapper.rotation.z += Math.cos(elapsedTime * wrapper.userData.wobbleSpeedZ * 1000) * 0.002;
            
            // Gentle Y-axis bobbing
            wrapper.position.y = wrapper.userData.initialY + Math.sin(elapsedTime * wrapper.userData.floatSpeed * 1000) * 0.5;
        });

        // 2. Mouse Parallax Easing
        targetX = mouseX * 0.5;
        targetY = mouseY * 0.5;
        shapesGroup.rotation.x += 0.05 * (targetY - shapesGroup.rotation.x);
        shapesGroup.rotation.y += 0.05 * (targetX - shapesGroup.rotation.y);

        // 3. Scroll Rotation Easing
        shapesGroup.position.y = scrollY * 0.002; // Move group slightly up on scroll
        
        // Combine mouse rotation and scroll rotation
        camera.position.x += (mouseX - camera.position.x) * 0.05;
        camera.position.y += (-mouseY - camera.position.y) * 0.05;
        camera.lookAt(scene.position);

        renderer.render(scene, camera);
    }
    
    animate();

    // Handle Window Resize
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
