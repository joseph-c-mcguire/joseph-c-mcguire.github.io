---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Joseph McGuire
subtitle: Research Engineer | Data Scientist | Software Engineer
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

<div class="section">
  <div class="card-container">
    <div class="card">
      <i class="fas fa-brain"></i>
      <h3>AI/ML Development</h3>
      <p>Expert in developing and implementing advanced AI/ML algorithms, particularly using in time-series applications to enhance dynamic environment simulations.</p>
    </div>
    <div class="card">
      <i class="fas fa-project-diagram"></i>
      <h3>Exercised Project Management Experience</h3>
      <p>Led cross-functional teams on high-profile projects, successfully securing contracts and delivering innovative solutions.</p>
    </div>
    <div class="card">
      <i class="fas fa-database"></i>
      <h3>Data Science Professional</h3>
      <p>Proficient in developing and deploying efficient ML pipelines for large datasets, improving data analysis speed and accuracy, and contributing to data anonymization projects.</p>
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
    <li>Time-Series</li>
    <li>Data Science</li>
    <li>Python</li>
    <li>Artificial Intelligence (AI)</li>
  </ul>
</div>

<div class="section">
  <h2>Summary</h2>
  <p>As a Research Engineer at AIMdyn, Inc., I specialize in developing and implementing advanced AI/ML algorithms, particularly using Koopman operator theory to enhance dynamic environment simulations. I have a proven track record of leading cross-functional teams on high-profile projects, such as DARPA’s SCEPTER program, where I successfully secured contracts and delivered innovative solutions. My expertise extends to data science, where I excel in developing and deploying efficient ML pipelines for large datasets, improving data analysis speed and accuracy, and contributing to data anonymization projects.</p>

  <p>In addition to my technical skills, I am passionate about mentoring junior engineers and fostering their development within Agile workflows. I am also adept at client engagement, acting as the primary technical contact to deliver updates and address engineering inquiries. Outside of work, I’m an avid hiker, traveler, and cooking enthusiast, and I’m currently learning to fence.</p>
</div>

<div class="section">
  <h2>Experience</h2>
  <ul>
    <li><strong>AIMdyn, Inc.</strong> - Research Engineer (October 2022 - Present)
      <ul>
        <li>Project Management: Led a cross-functional team of engineers and scientists on the DARPA SCEPTER/KHAOSRAZOR program, successfully securing a Phase 2 contract with BAE Systems.</li>
        <li>Algorithm Development: Designed and implemented advanced algorithms using AIMdyn’s Koopman operator theory, enhancing dynamic environment simulations.</li>
        <li>Machine Learning Pipeline: Developed and deployed an efficient ML pipeline for processing large datasets, improving data analysis speed and accuracy.</li>
        <li>Research and Development: Conducted research to develop innovative solutions, optimizing performance and scalability of dynamic simulations.</li>
        <li>Mentorship: Mentored junior engineers, fostering skill development and integration into Agile workflows.</li>
        <li>Client Engagement: Acted as the primary technical contact for clients, delivering updates and addressing engineering inquiries.</li>
      </ul>
    </li>
    <li><strong>Deloitte US - Data and Analytics</strong> - Data Scientist (June 2022 - October 2022)
      <ul>
        <li>Data Privacy: Contributed to data anonymization projects, implementing robust measures to enhance privacy and compliance.</li>
        <li>ETL Development: Developed and optimized ETL processes using Informatica, improving data flow and processing efficiency.</li>
        <li>Generative AI: Created generative AI models in Python for data anonymization, enhancing data handling processes.</li>
      </ul>
    </li>
    <li><strong>Cal Poly, San Luis Obispo</strong> - Graduate Research: Detection of Community Structure in Networks (September 2021 - June 2022)
      <ul>
        <li>Predictive Modeling: Developed a COVID-19 prediction model using Python and network analysis, demonstrating superior accuracy compared to traditional methods.</li>
        <li>Communication: Presented research findings to academic committees and the public, receiving accolades for presentation quality.</li>
      </ul>
    </li>
    <li><strong>University of California, Los Angeles</strong> - Research Intern: Modeling Deforestation in the Amazon (May 2019 - September 2019)
      <ul>
        <li>Model Design: Developed a predictive model achieving 86% accuracy in deforestation pattern analysis using time-series data.</li>
        <li>Data Analysis: Utilized MATLAB’s topography toolbox for detailed spatial data analysis, enhancing research insights.</li>
      </ul>
    </li>
  </ul>
</div>

<div class="section">
  <h2>GitHub Projects</h2>
  <ul>
    <li><a href="https://github.com/joseph-c-mcguire/desktop-reminders">Desktop-Reminders</a>: A super simple script that allows you to get reminders on your desktop.</li>
    <li><a href="https://github.com/joseph-c-mcguire/joseph-c-mcguire.github.io">This Website</a>: The source code for my personal website, built using Jekyll and hosted on GitHub Pages.</li>
    <li><a href="https://github.com/joseph-c-mcguire/Machine-Learning-Notes">Murphy's Machine Learning Notes</a>: A repository for my notebooks as I work through Murphy's Machine Learning: A Probabilistic Perspective.</li>
    <li><a href="https://github.com/joseph-c-mcguire/Math-of-data-science">Math of Data Science Course Material</a>: Course materials and notes for the Math of Data Science course.</li>
  </ul>
</div>

<div class="section">
  <h2>Technical Writing</h2>
  <p>Explore my technical writing pieces where I delve into various topics related to data science, machine learning, and software engineering. These writings provide insights, tutorials, and in-depth analyses of complex subjects.</p>
  <ul>
    <li><a href="/technical-writing/">Technical Writing Page</a></li>
  </ul>
</div>

<div class="section">
  <h2>Services Offered</h2>
  <p>I offer a range of professional services leveraging my expertise in AI/ML development, data science, and project management. Visit my services page to learn more about how I can help you or your organization.</p>
  <ul>
    <li><a href="/services/">View All Services</a></li>
  </ul>
</div>
