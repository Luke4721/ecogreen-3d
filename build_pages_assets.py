import os

header = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Eco Green Recyclers</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<nav class="navbar">
<div class="container nav-container">
<a href="index.html" class="logo">
<img src="assets/logos/eco-green-logo.png" alt="Eco Green Logo" style="height: 40px; width: auto;">
</a>
<ul class="nav-menu">
<li><a href="index.html" class="nav-link">Home</a></li>
<li><a href="about.html" class="nav-link">About</a></li>
<li class="has-dropdown">
<a href="services.html" class="nav-link">Services</a>
<ul class="dropdown">
<li><a href="e-waste-management.html">E-Waste Management</a></li>
<li><a href="lithium-battery-recycling.html">Lithium Battery Recycling</a></li>
<li><a href="plastic-waste-recycling.html">Plastic Waste Recycling</a></li>
<li><a href="paper-recycling.html">Paper Recycling</a></li>
<li><a href="green-metal-recovery.html">Green Metal Recovery</a></li>
<li><a href="epr-consulting.html">EPR Consulting</a></li>
</ul>
</li>
<li><a href="impact.html" class="nav-link">Impact</a></li>
<li><a href="sustainability.html" class="nav-link">Sustainability</a></li>
<li><a href="faq.html" class="nav-link">FAQ</a></li>
<li><a href="contact.html" class="nav-link">Contact</a></li>
</ul>
<div class="nav-ctas">
<a href="contact.html" class="btn btn-outline">Get In Touch</a>
<a href="contact.html" class="btn btn-primary">Request Quote</a>
</div>
<button class="mobile-toggle"><span></span><span></span><span></span></button>
</div>
</nav>
<canvas id="webgl-canvas"></canvas>
<main class="ui-layer">
"""

footer = """
</main>
<footer class="footer bg-secondary">
<div class="container">
<div class="grid four-col">
<div class="footer-col reveal">
<h3 class="logo mb-2 text-white">
<img src="assets/logos/eco-green-logo.png" alt="Eco Green Logo" style="height: 40px; width: auto; filter: brightness(0) invert(1);">
</h3>
<p class="text-secondary mb-4 text-sm">Industrial-scale materials recovery pioneer — certified IT asset disposition, green metal recovery and EPR compliance for enterprises across India.</p>
<div class="social-links">
<a href="#">LinkedIn</a><a href="#">Twitter</a><a href="#">Facebook</a><a href="#">Instagram</a>
</div>
</div>
<div class="footer-col reveal" style="transition-delay: 0.1s;">
<h4>Company</h4>
<ul>
<li><a href="index.html">Home</a></li>
<li><a href="about.html">About Us</a></li>
<li><a href="services.html">Services</a></li>
<li><a href="impact.html">Impact</a></li>
<li><a href="contact.html">Contact</a></li>
</ul>
</div>
<div class="footer-col reveal" style="transition-delay: 0.2s;">
<h4>Services</h4>
<ul>
<li><a href="e-waste-management.html">E-Waste Management</a></li>
<li><a href="lithium-battery-recycling.html">Lithium Battery Recycling</a></li>
<li><a href="plastic-waste-recycling.html">Plastic Waste Recycling</a></li>
<li><a href="paper-recycling.html">Paper Recycling</a></li>
<li><a href="green-metal-recovery.html">Green Metal Recovery</a></li>
<li><a href="epr-consulting.html">EPR Consulting</a></li>
</ul>
</div>
<div class="footer-col reveal" style="transition-delay: 0.3s;">
<h4>Get In Touch</h4>
<p class="text-secondary text-sm mb-2"><a href="mailto:operation@ecogreen.eco" class="hover-white">operation@ecogreen.eco</a></p>
<p class="text-secondary text-sm mb-2"><a href="tel:+919319253708" class="hover-white">+91 93192 53708</a></p>
<p class="text-secondary text-sm mb-4">479, Habibpur, Dadri,<br>Gr. Noida, Uttar Pradesh</p>
<a href="contact.html" class="btn btn-primary btn-sm">Request Quote &rarr;</a>
</div>
</div>
<div class="footer-bottom mt-5 reveal">
<p>&copy; 2026 Eco Green Recyclers (P) Limited. All rights reserved.</p>
<div class="footer-legal">
<a href="#">Privacy Policy</a> | <a href="#">Terms & Conditions</a>
</div>
</div>
</div>
</footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="script.js"></script>
</body>
</html>
"""

pages = {
"index.html": """
<section class="section hero hero-gradient">
<div class="container hero-grid">
<div class="hero-content reveal">
<p class="label label-accent">SUSTAINABLE SOLUTIONS • SINCE 2015</p>
<h1 class="hero-title text-gradient">India's specialist in e-waste management.</h1>
<p class="hero-subtitle">Certified IT asset disposition, military-grade data destruction and high-purity metal recovery — the full e-waste lifecycle, handled under one compliant roof.</p>
<div class="btn-group">
<a href="services.html" class="btn btn-primary">Explore solutions</a>
<a href="about.html" class="btn btn-outline">See how it works</a>
</div>
</div>
<div class="hero-stats reveal">
<div class="glass-card stat-pill"><span class="stat-pill-num">10+</span><span class="stat-pill-label">YEARS</span></div>
<div class="glass-card stat-pill"><span class="stat-pill-num">342+</span><span class="stat-pill-label">CLIENTS</span></div>
</div>
</div>
</section>

