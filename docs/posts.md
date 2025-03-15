---
layout: page
title: Blog Posts
permalink: /posts/
---
{% include y2k-header.html %}

<style>
  .posts {
    font-family: 'Roboto', sans-serif;
    color: #333;
    margin: 20px 0;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  .posts h1 {
    color: #555;
    margin-bottom: 20px;
  }
  .posts ul {
    list-style-type: none;
    padding: 0;
  }
  .posts ul li {
    margin: 10px 0;
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  .posts ul li a {
    color: #007bff;
    text-decoration: none;
    font-weight: bold;
  }
  .posts ul li a:hover {
    text-decoration: underline;
  }
  .posts ul li span {
    display: block;
    color: #999;
    font-size: 0.9em;
  }
</style>

<div class="posts">
  <h1>Blog Posts</h1>
  <ul>
    {% for post in site.posts %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span>{{ post.date | date: "%B %d, %Y" }}</span>
      </li>
    {% endfor %}
  </ul>
</div>
