import os

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Eco Green - India's specialist in e-waste management.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  
  <nav class="navbar">
    <div class="container">
      <a href="index.html" class="logo">Eco Green</a>
      <ul class="nav-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About Us</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="impact.html">Impact</a></li>
        <li><a href="faq.html">FAQ</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
      <a href="contact.html" class="btn btn-primary">Request Quote</a>
    </div>
  </nav>

  <!-- WebGL Background Canvas (z-index: 0) -->
  <canvas id="webgl-canvas"></canvas>

  <main class="ui-layer">
    
    <!-- Section 1: Hero -->
    <section class="section hero">
      <div class="container">
        <div class="hero-content reveal">
          <h1 class="hero-title">India's specialist in<br><span class="text-accent">e-waste</span> management.</h1>
          <p class="hero-subtitle mt-4">Certified IT asset disposition, military-grade data destruction and high-purity metal recovery — the full e-waste lifecycle, handled under one compliant roof.</p>
          <div class="btn-group mt-4">
            <a href="services.html" class="btn btn-primary">E-Waste Solutions</a>
            <a href="contact.html" class="btn btn-outline">Partner With Us</a>
          </div>
          
          <div class="hero-floating-stats mt-4">
            <div class="glass-card small-stat reveal">
              <span class="text-accent stat-num">10+</span> Years
            </div>
            <div class="glass-card small-stat reveal">
              <span class="text-accent stat-num">342+</span> Clients
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Shocking Figures (Impact Stats) -->
    <section class="section">
      <div class="container">
        <div class="grid stats-grid-large">
          <div class="glass-card reveal">
            <h2 class="huge-number">1.6Mt</h2>
            <p>million tonnes of e-waste India generates every year — the world's third-largest pile.</p>
          </div>
          <div class="glass-card reveal">
            <h2 class="huge-number">32%</h2>
            <p>one in five devices handed to informal recyclers ends up burnt in the open.</p>
          </div>
          <div class="glass-card reveal">
            <h2 class="huge-number">2.6Mt</h2>
            <p>million tonnes of embodied carbon thrown away with unrecycled circuitry — ore we already mined</p>
          </div>
        </div>
        <p class="source-text reveal mt-4">Source: GLOBAL E-WASTE MONITOR 2024 • CPCB ANNUAL REPORT — SOURCES CITED, NOT FEARED.</p>
      </div>
    </section>

    <!-- Section 3: A fight for what's next -->
    <section class="section dark-section">
      <div class="container grid two-col align-center">
        <div class="reveal">
          <h2 class="section-title">A fight for what's next.</h2>
          <p class="text-lg">Every retired device is a choice: a landfill burning in the open, or a vault of metals re-entering the economy. Ecogreen exists to make the second choice the easy one — certified, tracked and reported end to end, for enterprises that answer to their own ESG commitments.</p>
        </div>
        <div class="dark-card reveal">
          <h3>GREEN METALS RECOVERED</h3>
          <p class="mt-4">Every retired asset is a vein of ore we have already mined once. Recovering it is the cheapest, cleanest tonne of metal on Earth.</p>
          <div class="metal-tags mt-4">
            <span>Iron</span>
            <span>Copper</span>
            <span>Lithium</span>
            <span>Cobalt</span>
            <span>Aluminum</span>
          </div>
          <a href="green-metal-recovery.html" class="btn btn-outline-white mt-4">EXPLORE GREEN METAL RECOVERY</a>
        </div>
      </div>
    </section>

    <!-- Section 4: Marquee Banner -->
    <div class="marquee-section">
        <h2 class="marquee-text">TAKE ACTION & RECYCLE RIGHT • TAKE ACTION & RECYCLE RIGHT • TAKE ACTION & RECYCLE RIGHT • TAKE ACTION & RECYCLE RIGHT • TAKE ACTION & RECYCLE RIGHT</h2>
    </div>

    <!-- Section 5: Extraction Figures -->
    <section class="section">
      <div class="container text-center">
        <p class="label reveal">MEASURED, NOT PROMISED</p>
        <h2 class="section-title reveal">The extraction figures behind every batch</h2>
        
        <div class="grid two-col mt-4">
          <div class="glass-card extraction-card reveal">
            <h3 class="highlight-stat text-accent">98%+</h3>
            <h4>EXTRACTION EFFICIENCY</h4>
            <p>Safe discharge and hydrometallurgical recovery of cobalt, lithium and nickel.</p>
          </div>
          <div class="glass-card extraction-card reveal">
            <h3 class="highlight-stat text-accent">99.5%</h3>
            <h4>Purity level</h4>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Services Grid -->
    <section class="section bg-light">
      <div class="container">
        <p class="label reveal">SERVICES</p>
        <div class="flex-between reveal">
          <h2 class="section-title" style="margin-bottom: 0;">Expert collection, recycling, and disposal</h2>
          <a href="services.html" class="btn btn-outline">VIEW ALL SERVICES</a>
        </div>
        
        <div class="grid services-image-grid mt-4">
          <div class="service-image-card reveal">
            <img src="https://images.unsplash.com/photo-1550005973-78ce3f78fa45?w=600&q=80" alt="E-Waste Management">
            <div class="card-content">
              <h3>E-Waste Management</h3>
              <p>End-to-end IT asset disposition with certified dismantling and military-grade data destruction.</p>
              <a href="e-waste-management.html" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
          <div class="service-image-card reveal">
            <img src="https://images.unsplash.com/photo-1620802051778-e8cb5043ccbc?w=600&q=80" alt="Lithium Battery Recycling">
            <div class="card-content">
              <h3>Lithium Battery Recycling</h3>
              <p>High-purity extraction of lithium and cobalt from EV and electronic batteries.</p>
              <a href="lithium-battery-recycling.html" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
          <div class="service-image-card reveal">
            <img src="https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?w=600&q=80" alt="Plastic Waste Recycling">
            <div class="card-content">
              <h3>Plastic Waste Recycling</h3>
              <p>Advanced sorting and precision pelletizing into reusable manufacturing materials.</p>
              <a href="plastic-recycling.html" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
          <div class="service-image-card reveal">
            <img src="https://images.unsplash.com/photo-1603351154351-5e2d0600bb77?w=600&q=80" alt="Paper Recycling">
            <div class="card-content">
              <h3>Paper Recycling</h3>
              <p>Closed-loop processing that saves trees, conserves water and cuts corporate carbon.</p>
              <a href="paper-recycling.html" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
          <div class="service-image-card reveal">
            <img src="https://images.unsplash.com/photo-1581093458791-9f3c3900df4b?w=600&q=80" alt="Green Metal Recovery">
            <div class="card-content">
              <h3>Green Metal Recovery</h3>
              <p>High-yield extraction of iron, copper and aluminum from complex waste streams.</p>
              <a href="green-metal-recovery.html" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
          <div class="service-image-card reveal">
            <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&q=80" alt="EPR Consulting">
            <div class="card-content">
              <h3>EPR Consulting</h3>
              <p>Regulatory navigation, compliance documentation and mandated EPR targets, handled.</p>
              <a href="epr-consulting.html" class="read-more">READ MORE &rarr;</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 7: Why Enterprises Trust -->
    <section class="section">
      <div class="container text-center reveal">
        <h2 class="section-title">Why Enterprises trust ECO GREEN</h2>
        <p class="text-lg mx-auto" style="max-width: 800px;">We empower global brands to achieve zero-waste goals through state-of-the-art recycling technology and uncompromising data security. By integrating circular economy principles with pan-India logistics, we ensure your retired assets are managed with absolute transparency and 100% regulatory compliance.</p>
        
        <div class="grid stats-grid mt-4">
          <div class="glass-card">
            <h2 class="stat-number">10</h2>
            <p class="stat-label">Years Experience</p>
          </div>
          <div class="glass-card">
            <h2 class="stat-number">8</h2>
            <p class="stat-label">Awards Won</p>
          </div>
          <div class="glass-card">
            <h2 class="stat-number">342</h2>
            <p class="stat-label">Happy Clients</p>
          </div>
          <div class="glass-card">
            <h2 class="stat-number">84</h2>
            <p class="stat-label">Partners</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 8: Certifications -->
    <section class="section bg-light">
      <div class="container">
        <p class="label reveal text-center">VERIFIED COMPLIANCE</p>
        <h2 class="section-title reveal text-center">Certifications & Achievements</h2>
        
        <div class="grid three-col mt-4">
          <div class="glass-card text-center reveal">
            <h3>ISO Certification</h3>
            <p class="mt-4">Ensuring operational excellence, rigorous quality management, and strict environmental compliance across all asset disposition facilities.</p>
          </div>
          <div class="glass-card text-center reveal">
            <h3>Global Recycled Standard</h3>
            <p class="mt-4">Verifying safe, equitable, and transparent supply chains from end-of-life processing all the way to secondary raw material production.</p>
          </div>
          <div class="glass-card text-center reveal">
            <h3>Green Air Standard</h3>
            <p class="mt-4">Maintaining industry-leading emission controls and zero-harm atmospheric processing during complex metal extraction and dismantling.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 9: FAQ -->
    <section class="section">
      <div class="container max-w-800">
        <p class="label reveal text-center">LOOKING FORWARD</p>
        <h2 class="section-title reveal text-center">Future Vision & FAQs</h2>
        
        <div class="accordion mt-4">
          <div class="accordion-item reveal">
            <h3>What specific materials and metals can be recovered?</h3>
            <p>We utilize advanced, clean metallurgical processes to extract up to 99% of precious and base metals. This includes high-yield recovery of Gold, Silver, Palladium, Copper, Aluminum, and highly sought-after battery components like Lithium and Cobalt from end-of-life electronics.</p>
          </div>
          <div class="accordion-item reveal">
            <h3>How do you guarantee the destruction of sensitive corporate data?</h3>
            <p>Security is our absolute priority. We employ military-grade, certified data destruction protocols. Assets undergo physical micro-shredding and cryptographic wiping to ensure complete data sanitization before any physical recycling begins. A comprehensive Certificate of Destruction is provided for your compliance audits.</p>
          </div>
          <div class="accordion-item reveal">
            <h3>How does the EPR (Extended Producer Responsibility) consulting work?</h3>
            <p>We act as an extension of your compliance team. EcoGreen manages the complex regulatory landscape on your behalf, handling collection targets, statutory documentation, and government liaison to ensure your brand meets all legal EPR mandates seamlessly and transparently.</p>
          </div>
          <div class="accordion-item reveal">
            <h3>Are your extraction processes environmentally safe?</h3>
            <p>Unlike traditional smelting which causes severe pollution, our proprietary closed-loop hydrometallurgical technology operates with zero-harm atmospheric emissions and minimal water discharge. This drastically reduces the carbon footprint of metal recovery.</p>
          </div>
          <div class="accordion-item reveal">
            <h3>Do you provide tracking and reporting for ESG goals?</h3>
            <p>Yes. Every batch processed through our facilities generates a comprehensive sustainability dashboard. We provide exact metrics on carbon offsets, materials recovered, and landfill diversion rates to directly support and validate your corporate ESG reporting.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 10: Vision Quote -->
    <section class="section dark-section text-center" style="padding: 10rem 0;">
      <div class="container">
        <h2 class="quote-text reveal">"Our vision is a zero-waste future driven by continuous innovation, where end-of-life technology fuels the next generation of manufacturing."</h2>
      </div>
    </section>

    <!-- Section 11: Footer -->
    <footer class="footer dark-section">
      <div class="container">
        <div class="grid four-col">
          <div class="footer-col">
            <h3 class="logo" style="color: white; margin-bottom: 1rem;">Eco Green Recyclers</h3>
            <p>India's specialist in e-waste management and green metal recovery.</p>
          </div>
          <div class="footer-col">
            <h4>Quick Links</h4>
            <ul>
              <li><a href="about.html">About Us</a></li>
              <li><a href="impact.html">Our Impact</a></li>
              <li><a href="faq.html">FAQ</a></li>
              <li><a href="contact.html">Contact Us</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Services</h4>
            <ul>
              <li><a href="e-waste-management.html">E-Waste Management</a></li>
              <li><a href="lithium-battery-recycling.html">Battery Recycling</a></li>
              <li><a href="plastic-recycling.html">Plastic Recycling</a></li>
              <li><a href="green-metal-recovery.html">Green Metal Recovery</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Contact</h4>
            <p>479, Habibpur, Dadri,<br>Gr. Noida, Uttar Pradesh</p>
            <p class="mt-4"><strong>Phone:</strong> <a href="tel:+919319253708">+91 93192 53708</a></p>
            <p><strong>Email:</strong> <a href="mailto:operation@ecogreen.eco">operation@ecogreen.eco</a></p>
            <div class="social-links mt-4">
              <a href="#">LinkedIn</a>
              <a href="#">Twitter</a>
              <a href="#">Facebook</a>
              <a href="#">Instagram</a>
            </div>
          </div>
        </div>
        <div class="footer-bottom mt-4">
          <p>© 2026 Eco Green Recyclers (P) Limited. All rights reserved.</p>
        </div>
      </div>
    </footer>

  </main>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="script.js"></script>
