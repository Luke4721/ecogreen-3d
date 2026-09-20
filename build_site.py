import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Eco Green Recyclers</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  
  <!-- Navigation -->
  <nav class="navbar">
    <div class="container nav-container">
      <a href="index.html" class="logo">Eco Green</a>
      <ul class="nav-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About Us</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#impact">Sustainability</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <a href="#contact" class="btn btn-primary">REQUEST QUOTE</a>
    </div>
  </nav>

  <!-- WebGL Background Canvas (z-index: 0) -->
  <canvas id="webgl-canvas"></canvas>

  <main class="ui-layer">
    
    <!-- SECTION 1: HERO -->
    <section id="home" class="section hero">
      <div class="container hero-grid">
        <div class="hero-content reveal">
          <p class="label label-accent">SUSTAINABLE SOLUTIONS • SINCE 2015</p>
          <h1 class="hero-title">India's specialist in e-waste management.</h1>
          <p class="hero-subtitle">Certified IT asset disposition, military-grade data destruction and high-purity metal recovery — the full e-waste lifecycle, handled under one compliant roof.</p>
          <div class="btn-group">
            <a href="#services" class="btn btn-primary">Explore solutions</a>
            <a href="#about" class="btn btn-outline">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right:8px;"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              See how it works
            </a>
          </div>
        </div>
        <div class="hero-stats reveal">
          <div class="glass-card stat-pill">
            <span class="stat-pill-num">10+</span>
            <span class="stat-pill-label">YEARS</span>
          </div>
          <div class="glass-card stat-pill">
            <span class="stat-pill-num">342+</span>
            <span class="stat-pill-label">CLIENTS</span>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: SHOCKING FIGURES -->
    <section id="impact" class="section pt-0">
      <div class="container">
        <p class="label label-accent text-center reveal">SHOCKING FIGURES</p>
        <div class="grid three-col mt-4">
          <div class="glass-card reveal">
            <h2 class="huge-number">1.6Mt</h2>
            <p>million tonnes of e-waste India generates every year — the world's third-largest pile.</p>
          </div>
          <div class="glass-card reveal" style="transition-delay: 0.1s;">
            <h2 class="huge-number">32%</h2>
            <p>one in five devices handed to informal recyclers ends up burnt in the open.</p>
          </div>
          <div class="glass-card reveal" style="transition-delay: 0.2s;">
            <h2 class="huge-number">2.6Mt</h2>
            <p>million tonnes of embodied carbon thrown away with unrecycled circuitry — ore we already mined</p>
          </div>
        </div>
        <p class="source-text reveal mt-4 text-center">GLOBAL E-WASTE MONITOR 2024 • CPCB ANNUAL REPORT — SOURCES CITED, NOT FEARED.</p>
      </div>
    </section>

    <!-- SECTION 3: "A FIGHT FOR WHAT'S NEXT" -->
    <section class="section dark-section">
      <div class="container grid two-col align-center">
        <div class="reveal">
          <h2 class="section-title text-white">A fight for what's next.</h2>
          <p class="text-lg text-white-alpha">Every retired device is a choice: a landfill burning in the open, or a vault of metals re-entering the economy. Ecogreen exists to make the second choice the easy one — certified, tracked and reported end to end, for enterprises that answer to their own ESG commitments.</p>
        </div>
        <div class="dark-card reveal" style="transition-delay: 0.2s;">
          <p class="label label-accent">GREEN METALS RECOVERED</p>
          <p class="text-white mt-2">Every retired asset is a vein of ore we have already mined once. Recovering it is the cheapest, cleanest tonne of metal on Earth.</p>
          <div class="metal-tags mt-4">
            <span>Iron</span>
            <span>Copper</span>
            <span>Lithium</span>
            <span>Cobalt</span>
            <span>Aluminum</span>
          </div>
          <a href="#services" class="btn btn-outline-white mt-4">EXPLORE GREEN METAL RECOVERY &rarr;</a>
        </div>
      </div>
    </section>

    <!-- SECTION 4: MARQUEE BANNER -->
    <div class="marquee-section dark-bg">
        <h2 class="marquee-text">TAKE ACTION <span class="text-accent">&</span> RECYCLE RIGHT &nbsp;&nbsp;&nbsp; TAKE ACTION <span class="text-accent">&</span> RECYCLE RIGHT &nbsp;&nbsp;&nbsp; TAKE ACTION <span class="text-accent">&</span> RECYCLE RIGHT &nbsp;&nbsp;&nbsp; TAKE ACTION <span class="text-accent">&</span> RECYCLE RIGHT &nbsp;&nbsp;&nbsp; TAKE ACTION <span class="text-accent">&</span> RECYCLE RIGHT &nbsp;&nbsp;&nbsp; TAKE ACTION <span class="text-accent">&</span> RECYCLE RIGHT</h2>
    </div>

    <!-- SECTION 5: EXTRACTION FIGURES -->
    <section class="section">
      <div class="container text-center">
        <p class="label label-accent reveal">MEASURED, NOT PROMISED</p>
        <h2 class="section-title reveal">The extraction figures behind every batch</h2>
        
        <div class="grid two-col mt-4">
          <div class="glass-card extraction-card reveal">
            <h3 class="highlight-stat">98%+</h3>
            <h4 class="mt-2">EXTRACTION EFFICIENCY</h4>
            <p class="mt-2">Safe discharge and hydrometallurgical recovery of cobalt, lithium and nickel.</p>
          </div>
          <div class="glass-card extraction-card reveal" style="transition-delay: 0.2s;">
            <h3 class="highlight-stat">99.5%</h3>
            <h4 class="mt-2">Purity level of recovered metals</h4>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 6: SERVICES GRID -->
    <section id="services" class="section">
      <div class="container">
        <div class="flex-between reveal">
          <div>
            <p class="label label-accent">SERVICES</p>
            <h2 class="section-title" style="margin-bottom: 0;">Expert collection, recycling, and disposal</h2>
          </div>
          <a href="#services" class="btn btn-outline">VIEW ALL SERVICES</a>
        </div>
        
        <div class="grid services-grid mt-4">
          <!-- Card 1 -->
          <div class="service-image-card glass-card-strict reveal">
            <img src="https://images.unsplash.com/photo-1550005973-78ce3f78fa45?w=800&q=80" alt="E-Waste Management">
            <div class="card-content">
              <h3>E-Waste Management</h3>
              <p>End-to-end IT asset disposition with certified dismantling and military-grade data destruction.</p>
              <a href="#" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
          <!-- Card 2 -->
          <div class="service-image-card glass-card-strict reveal" style="transition-delay: 0.1s;">
            <img src="https://images.unsplash.com/photo-1620802051778-e8cb5043ccbc?w=800&q=80" alt="Lithium Battery Recycling">
            <div class="card-content">
              <h3>Lithium Battery Recycling</h3>
              <p>High-purity extraction of lithium and cobalt from EV and electronic batteries.</p>
              <a href="#" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
          <!-- Card 3 -->
          <div class="service-image-card glass-card-strict reveal" style="transition-delay: 0.2s;">
            <img src="https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?w=800&q=80" alt="Plastic Waste Recycling">
            <div class="card-content">
              <h3>Plastic Waste Recycling</h3>
              <p>Advanced sorting and precision pelletizing into reusable manufacturing materials.</p>
              <a href="#" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
          <!-- Card 4 -->
          <div class="service-image-card glass-card-strict reveal">
            <img src="https://images.unsplash.com/photo-1603351154351-5e2d0600bb77?w=800&q=80" alt="Paper Recycling">
            <div class="card-content">
              <h3>Paper Recycling</h3>
              <p>Closed-loop processing that saves trees, conserves water and cuts corporate carbon.</p>
              <a href="#" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
          <!-- Card 5 -->
          <div class="service-image-card glass-card-strict reveal" style="transition-delay: 0.1s;">
            <img src="https://images.unsplash.com/photo-1581093458791-9f3c3900df4b?w=800&q=80" alt="Green Metal Recovery">
            <div class="card-content">
              <h3>Green Metal Recovery</h3>
              <p>High-yield extraction of iron, copper and aluminum from complex waste streams.</p>
              <a href="#" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
          <!-- Card 6 -->
          <div class="service-image-card glass-card-strict reveal" style="transition-delay: 0.2s;">
            <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&q=80" alt="EPR Consulting">
            <div class="card-content">
              <h3>EPR Consulting</h3>
              <p>Regulatory navigation, compliance documentation and mandated EPR targets, handled.</p>
              <a href="#" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 7: WHY ENTERPRISES TRUST -->
    <section class="section bg-glass-panel">
      <div class="container grid two-col align-center">
        <div class="reveal">
          <h2 class="section-title">Why Enterprises trust ECO GREEN</h2>
          <p class="text-lg">We empower global brands to achieve zero-waste goals through state-of-the-art recycling technology and uncompromising data security. By integrating circular economy principles with pan-India logistics, we ensure your retired assets are managed with absolute transparency and 100% regulatory compliance.</p>
        </div>
        <div class="grid two-col small-gap reveal" style="transition-delay: 0.2s;">
          <div class="glass-card text-center py-4">
            <h3 class="text-accent text-3xl">10</h3>
            <p class="font-bold uppercase text-sm mt-1">Years Experience</p>
          </div>
          <div class="glass-card text-center py-4">
            <h3 class="text-accent text-3xl">8</h3>
            <p class="font-bold uppercase text-sm mt-1">Awards Won</p>
          </div>
          <div class="glass-card text-center py-4">
            <h3 class="text-accent text-3xl">342</h3>
            <p class="font-bold uppercase text-sm mt-1">Happy Clients</p>
          </div>
          <div class="glass-card text-center py-4">
            <h3 class="text-accent text-3xl">84</h3>
            <p class="font-bold uppercase text-sm mt-1">Partners</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8: GREEN METAL RECOVERY HIGHLIGHT -->
    <section class="section text-center">
      <div class="container reveal">
        <p class="label label-accent">REDEFINING GREEN METALS</p>
        <div class="metal-pill-list mt-4">
          <span>Iron</span> &middot; 
          <span>Copper</span> &middot; 
          <span>Lithium</span> &middot; 
          <span>Cobalt</span> &middot; 
          <span>Aluminum</span>
        </div>
      </div>
    </section>

    <!-- SECTION 9: PARTNERS/MARQUEE -->
    <section class="section pt-0">
      <div class="container text-center reveal">
        <p class="label label-accent">OUR PARTNERS</p>
        <h2 class="section-title">Trusted by Industry Leaders</h2>
        <p class="text-lg mx-auto" style="max-width: 800px;">Partnering with global brands to ensure secure, compliant, and zero-waste IT asset disposition and green metal recovery.</p>
        
        <div class="partners-marquee mt-4 glass-card">
          <div class="partners-track">
            <span>TECHCORP</span> &bull; <span>GLOBAL INDUSTRIES</span> &bull; <span>FINANCE BANK</span> &bull; <span>INNOVATE AI</span> &bull; <span>DATA SECURE</span> &bull;
            <span>TECHCORP</span> &bull; <span>GLOBAL INDUSTRIES</span> &bull; <span>FINANCE BANK</span> &bull; <span>INNOVATE AI</span> &bull; <span>DATA SECURE</span>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 10: ABOUT US SECTION -->
    <section id="about" class="section dark-section">
      <div class="container">
        <div class="reveal text-center mb-5">
          <p class="label label-accent">ABOUT US</p>
          <h2 class="section-title text-white mx-auto" style="max-width: 900px;">Empowering sustainable futures through responsible e-waste management and recycling solutions.</h2>
        </div>

        <div class="grid three-col mt-5">
          <div class="dark-card reveal">
            <h3 class="highlight-stat">98%+</h3>
            <p class="text-white mt-2 mb-4">Extraction efficiency on e-waste and lithium-ion cells — safe discharge and hydrometallurgical recovery of cobalt, lithium and nickel.</p>
            <ul class="process-list">
              <li>Thermal Management & Safe Discharge</li>
              <li>Black Mass Refining</li>
            </ul>
          </div>
          <div class="dark-card reveal" style="transition-delay: 0.1s;">
            <h3 class="highlight-stat">10+</h3>
            <p class="text-white mt-2 mb-4">Partner organizations across industrial and e-waste plastic recovery streams</p>
            <ul class="process-list">
              <li>Polymer Identification</li>
              <li>Precision Pelletizing</li>
            </ul>
          </div>
          <div class="dark-card reveal" style="transition-delay: 0.2s;">
            <h3 class="highlight-stat">22+</h3>
            <p class="text-white mt-2">Distinct green metals recovered from e-waste at greater than 99.5% purity, reintegrated into manufacturing supply chains.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 11: SCROLLING TAGS -->
    <div class="marquee-section transparent-bg border-y">
        <h2 class="marquee-text outline-text">RECYCLING &nbsp;&bull;&nbsp; GOGREEN &nbsp;&bull;&nbsp; ECOCONSCIOUS &nbsp;&bull;&nbsp; SUSTAINABILITY &nbsp;&bull;&nbsp; ECOFRIENDLY &nbsp;&bull;&nbsp; GREENLIVING &nbsp;&bull;&nbsp; RECYCLING &nbsp;&bull;&nbsp; GOGREEN &nbsp;&bull;&nbsp; ECOCONSCIOUS &nbsp;&bull;&nbsp; SUSTAINABILITY &nbsp;&bull;&nbsp; ECOFRIENDLY &nbsp;&bull;&nbsp; GREENLIVING</h2>
    </div>

    <!-- SECTION 12: CERTIFICATIONS -->
    <section class="section">
      <div class="container">
        <div class="text-center reveal">
          <p class="label label-accent">VERIFIED COMPLIANCE</p>
          <h2 class="section-title">Certifications & Achievements</h2>
        </div>
        
        <div class="grid three-col mt-4">
          <div class="glass-card reveal">
            <h3>ISO Certification</h3>
            <p class="mt-2">Ensuring operational excellence, rigorous quality management, and strict environmental compliance across all asset disposition facilities.</p>
          </div>
          <div class="glass-card reveal" style="transition-delay: 0.1s;">
            <h3>Global Recycled Standard</h3>
            <p class="mt-2">Verifying safe, equitable, and transparent supply chains from end-of-life processing all the way to secondary raw material production.</p>
          </div>
          <div class="glass-card reveal" style="transition-delay: 0.2s;">
            <h3>Green Air Standard</h3>
            <p class="mt-2">Maintaining industry-leading emission controls and zero-harm atmospheric processing during complex metal extraction and dismantling.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 13: FAQ -->
    <section class="section pt-0">
      <div class="container max-w-800">
        <div class="text-center reveal">
          <p class="label label-accent">LOOKING FORWARD</p>
          <h2 class="section-title">Future Vision & FAQs</h2>
        </div>
        
        <div class="accordion mt-4">
          <div class="glass-card accordion-item reveal">
            <h3>What specific materials and metals can be recovered?</h3>
            <p class="mt-2 text-muted">We utilize advanced, clean metallurgical processes to extract up to 99% of precious and base metals. This includes high-yield recovery of Gold, Silver, Palladium, Copper, Aluminum, and highly sought-after battery components like Lithium and Cobalt from end-of-life electronics.</p>
          </div>
          <div class="glass-card accordion-item reveal">
            <h3>How do you guarantee the destruction of sensitive corporate data?</h3>
            <p class="mt-2 text-muted">Security is our absolute priority. We employ military-grade, certified data destruction protocols. Assets undergo physical micro-shredding and cryptographic wiping to ensure complete data sanitization before any physical recycling begins. A comprehensive Certificate of Destruction is provided for your compliance audits.</p>
          </div>
          <div class="glass-card accordion-item reveal">
            <h3>How does the EPR (Extended Producer Responsibility) consulting work?</h3>
            <p class="mt-2 text-muted">We act as an extension of your compliance team. EcoGreen manages the complex regulatory landscape on your behalf, handling collection targets, statutory documentation, and government liaison to ensure your brand meets all legal EPR mandates seamlessly and transparently.</p>
          </div>
          <div class="glass-card accordion-item reveal">
            <h3>Are your extraction processes environmentally safe?</h3>
            <p class="mt-2 text-muted">Unlike traditional smelting which causes severe pollution, our proprietary closed-loop hydrometallurgical technology operates with zero-harm atmospheric emissions and minimal water discharge. This drastically reduces the carbon footprint of metal recovery.</p>
          </div>
          <div class="glass-card accordion-item reveal">
            <h3>Do you provide tracking and reporting for ESG goals?</h3>
            <p class="mt-2 text-muted">Yes. Every batch processed through our facilities generates a comprehensive sustainability dashboard. We provide exact metrics on carbon offsets, materials recovered, and landfill diversion rates to directly support and validate your corporate ESG reporting.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 14: VISION QUOTE -->
    <section class="section dark-section text-center py-10">
      <div class="container">
        <h2 class="quote-text text-white reveal">"Our vision is a zero-waste future driven by continuous innovation, where end-of-life technology fuels the next generation of manufacturing."</h2>
      </div>
    </section>

    <!-- SECTION 15: FOOTER -->
    <footer id="contact" class="footer dark-section">
      <div class="container">
        <div class="grid four-col">
          <div class="footer-col reveal">
            <h3 class="logo text-white mb-2">Eco Green Recyclers</h3>
            <p class="text-white-alpha mb-4 text-sm">Industrial-scale materials recovery pioneer — certified IT asset disposition, green metal recovery and EPR compliance for enterprises across India.</p>
            <div class="social-links">
              <a href="#">LinkedIn</a>
              <a href="#">Twitter</a>
              <a href="#">Facebook</a>
              <a href="#">Instagram</a>
            </div>
          </div>
          <div class="footer-col reveal" style="transition-delay: 0.1s;">
            <h4>COMPANY</h4>
            <ul>
              <li><a href="#">Home</a></li>
              <li><a href="#">About Us</a></li>
              <li><a href="#">Business Solutions</a></li>
              <li><a href="#">Journey of One Device</a></li>
              <li><a href="#">Sustainability</a></li>
              <li><a href="#">Careers</a></li>
            </ul>
          </div>
          <div class="footer-col reveal" style="transition-delay: 0.2s;">
            <h4>SERVICES</h4>
            <ul>
              <li><a href="#">E-Waste Management</a></li>
              <li><a href="#">Lithium Battery Recycling</a></li>
              <li><a href="#">Plastic Waste Recycling</a></li>
              <li><a href="#">Paper Recycling</a></li>
              <li><a href="#">Green Metal Recovery</a></li>
              <li><a href="#">EPR Consulting</a></li>
            </ul>
          </div>
          <div class="footer-col reveal" style="transition-delay: 0.3s;">
            <h4>GET IN TOUCH</h4>
            <p class="text-white-alpha text-sm mb-2"><a href="mailto:operation@ecogreen.eco" class="hover-white">operation@ecogreen.eco</a></p>
            <p class="text-white-alpha text-sm mb-2"><a href="tel:+919319253708" class="hover-white">+91 93192 53708</a></p>
            <p class="text-white-alpha text-sm mb-4">479, Habibpur, Dadri,<br>Gr. Noida, Uttar Pradesh</p>
            <a href="#" class="btn btn-primary btn-sm">Start your green transition &rarr;</a>
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

  </main>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="script.js"></script>
