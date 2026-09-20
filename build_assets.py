import os

css_content = """
:root {
  --bg-color: #0B1F18;
  --bg-secondary: #1B4332;
  --glass-bg: rgba(27, 67, 50, 0.6);
  --glass-border: rgba(16, 185, 129, 0.2);
  --text-primary: #FFFFFF;
  --text-secondary: #D1FAF5;
  --accent: #10B981;
  --accent-hover: #059669;
  --accent-glow: #34D399;
  --gold: #FFD700;
  --white: #FFFFFF;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { font-family: 'Inter', sans-serif; background-color: var(--bg-color); color: var(--text-primary); line-height: 1.8; overflow-x: hidden; -webkit-font-smoothing: antialiased; }
body::after { content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 9999; opacity: 0.03; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E"); }
#webgl-canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 0; pointer-events: none; }
.ui-layer { position: relative; z-index: 10; min-height: calc(100vh - 400px); }

/* Navigation */
.navbar { position: fixed; top: 0; left: 0; width: 100%; height: 80px; background: rgba(11, 31, 24, 0.8); backdrop-filter: blur(20px); border-bottom: 1px solid var(--glass-border); z-index: 1000; transition: all 0.3s ease; display: flex; align-items: center; }
.navbar.scrolled { background: rgba(11, 31, 24, 0.95); box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3); }
.nav-container { width: 100%; max-width: 1280px; margin: 0 auto; padding: 0 2rem; display: flex; justify-content: space-between; align-items: center; }
.logo { font-size: 24px; font-weight: 800; color: var(--text-primary); text-decoration: none; display: flex; align-items: center; gap: 0.5rem; }
.text-emerald { color: var(--accent); }
.nav-menu { display: flex; gap: 2rem; list-style: none; align-items: center; margin: 0; padding: 0; }
.nav-link { color: var(--text-primary); text-decoration: none; font-weight: 500; font-size: 0.95rem; opacity: 0.8; position: relative; padding: 0.5rem 0; transition: opacity 0.3s ease, color 0.3s ease; }
.nav-link:hover, .nav-link.active { opacity: 1; color: var(--accent); }
.nav-link::after { content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--accent); transition: width 0.3s ease; box-shadow: 0 0 10px var(--accent-glow); }
.nav-link:hover::after, .nav-link.active::after { width: 100%; }

/* Dropdown */
.has-dropdown { position: relative; }
.dropdown { position: absolute; top: 100%; left: 0; background: rgba(11, 31, 24, 0.95); backdrop-filter: blur(20px); border: 1px solid var(--glass-border); list-style: none; padding: 1rem 0; border-radius: 12px; min-width: 240px; opacity: 0; visibility: hidden; transform: translateY(10px); transition: all 0.3s; z-index: 1000; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
.has-dropdown:hover .dropdown { opacity: 1; visibility: visible; transform: translateY(0); }
.dropdown li { margin: 0; }
.dropdown a { display: block; padding: 0.75rem 1.5rem; color: var(--text-primary); text-decoration: none; transition: 0.3s; font-size: 0.9rem; }
.dropdown a:hover { background: rgba(16, 185, 129, 0.15); color: var(--accent-glow); padding-left: 1.75rem; }

.nav-ctas { display: flex; gap: 1rem; }
.mobile-toggle { display: none; flex-direction: column; justify-content: space-between; width: 30px; height: 20px; background: none; border: none; cursor: pointer; z-index: 1001; }
.mobile-toggle span { display: block; width: 100%; height: 2px; background: var(--white); transition: all 0.3s ease; }
.mobile-toggle.active span:nth-child(1) { transform: translateY(9px) rotate(45deg); }
.mobile-toggle.active span:nth-child(2) { opacity: 0; }
.mobile-toggle.active span:nth-child(3) { transform: translateY(-9px) rotate(-45deg); }

/* Globals */
.container { max-width: 1280px; margin: 0 auto; padding: 0 2rem; }
.max-w-800 { max-width: 800px; margin: 0 auto; }
.text-center { text-align: center; }
.text-white { color: var(--white); }
.text-secondary { color: var(--text-secondary); }
.text-accent { color: var(--accent); }
.font-bold { font-weight: 700; }
.uppercase { text-transform: uppercase; }
.text-sm { font-size: 0.875rem; }
.text-2xl { font-size: 1.5rem; font-weight: 800; }
.text-3xl { font-size: 2.5rem; font-weight: 800; letter-spacing: -0.05em; }
.bg-secondary { background-color: var(--bg-secondary); }

/* Gradients */
.hero-gradient { background: linear-gradient(135deg, rgba(11,31,24,0.3) 0%, rgba(27,67,50,0.5) 50%, rgba(6,78,59,0.3) 100%); }
.text-gradient { background: linear-gradient(135deg, #FFFFFF 0%, #34D399 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

/* Typography */
h1, h2, h3, h4 { font-weight: 800; letter-spacing: -0.03em; line-height: 1.2; }
.section-title { font-size: clamp(2rem, 5vw, 3.5rem); margin-bottom: 1.5rem; }
.text-lg { font-size: 1.125rem; }
.label { font-weight: 700; letter-spacing: 0.1em; font-size: 0.8rem; margin-bottom: 1rem; text-transform: uppercase; display: block; }
.label-accent { color: var(--accent); }

/* Spacing */
.mt-1 { margin-top: 0.25rem; } .mt-2 { margin-top: 0.5rem; } .mt-4 { margin-top: 2rem; } .mt-5 { margin-top: 3rem; }
.mb-2 { margin-bottom: 0.5rem; } .mb-4 { margin-bottom: 1.5rem; } .mb-5 { margin-bottom: 3rem; }
.py-4 { padding-top: 2rem; padding-bottom: 2rem; } .py-10 { padding-top: 8rem; padding-bottom: 8rem; } .pt-0 { padding-top: 0 !important; }

/* Sections */
.section { padding: 6rem 0; }
.hero { display: flex; align-items: center; padding-top: 8rem; }
.hero-grid { display: grid; grid-template-columns: 1.5fr 1fr; gap: 4rem; align-items: center; }
.hero-title { font-size: clamp(3rem, 6vw, 4.5rem); line-height: 1.1; margin-bottom: 1.5rem; }
.hero-subtitle { font-size: clamp(1.1rem, 2vw, 1.25rem); max-width: 55ch; margin-bottom: 2.5rem; color: var(--text-secondary); font-weight: 500; }
.hero-stats { display: flex; flex-direction: column; gap: 1.5rem; align-items: flex-end; }
.stat-pill { padding: 1.5rem 2.5rem; min-width: 200px; text-align: center; }
.stat-pill-num { font-size: 2.5rem; font-weight: 800; color: var(--accent); display: block; text-shadow: 0 0 10px rgba(16, 185, 129, 0.4); }
.stat-pill-label { font-size: 0.8rem; font-weight: 700; letter-spacing: 0.1em; color: var(--white); }

/* Buttons */
.btn-group { display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center; }
.btn { display: inline-flex; align-items: center; justify-content: center; padding: 1rem 2rem; border-radius: 999px; font-weight: 600; text-decoration: none; transition: all 0.3s ease; font-size: 1rem; cursor: pointer; }
.btn-sm { padding: 0.75rem 1.5rem; font-size: 0.9rem; }
.btn-primary { background-color: var(--accent); color: #fff; border: none; }
.btn-primary:hover { background-color: var(--accent-hover); transform: translateY(-2px); box-shadow: 0 10px 20px rgba(16, 185, 129, 0.4); }
.btn-outline { background-color: transparent; color: var(--text-primary); border: 1px solid var(--accent); }
.btn-outline:hover { background-color: var(--accent); transform: translateY(-2px); box-shadow: 0 10px 20px rgba(16, 185, 129, 0.2); }
.w-100 { width: 100%; }

/* Glassmorphism Cards */
.glass-card { background: linear-gradient(180deg, rgba(27,67,50,0.8) 0%, rgba(27,67,50,0.4) 100%); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid var(--glass-border); border-radius: 24px; padding: 2.5rem; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2); transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease; }
.glass-card:hover { transform: translateY(-8px); box-shadow: 0 16px 48px rgba(16, 185, 129, 0.15); border-color: rgba(16, 185, 129, 0.5); }

/* Grids */
.grid { display: grid; gap: 2rem; }
.two-col { grid-template-columns: 1fr; }
.three-col { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
.four-col { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
.align-center { align-items: center; }
.small-gap { gap: 1rem; }
@media (min-width: 992px) { .two-col { grid-template-columns: 1fr 1fr; gap: 4rem; } }

/* Stats */
.huge-number { font-size: clamp(3.5rem, 6vw, 5rem); color: var(--accent); line-height: 1; margin-bottom: 1rem; letter-spacing: -0.05em; text-shadow: 0 0 20px rgba(16, 185, 129, 0.3); }
.highlight-stat { font-size: clamp(3.5rem, 6vw, 5rem); color: var(--accent); line-height: 1; letter-spacing: -0.05em; text-shadow: 0 0 20px rgba(16, 185, 129, 0.3); }

/* Metal Tags */
.metal-tags { display: flex; flex-wrap: wrap; gap: 0.75rem; }
.metal-tags span { padding: 0.5rem 1.25rem; background: rgba(16, 185, 129, 0.15); border-radius: 99px; font-size: 0.875rem; font-weight: 600; border: 1px solid var(--accent); color: var(--accent-glow); box-shadow: 0 0 10px rgba(16, 185, 129, 0.2); }

/* Services Image Grid */
.services-grid { grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; }
.service-image-card { padding: 0 !important; display: flex; flex-direction: column; overflow: hidden; }
.service-image-card img { width: 100%; height: 240px; object-fit: cover; border-bottom: 1px solid var(--glass-border); }
.card-content { padding: 2rem; flex: 1; display: flex; flex-direction: column; }
.card-content h3 { margin-bottom: 1rem; font-size: 1.5rem; }
.card-content p { flex: 1; }

/* Lists & Accordion */
.process-list { list-style: none; }
.process-list li { margin-bottom: 0.5rem; position: relative; padding-left: 1.5rem; }
.process-list li::before { content: "→"; position: absolute; left: 0; color: var(--accent); font-weight: bold; }

/* Forms */
.contact-form { width: 100%; }
.form-group { margin-bottom: 1.5rem; text-align: left; }
.form-group label { display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-size: 0.9rem; font-weight: 600; }
.form-control { width: 100%; padding: 1rem; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); border-radius: 12px; color: var(--white); font-family: inherit; font-size: 1rem; transition: 0.3s; }
.form-control:focus { outline: none; border-color: var(--accent); background: rgba(255,255,255,0.1); box-shadow: 0 0 10px rgba(16, 185, 129, 0.2); }
textarea.form-control { min-height: 150px; resize: vertical; }

/* Footer */
.footer { padding: 6rem 0 2rem; border-top: 1px solid var(--glass-border); }
.footer ul { list-style: none; }
.footer ul li { margin-bottom: 0.75rem; }
.footer a { color: var(--text-secondary); text-decoration: none; transition: color 0.3s; font-size: 0.95rem; }
.footer a:hover { color: var(--accent-glow); }
.footer h4 { margin-bottom: 2rem; color: #fff; font-size: 0.9rem; letter-spacing: 0.1em; text-transform: uppercase; }
.social-links { display: flex; gap: 1.5rem; flex-wrap: wrap; margin-top: 2rem; }
.social-links a { font-weight: 600; font-size: 0.9rem; letter-spacing: 0.05em; text-transform: uppercase; color: var(--white); }
.footer-bottom { border-top: 1px solid var(--glass-border); padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; flex-wrap: wrap; gap: 1rem; color: var(--text-secondary); }

/* Animations */
.reveal { opacity: 0; transform: translateY(40px); transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1); }
.reveal.active { opacity: 1; transform: translateY(0); }

/* Responsive adjustments */
@media (max-width: 991px) {
  .hero-grid { grid-template-columns: 1fr; gap: 2rem; }
  .hero-stats { flex-direction: row; align-items: center; justify-content: flex-start; }
  .stat-pill { min-width: auto; padding: 1.5rem; }
  .nav-menu { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: rgba(11, 31, 24, 0.98); flex-direction: column; justify-content: center; align-items: center; gap: 2rem; opacity: 0; visibility: hidden; transition: all 0.3s ease; overflow-y: auto; padding: 4rem 0; }
  .nav-menu.active { opacity: 1; visibility: visible; }
  .nav-link { font-size: 1.5rem; }
  .dropdown { position: static; background: transparent; border: none; box-shadow: none; opacity: 1; visibility: visible; transform: none; min-width: auto; text-align: center; display: none; }
  .has-dropdown:hover .dropdown, .has-dropdown:active .dropdown { display: block; }
  .nav-ctas { display: none; }
  .mobile-toggle { display: flex; }
}
"""

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

    // 2. Form Validation (Contact Page)
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = form.querySelector('button[type="submit"]');
            const originalText = btn.innerText;
            btn.innerText = "Sending...";
            btn.style.opacity = "0.7";
            setTimeout(() => {
                btn.innerText = "Message Sent!";
                btn.style.background = "#10B981";
                form.reset();
                setTimeout(() => {
                    btn.innerText = originalText;
                    btn.style.opacity = "1";
                }, 3000);
            }, 1500);
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

files = {
    "style.css": css_content,
    "script.js": js_content
}

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated style and scripts successfully.")