</body>
</html>"""

style_css = """
:root {
  /* Theme Colors */
  --bg-color: #FAFAF9;
  --text-dark: #1B4332;
  --text-light: #FAFAF9;
  --accent: #10B981;
  --accent-hover: #059669;
  --dark-bg: #1B4332;
  
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

/* WebGL Background */
#webgl-canvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 0;
  pointer-events: none; /* Allows scrolling and clicking through the canvas */
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
  background: rgba(250, 250, 249, 0.8);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--glass-border);
  z-index: 100;
  padding: 1rem 0;
}

.navbar .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar .logo {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--text-dark);
  text-decoration: none;
}

.navbar .nav-links {
  display: flex;
  gap: 2rem;
  list-style: none;
}

.navbar .nav-links a {
  color: var(--text-dark);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.navbar .nav-links a:hover {
  color: var(--accent);
}

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 2rem;
}

.max-w-800 {
  max-width: 800px;
  margin: 0 auto;
}

/* Typography */
h1, h2, h3, h4 {
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.2;
}

.text-accent { color: var(--accent); }
.text-center { text-align: center; }
.mx-auto { margin-left: auto; margin-right: auto; }

.section-title {
  font-size: clamp(2rem, 5vw, 3.5rem);
  margin-bottom: 2rem;
}