<section class="section pt-0">
<div class="container">
<p class="label label-accent text-center reveal">SHOCKING FIGURES</p>
<div class="grid three-col mt-4">
<div class="glass-card reveal">
<h2 class="huge-number"><span class="counter-val" data-target="1.6" data-suffix="Mt">0</span></h2>
<p class="text-secondary">India's e-waste generation every year.</p>
</div>
<div class="glass-card reveal" style="transition-delay: 0.1s;">
<h2 class="huge-number"><span class="counter-val" data-target="32" data-suffix="%">0</span></h2>
<p class="text-secondary">Informal recycling issue.</p>
</div>
<div class="glass-card reveal" style="transition-delay: 0.2s;">
<h2 class="huge-number"><span class="counter-val" data-target="2.6" data-suffix="Mt">0</span></h2>
<p class="text-secondary">Embodied carbon wasted.</p>
</div>
</div>
</div>
</section>

<section class="section bg-secondary">
<div class="container text-center">
<p class="label label-accent reveal">OUR EXPERTISE</p>
<h2 class="section-title text-gradient reveal">Services Preview</h2>
<div class="grid three-col mt-4">
<div class="service-image-card glass-card reveal">
<img src="assets/images/e-waste-management.jpg" alt="E-Waste Management">
<div class="card-content">
<h3>E-Waste Management</h3>
<p class="text-secondary">Certified IT asset disposition and data destruction.</p>
<a href="e-waste-management.html" class="btn btn-outline mt-2">Learn More &rarr;</a>
</div>
</div>
<div class="service-image-card glass-card reveal" style="transition-delay: 0.1s;">
<img src="assets/images/lithium-battery.jpg" alt="Lithium Battery Recycling">
<div class="card-content">
<h3>Lithium Battery Recycling</h3>
<p class="text-secondary">High-purity extraction of lithium and cobalt.</p>
<a href="lithium-battery-recycling.html" class="btn btn-outline mt-2">Learn More &rarr;</a>
</div>
</div>
<div class="service-image-card glass-card reveal" style="transition-delay: 0.2s;">
<img src="assets/images/plastic-recycling.jpg" alt="Plastic Waste Recycling">
<div class="card-content">
<h3>Plastic Waste Recycling</h3>
<p class="text-secondary">Advanced sorting and precision pelletizing.</p>
<a href="plastic-waste-recycling.html" class="btn btn-outline mt-2">Learn More &rarr;</a>
</div>
</div>
</div>
<a href="services.html" class="btn btn-primary mt-5 reveal">View All Services</a>
</div>
</section>

<section class="section">
<div class="container grid two-col align-center">
<div class="reveal">
<h2 class="section-title text-gradient">Why Choose Us</h2>
<p class="text-lg text-secondary">We empower global brands to achieve zero-waste goals through state-of-the-art recycling technology and uncompromising data security.</p>
</div>
<div class="grid two-col small-gap reveal" style="transition-delay: 0.2s;">
<div class="glass-card text-center py-4"><h3 class="text-accent text-3xl">10</h3><p class="font-bold uppercase text-sm mt-1">Years Experience</p></div>
<div class="glass-card text-center py-4"><h3 class="text-accent text-3xl">8</h3><p class="font-bold uppercase text-sm mt-1">Awards Won</p></div>
<div class="glass-card text-center py-4"><h3 class="text-accent text-3xl">342</h3><p class="font-bold uppercase text-sm mt-1">Happy Clients</p></div>
<div class="glass-card text-center py-4"><h3 class="text-accent text-3xl">84</h3><p class="font-bold uppercase text-sm mt-1">Partners</p></div>
</div>
</div>
</section>

