#!/usr/bin/env python3
# roadmap_generator.py
import json
import os
from datetime import datetime

def read_roadmap_data(filepath='roadmap-data.json'):
    """Read the roadmap data from JSON file"""
    with open(filepath, 'r') as file:
        return json.load(file)

def sort_projects(projects):
    """Sort projects by type and then by start date"""
    # Group projects by type
    grouped_by_type = {}
    for project in projects:
        project_type = project.get('type', 'Other')
        if project_type not in grouped_by_type:
            grouped_by_type[project_type] = []
        grouped_by_type[project_type].append(project)
    
    # Sort each group by start date
    for project_type in grouped_by_type:
        grouped_by_type[project_type].sort(
            key=lambda x: datetime.strptime(x.get('start_date', '2099-01-01'), '%Y-%m-%d')
        )
    
    return grouped_by_type

def generate_mermaid_gantt(projects):
    """Generate Mermaid Gantt chart"""
    grouped_projects = sort_projects(projects)
    
    mermaid_code = """gantt
  title Architecture Roadmap Timeline
  dateFormat YYYY-MM-DD
  axisFormat %b %Y
"""
    
    # For each project type, create a section
    for project_type, type_projects in grouped_projects.items():
        mermaid_code += f"\n  section {project_type}\n"
        
        for project in type_projects:
            project_status = 'planned' if project.get('status') == 'Planned' else 'active'
            mermaid_code += f"    {project.get('project_name')} ({project.get('architect')}) :{project_status}, {project.get('start_date')}, {project.get('end_date')}\n"
    
    return mermaid_code

def generate_project_table_html(projects):
    """Generate HTML table for project details"""
    table_html = """<table>
    <tr>
        <th>Project</th>
        <th>Architect</th>
        <th>Type</th>
        <th>Status</th>
        <th>Start Date</th>
        <th>End Date</th>
        <th>Description</th>
        <th>Technologies</th>
    </tr>
"""
    
    for project in projects:
        technologies = ', '.join(project.get('technologies', [])) if project.get('technologies') else ''
        description = project.get('description', '')
        
        table_html += f"""    <tr>
        <td>{project.get('project_name', '')}</td>
        <td>{project.get('architect', '')}</td>
        <td>{project.get('type', '')}</td>
        <td>{project.get('status', '')}</td>
        <td>{project.get('start_date', '')}</td>
        <td>{project.get('end_date', '')}</td>
        <td>{description}</td>
        <td>{technologies}</td>
    </tr>
"""
    
    table_html += '</table>'
    return table_html

def generate_confluence_markup(projects):
    """Generate Confluence markup"""
    mermaid_gantt = generate_mermaid_gantt(projects)
    
    confluence_markup = """h1. Architecture Roadmap

h2. Roadmap Timeline

{code:language=mermaid}
"""
    confluence_markup += mermaid_gantt
    confluence_markup += """{code}

h2. Project Details

||Project||Architect||Type||Status||Start Date||End Date||Description||Technologies||
"""
    
    for project in projects:
        technologies = ', '.join(project.get('technologies', [])) if project.get('technologies') else ''
        description = project.get('description', '')
        
        confluence_markup += f"|{project.get('project_name', '')}|{project.get('architect', '')}|{project.get('type', '')}|{project.get('status', '')}|{project.get('start_date', '')}|{project.get('end_date', '')}|{description}|{technologies}|\n"
    
    return confluence_markup

def generate_simple_html(projects):
    """Generate simple HTML file"""
    mermaid_gantt = generate_mermaid_gantt(projects)
    project_table = generate_project_table_html(projects)
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architecture Roadmap</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@9.4.3/dist/mermaid.min.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; overflow-x: auto; display: block; }}
        th, td {{ padding: 8px; text-align: left; border: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; position: sticky; top: 0; }}
        .mermaid {{ margin: 20px 0; overflow-x: auto; }}
        .export-btn {{ padding: 8px 12px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer; margin: 10px 5px 10px 0; }}
        .gantt-container {{ overflow-x: auto; max-width: 100%; }}
    </style>
