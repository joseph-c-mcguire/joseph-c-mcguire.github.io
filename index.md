---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Joseph McGuire
subtitle: AI/ML Engineer | Data Scientist | Software Engineer
hero_height: is-large
hero_image: /assets/images/bishop-peak.png
---

<div class="section">
  <h2>About Me</h2>
  <p>Results-driven AI/ML Engineer, Data Scientist, and Software Engineer with expertise in developing scalable machine learning models, cloud-based ML systems, and full-stack applications. I specialize in predictive analytics, real-time inference, and automation solutions, optimizing workflows and enhancing decision-making across multiple industries, including finance, healthcare, and material science.</p>
  <p>I have a proven track record of securing government contracts, leading R&D efforts, and deploying high-performance AI solutions. I'm passionate about bridging the gap between cutting-edge research and practical AI deployment to drive business impact.</p>
</div>

<div class="section">
  <h2>Experience</h2>
  <ul>
    <li><strong>Freelance Software Engineer and Consultant</strong> - Self-Employed / NextFrame Analytics (October 2024 - Present)
      <ul>
        <li>Developed and deployed AI/ML-powered applications for research and financial sectors, enhancing predictive accuracy by 15% and optimizing millions of financial strategies.</li>
        <li>Built scalable ML pipelines, enabling 100 TPS real-time inference, automated model retraining, and cloud deployment.</li>
        <li>Designed and implemented an algorithmic trading optimization system leveraging reinforcement learning, improving financial modeling performance.</li>
      </ul>
    </li>
    <li><strong>AIMdyn, Inc.</strong> - Research Engineer (October 2022 - November 2024)
      <ul>
        <li>Developed ML inference systems and APIs for high-impact government projects, improving decision-making capabilities.</li>
        <li>Led R&D efforts for DARPA, securing a $1 million contract in AI-driven predictive modeling.</li>
        <li>Achieved 10% relative RMSE for multi-state, 100-step ahead predictions.</li>
      </ul>
    </li>
    <li><strong>Brooksource (Contractor for Deloitte US - Data and Analytics)</strong> - Data Scientist (June 2022 - October 2022)
      <ul>
        <li>Developed AI-driven anonymization frameworks, reducing data breach risks by 40% for enterprise clients.</li>
        <li>Optimized data engineering pipelines, improving efficiency and scalability by 35%.</li>
      </ul>
    </li>
    <li><strong>Cal Poly, San Luis Obispo</strong> - Graduate Researcher (September 2021 - June 2022)
      <ul>
        <li>Developed a COVID-19 forecasting model, improving predictions by 15% compared to ARIMA models.</li>
        <li>Presented research on network-based ML methods for public health applications, influencing policy recommendations.</li>
      </ul>
    </li>
  </ul>
</div>

<div class="section">
  <h2>Key Competencies</h2>
  <div class="cards">
    <div class="card">
      <i class="fas fa-brain"></i>
      <h3>AI/ML Expertise</h3>
      <p>Expert in developing scalable machine learning models, predictive analytics, and real-time inference systems for finance, healthcare, and material science applications.</p>
    </div>
    <div class="card">
      <i class="fas fa-project-diagram"></i>
      <h3>Technical Leadership</h3>
      <p>Led cross-functional teams on high-profile projects, securing contracts and delivering innovative solutions for government and enterprise clients.</p>
    </div>
    <div class="card">
      <i class="fas fa-database"></i>
      <h3>Full-Stack Development</h3>
      <p>Proficient in developing and deploying efficient ML pipelines, RESTful APIs, microservices, and cloud-based applications with a focus on performance and scalability.</p>
    </div>
  </div>
</div>

<div class="nav">
  <a href="/">Home</a>
  <a href="/about/">About</a>
  <a href="/contact/">Contact</a>
  <a href="/technical-writing/">Technical Writing</a>
  <a href="/github-projects/">GitHub Projects</a>
  <a href="/posts/">Blog Posts</a>
  <a href="/services/">Services</a>
</div>

<div class="section">
  <h2>Blog Posts</h2>
  <ul>
    {% for post in site.posts limit:5 %}
      <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> - {{ post.date | date: "%B %d, %Y" }}</li>
    {% endfor %}
  </ul>
</div>

<div class="section">
  <h2>Subscribe to Newsletter</h2>
  <form action="https://YOUR_MAILCHIMP_URL" method="post" target="_blank">
    <div>
      <label for="email">Email:</label>
      <input type="email" id="email" name="EMAIL" required>
    </div>
    <div>
      <input type="submit" value="Subscribe">
    </div>
  </form>
</div>

<div class="section">
  <h2>Contact</h2>
  <ul>
    <li>Location: Providence, RI 02906</li>
    <li>Phone: +1 (805) 468-5639</li>
    <li>Email: <a href="mailto:joseph.c.mcg@gmail.com">joseph.c.mcg@gmail.com</a></li>
    <li>GitHub: <a href="https://github.com/joseph-c-mcguire">joseph-c-mcguire</a></li>
    <li>LinkedIn: <a href="https://www.linkedin.com/in/joseph-c-mcg">joseph-c-mcg</a></li>
    <li>Website: <a href="https://joseph-c-mcguire.github.io">joseph-c-mcguire.github.io</a></li>
  </ul>
</div>

<div class="section">
  <h2>Top Skills</h2>
  <ul>
    <li>Machine Learning</li>
    <li>Time-Series Analysis</li>
    <li>Data Science</li>
    <li>Python</li>
    <li>Cloud Computing</li>
    <li>Full-Stack Development</li>
  </ul>
</div>

<div class="section">
  <h2>GitHub Projects</h2>
  <ul>
    <li><a href="https://github.com/joseph-c-mcguire/strategy-quant-clone">StrategyQuant Clone</a>: Optimized and backtested 100,000+ trading strategies using backtrader, pandas, numpy, and yfinance.</li>
    <li><a href="https://github.com/joseph-c-mcguire/ercot-scraping">ERCOT Scraping Module</a>: Scraped over 1TB of market data from the ERCOT API, optimizing SQL queries for large-scale data extraction.</li>
    <li><a href="https://github.com/joseph-c-mcguire/predictive-maintenance">Predictive Maintenance System</a>: Backend API supported 1000+ simultaneous users and achieved 84% accuracy in a multi-class problem.</li>
    <li><a href="https://github.com/joseph-c-mcguire/desktop-reminders">Desktop-Reminders</a>: A super simple script that allows you to get reminders on your desktop.</li>
    <li><a href="https://github.com/joseph-c-mcguire/joseph-c-mcguire.github.io">This Website</a>: The source code for my personal website, built using Jekyll and hosted on GitHub Pages.</li>
  </ul>
</div>

<div class="section">
  <h2>Technical Writing</h2>
  <p>Explore my technical writing pieces where I delve into various topics related to data science, machine learning, and software engineering. These writings provide insights, tutorials, and in-depth analyses of complex subjects.</p>
  <ul>
    <li><a href="/technical-writing/github-vscode-workflow/">Mastering GitHub & VS Code</a>: Streamlined workflows and best practices.</li>
    <li><a href="/technical-writing/selenium-vs-requests/">Selenium vs. HTML Requests</a>: Choosing the right tool for web automation.</li>
    <li><a href="/technical-writing/">View All Technical Writing</a></li>
  </ul>
</div>

<div class="section">
  <h2>Services Offered</h2>
  <p>I offer a range of professional services leveraging my expertise in AI/ML development, data science, and project management. Visit my services page to learn more about how I can help you or your organization.</p>
  <ul>
    <li><a href="/services/">View All Services</a></li>
  </ul>
</div>