<section class="section bg-secondary">
<div class="container text-center">
<h2 class="section-title text-gradient reveal">Certifications Preview</h2>
<div class="grid three-col mt-4">
<div class="glass-card reveal">
<img src="assets/images/certifications/iso.png" alt="ISO Certification" style="max-height:80px; margin-bottom:1rem; opacity:0.8;">
<h3>ISO Certification</h3>
</div>
<div class="glass-card reveal" style="transition-delay:0.1s;">
<img src="assets/images/certifications/grs.png" alt="Global Recycled Standard" style="max-height:80px; margin-bottom:1rem; opacity:0.8;">
<h3>Global Recycled Standard</h3>
</div>
<div class="glass-card reveal" style="transition-delay:0.2s;">
<img src="assets/images/certifications/green-air.png" alt="Green Air Standard" style="max-height:80px; margin-bottom:1rem; opacity:0.8;">
<h3>Green Air Standard</h3>
</div>
</div>
<a href="sustainability.html" class="btn btn-outline mt-5 reveal">Learn More</a>
</div>
</section>

<section class="section text-center py-10">
<div class="container reveal">
<h2 class="section-title text-gradient">Start your green transition.</h2>
<a href="contact.html" class="btn btn-primary mt-4">Request a Quote</a>
</div>
</section>
""",

"about.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<h1 class="hero-title text-gradient">Empowering sustainable futures through responsible e-waste management</h1>
<p class="text-lg text-secondary mx-auto" style="max-width: 800px;">Our comprehensive approach to resource recovery drives the circular economy forward.</p>
</div>
</section>
<section class="section">
<div class="container grid two-col align-center">
<div class="reveal">
<h2 class="section-title text-gradient">Our Story</h2>
<p class="text-lg text-secondary">Since 2015, Eco Green Recyclers has pioneered industrial-scale materials recovery. We began with a single mission: to divert toxic e-waste from landfills and informal sectors, ensuring zero-harm atmospheric processing and high-yield asset recovery.</p>
</div>
<div class="glass-card reveal" style="transition-delay: 0.2s; min-height: 300px; background: url('assets/images/facility-1.jpg') center/cover;">
</div>
</div>
</section>
<section class="section bg-secondary">
<div class="container grid two-col">
<div class="glass-card reveal">
<h3 class="text-2xl text-accent mb-2">Vision</h3>
<p class="text-secondary text-lg">Our vision is a zero-waste future driven by continuous innovation, where end-of-life technology fuels the next generation of manufacturing.</p>
</div>
<div class="glass-card reveal" style="transition-delay: 0.1s;">
<h3 class="text-2xl text-accent mb-2">Mission</h3>
<p class="text-secondary text-lg">We empower global brands to achieve zero-waste goals through state-of-the-art recycling technology and uncompromising data security.</p>
</div>
</div>
</section>
<section class="section">
<div class="container text-center reveal">
<h2 class="section-title text-gradient">What We Do</h2>
<div class="grid four-col mt-5">
<div class="glass-card"><h4>Collection</h4></div>
<div class="glass-card"><h4>Dismantling</h4></div>
<div class="glass-card"><h4>Data Destruction</h4></div>
<div class="glass-card"><h4>Metal Recovery</h4></div>
</div>
</div>
</section>
<section class="section bg-secondary text-center">
<div class="container reveal">
<div class="grid four-col">
<div class="glass-card"><h3 class="highlight-stat">98%+</h3><p class="text-secondary">Extraction efficiency</p></div>
<div class="glass-card"><h3 class="highlight-stat">99.5%</h3><p class="text-secondary">Purity level</p></div>
<div class="glass-card"><h3 class="highlight-stat">22+</h3><p class="text-secondary">Metals recovered</p></div>
<div class="glass-card"><h3 class="highlight-stat">10+</h3><p class="text-secondary">Partner orgs</p></div>
</div>
</div>
</section>
""",

