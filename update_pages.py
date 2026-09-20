import os

pages = {
    "index.html": """
    <!-- Hero Section -->
    <section class="section hero" style="min-height: 100vh; padding-top: 12rem;">
      <div class="container">
        <div class="hero-content reveal">
          <h1 class="hero-title" style="font-size: clamp(3rem, 8vw, 6rem); max-width: 15ch; line-height: 1.05;">India's specialist in<br><span class="text-accent">e-waste</span> management.</h1>
          <p class="hero-subtitle mt-4" style="max-width: 60ch; font-size: 1.25rem;">Certified IT asset disposition, military-grade data destruction and high-purity metal recovery — the full e-waste lifecycle, handled under one compliant roof.</p>
          <div class="btn-group mt-4">
            <a href="#services" class="btn btn-primary">E-Waste Solutions</a>
            <a href="contact.html" class="btn btn-outline">Partner With Us</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Impact Stats Section -->
    <section class="section impact" style="min-height: 100vh; display: flex; align-items: center;">
      <div class="container">
        <div class="grid stats-grid">
          <div class="glass-card reveal">
            <h2 class="stat-number">10+</h2>
            <p class="stat-label">Years Experience</p>
          </div>
          <div class="glass-card reveal">
            <h2 class="stat-number">8</h2>
            <p class="stat-label">Awards Won</p>
          </div>
          <div class="glass-card reveal">
            <h2 class="stat-number">342+</h2>
            <p class="stat-label">Happy Clients</p>
          </div>
          <div class="glass-card reveal">
            <h2 class="stat-number">84</h2>
            <p class="stat-label">Partners</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Grid Section -->
    <section id="services" class="section services" style="min-height: 100vh; display: flex; align-items: center;">
      <div class="container">
        <h2 class="section-title reveal">Our Expertise</h2>
        <div class="grid services-grid">
          
          <div class="glass-card service-card reveal">
            <h3>E-Waste Management</h3>
            <p>End-to-end IT asset disposition featuring certified dismantling and military-grade data destruction to protect your enterprise security and ensure compliance.</p>
          </div>

          <div class="glass-card service-card reveal">
            <h3>Lithium Battery Recycling</h3>
            <p>Specialized processing for EV and electronic batteries, focusing on the high-purity extraction of lithium and cobalt to power tomorrow sustainably.</p>
          </div>

          <div class="glass-card service-card reveal">
            <h3>Plastic Waste Recycling</h3>
            <p>Advanced sorting and precision pelletizing technology that transforms industrial and commercial plastic waste into high-quality, reusable manufacturing materials.</p>
          </div>

          <div class="glass-card service-card reveal">
            <h3>Paper Recycling</h3>
            <p>Maximize environmental impact with closed-loop processing that saves trees, conserves water, and dramatically reduces your corporate carbon footprint.</p>
          </div>

          <div class="glass-card service-card reveal">
            <h3>Green Metal Recovery</h3>
            <p>High-yield extraction of iron, copper, and aluminum from complex industrial waste streams, securing essential raw materials for the circular economy.</p>
          </div>

          <div class="glass-card service-card reveal">
            <h3>EPR Consulting</h3>
            <p>Strategic guidance to seamlessly navigate government regulations, manage compliance documentation, and effortlessly achieve your mandated Extended Producer Responsibility targets.</p>
          </div>

        </div>
      </div>
    </section>

    <!-- Extraction Stats & Certifications -->
    <section class="section extraction-certs" style="min-height: 100vh; display: flex; align-items: center;">
      <div class="container">
        <div class="grid two-col">
          
          <!-- Extraction Stats -->
          <div class="extraction-content">
            <h2 class="section-title reveal">Maximum Recovery</h2>
            <div class="glass-card reveal">
              <h3 class="highlight-stat text-accent">98%+</h3>
              <p>efficiency</p>
            </div>
            <div class="glass-card reveal mt-4">
              <h3 class="highlight-stat text-accent">99.5%</h3>
              <p>purity</p>
            </div>
          </div>

          <!-- Certifications -->
          <div class="certs-content">
            <h2 class="section-title reveal">Auditable Compliance</h2>
            <ul class="cert-list">
              <li class="glass-card reveal">
                <h4>ISO Certification</h4>
                <p>Fully compliant with international environmental management standards.</p>
              </li>
              <li class="glass-card reveal mt-4">
                <h4>Global Recycled Standard</h4>
                <p>Verified recycled content and responsible social, environmental practices.</p>
              </li>
              <li class="glass-card reveal mt-4">
                <h4>Green Air Standard</h4>
                <p>Operating with zero-harm atmospheric emissions and minimal water discharge.</p>
              </li>
            </ul>
          </div>

        </div>
      </div>
    </section>
    """,
    "about.html": """
    <section class="section page-header" style="padding-top: 12rem;">
      <div class="container">
        <h1 class="hero-title reveal" style="font-size: clamp(2rem, 5vw, 4rem);">Empowering sustainable futures through responsible e-waste management and recycling solutions.</h1>
      </div>
    </section>
    <section class="section">
      <div class="container grid two-col">
        <div class="glass-card reveal">
          <h2>Our Vision</h2>
          <p class="mt-4">Our vision is a zero-waste future driven by continuous innovation, where end-of-life technology fuels the next generation of manufacturing.</p>
        </div>
        <div class="glass-card reveal">
          <h2>Why Enterprises trust ECO GREEN</h2>
          <p class="mt-4">We empower global brands to achieve zero-waste goals through state-of-the-art recycling technology and uncompromising data security. By integrating circular economy principles with pan-India logistics, we ensure your retired assets are managed with absolute transparency and 100% regulatory compliance.</p>
        </div>
      </div>
      <div class="container grid stats-grid mt-4">
        <div class="glass-card reveal">
          <h2 class="stat-number">10</h2>
          <p class="stat-label">Years Experience</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">8</h2>
          <p class="stat-label">Awards Won</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">342</h2>
          <p class="stat-label">Happy Clients</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">84</h2>
          <p class="stat-label">Partners</p>
        </div>
      </div>
    </section>
    """,
    "services.html": """
    <section class="section page-header" style="padding-top: 12rem;">
      <div class="container">
        <h1 class="hero-title reveal" style="font-size: clamp(2rem, 5vw, 4rem);">Expert collection, recycling, and disposal services for all industries</h1>
      </div>
    </section>
    <section class="section services">
      <div class="container">
        <div class="grid services-grid">
          <a href="e-waste-management.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>E-Waste Management</h3>
            <p>End-to-end IT asset disposition featuring certified dismantling and military-grade data destruction to protect your enterprise security and ensure compliance.</p>
          </a>
          <a href="lithium-battery-recycling.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>Lithium Battery Recycling</h3>
            <p>Specialized processing for EV and electronic batteries, focusing on the high-purity extraction of lithium and cobalt to power tomorrow sustainably.</p>
          </a>
          <a href="plastic-recycling.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>Plastic Waste Recycling</h3>
            <p>Advanced sorting and precision pelletizing technology that transforms industrial and commercial plastic waste into high-quality, reusable manufacturing materials.</p>
          </a>
          <a href="paper-recycling.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>Paper Recycling</h3>
            <p>Maximize environmental impact with closed-loop processing that saves trees, conserves water, and dramatically reduces your corporate carbon footprint.</p>
          </a>
          <a href="green-metal-recovery.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>Green Metal Recovery</h3>
            <p>High-yield extraction of iron, copper, and aluminum from complex industrial waste streams, securing essential raw materials for the circular economy.</p>
          </a>
          <a href="epr-consulting.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>EPR Consulting</h3>
            <p>Strategic guidance to seamlessly navigate government regulations, manage compliance documentation, and effortlessly achieve your mandated Extended Producer Responsibility targets.</p>
          </a>
        </div>
      </div>
    </section>
    """,
    "e-waste-management.html": """
    <section class="section page-header" style="padding-top: 12rem;">
      <div class="container">
        <h1 class="hero-title reveal">E-Waste Management</h1>
        <p class="hero-subtitle reveal">End-to-end IT asset disposition featuring certified dismantling and military-grade data destruction to protect your enterprise security and ensure compliance.</p>
      </div>
    </section>
    <section class="section">
      <div class="container glass-card reveal">
        <h2>Certified Data Destruction</h2>
        <p class="mt-4">Storage media undergo DoD 5220.22-M standard wiping and physical shredding, with a serialised Certificate of Destruction issued for every batch.</p>
      </div>
    </section>
    """,
    "lithium-battery-recycling.html": """
    <section class="section page-header" style="padding-top: 12rem;">
      <div class="container">
        <h1 class="hero-title reveal">Lithium Battery Recycling</h1>
        <p class="hero-subtitle reveal">Specialized processing for EV and electronic batteries, focusing on the high-purity extraction of lithium and cobalt to power tomorrow sustainably.</p>
      </div>
    </section>
    <section class="section">
      <div class="container grid two-col">
        <div class="glass-card reveal">
          <h2>Technical Process</h2>
          <ul style="margin-top: 1rem; list-style-position: inside;">
            <li>Thermal Management & Safe Discharge</li>
            <li>Black Mass Refining</li>
          </ul>
        </div>
        <div class="glass-card reveal">
          <h2>Efficiency</h2>
          <p>98%+ Extraction efficiency on e-waste and lithium-ion cells — safe discharge and hydrometallurgical recovery of cobalt, lithium and nickel.</p>
        </div>
      </div>
    </section>
    """,
    "plastic-recycling.html": """
    <section class="section page-header" style="padding-top: 12rem;">
      <div class="container">
        <h1 class="hero-title reveal">Plastic Waste Recycling</h1>
        <p class="hero-subtitle reveal">Advanced sorting and precision pelletizing technology that transforms industrial and commercial plastic waste into high-quality, reusable manufacturing materials.</p>
      </div>
    </section>
    <section class="section">
      <div class="container grid two-col">
        <div class="glass-card reveal">
          <h2>Process</h2>
          <ul style="margin-top: 1rem; list-style-position: inside;">
            <li>Polymer Identification</li>
            <li>Precision Pelletizing</li>
          </ul>
        </div>
        <div class="glass-card reveal">
          <h2>Impact</h2>
          <p>10+ Partner organizations across industrial and e-waste plastic recovery streams.</p>
        </div>
      </div>
    </section>
    """,
    "paper-recycling.html": """
    <section class="section page-header" style="padding-top: 12rem;">
      <div class="container">
        <h1 class="hero-title reveal">Paper Recycling</h1>
      </div>
    </section>
    <section class="section">
      <div class="container glass-card reveal">
        <h2>Overview</h2>
        <p class="mt-4">Maximize environmental impact with closed-loop processing that saves trees, conserves water, and dramatically reduces your corporate carbon footprint.</p>
      </div>
    </section>
    """,
    "green-metal-recovery.html": """
    <section class="section page-header" style="padding-top: 12rem;">
      <div class="container">
        <h1 class="hero-title reveal">Green Metal Recovery</h1>
        <p class="hero-subtitle reveal">High-yield extraction of iron, copper, and aluminum from complex industrial waste streams, securing essential raw materials for the circular economy.</p>
      </div>
    </section>
    <section class="section">
      <div class="container grid two-col">
        <div class="glass-card reveal">
          <h2>Metals Recovered</h2>
          <p>Iron, Copper, Lithium, Cobalt, Aluminum</p>
        </div>
        <div class="glass-card reveal">
          <h2>Purity</h2>
          <p>22+ Distinct green metals recovered from e-waste at greater than 99.5% purity, reintegrated into manufacturing supply chains.</p>
        </div>
      </div>
    </section>
    """,
    "epr-consulting.html": """
    <section class="section page-header" style="padding-top: 12rem;">
      <div class="container">
        <h1 class="hero-title reveal">EPR Consulting</h1>
      </div>
    </section>
    <section class="section">
      <div class="container glass-card reveal">
        <h2>Overview</h2>
        <p class="mt-4">Strategic guidance to seamlessly navigate government regulations, manage compliance documentation, and effortlessly achieve your mandated Extended Producer Responsibility targets.</p>
      </div>
    </section>
    """,
    "impact.html": """
    <section class="section page-header" style="padding-top: 12rem;">
      <div class="container">
        <h1 class="hero-title reveal">Our Impact</h1>
      </div>
    </section>
    <div style="background: var(--text-dark); color: white; padding: 1rem 0; overflow: hidden; white-space: nowrap;">
        <h2 style="font-size: 2rem; margin: 0; display: inline-block; animation: scrollText 15s linear infinite;">TAKE ACTION & RECYCLE RIGHT • TAKE ACTION & RECYCLE RIGHT • TAKE ACTION & RECYCLE RIGHT • TAKE ACTION & RECYCLE RIGHT • TAKE ACTION & RECYCLE RIGHT</h2>
    </div>
    <style>
    @keyframes scrollText {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
    </style>
    <section class="section">
      <div class="container grid stats-grid">
        <div class="glass-card reveal">
          <h2 class="stat-number">1.6Mt</h2>
          <p class="stat-label">e-waste</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">32%</h2>
          <p class="stat-label">one in five devices</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">2.6Mt</h2>
          <p class="stat-label">embodied carbon</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">98%+</h2>
          <p class="stat-label">extraction</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">99.5%</h2>
          <p class="stat-label">purity</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">10+</h2>
          <p class="stat-label">years</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">8</h2>
          <p class="stat-label">awards</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">342+</h2>
          <p class="stat-label">clients</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">84</h2>
          <p class="stat-label">partners</p>
        </div>
      </div>
    </section>
    """,
    "faq.html": """
    <section class="section page-header" style="padding-top: 12rem;">
      <div class="container">
        <h1 class="hero-title reveal">Frequently Asked Questions</h1>
      </div>
    </section>
    <section class="section">
      <div class="container accordion">
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
    </section>
    """,
    "contact.html": """
    <section class="section page-header" style="padding-top: 12rem;">
      <div class="container">
        <h1 class="hero-title reveal">Contact Us</h1>
      </div>
    </section>
    <section class="section">
      <div class="container grid two-col">
        <div class="glass-card reveal">
          <h2>Business Details</h2>
          <div class="contact-details mt-4">
            <p><strong>Address:</strong><br>479, Habibpur, Dadri,<br>Gr. Noida, Uttar Pradesh</p>
            <p class="mt-4"><strong>Phone:</strong> <a href="tel:+919319253708">+91 93192 53708</a></p>
            <p class="mt-4"><strong>Email:</strong> <a href="mailto:operation@ecogreen.eco">operation@ecogreen.eco</a></p>
          </div>
          <div class="mt-4">
            <strong>Social:</strong> LinkedIn, Twitter, Facebook, Instagram
          </div>
        </div>
      </div>
    </section>
    """
}

template = """<!DOCTYPE html>
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
  
  <nav class="navbar">
    <div class="container">
      <a href="index.html" class="logo">Eco Green Recyclers</a>
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
    {content}
    
    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <div class="glass-card footer-card reveal">
          <div class="footer-info">
            <h2>Start your green transition.</h2>
            <div class="contact-details">
              <p><strong>Address:</strong> 479, Habibpur, Dadri, Gr. Noida, Uttar Pradesh</p>
              <p><strong>Phone:</strong> <a href="tel:+919319253708">+91 93192 53708</a></p>
              <p><strong>Email:</strong> <a href="mailto:operation@ecogreen.eco">operation@ecogreen.eco</a></p>
            </div>
          </div>
          <div class="footer-logo">
            <h3>Eco Green<br><span class="text-accent">Recyclers</span></h3>
          </div>
        </div>
      </div>
    </footer>
  </main>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="script.js"></script>
</body>
</html>
"""

for filename, content in pages.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(template.replace("{content}", content))

print("Updated all pages successfully!")