</body>
</html>"""

css_content = """
:root {
  /* Theme Colors */
  --bg-color: #FAFAF9;
  --text-dark: #1F2937;
  --text-muted: #4B5563;
  --accent: #10B981;
  --accent-hover: #059669;
  --dark-bg: #1B4332;
  --white: #FFFFFF;
  
  /* Glassmorphism Variables */
  --glass-bg: rgba(255, 255, 255, 0.6);
  --glass-border: rgba(255, 255, 255, 0.4);
}

/* Reset & Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-color);
  color: var(--text-dark);
  line-height: 1.6;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* Cinematic Film Grain Overlay */
body::after { 
  content: ""; 
  position: fixed; 
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 100%; 
  pointer-events: none; 
  z-index: 9999; 
  opacity: 0.04; 
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E"); 
}

/* WebGL Background */
#webgl-canvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 0;
  pointer-events: none;
}

/* UI Overlay */
.ui-layer {
  position: relative;
  z-index: 10;
}

/* Navbar */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background: rgba(250, 250, 249, 0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--glass-border);
  z-index: 100;
  padding: 1rem 0;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--text-dark);
  text-decoration: none;
  letter-spacing: -0.05em;
}

.nav-links {
  display: flex;
  gap: 2.5rem;
  list-style: none;
}