"services.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<h1 class="hero-title text-gradient">Our Expertise</h1>
<p class="text-lg text-secondary mx-auto">Expert collection, recycling, and disposal services for all industries.</p>
</div>
</section>
<section class="section bg-secondary pt-0">
<div class="container">
<div class="grid services-grid mt-4">
<div class="service-image-card glass-card reveal">
<img src="assets/images/e-waste-management.jpg" alt="E-Waste">
<div class="card-content">
<h3>E-Waste Management</h3>
<p class="text-secondary">End-to-end IT asset disposition with certified dismantling and military-grade data destruction.</p>
<a href="e-waste-management.html" class="btn btn-outline mt-4">Learn More &rarr;</a>
</div>
</div>
<div class="service-image-card glass-card reveal" style="transition-delay:0.1s;">
<img src="assets/images/lithium-battery.jpg" alt="Battery">
<div class="card-content">
<h3>Lithium Battery Recycling</h3>
<p class="text-secondary">High-purity extraction of lithium and cobalt from EV and electronic batteries.</p>
<a href="lithium-battery-recycling.html" class="btn btn-outline mt-4">Learn More &rarr;</a>
</div>
</div>
<div class="service-image-card glass-card reveal" style="transition-delay:0.2s;">
<img src="assets/images/plastic-recycling.jpg" alt="Plastic">
<div class="card-content">
<h3>Plastic Waste Recycling</h3>
<p class="text-secondary">Advanced sorting and precision pelletizing into reusable manufacturing materials.</p>
<a href="plastic-waste-recycling.html" class="btn btn-outline mt-4">Learn More &rarr;</a>
</div>
</div>
<div class="service-image-card glass-card reveal">
<img src="assets/images/paper-recycling.jpg" alt="Paper">
<div class="card-content">
<h3>Paper Recycling</h3>
<p class="text-secondary">Closed-loop processing that saves trees, conserves water and cuts corporate carbon.</p>
<a href="paper-recycling.html" class="btn btn-outline mt-4">Learn More &rarr;</a>
</div>
</div>
<div class="service-image-card glass-card reveal" style="transition-delay:0.1s;">
<img src="assets/images/green-metal-recovery.jpg" alt="Metal">
<div class="card-content">
<h3>Green Metal Recovery</h3>
<p class="text-secondary">High-yield extraction of iron, copper and aluminum from complex waste streams.</p>
<a href="green-metal-recovery.html" class="btn btn-outline mt-4">Learn More &rarr;</a>
</div>
</div>
<div class="service-image-card glass-card reveal" style="transition-delay:0.2s;">
<img src="assets/images/epr-consulting.jpg" alt="EPR">
<div class="card-content">
<h3>EPR Consulting</h3>
<p class="text-secondary">Regulatory navigation, compliance documentation and mandated EPR targets, handled.</p>
<a href="epr-consulting.html" class="btn btn-outline mt-4">Learn More &rarr;</a>
</div>
</div>
</div>
</div>
</section>
<section class="section text-center">
<div class="container reveal">
<h2 class="section-title text-gradient">Why Work With Us</h2>
<p class="text-secondary text-lg">Partner with us for certified, compliant resource recovery.</p>
<div class="grid four-col mt-5">
<div class="glass-card"><h3 class="highlight-stat">10</h3><p>Years</p></div>
<div class="glass-card"><h3 class="highlight-stat">8</h3><p>Awards</p></div>
<div class="glass-card"><h3 class="highlight-stat">342</h3><p>Clients</p></div>
<div class="glass-card"><h3 class="highlight-stat">84</h3><p>Partners</p></div>
</div>
</div>
</section>
<section class="section bg-secondary text-center py-10">
<div class="container reveal">
<h2 class="section-title text-gradient">Ready to start your green transition?</h2>
<a href="contact.html" class="btn btn-primary mt-4">Request a Quote</a>
</div>
</section>
""",

"e-waste-management.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<p class="label label-accent">SERVICES</p>
<h1 class="hero-title text-gradient">E-Waste Management</h1>
<p class="text-lg text-secondary mx-auto">End-to-end IT asset disposition with certified dismantling and military-grade data destruction.</p>
</div>
</section>
<section class="section">
<div class="container max-w-800 reveal">
<img src="assets/images/e-waste-management.jpg" alt="E-Waste Management" style="width:100%; border-radius: 12px; margin-bottom: 2rem; border: 1px solid var(--glass-border);">
<h2 class="text-2xl mb-4 text-accent">Overview</h2>
<p class="text-secondary mb-5">We provide comprehensive e-waste management solutions designed for modern enterprises. From secure collection logistics to complete material recovery, our certified processes ensure your retired IT assets are processed sustainably.</p>

<h2 class="text-2xl mb-4 text-accent mt-5">Process</h2>
<div class="glass-card mb-4"><h4>Step 1: Collection & Transportation</h4></div>
<div class="glass-card mb-4"><h4>Step 2: Certified Dismantling</h4></div>
<div class="glass-card mb-4"><h4>Step 3: Data Destruction (DoD 5220.22-M standard)</h4></div>
<div class="glass-card mb-4"><h4>Step 4: Material Segregation</h4></div>
<div class="glass-card mb-4"><h4>Step 5: Recycling & Recovery</h4></div>

<h2 class="text-2xl mb-4 text-accent mt-5">Certified Data Destruction</h2>
<p class="text-secondary mb-5">Storage media undergo DoD 5220.22-M standard wiping and physical shredding, with a serialised Certificate of Destruction issued for every batch.</p>

<h2 class="text-2xl mb-4 text-accent mt-5">What We Accept</h2>
<ul class="process-list text-secondary">
<li>Desktop Computers & Laptops</li><li>Servers & Enterprise Networking Gear</li><li>Mobile Devices & Tablets</li><li>Telecommunication Equipment</li>
</ul>

<div class="text-center mt-5"><a href="contact.html" class="btn btn-primary">Request a quote for e-waste management</a></div>
</div>
</section>
""",

