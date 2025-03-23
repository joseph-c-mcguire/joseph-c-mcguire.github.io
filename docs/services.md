---
layout: page
title: Services
permalink: /services/
description: Professional services offered by Joseph McGuire.
---
{% include y2k-header.html %}

<style>
  .services {
    font-family: 'Roboto', sans-serif;
    color: #333;
    margin: 20px 0;
    padding: 20px;
  }
  .services h1 {
    color: #555;
    margin-bottom: 20px;
    text-align: center;
  }
  .service-card {
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    padding: 20px;
    transition: transform 0.3s ease;
  }
  .service-card:hover {
    transform: translateY(-5px);
  }
  .service-card h2 {
    color: #007bff;
    margin-top: 0;
  }
  .service-card h3 {
    color: #333;
    margin-top: 10px;
  }
  .service-card .service-description {
    margin-bottom: 15px;
  }
  .service-card .service-meta {
    display: flex;
    justify-content: space-between;
    color: #777;
    font-size: 0.9em;
    border-top: 1px solid #eee;
    padding-top: 10px;
    margin-top: 10px;
  }
  .service-card a.service-link {
    display: inline-block;
    background-color: #007bff;
    color: white;
    padding: 8px 16px;
    text-decoration: none;
    border-radius: 4px;
    margin-top: 10px;
    transition: background-color 0.3s ease;
  }
  .service-card a.service-link:hover {
    background-color: #0056b3;
  }
  .service-category {
    display: inline-block;
    background-color: #f0f0f0;
    padding: 3px 8px;
    border-radius: 4px;
    margin-right: 5px;
    font-size: 0.8em;
  }
</style>

<div class="services">
  <h1>Professional Services</h1>
  
  {% assign services = site.services | sort: 'date' | reverse %}
  {% for service in services %}
    <div class="service-card">
      <h2>{{ service.title }}</h2>
      <div class="service-description">
        {{ service.excerpt }}
      </div>
      <div>
        {% for category in service.categories %}
          <span class="service-category">{{ category }}</span>
        {% endfor %}
      </div>
      <div class="service-meta">
        <span>Starting at: ${{ service.rate }}</span>
        <span>{{ service.duration }}</span>
      </div>
      <a href="{{ service.url }}" class="service-link">Learn More</a>
    </div>
  {% endfor %}
  
  {% if services.size == 0 %}
    <p class="text-center">No services listed yet. Check back soon!</p>
  {% endif %}
</div>