.nav-links a {
  color: var(--text-dark);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  transition: color 0.3s;
}

.nav-links a:hover {
  color: var(--accent);
}

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 2rem;
}

.max-w-800 { max-width: 800px; margin: 0 auto; }
.text-center { text-align: center; }
.text-white { color: var(--white); }
.text-white-alpha { color: rgba(255,255,255,0.7); }
.text-accent { color: var(--accent); }
.text-muted { color: var(--text-muted); }
.font-bold { font-weight: 700; }
.uppercase { text-transform: uppercase; }
.text-sm { font-size: 0.875rem; }
.text-3xl { font-size: 2.5rem; font-weight: 800; letter-spacing: -0.05em; }

/* Typography */
h1, h2, h3, h4 { font-weight: 800; letter-spacing: -0.03em; line-height: 1.2; }

.section-title { font-size: clamp(2rem, 5vw, 3.5rem); margin-bottom: 1.5rem; }
.text-lg { font-size: 1.125rem; }

.label { 
  font-weight: 700; 
  letter-spacing: 0.1em; 
  font-size: 0.8rem; 
  margin-bottom: 1rem; 
  text-transform: uppercase; 
}
.label-accent { color: var(--accent); }

/* Spacing */
.mt-1 { margin-top: 0.25rem; }
.mt-2 { margin-top: 0.5rem; }
.mt-4 { margin-top: 2rem; }
.mt-5 { margin-top: 3rem; }
.mb-2 { margin-bottom: 0.5rem; }
.mb-4 { margin-bottom: 1.5rem; }
.mb-5 { margin-bottom: 3rem; }
.py-4 { padding-top: 2rem; padding-bottom: 2rem; }
.py-10 { padding-top: 8rem; padding-bottom: 8rem; }
.pt-0 { padding-top: 0 !important; }