"lithium-battery-recycling.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<p class="label label-accent">SERVICES</p>
<h1 class="hero-title text-gradient">Lithium Battery Recycling</h1>
<p class="text-lg text-secondary mx-auto">High-purity extraction of lithium and cobalt from EV and electronic batteries.</p>
</div>
</section>
<section class="section">
<div class="container max-w-800 reveal">
<img src="assets/images/lithium-battery.jpg" alt="Lithium Battery Recycling" style="width:100%; border-radius: 12px; margin-bottom: 2rem; border: 1px solid var(--glass-border);">
<h2 class="text-2xl mb-4 text-accent">Overview</h2>
<p class="text-secondary mb-5">Specialized processing for EV and electronic batteries, focusing on the high-purity extraction of lithium and cobalt to power tomorrow sustainably.</p>

<h2 class="text-2xl mb-4 text-accent mt-5">Process</h2>
<ul class="process-list text-secondary mb-5">
<li>Thermal Management & Safe Discharge</li><li>Black Mass Refining</li><li>Hydrometallurgical recovery</li>
</ul>

<h2 class="text-2xl mb-4 text-accent mt-5">Key Stats</h2>
<div class="grid two-col mb-5">
<div class="glass-card"><h3 class="highlight-stat">98%+</h3><p>Extraction efficiency</p></div>
<div class="glass-card"><h3>Materials</h3><p class="text-secondary">Cobalt, Lithium, Nickel</p></div>
</div>

<h2 class="text-2xl mb-4 text-accent mt-5">Applications</h2>
<ul class="process-list text-secondary mb-5">
<li>EV batteries</li><li>Electronic device batteries</li><li>Industrial batteries</li>
</ul>

<div class="text-center mt-5"><a href="contact.html" class="btn btn-primary">Request a Quote</a></div>
</div>
</section>
""",

"plastic-waste-recycling.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<p class="label label-accent">SERVICES</p>
<h1 class="hero-title text-gradient">Plastic Waste Recycling</h1>
<p class="text-lg text-secondary mx-auto">Advanced sorting and precision pelletizing into reusable manufacturing materials.</p>
</div>
</section>
<section class="section">
<div class="container max-w-800 reveal">
<img src="assets/images/plastic-recycling.jpg" alt="Plastic Waste Recycling" style="width:100%; border-radius: 12px; margin-bottom: 2rem; border: 1px solid var(--glass-border);">
<h2 class="text-2xl mb-4 text-accent">Overview</h2>
<p class="text-secondary mb-5">Advanced sorting and precision pelletizing into reusable manufacturing materials.</p>
<h2 class="text-2xl mb-4 text-accent">Process</h2>
<ul class="process-list text-secondary mb-5">
<li>Polymer Identification</li><li>Precision Pelletizing</li><li>Quality Control</li>
</ul>

<h2 class="text-2xl mb-4 text-accent mt-5">Stats & Types</h2>
<div class="glass-card mb-5"><h3 class="highlight-stat">10+</h3><p>Partner organizations</p></div>
<ul class="process-list text-secondary mb-5">
<li>Industrial plastic waste</li><li>Commercial plastic waste</li><li>E-waste plastic components</li>
</ul>

<div class="text-center mt-5"><a href="contact.html" class="btn btn-primary">Request a Quote</a></div>
</div>
</section>
""",