.text-lg { font-size: 1.125rem; }
.label { font-weight: 600; color: var(--accent); letter-spacing: 0.1em; font-size: 0.875rem; margin-bottom: 1rem; text-transform: uppercase; }

.mt-4 { margin-top: 2rem; }

/* Sections */
.section { padding: 6rem 0; }
.bg-light { background: rgba(255,255,255,0.3); backdrop-filter: blur(5px); }

/* Dark Sections */
.dark-section {
  background-color: var(--dark-bg);
  color: var(--text-light);
}
.dark-card {
  background: rgba(0,0,0,0.2);
  border: 1px solid rgba(255,255,255,0.1);
  padding: 2.5rem;
  border-radius: 16px;
}

/* Hero Section */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding-top: 8rem;
}

.hero-title {
  font-size: clamp(3rem, 8vw, 5.5rem);
  line-height: 1.05;
  margin-bottom: 1.5rem;
  max-width: 15ch;
}

.hero-subtitle {
  font-size: clamp(1.1rem, 2vw, 1.25rem);
  max-width: 60ch;
  margin-bottom: 2rem;
  color: #2D6A4F;
  font-weight: 500;
}

.hero-floating-stats {
  display: flex; gap: 1rem; margin-top: 3rem;
}
.small-stat {
  padding: 1rem 1.5rem; border-radius: 99px; display: inline-flex; align-items: center; gap: 0.5rem; font-weight: 600;
}
.stat-num { font-size: 1.5rem; }


