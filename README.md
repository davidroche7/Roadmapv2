# Architecture-Roadmap
Roadmap repository for Engineering Architecture team.

## Purpose
This repository contains automated tools for the Architecture Team to maintain and publish:
- The team roadmap (shown below)
- A technology radar
- An asset registry

## 🛤️ Architecture Team Roadmap 2025

<div id="roadmap">
  <h2>Roadmap Timeline</h2>
  <div class="mermaid" id="roadmap-chart">
    <!-- Mermaid chart will be inserted here by JavaScript -->
  </div>
  
  <div id="project-table">
    <!-- Project table will be inserted here by JavaScript -->
  </div>
  
  <div class="export-buttons">
    <button id="export-html">Export as HTML</button>
    <button id="export-confluence">Export for Confluence</button>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({ startOnLoad: false, theme: 'default' });
</script>
<script src="roadmap.js"></script>
<script>
  // Load the roadmap when the page loads
  document.addEventListener('DOMContentLoaded', loadRoadmap);
</script>

<style>
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  th {
    background-color: #f2f2f2;
  }
  button {
    padding: 8px 12px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin: 10px 5px 10px 0;
  }
</style>

## How It Works
1. Edit the `roadmap-data.json` file to update the roadmap data
2. The roadmap and project table are automatically generated in this README
3. Use the export buttons to download the roadmap in different formats

## System Overview
This automation system keeps the roadmap above in sync with our Monday.com board and connects it to our existing Tech Radar and a new Asset Registry.
