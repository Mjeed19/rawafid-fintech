# Rawafid Fintech — روافد فنتك

## Project Overview
A static Arabic-language landing page for the Rawafid Fintech Exhibition 2026 — a sponsorship/event showcase targeting fintech companies in Saudi Arabia (Imam University, Riyadh, May 5-6 2026).

## Architecture
- **Type:** Pure static HTML (single file)
- **Language:** Arabic (RTL layout)
- **Fonts:** Cairo & Tajawal (Google Fonts)
- **No build system required**

## Running the Project
The project is served via Python's built-in HTTP server:
```
python3 -m http.server 5000
```

## Deployment
- **Target:** Static
- **Public directory:** `.` (project root)
- The single `index.html` file contains all HTML, CSS, and JavaScript inline.

## Key Files
- `index.html` — Entire application (883 lines, all-in-one)
