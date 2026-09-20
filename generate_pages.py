import os

pages = {
    "about.html": """
    <section class="section page-header">
      <div class="container">
        <h1 class="hero-title reveal">About Us</h1>
        <p class="hero-subtitle reveal">Empowering sustainable futures through responsible e-waste management and recycling solutions.</p>
      </div>
    </section>
    <section class="section">
      <div class="container grid two-col">
        <div class="glass-card reveal">
          <h2>Our Story & Timeline</h2>
          <ul style="margin-top: 1rem; list-style-position: inside;">
            <li><strong>2012:</strong> Founded Eco Green Recyclers</li>
            <li><strong>2015:</strong> Opened first major extraction facility</li>
            <li><strong>2020:</strong> Reached 1Mt e-waste milestone</li>
            <li><strong>2024:</strong> Expanded to Lithium recycling</li>
          </ul>
        </div>
        <div class="glass-card reveal">
          <h2>Mission & Vision</h2>
          <p class="mt-4"><strong>Mission:</strong> To provide secure, compliant, and environmentally positive lifecycle solutions for IT assets and complex materials.</p>
          <p class="mt-4"><strong>Vision:</strong> A true circular economy where absolutely nothing goes to waste and natural resources are preserved.</p>
        </div>
      </div>
    </section>
    """,
    "services.html": """
    <section class="section page-header">
      <div class="container">
        <h1 class="hero-title reveal">Our Services</h1>
      </div>
    </section>
    <section class="section services">
      <div class="container">
        <div class="grid services-grid">
          <a href="e-waste-management.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>E-Waste Management</h3>
            <p>End-to-end IT asset disposition, certified dismantling.</p>
          </a>
          <a href="lithium-battery-recycling.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>Lithium Battery Recycling</h3>
            <p>Specialized processing for EV and electronic batteries.</p>
          </a>
          <a href="plastic-recycling.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>Plastic Waste Recycling</h3>
            <p>Advanced sorting and precision pelletizing.</p>
          </a>
          <a href="paper-recycling.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>Paper Recycling</h3>
            <p>Closed-loop processing that saves trees.</p>
          </a>
          <a href="green-metal-recovery.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>Green Metal Recovery</h3>
            <p>High-yield extraction of iron, copper, and aluminum.</p>
          </a>
          <a href="epr-consulting.html" style="text-decoration: none; color: inherit;" class="glass-card service-card reveal">
            <h3>EPR Consulting</h3>
            <p>Strategic guidance to navigate government regulations.</p>
          </a>
        </div>
      </div>
    </section>
    """,
    "e-waste-management.html": """
    <section class="section page-header">
      <div class="container">
        <h1 class="hero-title reveal">E-Waste Management</h1>
        <p class="hero-subtitle reveal">Detailed IT asset disposition.</p>
      </div>
    </section>
    <section class="section">
      <div class="container grid two-col">
        <div class="glass-card reveal">
          <h2>Process Steps</h2>
          <ol style="margin-top: 1rem; padding-left: 1rem;">
            <li>Collection & Secure Transport</li>
            <li>Sorting & Dismantling</li>
            <li>Military-Grade Data Destruction</li>
            <li>Material Recycling & Recovery</li>
          </ol>
        </div>
        <div class="glass-card reveal">
          <h2>Certifications</h2>
          <p>We comply with the DoD 5220.22-M standard for secure data erasure and physical destruction.</p>
          <a href="contact.html" class="btn btn-primary mt-4">Request Quote</a>
        </div>
      </div>
    </section>
    """,
    "lithium-battery-recycling.html": """
    <section class="section page-header">
      <div class="container">
        <h1 class="hero-title reveal">Lithium Battery Recycling</h1>
        <p class="hero-subtitle reveal">Focusing on EV and electronic batteries.</p>
      </div>
    </section>
    <section class="section">
      <div class="container grid two-col">
        <div class="glass-card reveal">
          <h2>Technical Process</h2>
          <ul style="margin-top: 1rem; list-style-position: inside;">
            <li>Thermal Management</li>
            <li>Safe Discharge</li>
            <li>Black Mass Refining</li>
          </ul>
        </div>
        <div class="glass-card reveal">
          <h2>Efficiency</h2>
          <p>We achieve a <strong>98%+ extraction efficiency</strong> for critical elements like lithium and cobalt.</p>
          <a href="contact.html" class="btn btn-primary mt-4">Request Quote</a>
        </div>
      </div>
    </section>
    """,
    "plastic-recycling.html": """
    <section class="section page-header">
      <div class="container">
        <h1 class="hero-title reveal">Plastic Waste Recycling</h1>
      </div>
    </section>
    <section class="section">
      <div class="container glass-card reveal">
        <h2>Advanced Sorting Technology</h2>
        <p class="mt-4">Using precision polymer identification, we sort and pelletize industrial plastic waste into high-quality, reusable manufacturing materials. This significantly lowers environmental impact and reliance on virgin plastics.</p>
      </div>
    </section>
    """,
    "paper-recycling.html": """
    <section class="section page-header">
      <div class="container">
        <h1 class="hero-title reveal">Paper Recycling</h1>
      </div>
    </section>
    <section class="section">
      <div class="container glass-card reveal">
        <h2>Closed-Loop Processing</h2>
        <p class="mt-4">Our paper recycling programs are designed to save trees, conserve water, and reduce your corporate carbon footprint. Ask about our secure document shredding and corporate recycling bins.</p>
      </div>
    </section>
    """,
    "green-metal-recovery.html": """
    <section class="section page-header">
      <div class="container">
        <h1 class="hero-title reveal">Green Metal Recovery</h1>
      </div>
    </section>
    <section class="section">
      <div class="container grid two-col">
        <div class="glass-card reveal">
          <h2>Recovered Metals</h2>
          <p>Iron, Copper, Lithium, Cobalt, Aluminum, Gold, Silver, Palladium, and more.</p>
          <p class="mt-4">Over 22+ distinct metals recovered!</p>
        </div>
        <div class="glass-card reveal">
          <h2>Hydrometallurgical Process</h2>
          <p>We use advanced chemical processing to achieve a <strong>99.5% purity rate</strong>, ready for direct supply chain reintegration.</p>
        </div>
      </div>
    </section>
    """,
    "epr-consulting.html": """
    <section class="section page-header">
      <div class="container">
        <h1 class="hero-title reveal">EPR Consulting</h1>
        <p class="hero-subtitle reveal">Extended Producer Responsibility solutions.</p>
      </div>
    </section>
    <section class="section">
      <div class="container glass-card reveal">
        <h2>Regulatory Compliance</h2>
        <p class="mt-4">Navigate government regulations and achieve collection targets seamlessly. We handle documentation management and serve as your government liaison for all EPR matters.</p>
        <a href="contact.html" class="btn btn-primary mt-4">Book Consultation</a>
      </div>
    </section>
    """,
    "impact.html": """
    <section class="section page-header">
      <div class="container">
        <h1 class="hero-title reveal">Our Impact</h1>
      </div>
    </section>
    <section class="section">
      <div class="container grid stats-grid">
        <div class="glass-card reveal">
          <h2 class="stat-number">1.6Mt</h2>
          <p class="stat-label">E-Waste Processed</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">98%+</h2>
          <p class="stat-label">Extraction Efficiency</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">99.5%</h2>
          <p class="stat-label">Purity Rate</p>
        </div>
        <div class="glass-card reveal">
          <h2 class="stat-number">342+</h2>
          <p class="stat-label">Happy Clients</p>
        </div>
      </div>
    </section>
    """,
    "faq.html": """
    <section class="section page-header">
      <div class="container">
        <h1 class="hero-title reveal">Frequently Asked Questions</h1>
      </div>
    </section>
    <section class="section">
      <div class="container accordion">
        <div class="accordion-item reveal">
          <h3>What materials can be recovered?</h3>
          <p>We recover over 22 distinct metals including copper, gold, aluminum, lithium, and cobalt.</p>
        </div>
        <div class="accordion-item reveal">
          <h3>How do you guarantee data destruction?</h3>
          <p>We follow the DoD 5220.22-M standard involving both software wiping and physical shredding of drives.</p>
        </div>
        <div class="accordion-item reveal">
          <h3>How does EPR consulting work?</h3>
          <p>We assess your manufacturing volume, calculate your target collection quotas, and manage the physical recycling and documentation required to meet those goals.</p>
        </div>
        <div class="accordion-item reveal">
          <h3>Are extraction processes safe?</h3>
          <p>Yes, we are ISO and Green Air Standard certified, ensuring zero-harm atmospheric emissions.</p>
        </div>
        <div class="accordion-item reveal">
          <h3>Do you provide ESG tracking?</h3>
          <p>Absolutely. We provide comprehensive CO2 reduction stats and certificates of recycling for your ESG reporting.</p>
        </div>
      </div>
    </section>
    """,
    "contact.html": """
    <section class="section page-header">
      <div class="container">
        <h1 class="hero-title reveal">Contact Us</h1>
      </div>
    </section>
    <section class="section">
      <div class="container grid two-col">
        <div class="glass-card reveal">
          <h2>Send a Message</h2>
          <form class="contact-form mt-4">
            <input type="text" placeholder="Your Name" required>
            <input type="email" placeholder="Your Email" required>
            <input type="text" placeholder="Company">
            <input type="tel" placeholder="Phone">
            <textarea placeholder="Message" rows="5" required></textarea>
            <button type="submit" class="btn btn-primary">Submit Request</button>
          </form>
        </div>
        <div class="glass-card reveal">
          <h2>Business Details</h2>
          <div class="contact-details mt-4">
            <p><strong>Address:</strong><br>479, Habibpur, Dadri,<br>Gr. Noida, Uttar Pradesh</p>
            <p class="mt-4"><strong>Phone:</strong> <a href="tel:+919319253708">+91 93192 53708</a></p>
            <p class="mt-4"><strong>Email:</strong> <a href="mailto:operation@ecogreen.eco">operation@ecogreen.eco</a></p>
            <p class="mt-4"><strong>Hours:</strong><br>Mon-Fri: 9:00 AM - 6:00 PM</p>
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

print("Created all pages successfully!")
