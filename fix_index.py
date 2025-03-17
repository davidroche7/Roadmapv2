#!/usr/bin/env python3

# Read the existing files
with open('roadmap-simple.html', 'r') as file:
    simple_content = file.read()

# Create a new index.html that embeds the roadmap-simple.html file in an iframe
index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architecture Team Roadmap</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 0;
            padding: 20px; 
            line-height: 1.6;
            color: #333;
        }
        .container { 
            max-width: 1200px; 
            margin: 0 auto;
            padding: 20px;
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
        .github-link {
            position: absolute;
            top: 10px;
            right: 10px;
        }
        iframe {
            width: 100%;
            height: 800px;
            border: none;
        }
    </style>
</head>
<body>
    <a href="https://github.com/davidroche7/Roadmapv2" class="github-link">View on GitHub</a>
    
    <div class="container">
        <h1>Architecture Team Roadmap 2025</h1>
        
        <div>
            <button onclick="window.location.href='roadmap-simple.html'">Export as HTML</button>
            <button onclick="window.location.href='export-confluence.html'">Export for Confluence</button>
        </div>
        
        <iframe src="roadmap-simple.html"></iframe>
    </div>
</body>
</html>"""

# Write the new index.html
with open('index.html', 'w') as file:
    file.write(index_content)

print("Successfully created index.html with iframe!")
