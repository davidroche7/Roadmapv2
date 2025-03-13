// Function to generate Mermaid gantt chart from project data
function generateGanttChart(projects) {
  let gantt = 'gantt\n';
  gantt += '  title Architecture Roadmap Timeline\n';
  gantt += '  dateFormat YYYY-MM-DD\n';
  gantt += '  axisFormat %b %Y\n\n';
  
  // Group projects by architect
  const architectProjects = {};
  
  projects.forEach(project => {
    const architect = project.architect || 'Unassigned';
    if (!architectProjects[architect]) {
      architectProjects[architect] = [];
    }
    architectProjects[architect].push(project);
  });
  
  // Add projects to gantt chart
  for (const architect in architectProjects) {
    gantt += `  section ${architect}\n`;
    
    architectProjects[architect].forEach(project => {
      let status = 'active';
      const statusLower = (project.status || '').toLowerCase();
      
      if (statusLower.includes('complete') || statusLower.includes('done')) {
        status = 'done';
      } else if (statusLower.includes('plan')) {
        status = 'planned';
      }
      
      gantt += `    ${project.project_name} :${status}, ${project.start_date}, ${project.end_date}\n`;
    });
  }
  
  return gantt;
}

// Function to generate project details HTML table
function generateProjectTable(projects) {
  let html = '<h2>Project Details</h2>\n';
  html += '<table>\n';
  html += '  <tr>\n';
  html += '    <th>Project</th>\n';
  html += '    <th>Architect</th>\n';
  html += '    <th>Type</th>\n';
  html += '    <th>Status</th>\n';
  html += '    <th>Start Date</th>\n';
  html += '    <th>End Date</th>\n';
  html += '  </tr>\n';
  
  projects.forEach(project => {
    html += '  <tr>\n';
    html += `    <td>${project.project_name || ''}</td>\n`;
    html += `    <td>${project.architect || ''}</td>\n`;
    html += `    <td>${project.type || ''}</td>\n`;
    html += `    <td>${project.status || ''}</td>\n`;
    html += `    <td>${project.start_date || ''}</td>\n`;
    html += `    <td>${project.end_date || ''}</td>\n`;
    html += '  </tr>\n';
  });
  
  html += '</table>';
  return html;
}

// Function to generate Confluence markup
function generateConfluenceMarkup(projects) {
  let confluence = 'h1. Architecture Roadmap\n\n';
  
  // Mermaid diagram
  confluence += 'h2. Roadmap Timeline\n\n';
  confluence += '{code:language=mermaid}\n';
  confluence += generateGanttChart(projects);
  confluence += '{code}\n\n';
  
  // Project details table
  confluence += 'h2. Project Details\n\n';
  confluence += '||Project||Architect||Type||Status||Start Date||End Date||\n';
  
  projects.forEach(project => {
    confluence += `|${project.project_name || ''}|${project.architect || ''}|${project.type || ''}|${project.status || ''}|${project.start_date || ''}|${project.end_date || ''}|\n`;
  });
  
  return confluence;
}

// Load roadmap data and setup the page
async function loadRoadmap() {
  try {
    const response = await fetch('roadmap-data.json');
    if (!response.ok) {
      throw new Error('Failed to load roadmap data');
    }
    
    const projects = await response.json();
    
    // Generate gantt chart
    const ganttChart = generateGanttChart(projects);
    document.getElementById('roadmap-chart').textContent = ganttChart;
    
    // Generate project table
    const projectTable = generateProjectTable(projects);
    document.getElementById('project-table').innerHTML = projectTable;
    
    // Initialize Mermaid
    mermaid.init(undefined, document.querySelectorAll('.mermaid'));
    
    // Setup export buttons
    document.getElementById('export-confluence').addEventListener('click', () => {
      const confluence = generateConfluenceMarkup(projects);
      
      // Create and trigger download
      const blob = new Blob([confluence], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'confluence-roadmap.txt';
      a.click();
      URL.revokeObjectURL(url);
      
      alert('Confluence markup exported. To use in Confluence:\n\n1. Create or edit a Confluence page\n2. Click "Insert" > "Markup"\n3. Choose "Confluence Wiki" format\n4. Paste the contents of the downloaded file\n5. Click "Insert"');
    });
    
    document.getElementById('export-html').addEventListener('click', () => {
      const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Architecture Team Roadmap</title>
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    table { width: 100%; border-collapse: collapse; margin: 20px 0; }
    th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
    th { background-color: #f2f2f2; }
  </style>
</head>
<body>
  <h1>Architecture Roadmap</h1>
  
  <h2>Roadmap Timeline</h2>
  <div class="mermaid">
${ganttChart}
  </div>
  
  ${projectTable}
  
  <script>
    mermaid.initialize({ startOnLoad: true });
  </script>
</body>
</html>`;
      
      // Create and trigger download
      const blob = new Blob([html], { type: 'text/html' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'architecture-roadmap.html';
      a.click();
      URL.revokeObjectURL(url);
    });
    
  } catch (error) {
    console.error('Error loading roadmap:', error);
    document.getElementById('roadmap-chart').textContent = 'Error loading roadmap data: ' + error.message;
  }
}