"paper-recycling.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<p class="label label-accent">SERVICES</p>
<h1 class="hero-title text-gradient">Paper Recycling</h1>
<p class="text-lg text-secondary mx-auto">Closed-loop processing that saves trees, conserves water and cuts corporate carbon.</p>
</div>
</section>
<section class="section">
<div class="container max-w-800 reveal">
<img src="assets/images/paper-recycling.jpg" alt="Paper Recycling" style="width:100%; border-radius: 12px; margin-bottom: 2rem; border: 1px solid var(--glass-border);">
<h2 class="text-2xl mb-4 text-accent">Overview</h2>
<p class="text-secondary mb-5">Closed-loop processing that saves trees, conserves water and cuts corporate carbon.</p>
<h2 class="text-2xl mb-4 text-accent">Environmental Impact</h2>
<ul class="process-list text-secondary mb-5">
<li>Trees saved</li><li>Water conserved</li><li>Carbon footprint reduction</li>
</ul>

<h2 class="text-2xl mb-4 text-accent mt-5">Process</h2>
<ul class="process-list text-secondary mb-5">
<li>Collection</li><li>Sorting</li><li>Pulping</li><li>Remanufacturing</li>
</ul>

<div class="text-center mt-5"><a href="contact.html" class="btn btn-primary">Request a Quote</a></div>
</div>
</section>
""",

"green-metal-recovery.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<p class="label label-accent">SERVICES</p>
<h1 class="hero-title text-gradient">Green Metal Recovery</h1>
<p class="text-lg text-secondary mx-auto">High-yield extraction of iron, copper and aluminum from complex waste streams.</p>
</div>
</section>
<section class="section">
<div class="container max-w-800 reveal">
<img src="assets/images/green-metal-recovery.jpg" alt="Green Metal Recovery" style="width:100%; border-radius: 12px; margin-bottom: 2rem; border: 1px solid var(--glass-border);">
<h2 class="text-2xl mb-4 text-accent">Overview</h2>
<p class="text-secondary mb-5">Securing essential raw materials for the circular economy through zero-harm processing.</p>

<h2 class="text-2xl mb-4 text-accent mt-5">Metals Recovered</h2>
<div class="metal-tags mb-5">
<span>Iron</span><span>Copper</span><span>Lithium</span><span>Cobalt</span><span>Aluminum</span><span>Gold</span><span>Silver</span><span>Palladium</span>
</div>

<h2 class="text-2xl mb-4 text-accent mt-5">Stats & Process</h2>
<div class="grid two-col mb-5">
<div class="glass-card"><h3 class="highlight-stat">99.5%</h3><p>Purity level</p></div>
<div class="glass-card"><h3 class="highlight-stat">22+</h3><p>Distinct metals recovered</p></div>
</div>
<ul class="process-list text-secondary mb-5">
<li>Hydrometallurgical extraction</li><li>Supply chain reintegration</li>
</ul>

<div class="text-center mt-5"><a href="contact.html" class="btn btn-primary">Request a Quote</a></div>
</div>
</section>
""",

"epr-consulting.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<p class="label label-accent">SERVICES</p>
<h1 class="hero-title text-gradient">EPR Consulting</h1>
<p class="text-lg text-secondary mx-auto">Extended Producer Responsibility compliance made simple.</p>
</div>
</section>
<section class="section">
<div class="container max-w-800 reveal">
<img src="assets/images/epr-consulting.jpg" alt="EPR Consulting" style="width:100%; border-radius: 12px; margin-bottom: 2rem; border: 1px solid var(--glass-border);">
<h2 class="text-2xl mb-4 text-accent">Overview</h2>
<p class="text-secondary mb-5">Regulatory navigation, compliance documentation and mandated EPR targets, handled.</p>

<h2 class="text-2xl mb-4 text-accent mt-5">What We Do</h2>
<ul class="process-list text-secondary mb-5">
<li>Strategic guidance for government regulations</li><li>Collection targets management</li><li>Statutory documentation</li><li>Government liaison</li>
</ul>

<h2 class="text-2xl mb-4 text-accent mt-5">Benefits</h2>
<ul class="process-list text-secondary mb-5">
<li>Seamless compliance</li><li>Transparent reporting</li><li>Legal mandate fulfillment</li>
</ul>

