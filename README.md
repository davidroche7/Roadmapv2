# Architecture-Roadmap
Road map repository for Engineering Architecture team.

## Purpose
This repository contains automation tools for the Architecture Team to maintain and publish:
 - The team roadmap (shown below)
 - A technology radar
 - An asset registry

## 🛤️ Architecture Team Roadmap 2025

![Roadmap Timeline](https://mermaid.ink/img/eyJjb2RlIjoiZ2FudHRcbiAgdGl0bGUgQXJjaGl0ZWN0dXJlIFJvYWRtYXAgVGltZWxpbmVcbiAgZGF0ZUZvcm1hdCBZWVlZLU1NLUREXG4gIGF4aXNGb3JtYXQgJWIgJVlcblxuICBzZWN0aW9uIEJ1c2luZXNzIENhc2VcbiAgICBBdXRvLXNjYWxpbmcgZm9yIEdhbWUgUGxhdGZvcm1zIChLZWl0aCkgOmFjdGl2ZSwgMjAyNS0wMy0wMSwgMjAyNS0wNS0zMFxuICBcbiAgc2VjdGlvbiBDbGllbnQgRGVsaXZlcnlcbiAgICBQR0NCIFBvcnRhbCAoVG9ieSkgOmFjdGl2ZSwgMjAyNS0wMy0wMSwgMjAyNS0wNi0zMFxuICAgIFZlaWtrYXVzIE9HUyBJbnRlZ3JhdGlvbiAoS2VpdGgpIDphY3RpdmUsIDIwMjUtMDMtMDEsIDIwMjUtMDYtMzBcbiAgXG4gIHNlY3Rpb24gQ2xpZW50IFJGUFxuICAgIEJDTEMgU29sdXRpb24gRGVzaWduIChVbmFzc2lnbmVkKSA6YWN0aXZlLCAyMDI1LTAzLTAxLCAyMDI1LTA2LTAxXG4gICAgVmVpa2thdXMgUEFNIChUb2J5LCBBY2hpbGxlYXMsIEVyaWspIDphY3RpdmUsIDIwMjUtMDMtMDEsIDIwMjUtMDUtMDFcbiAgXG4gIHNlY3Rpb24gTGVhbiBXb3Jrc2hvcCBPdXRwdXRcbiAgICBTZXBhcmF0aW9uIG9mIEVudmlyb25tZW50cyAoTWFyaykgOmFjdGl2ZSwgMjAyNS0wMy0wMSwgMjAyNS0wNy0wMVxuICAgIENvbnNvbGlkYXRlZCBHYW1lIFN0YXR1cyBEYXNoYm9hcmQgKFVuYXNzaWduZWQpIDpwbGFubmVkLCAyMDI1LTA0LTAxLCAyMDI1LTA3LTAxXG4gICAgQ29tcGxpYW5jZSBDaGVja2luZyAoVW5hc3NpZ25lZCkgOnBsYW5uZWQsIDIwMjUtMDQtMDEsIDIwMjUtMDctMDFcbiAgXG4gIHNlY3Rpb24gVGVjaG5vbG9neVxuICAgIEFQSSBHYXRld2F5IEltcGxlbWVudGF0aW9uIChBbGJpbiwgTWFyaykgOmFjdGl2ZSwgMjAyNS0wMy0wMSwgMjAyNS0wNC0xNVxuICBcbiAgc2VjdGlvbiBQcm9vZiBvZiBDb25jZXB0XG4gICAgQXV0aDAgU0FQSSBQb0MgKE1hcmspIDphY3RpdmUsIDIwMjUtMDMtMDEsIDIwMjUtMDQtMDFcbiAgXG4gIHNlY3Rpb24gUHJvZHVjdCBEZXZlbG9wbWVudFxuICAgIFByb2plY3QgTm92YSAoQWNoaWxsZWFzLCBFcmlrLCBUb2J5KSA6YWN0aXZlLCAyMDI1LTAzLTAxLCAyMDI1LTA5LTAxXG4gIFxuICBzZWN0aW9uIFByb2R1Y3RcbiAgICBJdGFsaWFuIENoZWNrdW0gUHJvamVjdCAoTWFyaykgOmFjdGl2ZSwgMjAyNS0wMy0xNSwgMjAyNS0wNi0xNVxuICAgIEZyZWUycGxheSAoU2FtKSA6YWN0aXZlLCAyMDI1LTAzLTE1LCAyMDI1LTA5LTE1XG4gICAgRGF0YUh1YiBQaGFzZSAzIChBbGJpbikgOmFjdGl2ZSwgMjAyNS0wMy0wMSwgMjAyNS0wNS0wMVxuICAgIEdDTSBOZXcgUmVsaWMgRGV2ZWxvcG1lbnQgKFNhbSkgOmFjdGl2ZSwgMjAyNS0wMy0xNSwgMjAyNS0wNy0xNVxuICAgIFJHUyBMaWdodCBSb2xsb3V0IChBbGJpbikgOnBsYW5uZWQsIDIwMjUtMDMtMTUsIDIwMjUtMDYtMzBcbiAgICBHQ00gSW50ZWdyYXRpb24gSW1wcm92ZW1lbnRzIChTYW0pIDphY3RpdmUsIDIwMjUtMDMtMTUsIDIwMjUtMDYtMTVcblxuICBzZWN0aW9uIEludGVybmFsIEVuZ2luZWVyaW5nXG4gICAgQUkgQ2hhdGJvdCAoQWxiaW4pIDphY3RpdmUsIDIwMjUtMDMtMDEsIDIwMjUtMDctMDFcbiAgIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOnRydWV9?bgColor=white)

> **View full roadmap**: [Architecture Roadmap](https://davidroche7.github.io/Roadmapv2/)
>
> **Download formats**: [HTML](https://davidroche7.github.io/Roadmapv2/roadmap-simple.html) | [Confluence Markup](https://davidroche7.github.io/Roadmapv2/export-confluence.html)

## Current Implementation

The current implementation provides a client-side rendered roadmap based on JSON data:

1. **Core Data Source**: `roadmap-data.json` contains all project information
2. **HTML Views**:
   - `index.html` - Main page that embeds the roadmap
   - `roadmap-simple.html` - Standalone roadmap with Gantt chart and table
   - `export-confluence.html` - Confluence markup exporter

### How It Works
1. Edit the `roadmap-data.json` file to update the roadmap data
2. The HTML files read this JSON data and render it dynamically in the browser
3. No build process or server-side rendering required

### Current Features
- Gantt chart showing project timelines
- Detailed project table with all metadata
- Export to CSV functionality
- Confluence markup export
- Responsive design with improved formatting

## Future Plans

This is a simplified version of a more comprehensive system planned for the future. The complete system will include:

```mermaid
graph TD
    A[Monday.com] -->|Daily sync| B[GitHub Actions]
    B -->|Updates| C[Roadmap]
    B -->|Updates| D[Tech Radar]
    B -->|Updates| E[Asset Registry]
    C -->|Published to| F[Confluence]
    D -->|Published to| F
    E -->|Published to| F
    G[Confluence Pages] -->|Asset info| E
```

## Planned Components

### 1. Roadmap
The roadmap (currently implemented) displays architecture team activities organized by team member. It includes:
 - Project/product name
 - Status (done, active, planned)
 - Timeline (start and end dates)

### 2. Technology Radar
We plan to use the existing company Tech Radar and automatically update it with technologies from our projects. The automation will:
 - Extract technologies from Monday.com projects and confluence
 - Format them for the Tech Radar
 - Push updates to the Tech Radar repository

### 3. Asset Registry
The planned asset registry will provide a comprehensive inventory of all technology assets with:
 - Technology name and type
 - Maturity level within the organisation
 - Projects using the technology
 - Links to documentation in Confluence

## Prerequisites for Future Implementation

### Monday.com Setup
A Monday.com board with the following columns:
 - Technologies (tags/multiple values)
 - Status (status column)
 - Owner (person column)
 - Start Date (date column)
 - End Date (date column)
 - Monday.com API token with read access to the board

### Confluence Setup
A Confluence space where documentation will be published:
 - Architecture Team Roadmap
 - Technology Radar
 - Asset Registry
 - Confluence API credentials with write access to these pages

### GitHub Setup
 - Repository secrets configured with API credentials

## Planned Configuration
 - All configuration settings will be stored in `config.json`:
 - Monday.com board and column IDs
 - Confluence space and page IDs
 - Tech Radar quadrant and ring definitions

## How It Will Work
 - GitHub Actions workflow will run daily to fetch data from Monday.com
 - The data will be processed to update the roadmap
 - Technologies mentioned in projects will be extracted for the Tech Radar
 - The Asset Registry will be compiled from Tech Radar data and Confluence
 - All visualizations will be published to Confluence for wider access

## Adding New Projects (Future)
To add a new project to the system:
 - Add a new item to the Monday.com board
 - Fill in all required columns (technologies, status, owner, dates)
 - The automation will include the new project in the next update

## Maturity Levels for Technology (TBC)
Technology maturity will be determined automatically based on:
 - Adoption across projects
 - Status of projects using the technology

The levels are:
 - Adopted: Technology is widely used and proven
 - Trial: Technology is being used in limited projects
 - Assessing: Technology is being evaluated
 - Unknown: Maturity level not determined