/* Sections */
.section { padding: 8rem 0; }
.bg-glass-panel { background: linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.3) 50%, rgba(255,255,255,0) 100%); }

/* Dark Sections */
.dark-section {
  background-color: var(--dark-bg);
  color: var(--white);
}
.dark-card {
  background: rgba(255,255,255,0.05);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255,255,255,0.1);
  padding: 2.5rem;
  border-radius: 24px;
}

/* Hero Section */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding-top: 6rem;
}
.hero-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 4rem;
  align-items: center;
}
.hero-title {
  font-size: clamp(3.5rem, 7vw, 5.5rem);
  line-height: 1.05;
  margin-bottom: 1.5rem;
}
.hero-subtitle {
  font-size: clamp(1.1rem, 2vw, 1.25rem);
  max-width: 55ch;
  margin-bottom: 2.5rem;
  color: var(--text-muted);
  font-weight: 500;
}
.hero-stats {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  align-items: flex-end;
}
.stat-pill {
  display: flex;
  flex-direction: column;
  padding: 1.5rem 2.5rem;
  border-radius: 24px;
  min-width: 200px;
}
.stat-pill-num { font-size: 2.5rem; font-weight: 800; color: var(--accent); line-height: 1; }
.stat-pill-label { font-size: 0.8rem; font-weight: 700; letter-spacing: 0.1em; color: var(--text-dark); margin-top: 0.25rem; }