<div class="text-center mt-5"><a href="contact.html" class="btn btn-primary">Request a Quote</a></div>
</div>
</section>
""",

"impact.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<h1 class="hero-title text-gradient">Our Impact</h1>
<p class="text-lg text-secondary mx-auto">Measured. Not promised.</p>
</div>
</section>
<section class="section bg-secondary pt-0">
<div class="container text-center reveal">
<div class="grid three-col">
<div class="glass-card"><h3 class="huge-number"><span class="counter-val" data-target="1.6" data-suffix="Mt">0</span></h3><p>E-waste processed</p></div>
<div class="glass-card"><h3 class="huge-number"><span class="counter-val" data-target="98" data-suffix="%+">0</span></h3><p>Extraction efficiency</p></div>
<div class="glass-card"><h3 class="huge-number"><span class="counter-val" data-target="99.5" data-suffix="%">0</span></h3><p>Purity</p></div>
<div class="glass-card"><h3 class="huge-number"><span class="counter-val" data-target="342" data-suffix="+">0</span></h3><p>Happy clients</p></div>
<div class="glass-card"><h3 class="huge-number"><span class="counter-val" data-target="84" data-suffix="">0</span></h3><p>Partners</p></div>
<div class="glass-card"><h3 class="huge-number"><span class="counter-val" data-target="10" data-suffix="+">0</span></h3><p>Years experience</p></div>
</div>
</div>
</section>
<section class="section">
<div class="container grid two-col">
<div class="glass-card reveal">
<h3 class="text-2xl text-accent mb-4">Environmental Impact</h3>
<ul class="process-list text-secondary">
<li>CO2 reduction</li><li>Trees saved</li><li>Water conserved</li><li>Landfill diversion</li>
</ul>
</div>
<div class="glass-card reveal" style="transition-delay:0.1s;">
<h3 class="text-2xl text-accent mb-4">Social Impact</h3>
<ul class="process-list text-secondary">
<li>Jobs created</li><li>Communities served</li><li>Awareness programs</li>
</ul>
</div>
</div>
</section>
""",

"sustainability.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<h1 class="hero-title text-gradient">Sustainability</h1>
<p class="text-lg text-secondary mx-auto">Our commitment to the planet</p>
</div>
</section>
<section class="section pt-0">
<div class="container reveal">
<h2 class="section-title text-gradient text-center">Certifications</h2>
<div class="grid three-col mt-5">
<div class="glass-card">
<img src="assets/images/certifications/iso.png" alt="ISO Certification" style="max-height:80px; margin-bottom:1rem; opacity:0.8;">
<h3 class="text-accent mb-2">ISO Certification</h3>
<p class="text-secondary">Ensuring operational excellence, rigorous quality management, and strict environmental compliance across all asset disposition facilities.</p>
</div>
<div class="glass-card">
<img src="assets/images/certifications/grs.png" alt="Global Recycled Standard" style="max-height:80px; margin-bottom:1rem; opacity:0.8;">
<h3 class="text-accent mb-2">Global Recycled Standard</h3>
<p class="text-secondary">Verifying safe, equitable, and transparent supply chains from end-of-life processing all the way to secondary raw material production.</p>
</div>
<div class="glass-card">
<img src="assets/images/certifications/green-air.png" alt="Green Air Standard" style="max-height:80px; margin-bottom:1rem; opacity:0.8;">
<h3 class="text-accent mb-2">Green Air Standard</h3>
<p class="text-secondary">Maintaining industry-leading emission controls and zero-harm atmospheric processing during complex metal extraction and dismantling.</p>
</div>
</div>
</div>
</section>
<section class="section bg-secondary">
<div class="container grid two-col">
<div class="glass-card reveal">
<h3 class="text-2xl text-accent mb-4">Environmental Practices</h3>
<ul class="process-list text-secondary">
<li>Zero-harm atmospheric emissions</li><li>Minimal water discharge</li><li>Closed-loop processing</li><li>Carbon footprint reduction</li>
</ul>
</div>
<div class="glass-card reveal" style="transition-delay: 0.1s;">
<h3 class="text-2xl text-accent mb-4">Compliance & Initiatives</h3>
<ul class="process-list text-secondary">
<li>CPCB compliance</li><li>International standards</li><li>Renewable energy use</li><li>Community outreach</li>
</ul>
</div>
</div>
</section>
""",

"faq.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<p class="label label-accent">LOOKING FORWARD</p>
<h1 class="hero-title text-gradient">Frequently Asked Questions</h1>
</div>
</section>
<section class="section pt-0">
<div class="container max-w-800 reveal">
<div class="accordion">
<div class="glass-card accordion-item">
<h3 class="text-accent">What materials can be recovered?</h3>
<p class="mt-2 text-secondary">We utilize advanced, clean metallurgical processes to extract up to 99% of precious and base metals. This includes high-yield recovery of Gold, Silver, Palladium, Copper, Aluminum, and highly sought-after battery components like Lithium and Cobalt from end-of-life electronics.</p>
</div>
<div class="glass-card accordion-item mt-4">
<h3 class="text-accent">How do you guarantee data destruction?</h3>
<p class="mt-2 text-secondary">Security is our absolute priority. We employ military-grade, certified data destruction protocols. Assets undergo physical micro-shredding and cryptographic wiping to ensure complete data sanitization before any physical recycling begins. A comprehensive Certificate of Destruction is provided for your compliance audits.</p>
</div>
<div class="glass-card accordion-item mt-4">
<h3 class="text-accent">How does EPR consulting work?</h3>
<p class="mt-2 text-secondary">We act as an extension of your compliance team. EcoGreen manages the complex regulatory landscape on your behalf, handling collection targets, statutory documentation, and government liaison to ensure your brand meets all legal EPR mandates seamlessly and transparently.</p>
</div>
<div class="glass-card accordion-item mt-4">
<h3 class="text-accent">Are extraction processes safe?</h3>
<p class="mt-2 text-secondary">Unlike traditional smelting which causes severe pollution, our proprietary closed-loop hydrometallurgical technology operates with zero-harm atmospheric emissions and minimal water discharge. This drastically reduces the carbon footprint of metal recovery.</p>
</div>
<div class="glass-card accordion-item mt-4">
<h3 class="text-accent">Do you provide ESG tracking?</h3>
<p class="mt-2 text-secondary">Yes. Every batch processed through our facilities generates a comprehensive sustainability dashboard. We provide exact metrics on carbon offsets, materials recovered, and landfill diversion rates to directly support and validate your corporate ESG reporting.</p>
</div>
</div>
<div class="text-center mt-5"><a href="contact.html" class="btn btn-primary">Contact Us</a></div>
</div>
</section>
""",

