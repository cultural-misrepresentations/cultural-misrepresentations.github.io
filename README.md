# Cultural Representation of AI-Generated Stories

A research project examining cultural misrepresentation and bias in Large Language Models.

## Project Structure

```
.
├── assets/
│   ├── css/              # Stylesheets (embedded in HTML currently)
│   ├── js/
│   │   └── annotations_js/   # Annotation data as JavaScript files
│   └── images/           # Images and generated maps
├── scripts/              # Python scripts for map generation
│   ├── create_simple_map.py
│   ├── generate_india_map.py
│   └── india.geojson
├── index.html            # Main landing page
├── annotations.html      # Interactive annotation viewer
├── .nojekyll            # Tells GitHub Pages to serve static HTML
└── README.md            # This file
```

## Live Site

Visit the project at: [https://cultural-misrepresentations.github.io/](https://cultural-misrepresentations.github.io/)

## Features

- Interactive map of India with study locations
- Annotation viewer with highlighted text spans
- Markdown rendering support
- Clean, academic design
- Fully static site (no backend required)

## Local Development

To test locally:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`

## Deployment

This site is automatically deployed via GitHub Pages. Any push to the `main` branch will update the live site within 1-2 minutes.