/* Buttons */
.btn-group { display: flex; gap: 1rem; flex-wrap: wrap; }
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 1rem 2rem; border-radius: 999px; font-weight: 600;
  text-decoration: none; transition: all 0.3s ease; font-size: 1rem; cursor: pointer;
}
.btn-sm { padding: 0.75rem 1.5rem; font-size: 0.9rem; }
.btn-primary { background-color: var(--accent); color: #fff; }
.btn-primary:hover { background-color: var(--accent-hover); transform: translateY(-2px); box-shadow: 0 10px 20px rgba(16, 185, 129, 0.2); }
.btn-outline { background-color: transparent; color: var(--text-dark); border: 1px solid var(--text-dark); }
.btn-outline:hover { background-color: var(--glass-bg); transform: translateY(-2px); }
.btn-outline-white { background-color: transparent; color: var(--white); border: 1px solid rgba(255,255,255,0.5); }
.btn-outline-white:hover { background-color: var(--white); color: var(--text-dark); }
.hover-white:hover { color: var(--white); text-decoration: underline; }

/* Glassmorphism Cards */
.glass-card {
  background: var(--glass-bg);
  backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
  border: 1px solid var(--glass-border); border-radius: 24px;
  padding: 2.5rem; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.03);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.glass-card-strict {
  background: rgba(255,255,255,0.6);
  backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(255,255,255,0.4);
}
.glass-card:hover, .glass-card-strict:hover { transform: translateY(-8px); box-shadow: 0 16px 48px rgba(0, 0, 0, 0.06); }

/* Grids */
.grid { display: grid; gap: 2rem; }
.two-col { grid-template-columns: 1fr; }
.three-col { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
.four-col { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
.align-center { align-items: center; }
.flex-between { display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem; }
.small-gap { gap: 1rem; }

@media (min-width: 992px) {
  .two-col { grid-template-columns: 1fr 1fr; gap: 4rem; }
}

/* Stats */
.huge-number { font-size: clamp(3.5rem, 6vw, 5rem); color: var(--accent); line-height: 1; margin-bottom: 1rem; letter-spacing: -0.05em; }
.source-text { font-size: 0.7rem; font-weight: 700; opacity: 0.6; letter-spacing: 0.1em; }
.highlight-stat { font-size: clamp(3.5rem, 6vw, 5rem); color: var(--accent); line-height: 1; letter-spacing: -0.05em; }

/* Metal Tags */
.metal-tags, .metal-pill-list { display: flex; flex-wrap: wrap; gap: 0.75rem; }
.metal-tags span { padding: 0.5rem 1.25rem; background: rgba(255,255,255,0.1); border-radius: 99px; font-size: 0.875rem; font-weight: 600; border: 1px solid rgba(255,255,255,0.2); color: white; }
.metal-pill-list { justify-content: center; align-items: center; font-size: 1.5rem; font-weight: 600; color: var(--text-dark); }
.metal-pill-list span { color: var(--accent); }

/* Marquee */
.marquee-section { padding: 2rem 0; overflow: hidden; white-space: nowrap; border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); }
.dark-bg { background: var(--dark-bg); }
.transparent-bg { background: transparent; }
.border-y { border-top: 1px solid rgba(0,0,0,0.1); border-bottom: 1px solid rgba(0,0,0,0.1); }
.marquee-text { font-size: 3rem; margin: 0; display: inline-block; animation: scrollText 20s linear infinite; color: white; }
.outline-text { color: transparent; -webkit-text-stroke: 1px var(--text-dark); }
@keyframes scrollText { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

/* Partners Marquee */
.partners-marquee { overflow: hidden; white-space: nowrap; padding: 1.5rem 0 !important; }
.partners-track { display: inline-block; animation: scrollText 30s linear infinite; font-weight: 800; font-size: 1.5rem; letter-spacing: 0.1em; color: var(--text-muted); }
.partners-track span { margin: 0 2rem; color: var(--text-dark); }

/* Services Image Grid */
.services-grid { grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; }
.service-image-card { border-radius: 24px; overflow: hidden; transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s; display: flex; flex-direction: column; }
.service-image-card img { width: 100%; height: 240px; object-fit: cover; border-radius: 24px 24px 0 0; }
.card-content { padding: 2.5rem; flex: 1; display: flex; flex-direction: column; }
.card-content h3 { margin-bottom: 1rem; font-size: 1.5rem; }
.card-content p { margin-bottom: 2rem; flex: 1; color: var(--text-muted); }
.read-more { font-weight: 700; color: var(--text-dark); text-decoration: none; font-size: 0.9rem; letter-spacing: 0.05em; transition: color 0.2s; }
.read-more:hover { color: var(--accent); }

/* Lists */
.process-list { list-style: none; color: rgba(255,255,255,0.8); }
.process-list li { margin-bottom: 0.5rem; position: relative; padding-left: 1.5rem; }
.process-list li::before { content: "→"; position: absolute; left: 0; color: var(--accent); font-weight: bold; }

/* Accordion */
.accordion { display: flex; flex-direction: column; gap: 1rem; }
.accordion-item { border-radius: 16px; padding: 2rem; cursor: pointer; }
.accordion-item h3 { font-size: 1.25rem; }

/* Vision Quote */
.quote-text { font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 500; max-width: 1000px; margin: 0 auto; line-height: 1.2; letter-spacing: -0.03em; }

/* Footer */
.footer { padding: 6rem 0 2rem; border-top: 1px solid rgba(255,255,255,0.1); }
.footer ul { list-style: none; }
.footer ul li { margin-bottom: 0.75rem; }
.footer a { color: var(--white); text-decoration: none; opacity: 0.7; transition: opacity 0.3s; font-size: 0.95rem; }
.footer a:hover { opacity: 1; color: var(--accent); }
.footer h4 { margin-bottom: 2rem; color: #fff; font-size: 0.9rem; letter-spacing: 0.1em; text-transform: uppercase; }
.social-links { display: flex; gap: 1.5rem; flex-wrap: wrap; margin-top: 2rem; }
.social-links a { font-weight: 600; font-size: 0.9rem; letter-spacing: 0.05em; text-transform: uppercase; }
.footer-bottom { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; opacity: 0.6; font-size: 0.85rem; flex-wrap: wrap; gap: 1rem; }
.footer-legal a { margin-left: 1rem; }

/* Animations */
.reveal { opacity: 0; transform: translateY(40px); transition: opacity 1s cubic-bezier(0.16, 1, 0.3, 1), transform 1s cubic-bezier(0.16, 1, 0.3, 1); }
.reveal.active { opacity: 1; transform: translateY(0); }

/* Responsive adjustments */
@media (max-width: 991px) {
  .hero-grid { grid-template-columns: 1fr; gap: 2rem; }
  .hero-stats { flex-direction: row; align-items: center; justify-content: flex-start; }
  .stat-pill { min-width: auto; padding: 1.5rem; }
  .nav-links { display: none; }
}
"""

script_content = """document.addEventListener('DOMContentLoaded', () => {
    /* ═══════════════════════════════════════════════════════════════════════════
       1. INTERSECTION OBSERVER (Scroll Reveals)
       ═══════════════════════════════════════════════════════════════════════════ */
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

    /* ═══════════════════════════════════════════════════════════════════════════
       2. THREE.JS HYBRID BACKGROUND: LIQUID METAL + DATA AURORA
       ═══════════════════════════════════════════════════════════════════════════ */
    const canvas = document.getElementById('webgl-canvas');
    if (!canvas) return;

    const isMobile = window.innerWidth < 768;
    const PIXEL_RATIO = isMobile ? 1 : Math.min(window.devicePixelRatio, 2);

    const scene = new THREE.Scene();
    scene.background = new THREE.Color('#FAFAF9');

    // Camera
    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
    camera.position.set(0, 0, 12);

    // Renderer
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: !isMobile, alpha: false });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(PIXEL_RATIO);
    renderer.outputEncoding = THREE.sRGBEncoding;

    // Light Setup (CRITICAL FOR AURA)
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
    scene.add(ambientLight);

    const keyLight = new THREE.DirectionalLight(0xffffff, 1.5);
    keyLight.position.set(5, 8, 5);
    scene.add(keyLight);

    const fillLight = new THREE.DirectionalLight(0x10B981, 0.8);
    fillLight.position.set(-5, 3, 3);
    scene.add(fillLight);

    const goldAccent = new THREE.PointLight(0xFFD700, 1.2, 50);
    goldAccent.position.set(-3, -5, 2);
    scene.add(goldAccent);

    const backGlow = new THREE.PointLight(0x34D399, 0.6, 50);
    backGlow.position.set(0, 0, -8);
    scene.add(backGlow);

    // ==========================================
    // LAYER 1: LIQUID METAL CORE
    // ==========================================
    const coreDetail = isMobile ? 4 : 8; // Icosahedron detail
    const coreGeo = new THREE.IcosahedronGeometry(2.5, coreDetail);
    
    // Store original positions for displacement calculation
    const posAttribute = coreGeo.attributes.position;
    coreGeo.userData.originalPositions = new Float32Array(posAttribute.count * 3);
    for(let i=0; i < posAttribute.count; i++) {
        coreGeo.userData.originalPositions[i*3] = posAttribute.getX(i);
        coreGeo.userData.originalPositions[i*3+1] = posAttribute.getY(i);
        coreGeo.userData.originalPositions[i*3+2] = posAttribute.getZ(i);
    }

    const coreMat = new THREE.MeshPhysicalMaterial({
        color: 0x10B981, metalness: 1.0, roughness: 0.05,
        clearcoat: 1.0, clearcoatRoughness: 0.03, reflectivity: 1.0,
        transparent: true, opacity: 0.9
    });
    
    const liquidCore = new THREE.Mesh(coreGeo, coreMat);
    liquidCore.position.set(1.5, 0, 0); // slightly offset to right
    scene.add(liquidCore);

    // ==========================================
    // LAYER 2: FLOWING AURORA RIBBONS
    // ==========================================
    const auroraGroup = new THREE.Group();
    scene.add(auroraGroup);
    
    const auroraMat = new THREE.MeshPhysicalMaterial({
        color: 0x10B981, transmission: 0.9, opacity: 0.3,
        roughness: 0.2, metalness: 0.1, transparent: true, side: THREE.DoubleSide
    });
    const auroraMatLight = new THREE.MeshPhysicalMaterial({
        color: 0x34D399, transmission: 0.9, opacity: 0.2,
        roughness: 0.2, metalness: 0.1, transparent: true, side: THREE.DoubleSide
    });

    const ribbons = [];
    const ribbonCount = isMobile ? 4 : 7;
    for (let i=0; i<ribbonCount; i++) {
        const radius = 8 + Math.random() * 4;
        const tube = 0.3 + Math.random() * 0.2;
        const geo = new THREE.TorusGeometry(radius, tube, 8, 100);
        const mesh = new THREE.Mesh(geo, Math.random() > 0.5 ? auroraMat : auroraMatLight);
        
        mesh.position.set((Math.random()-0.5)*10, (Math.random()-0.5)*10, (Math.random()-0.5)*15 - 5);
        mesh.rotation.set(Math.random()*Math.PI, Math.random()*Math.PI, Math.random()*Math.PI);
        
        mesh.userData = {
            rx: (Math.random() - 0.5) * 0.002,
            ry: (Math.random() - 0.5) * 0.002,
            rz: (Math.random() - 0.5) * 0.002
        };
        
        ribbons.push(mesh);
        auroraGroup.add(mesh);
    }

    // ==========================================
    // LAYER 3: FLOATING PARTICLE DUST
    // ==========================================
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
        pOpacities[i] = 0.2 + Math.random() * 0.6;
        
        dustData.push({
            x: x, y: y, z: z,
            speed: 0.0005 + Math.random() * 0.0005,
            phaseX: Math.random() * Math.PI*2,
            phaseY: Math.random() * Math.PI*2
        });
    }
    pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
    pGeo.setAttribute('opacity', new THREE.BufferAttribute(pOpacities, 1)); // custom attribute not strictly needed if we use generic material, but let's use it or size
    
    const pMat = new THREE.PointsMaterial({
        color: 0x10B981, size: 0.06, transparent: true, opacity: 0.6,
        sizeAttenuation: true, blending: THREE.AdditiveBlending
    });
    const dustParticles = new THREE.Points(pGeo, pMat);
    scene.add(dustParticles);

    /* ═══════════════════════════════════════════════════════════════════════════
       3. INTERACTION & ANIMATION
       ═══════════════════════════════════════════════════════════════════════════ */
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
        mouse.x = (event.clientX - windowHalfX) / windowHalfX; // -1 to 1
        mouse.y = -(event.clientY - windowHalfY) / windowHalfY; // -1 to 1
    });

    const clock = new THREE.Clock();

    function animate() {
        requestAnimationFrame(animate);
        const time = clock.getElapsedTime();

        // 1. LIQUID METAL VERTEX DISPLACEMENT
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
            
            // Generate multiple sine waves for boiling effect
            const noise = (Math.sin(ox * 2 + time * 1.5) * Math.cos(oy * 2 + time * 1.2) * Math.sin(oz * 2 + time)) * 0.3;
            
            currentPositions.setXYZ(i, ox + nx * noise, oy + ny * noise, oz + nz * noise);
        }
        currentPositions.needsUpdate = true;
        liquidCore.geometry.computeVertexNormals();

        // Core Rotation (affected by scroll)
        const coreSpeed = 0.001 + (scrollProgress * 0.004);
        liquidCore.rotation.y += coreSpeed;
        liquidCore.rotation.x += coreSpeed * 0.5;

        // 2. AURORA RIBBONS
        ribbons.forEach(ribbon => {
            ribbon.rotation.x += ribbon.userData.rx;
            ribbon.rotation.y += ribbon.userData.ry;
            ribbon.rotation.z += ribbon.userData.rz;
        });
        const targetAuroraY = -(scrollProgress * 4); // -2 to -5 equivalent
        auroraGroup.position.y += (targetAuroraY - auroraGroup.position.y) * 0.05;

        // 3. DUST PARTICLES
        const dPositions = dustParticles.geometry.attributes.position;
        for(let i=0; i<particleCount; i++) {
            const data = dustData[i];
            const px = data.x + Math.sin(time * 0.5 + data.phaseX) * 2;
            const py = data.y + Math.cos(time * 0.5 + data.phaseY) * 2;
            dPositions.setXYZ(i, px, py, data.z);
        }
        dPositions.needsUpdate = true;
        // Density increase via opacity scaling based on scroll
        pMat.opacity = 0.6 + (scrollProgress * 0.3);

        // 4. CAMERA PARALLAX & ZOOM
        const targetCamZ = 12 + (scrollProgress * 3);
        const targetCamX = mouse.x * 1.5;
        const targetCamY = mouse.y * 1.5;

        camera.position.z += (targetCamZ - camera.position.z) * 0.05;
        camera.position.x += (targetCamX - camera.position.x) * 0.05;
        camera.position.y += (targetCamY - camera.position.y) * 0.05;
        
        camera.lookAt(scene.position);

        // Background Color Lerping (Dark mode for dark sections)
        // Scroll progress > 0.2 means entering dark section, let's fade background to dark green
        const targetBg = (scrollProgress > 0.15 && scrollProgress < 0.3) ? new THREE.Color('#1B4332') : 
                         (scrollProgress > 0.75 ? new THREE.Color('#1B4332') : new THREE.Color('#FAFAF9'));
        scene.background.lerp(targetBg, 0.05);

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
    "index.html": html_content,
    "style.css": css_content,
    "script.js": script_content
}

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated Awwwards-style site successfully!")