/* Buttons */
.btn-group { display: flex; gap: 1rem; flex-wrap: wrap; }
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 1rem 2rem; border-radius: 999px; font-weight: 600;
  text-decoration: none; transition: all 0.3s ease; font-size: 1rem; cursor: pointer;
}
.btn-primary { background-color: var(--text-dark); color: #fff; }
.btn-primary:hover { background-color: var(--accent); transform: translateY(-2px); box-shadow: 0 10px 20px rgba(16, 185, 129, 0.2); }
.btn-outline { background-color: transparent; color: var(--text-dark); border: 1px solid var(--text-dark); }
.btn-outline:hover { background-color: var(--glass-bg); transform: translateY(-2px); }
.btn-outline-white { background-color: transparent; color: #fff; border: 1px solid #fff; }
.btn-outline-white:hover { background-color: #fff; color: var(--text-dark); }

/* Glassmorphism Cards */
.glass-card {
  background: var(--glass-bg);
  backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
  border: 1px solid var(--glass-border); border-radius: 24px;
  padding: 2.5rem; box-shadow: 0 8px 32px rgba(27, 67, 50, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.glass-card:hover { transform: translateY(-5px); box-shadow: 0 12px 40px rgba(27, 67, 50, 0.1); }

/* Grids */
.grid { display: grid; gap: 2rem; }
.two-col { grid-template-columns: 1fr; }
.three-col { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
.four-col { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
.align-center { align-items: center; }
.flex-between { display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem; }

@media (min-width: 992px) {
  .two-col { grid-template-columns: 1fr 1fr; gap: 4rem; }
}

/* Stats */
.stats-grid-large { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
.huge-number { font-size: clamp(3rem, 6vw, 5rem); color: var(--accent); line-height: 1; margin-bottom: 1rem; }
.source-text { font-size: 0.75rem; font-weight: 600; opacity: 0.7; letter-spacing: 0.05em; text-align: center; }

.stats-grid { grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); text-align: center; }
.stat-number { font-size: clamp(2.5rem, 5vw, 4rem); color: var(--accent); margin-bottom: 0.5rem; }
.stat-label { font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.9rem; }

.extraction-card { text-align: center; }
.highlight-stat { font-size: clamp(3.5rem, 6vw, 5rem); color: var(--accent); line-height: 1; margin-bottom: 0.5rem; }

/* Metal Tags */
.metal-tags { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.metal-tags span { padding: 0.5rem 1rem; background: rgba(255,255,255,0.1); border-radius: 99px; font-size: 0.875rem; font-weight: 500; border: 1px solid rgba(255,255,255,0.2); }

/* Marquee */
.marquee-section { background: var(--dark-bg); color: white; padding: 1.5rem 0; overflow: hidden; white-space: nowrap; border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); }
.marquee-text { font-size: 2.5rem; margin: 0; display: inline-block; animation: scrollText 15s linear infinite; }
@keyframes scrollText { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

/* Services Image Grid */
.services-image-grid { grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); }
.service-image-card {
  background: var(--glass-bg); backdrop-filter: blur(20px); border: 1px solid var(--glass-border);
  border-radius: 16px; overflow: hidden; transition: transform 0.3s;
  display: flex; flex-direction: column;
}
.service-image-card:hover { transform: translateY(-5px); }
.service-image-card img { width: 100%; height: 240px; object-fit: cover; }
.card-content { padding: 2rem; flex: 1; display: flex; flex-direction: column; }
.card-content h3 { margin-bottom: 1rem; font-size: 1.25rem; }
.card-content p { margin-bottom: 1.5rem; flex: 1; }
.read-more { font-weight: 600; color: var(--accent); text-decoration: none; font-size: 0.9rem; letter-spacing: 0.05em; }
.read-more:hover { text-decoration: underline; }

/* Accordion */
.accordion { display: flex; flex-direction: column; gap: 1rem; }
.accordion-item { background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; padding: 1.5rem; }
.accordion-item h3 { margin-bottom: 0.5rem; font-size: 1.2rem; }

/* Vision Quote */
.quote-text { font-size: clamp(2rem, 4vw, 3rem); font-weight: 500; max-width: 1000px; margin: 0 auto; line-height: 1.3; }

/* Footer */
.footer { padding: 4rem 0 2rem; border-top: 1px solid rgba(255,255,255,0.1); }
.footer ul { list-style: none; }
.footer ul li { margin-bottom: 0.5rem; }
.footer a { color: var(--text-light); text-decoration: none; opacity: 0.8; transition: opacity 0.3s; }
.footer a:hover { opacity: 1; color: var(--accent); }
.footer h4 { margin-bottom: 1.5rem; color: #fff; font-size: 1.1rem; }
.social-links { display: flex; gap: 1rem; flex-wrap: wrap; }
.social-links a { font-weight: 600; font-size: 0.9rem; }
.footer-bottom { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 2rem; text-align: center; opacity: 0.6; font-size: 0.9rem; }

/* Animations */
.reveal { opacity: 0; transform: translateY(40px); transition: opacity 1s cubic-bezier(0.16, 1, 0.3, 1), transform 1s cubic-bezier(0.16, 1, 0.3, 1); }
.reveal.active { opacity: 1; transform: translateY(0); }
"""

script_js = """document.addEventListener('DOMContentLoaded', () => {
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
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    });

    revealElements.forEach(el => revealObserver.observe(el));

    /* ═══════════════════════════════════════════════════════════════════════════
       2. THREE.JS PREMIUM BACKGROUND: PARTICLE NETWORK
       ═══════════════════════════════════════════════════════════════════════════ */
    const canvas = document.getElementById('webgl-canvas');
    if (!canvas) return;

    const isMobile = window.innerWidth < 768;
    const PIXEL_RATIO = isMobile ? 1 : Math.min(window.devicePixelRatio, 2);

    // Scene Setup
    const scene = new THREE.Scene();
    scene.background = new THREE.Color('#FAFAF9');

    // Camera
    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 100);
    camera.position.z = 25;

    // Renderer
    const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: !isMobile, alpha: false });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(PIXEL_RATIO);
    renderer.outputEncoding = THREE.sRGBEncoding;

    // Lights
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);
    
    // Group for the entire network
    const networkGroup = new THREE.Group();
    scene.add(networkGroup);

    // --- Particle Network Implementation ---
    const particleCount = isMobile ? 100 : 250;
    const maxConnectionDistance = 3.5;
    
    const particlesData = [];
    const positions = new Float32Array(particleCount * 3);
    const colors = new Float32Array(particleCount * 3);

    const emeraldColor = new THREE.Color(0x10B981);
    
    for (let i = 0; i < particleCount; i++) {
        const x = (Math.random() - 0.5) * 40;
        const y = (Math.random() - 0.5) * 40;
        const z = (Math.random() - 0.5) * 20;

        positions[i * 3] = x;
        positions[i * 3 + 1] = y;
        positions[i * 3 + 2] = z;

        colors[i * 3] = emeraldColor.r;
        colors[i * 3 + 1] = emeraldColor.g;
        colors[i * 3 + 2] = emeraldColor.b;

        particlesData.push({
            velocity: new THREE.Vector3((Math.random() - 0.5) * 0.05, (Math.random() - 0.5) * 0.05, (Math.random() - 0.5) * 0.05),
            numConnections: 0,
            baseX: x, baseY: y, baseZ: z,
            phase: Math.random() * Math.PI * 2,
            speed: 0.5 + Math.random() * 1.5
        });
    }

    // Particle Geometry (Points)
    const pGeometry = new THREE.BufferGeometry();
    pGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    pGeometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

    // Make spheres using points
    const pMaterial = new THREE.PointsMaterial({
        size: 0.25,
        color: 0x10B981,
        transparent: true,
        opacity: 0.8,
        sizeAttenuation: true
    });
    
    const particleSystem = new THREE.Points(pGeometry, pMaterial);
    networkGroup.add(particleSystem);

    // Lines Geometry
    // Maximum possible connections = count * count
    const linesGeometry = new THREE.BufferGeometry();
    const linesPositions = new Float32Array(particleCount * particleCount * 3);
    const linesColors = new Float32Array(particleCount * particleCount * 3);
    linesGeometry.setAttribute('position', new THREE.BufferAttribute(linesPositions, 3));
    linesGeometry.setAttribute('color', new THREE.BufferAttribute(linesColors, 3));

    const linesMaterial = new THREE.LineBasicMaterial({
        vertexColors: true,
        blending: THREE.AdditiveBlending,
        transparent: true,
        opacity: 0.3
    });
    
    const linesMesh = new THREE.LineSegments(linesGeometry, linesMaterial);
    networkGroup.add(linesMesh);

    /* ═══════════════════════════════════════════════════════════════════════════
       3. INTERACTION & SCROLL
       ═══════════════════════════════════════════════════════════════════════════ */
    let scrollProgress = 0;
    function updateScrollProgress() {
        const maxScroll = document.body.scrollHeight - window.innerHeight;
        scrollProgress = maxScroll > 0 ? (window.scrollY / maxScroll) : 0;
    }
    window.addEventListener('scroll', updateScrollProgress);
    window.addEventListener('resize', updateScrollProgress);
    updateScrollProgress();

    // Mouse Interaction
    const mouse = new THREE.Vector2(-9999, -9999);
    const raycaster = new THREE.Raycaster();
    const planeZ = new THREE.Plane(new THREE.Vector3(0, 0, 1), 0);
    const mousePos3D = new THREE.Vector3();

    document.addEventListener('mousemove', (event) => {
        mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
    });

    const clock = new THREE.Clock();

    function animate() {
        requestAnimationFrame(animate);
        const elapsedTime = clock.getElapsedTime();

        // 1. Raycast mouse to a 3D plane at Z=0 for repulsion effect
        raycaster.setFromCamera(mouse, camera);
        raycaster.ray.intersectPlane(planeZ, mousePos3D);

        // 2. Update Particles
        let vertexpos = 0;
        let colorpos = 0;
        let numConnected = 0;
        
        const posAttribute = pGeometry.attributes.position;
        const lPosAttribute = linesGeometry.attributes.position;
        const lColAttribute = linesGeometry.attributes.color;

        for (let i = 0; i < particleCount; i++) {
            particlesData[i].numConnections = 0;
        }

        for (let i = 0; i < particleCount; i++) {
            const data = particlesData[i];
            
            // Organic floating using sine waves
            data.baseX += data.velocity.x;
            data.baseY += data.velocity.y;
            data.baseZ += data.velocity.z;

            // Bounding box bounce
            if (data.baseX < -25 || data.baseX > 25) data.velocity.x = -data.velocity.x;
            if (data.baseY < -25 || data.baseY > 25) data.velocity.y = -data.velocity.y;
            if (data.baseZ < -15 || data.baseZ > 15) data.velocity.z = -data.velocity.z;

            let px = data.baseX + Math.sin(elapsedTime * data.speed + data.phase) * 0.5;
            let py = data.baseY + Math.cos(elapsedTime * data.speed + data.phase) * 0.5;
            let pz = data.baseZ;

            // Repulsion from mouse
            if (mousePos3D.lengthSq() < 10000) { // If mouse intersects
                const dx = px - mousePos3D.x;
                const dy = py - mousePos3D.y;
                const distSq = dx*dx + dy*dy;
                
                if (distSq < 25) { // 5 unit radius repulsion
                    const force = (25 - distSq) / 25;
                    px += dx * force * 0.1;
                    py += dy * force * 0.1;
                }
            }

            posAttribute.setXYZ(i, px, py, pz);

            // Connect nearby particles
            for (let j = i + 1; j < particleCount; j++) {
                const data2 = particlesData[j];
                
                let px2 = posAttribute.getX(j);
                let py2 = posAttribute.getY(j);
                let pz2 = posAttribute.getZ(j);
                
                const dx = px - px2;
                const dy = py - py2;
                const dz = pz - pz2;
                const dist = Math.sqrt(dx*dx + dy*dy + dz*dz);

                if (dist < maxConnectionDistance) {
                    data.numConnections++;
                    data2.numConnections++;

                    const alpha = 1.0 - (dist / maxConnectionDistance);

                    lPosAttribute.setXYZ(vertexpos++, px, py, pz);
                    lPosAttribute.setXYZ(vertexpos++, px2, py2, pz2);
                    
                    // Fade color based on distance
                    lColAttribute.setXYZ(colorpos++, emeraldColor.r * alpha, emeraldColor.g * alpha, emeraldColor.b * alpha);
                    lColAttribute.setXYZ(colorpos++, emeraldColor.r * alpha, emeraldColor.g * alpha, emeraldColor.b * alpha);
                    
                    numConnected++;
                }
            }
        }

        posAttribute.needsUpdate = true;
        
        linesMesh.geometry.setDrawRange(0, numConnected * 2);
        lPosAttribute.needsUpdate = true;
        lColAttribute.needsUpdate = true;

        // 3. Scroll Rotation and Camera movement
        // Network rotates as user scrolls down
        const targetRotY = scrollProgress * Math.PI; // Half turn across page
        const targetRotX = scrollProgress * Math.PI * 0.25;
        
        networkGroup.rotation.y += (targetRotY - networkGroup.rotation.y) * 0.05;
        networkGroup.rotation.x += (targetRotX - networkGroup.rotation.x) * 0.05;
        
        // Dark section color blending
        // Scroll progress > 0.3 means we are hitting dark sections, make background dark green
        const targetBgColor = scrollProgress > 0.2 && scrollProgress < 0.4 ? new THREE.Color('#1B4332') : 
                              (scrollProgress > 0.8 ? new THREE.Color('#1B4332') : new THREE.Color('#FAFAF9'));
        
        scene.background.lerp(targetBgColor, 0.05);
        
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
    "index.html": index_html,
    "style.css": style_css,
    "script.js": script_js
}

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Generated rebuild files successfully!")