</head>
<body>
    <h1>Architecture Roadmap</h1>
    
    <div>
        <button class="export-btn" onclick="exportToCSV()">Export to CSV</button>
        <button class="export-btn" onclick="window.location.href='export-confluence.html'">Export for Confluence</button>
    </div>
    
    <h2>Roadmap Timeline</h2>
    <div class="gantt-container">
        <div class="mermaid">
{mermaid_gantt}
        </div>
    </div>
    
    <h2>Project Details</h2>
    {project_table}
    
    <script>
        mermaid.initialize({{ 
            startOnLoad: true,
            securityLevel: 'loose',
            gantt: {{
                barHeight: 20,
                barGap: 4,
                topPadding: 50,
                leftPadding: 150,
                rightPadding: 20,
                fontFamily: 'Arial, sans-serif',
                fontSize: 12
            }}
        }});
        
        function exportToCSV() {{
            // Get the table
            const table = document.querySelector('table');
            
            // Prepare CSV content
            let csv = [];
            const rows = table.querySelectorAll('tr');
            
            rows.forEach(row => {{
                const rowData = [];
                const cells = row.querySelectorAll('th, td');
                cells.forEach(cell => {{
                    rowData.push('"' + cell.textContent.replace(/"/g, '""') + '"');
                }});
                csv.push(rowData.join(','));
            }});
            
            // Create CSV file
            const csvContent = csv.join('\\n');
            const blob = new Blob([csvContent], {{ type: 'text/csv;charset=utf-8;' }});
            const link = document.createElement('a');
            const url = URL.createObjectURL(blob);
            
            link.setAttribute('href', url);
            link.setAttribute('download', 'architecture_roadmap.csv');
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }}
    </script>
</body>
</html>"""

def generate_confluence_export_html(projects):
    """Generate Confluence export HTML"""
    confluence_markup = generate_confluence_markup(projects)
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confluence Markup Export</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        pre {{ white-space: pre-wrap; font-family: monospace; margin: 20px; padding: 15px; background-color: #f5f5f5; border: 1px solid #ddd; }}
        button {{ margin: 20px; padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer; }}
    </style>
</head>
<body>
    <h1>Confluence Markup Export</h1>
    
    <button onclick="copyToClipboard()">Copy to Clipboard</button>
    
    <pre id="confluence-content">{confluence_markup}</pre>
    
    <script>
        function copyToClipboard() {{
            const content = document.getElementById('confluence-content').textContent;
            navigator.clipboard.writeText(content).then(() => {{
                alert('Copied to clipboard');
            }}).catch(err => {{
                console.error('Failed to copy: ', err);
            }});
        }}
    </script>
</body>
</html>"""

def generate_index_html(projects):
    """Generate the main index.html"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architecture Team Roadmap</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@9.4.3/dist/mermaid.min.js"></script>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            margin: 0;
            padding: 20px; 
            line-height: 1.6;
            color: #333;
        }}
        .container {{ 
            max-width: 1200px; 
            margin: 0 auto;
            padding: 20px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        .table-container {{
            overflow-x: auto;
            max-width: 100%;
            margin-bottom: 20px;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
            position: sticky;
            top: 0;
        }}
        button {{
            padding: 8px 12px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin: 10px 5px 10px 0;
        }}
        .github-link {{
            position: absolute;
            top: 10px;
            right: 10px;
        }}
        .gantt-container {{
            overflow-x: auto;
            max-width: 100%;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <a href="https://github.com/davidroche7/Roadmapv2" class="github-link">View on GitHub</a>
    
    <div class="container">
        <h1>Architecture Team Roadmap 2025</h1>
        
        <div>
            <button id="export-html">Export as HTML</button>
            <button id="export-confluence">Export for Confluence</button>
            <button id="export-csv">Export as CSV</button>
        </div>
        
        <h2>Roadmap Timeline</h2>
        <div class="gantt-container">
            <div class="mermaid" id="roadmap-chart"></div>
        </div>
        
        <h2>Project Details</h2>
        <div class="table-container">
            <table id="project-table">
                <tr>
                    <th>Project</th>
                    <th>Architect</th>
                    <th>Type</th>
                    <th>Status</th>
                    <th>Start Date</th>
                    <th>End Date</th>
                    <th>Description</th>
                    <th>Technologies</th>
                </tr>
            </table>
        </div>
    </div>

    <script>
        // Initialize Mermaid
        mermaid.initialize({{ 
            startOnLoad: true,
            securityLevel: 'loose',
            gantt: {{
                barHeight: 20,
                barGap: 4,
                topPadding: 50,
                leftPadding: 150,
                rightPadding: 20,
                fontFamily: 'Arial, sans-serif',
                fontSize: 12
            }}
        }});
        
        // Load roadmap data
        async function loadRoadmap() {{
            try {{
                const response = await fetch('roadmap-data.json');
                if (!response.ok) {{
                    throw new Error('Failed to load roadmap data');
                }}
                
                const data = await response.json();
                
                // Populate the project table
                populateProjectTable(data);
                
                // Render the Mermaid chart
                renderMermaidChart(data);
                
                // Set up export buttons
                document.getElementById('export-html').addEventListener('click', () => {{
                    window.location.href = 'roadmap-simple.html';
                }});
                
                document.getElementById('export-confluence').addEventListener('click', () => {{
                    window.location.href = 'export-confluence.html';
                }});
                
                document.getElementById('export-csv').addEventListener('click', exportToCSV);
                
            }} catch (error) {{
                console.error('Error loading roadmap data:', error);
                document.getElementById('project-table').innerHTML = `<tr><td colspan="8" style="color: red;">Error loading roadmap data: ${{error.message}}</td></tr>`;
            }}
        }}
        
        // Populate project table
        function populateProjectTable(data) {{
            const table = document.getElementById('project-table');
            
            data.forEach(project => {{
                const technologies = project.technologies ? project.technologies.join(', ') : '';
                
                const row = table.insertRow();
                row.insertCell().textContent = project.project_name;
                row.insertCell().textContent = project.architect;
                row.insertCell().textContent = project.type;
                row.insertCell().textContent = project.status;
                row.insertCell().textContent = project.start_date;
                row.insertCell().textContent = project.end_date;
                row.insertCell().textContent = project.description || '';
                row.insertCell().textContent = technologies;
            }});
        }}
        
        // Render Mermaid chart
        function renderMermaidChart(data) {{
            // Group projects by type
            const groupedProjects = {{}};
            data.forEach(project => {{
                if (!groupedProjects[project.type]) {{
                    groupedProjects[project.type] = [];
                }}
                groupedProjects[project.type].push(project);
            }});
            
            // Generate Mermaid code
            let mermaidCode = `gantt
  title Architecture Roadmap Timeline
  dateFormat YYYY-MM-DD
  axisFormat %b %Y
`;
            
            Object.keys(groupedProjects).forEach(type => {{
                mermaidCode += `\\n  section ${{type}}\\n`;
                
                groupedProjects[type].forEach(project => {{
                    const projectStatus = project.status === 'Planned' ? 'planned' : 'active';
                    mermaidCode += `    ${{project.project_name}} (${{project.architect}}) :${{projectStatus}}, ${{project.start_date}}, ${{project.end_date}}\\n`;
                }});
            }});
            
            // Render the chart
            document.getElementById('roadmap-chart').textContent = mermaidCode;
            mermaid.contentLoaded();
        }}
        
        // Export to CSV
        function exportToCSV() {{
            // Get the table
            const table = document.getElementById('project-table');
            
            // Prepare CSV content
            let csv = [];
            const rows = table.querySelectorAll('tr');
            
            rows.forEach(row => {{
                const rowData = [];
                const cells = row.querySelectorAll('th, td');
                cells.forEach(cell => {{
                    rowData.push('"' + cell.textContent.replace(/"/g, '""') + '"');
                }});
                csv.push(rowData.join(','));
            }});
            
            // Create CSV file
            const csvContent = csv.join('\\n');
            const blob = new Blob([csvContent], {{ type: 'text/csv;charset=utf-8;' }});
            const link = document.createElement('a');
            const url = URL.createObjectURL(blob);
            
            link.setAttribute('href', url);
            link.setAttribute('download', 'architecture_roadmap.csv');
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }}
        
        // Load roadmap when the page loads
        document.addEventListener('DOMContentLoaded', loadRoadmap);
    </script>
</body>
</html>"""

def main():
    """Main function to generate all roadmap files"""
    try:
        projects = read_roadmap_data()
        
        # Generate the output files
        simple_html = generate_simple_html(projects)
        confluence_export_html = generate_confluence_export_html(projects)
        index_html = generate_index_html(projects)
        
        # Write the files
        with open('roadmap-simple.html', 'w') as f:
            f.write(simple_html)
        
        with open('export-confluence.html', 'w') as f:
            f.write(confluence_export_html)
        
        with open('index.html', 'w') as f:
            f.write(index_html)
        
        print('Roadmap files generated successfully!')
        return True
    
    except Exception as e:
        print(f'Error generating roadmap files: {e}')
        return False

if __name__ == '__main__':
    main()
