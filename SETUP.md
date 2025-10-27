# Cultural Misrepresentations - Setup Guide

## 📁 Project Structure

```
cultural-misrepresentations/
├── index.html              # Main landing page
├── annotations.html        # Interactive annotation viewer
├── data/                   # Original JSONL annotation files
├── annotations_js/         # Converted JavaScript files for web viewing
├── convert_annotations.py  # Script to convert JSONL to JS
├── README.md              # Project overview
└── SETUP.md              # This file
```

## 🚀 Quick Start

### Option 1: View Locally (Recommended for Development)

1. **Start a local server**:
   ```bash
   # Using Python 3
   python3 -m http.server 9000
   
   # Or using Node.js (if installed)
   npx http-server -p 9000
   ```

2. **Open in browser**:
   ```
   http://localhost:9000
   ```

### Option 2: Deploy to GitHub Pages

1. **Initialize Git repository** (if not already done):
   ```bash
   cd cultural-misrepresentations
   git init
   ```

2. **Add and commit files**:
   ```bash
   git add .
   git commit -m "Initial commit: Cultural misrepresentations viewer"
   ```

3. **Create GitHub repository**:
   - Go to https://github.com/new
   - Create a repository named `cultural-misrepresentations.github.io`
   - **Do not** initialize with README

4. **Push to GitHub**:
   ```bash
   git branch -M main
   git remote add origin https://github.com/[USERNAME]/cultural-misrepresentations.github.io.git
   git push -u origin main
   ```

5. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Source: Deploy from branch `main`
   - Save

6. **Visit your site**:
   ```
   https://[USERNAME].github.io
   ```

## 📊 Adding/Updating Annotation Data

### From JSONL Files

If you have new JSONL annotation files:

1. **Copy files to data folder**:
   ```bash
   cp /path/to/new/annotations/*.jsonl data/
   ```

2. **Run conversion script**:
   ```bash
   python3 convert_annotations.py
   ```

3. **Update annotations.html**:
   Add the new JavaScript file to the `<script>` tags:
   ```html
   <script src="annotations_js/YourNewLocation.js"></script>
   ```

4. **Add button** in `annotations.html`:
   ```html
   <button class="location-btn" data-file="YourNewLocation.jsonl">
       Your Location Name
   </button>
   ```

5. **Update data mapping**:
   ```javascript
   const annotationData = {
       // ... existing mappings
       'YourNewLocation.jsonl': YourNewLocation
   };
   ```

## 🎨 Customization

### Change Colors

Edit the CSS in `index.html` and `annotations.html`:

```css
/* Main gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Category colors */
.category-cultural { background: #e91e63; }
.category-linguistic { background: #9c27b0; }
.category-logical { background: #ff9800; }
```

### Update Content

- **Landing page**: Edit `index.html` sections
- **Contact info**: Update the Contact section in `index.html`
- **Metadata**: Modify `README.md`

## 🔧 Technical Details

### Annotation Data Structure

Each annotation file contains:
- `output`: The generated story text
- `annotations`: Array of identified issues
  - `text`: Highlighted text
  - `category`: Type of misrepresentation
  - `comment`: Explanation
  - `start`: Character position
- `participant`: Metadata about the story
- `sliders`: Rating scales
- `textFields`: Comments

### Browser Compatibility

- Modern browsers (Chrome, Firefox, Safari, Edge)
- JavaScript ES6+ required
- No build process needed

## 📝 Notes

- The `data/` folder contains original JSONL files (not served to web)
- The `annotations_js/` folder contains web-ready JavaScript files
- All annotation viewing happens client-side (no backend needed)
- Files are included as `<script>` tags for simplicity

## 🐛 Troubleshooting

### Annotations not loading?

1. Check browser console for errors (F12)
2. Verify JavaScript files are in `annotations_js/` folder
3. Make sure script tags point to correct files
4. Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)

### GitHub Pages not updating?

1. Clear browser cache
2. Wait 5-10 minutes for GitHub to rebuild
3. Check repository Settings → Pages for errors
4. Try accessing with `?v=2` parameter to bypass cache

### Local server not working?

1. Make sure you're in the correct directory
2. Try a different port (8080, 8000, etc.)
3. Check if another process is using the port

## 📧 Support

For questions or issues, please open an issue on the GitHub repository.

