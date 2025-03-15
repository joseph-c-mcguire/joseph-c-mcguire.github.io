---
layout: page
title: GitHub Projects
permalink: /github-projects/
description: Blurbs about some of my GitHub projects.
---
{% include y2k-header.html %}

<style>
  .github-projects {
    font-family: 'Roboto', sans-serif;
    color: #333;
    margin: 20px 0;
    padding: 20px;
    background-color: #f4f4f4;
  }
  .github-projects h1 {
    color: #555;
    margin-bottom: 20px;
    text-align: center;
  }
  .project-card {
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    padding: 20px;
  }
  .project-card h2 {
    color: #007bff;
    margin-top: 0;
  }
  .project-card h3 {
    color: #333;
    margin-top: 10px;
  }
  .project-card ul {
    list-style-type: none;
    padding: 0;
  }
  .project-card ul li {
    margin: 10px 0;
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  .project-card ul li a {
    color: #007bff;
    text-decoration: none;
    font-weight: bold;
  }
  .project-card ul li a:hover {
    text-decoration: underline;
  }
  .project-card pre {
    background-color: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
  }
  .project-card .project-description,
  .project-card .project-features,
  .project-card .project-usage,
  .project-card .project-configuration {
    margin-bottom: 20px;
  }
</style>

<div class="github-projects">
  <h1>GitHub Projects</h1>

  <div class="project-card">
    <h2><a href="https://github.com/joseph-c-mcguire/desktop-reminders">Desktop-Reminders</a></h2>
    <div class="project-description">
      <h3>Description</h3>
      <p>This is a super simple script that allows you to get reminders on your desktop.</p>
    </div>
    <div class="project-usage">
      <h3>How to Use</h3>
      <ol>
        <li>Clone the repository:
          <pre><code>git clone https://github.com/joseph-c-mcguire/desktop-reminders.git
cd desktop-reminders</code></pre>
        </li>
        <li>Run the script:
          <pre><code>python3 main.py -c &lt;PATH TO CONFIG FILE&gt;</code></pre>
          Or just run with the default config found in the repo:
          <pre><code>python3 main.py</code></pre>
        </li>
      </ol>
    </div>
    <div class="project-configuration">
      <h3>Configuration</h3>
      <p>To modify the config, edit the message in the following format:</p>
      <pre><code>&lt;MESSAGE ID&gt;
  wait: &lt;TIME TO WAIT BETWEEN NOTIFICATIONS&gt;
  message: &lt;THE BODY OF THE NOTIFICATION&gt;
  title: &lt;THE TITLE OF THE NOTIFICATION&gt;
  max-number: &lt;THE MAXIMUM NUMBER OF TIMES THE NOTIFICATION WILL BE POSTED&gt;</code></pre>
      <p>Additionally, supports extra parameters as supported by <a href="https://ms7m.github.io/notify-py/">notify-py</a>.</p>
    </div>
  </div>

  <div class="project-card">
    <h2><a href="https://github.com/joseph-c-mcguire/joseph-c-mcguire.github.io">This Website</a></h2>
    <div class="project-description">
      <h3>Description</h3>
      <p>The source code for my personal website, built using Jekyll and hosted on GitHub Pages.</p>
    </div>
    <div class="project-features">
      <h3>Features</h3>
      <ul>
        <li>Responsive design</li>
        <li>Blog posts</li>
        <li>Project showcase</li>
        <li>Contact form</li>
      </ul>
    </div>
    <div class="project-usage">
      <h3>How to Use</h3>
      <ol>
        <li>Clone the repository:
          <pre><code>git clone https://github.com/joseph-c-mcguire/joseph-c-mcguire.github.io.git
cd joseph-c-mcguire.github.io</code></pre>
        </li>
        <li>Install dependencies:
          <pre><code>bundle install</code></pre>
        </li>
        <li>Run the site locally:
          <pre><code>bundle exec jekyll serve</code></pre>
        </li>
      </ol>
    </div>
  </div>

  <div class="project-card">
    <h2><a href="https://github.com/joseph-c-mcguire/Machine-Learning-Notes">Murphy's Machine Learning Notes</a></h2>
    <div class="project-description">
      <h3>Description</h3>
      <p>A repository for my notebooks as I work through <a href="https://www.amazon.com/Machine-Learning-Probabilistic-Perspective-Computation/dp/0262018020/ref=sr_1_1?keywords=machine+learning+a+probabilistic+perspective&amp;qid=1662569955&amp;sprefix=machine+learning%3A+A+P%2Caps%2C184&amp;sr=8-1">Murphy's Machine Learning: A Probabilistic Perspective</a>.</p>
    </div>
    <div class="project-usage">
      <h3>How to Use</h3>
      <ol>
        <li>Clone the repository:
          <pre><code>git clone https://github.com/joseph-c-mcguire/Machine-Learning-Notes.git
cd Machine-Learning-Notes</code></pre>
        </li>
        <li>Open the notebooks using Jupyter Notebook or JupyterLab:
          <pre><code>jupyter notebook</code></pre>
        </li>
      </ol>
    </div>
  </div>

  <div class="project-card">
    <h2><a href="https://github.com/joseph-c-mcguire/Math-of-data-science">Math of Data Science Course Material</a></h2>
    <div class="project-description">
      <h3>Description</h3>
      <p>Course materials and notes for the Math of Data Science course.</p>
    </div>
    <div class="project-usage">
      <h3>How to Use</h3>
      <ol>
        <li>Clone the repository:
          <pre><code>git clone https://github.com/joseph-c-mcguire/Math-of-data-science.git
cd Math-of-data-science</code></pre>
        </li>
        <li>Open the materials using Jupyter Notebook or JupyterLab:
          <pre><code>jupyter notebook</code></pre>
        </li>
      </ol>
    </div>
  </div>

  <div class="project-card">
    <h2><a href="https://github.com/joseph-c-mcguire/webapp-example-frontend">Predictive Maintenance System</a></h2>
    <div class="project-description">
      <h3>Description</h3>
      <p>The Predictive Maintenance System is a web application designed to perform Exploratory Data Analysis (EDA) and model diagnostics on a predictive maintenance dataset. The frontend is built using React and communicates with a backend server to fetch and display data. The application allows users to interact with the model, query it with new inputs, and view performance metrics.</p>
    </div>
    <div class="project-usage">
      <h3>How to Use</h3>
      <ol>
        <li>Visit the deployed application: <a href="https://webapp-example-frontend-56f2ec31cf0a.herokuapp.com/">Predictive Maintenance System</a></li>
        <li>Clone the repository:
          <pre><code>git clone https://github.com/joseph-c-mcguire/webapp-example-frontend.git
cd webapp-example-frontend</code></pre>
        </li>
        <li>Install dependencies:
          <pre><code>npm install</code></pre>
        </li>
        <li>Run the application locally:
          <pre><code>npm start</code></pre>
        </li>
      </ol>
    </div>
  </div>

  <div class="project-card">
    <h2><a href="https://github.com/joseph-c-mcguire/webapp-example-backend">Predictive Maintenance System Backend</a></h2>
    <div class="project-description">
      <h3>Description</h3>
      <p>This project is a backend system for a predictive maintenance application. The system is designed for training, serving, and producing diagnostics for a set of models trained on a UCI dataset. This was a learning exercise to build a full-stack web application. The frontend repo can be found <a href="https://github.com/joseph-c-mcguire/webapp-example-frontend">here</a>.</p>
      <p>The dataset is a predictive maintenance dataset hosted by the University of California, Irvine, and can also be found on Kaggle.com. Three sample models (Decision Tree, Gradient Boosting, and Random Forest) were trained to handle the multi-class classification problem. These models were selected for their consistent class structure in Scikit-Learn, making it easier to retrieve attributes like <code>feature_importances_</code> and methods like <code>predict_proba</code> across different models.</p>
    </div>
    <div class="project-usage">
      <h3>How to Use</h3>
      <ol>
        <li>Clone the repository:
          <pre><code>git clone https://github.com/joseph-c-mcguire/webapp-example-backend.git
cd webapp-example-backend</code></pre>
        </li>
        <li>Install dependencies:
          <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Run the server locally:
          <pre><code>python run.py</code></pre>
        </li>
        <li>For production, use:
          <pre><code>python app.py</code></pre>
        </li>
      </ol>
    </div>
  </div>
</div>

Feel free to explore the repositories and contribute if you find something interesting!