"contact.html": """
<section class="section hero hero-gradient" style="min-height: 60vh;">
<div class="container text-center reveal">
<h1 class="hero-title text-gradient">Get In Touch</h1>
<p class="text-lg text-secondary mx-auto">Start your green transition today.</p>
</div>
</section>
<section class="section pt-0">
<div class="container grid two-col">
<div class="glass-card reveal">
<h2 class="text-2xl text-accent mb-4">Contact Form</h2>
<form class="contact-form" action="forms/contact-form.php" method="POST">
<div class="form-group"><label>Name *</label><input type="text" name="name" class="form-control" required></div>
<div class="form-group"><label>Email *</label><input type="email" name="email" class="form-control" required></div>
<div class="form-group"><label>Company</label><input type="text" name="company" class="form-control"></div>
<div class="form-group"><label>Service Interested In</label>
<select class="form-control" name="service">
<option>E-Waste Management</option>
<option>Lithium Battery Recycling</option>
<option>Plastic Waste Recycling</option>
<option>Paper Recycling</option>
<option>Green Metal Recovery</option>
<option>EPR Consulting</option>
</select>
</div>
<div class="form-group"><label>Message *</label><textarea class="form-control" name="message" required></textarea></div>
<button type="submit" class="btn btn-primary w-100" style="width:100%;">Submit</button>
</form>
</div>
<div class="glass-card reveal" style="transition-delay:0.1s;">
<h2 class="text-2xl text-accent mb-4">Contact Information</h2>
<p class="text-secondary mb-2"><strong>Address:</strong> 479, Habibpur, Dadri, Gr. Noida, Uttar Pradesh</p>
<p class="text-secondary mb-2"><strong>Phone:</strong> <a href="tel:+919319253708" style="color:var(--text-secondary); text-decoration:none;">+91 93192 53708</a></p>
<p class="text-secondary mb-4"><strong>Email:</strong> <a href="mailto:operation@ecogreen.eco" style="color:var(--text-secondary); text-decoration:none;">operation@ecogreen.eco</a></p>
<div class="map-placeholder mt-4 mb-4" style="height: 200px; background: rgba(0,0,0,0.2); border-radius:12px; display:flex; align-items:center; justify-content:center; border: 1px solid rgba(16,185,129,0.2); overflow:hidden;">
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14028.987679802093!2d77.5457224!3d28.5473133!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390cea64b8d81dd3%3A0xc6226197171e223!2sHabibpur%2C%20Greater%20Noida%2C%20Uttar%20Pradesh%20201306!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin" width="100%" height="100%" style="border:0; opacity:0.8; filter: grayscale(100%) invert(100%) contrast(1.2);" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
<h3 class="text-lg text-white mb-2">Social Media</h3>
<div class="social-links">
<a href="#">LinkedIn</a><a href="#">Twitter</a><a href="#">Facebook</a><a href="#">Instagram</a>
</div>
</div>
</div>
</section>
"""
}

for page_name, page_content in pages.items():
    with open(page_name, "w", encoding="utf-8") as f:
        f.write(header + page_content + footer)

print("Generated 13 pages successfully with updated local asset paths.")
