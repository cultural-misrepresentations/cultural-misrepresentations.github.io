# GitHub Pages Setup Instructions

## Folder Structure for GitHub Pages

Your current folder is ready for GitHub Pages! Here's what you have:

```
cultural-misrepresentations/
├── index.html                 # Main landing page
├── annotations.html           # Annotations viewer page
├── culture_india-white.png    # Logo image
├── annotations_js/            # JavaScript data files
│   ├── index.js
│   ├── Bengaluru_Karnataka.js
│   ├── Guwahati_Assam.js
│   ├── Imphal-East_Manipur.js
│   ├── Kasaragod_Kerala.js
│   ├── Kolkata_West Bengal.js
│   └── Nilgiris_Tamil Nadu.js
├── data/                      # Original JSONL files
│   ├── Bengaluru_Karnataka.jsonl
│   ├── Guwahati_Assam.jsonl
│   ├── Imphal-East_Manipur.jsonl
│   ├── Kasaragod_Kerala.jsonl
│   ├── Kolkata_West Bengal.jsonl
│   └── Nilgiris_Tamil Nadu.jsonl
├── convert_annotations.py     # Conversion script
├── _config.yml                # Jekyll config
├── .gitignore                 # Git ignore file
├── README.md                  # Project README
└── SETUP.md                   # Setup documentation
```

## Steps to Deploy on GitHub Pages

### 1. Create a GitHub Repository

```bash
# Navigate to your project folder
cd /Users/kirtibhagat/Desktop/UserStadyInterface/all_branches/cultural-misrepresentations

# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Cultural Representations project"
```

### 2. Create GitHub Repository Online

1. Go to https://github.com/new
2. Repository name: `cultural-misrepresentations` (or your preferred name)
3. Description: "Cultural Representation of AI-generated Stories"
4. Make it **Public** (required for free GitHub Pages)
5. DO NOT initialize with README (you already have one)
6. Click "Create repository"

### 3. Push to GitHub

```bash
# Add remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/cultural-misrepresentations.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### 4. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Scroll down to **Pages** (in left sidebar)
4. Under "Source":
   - Branch: Select **main**
   - Folder: Select **/ (root)**
5. Click **Save**

### 5. Access Your Site

After 1-2 minutes, your site will be live at:
```
https://YOUR_USERNAME.github.io/cultural-misrepresentations/
```

## Important Notes

### Files to Keep
- ✅ `index.html` - Landing page
- ✅ `annotations.html` - Annotations viewer
- ✅ `culture_india-white.png` - Logo
- ✅ `annotations_js/` - All JS data files (required for annotations to work)
- ✅ `_config.yml` - Jekyll configuration
- ✅ `.gitignore` - Git ignore rules
- ✅ `README.md` - Project documentation

### Files Optional for GitHub Pages
- ⚠️ `data/` - Original JSONL files (optional, can keep for backup)
- ⚠️ `convert_annotations.py` - Python script (not needed on live site, but good to keep)
- ⚠️ `SETUP.md` - Setup guide (optional)

### What's Currently Hidden
The main content on `index.html` is commented out, showing only:
- Navigation (Home | Annotations)
- Header with logo and title
- Subtitle

To restore content later, simply uncomment the HTML in `index.html`.

## Custom Domain (Optional)

If you want to use a custom domain:

1. Add a file named `CNAME` in the root directory
2. Inside `CNAME`, put your domain (e.g., `cultural-ai.example.com`)
3. Configure your domain's DNS settings to point to GitHub Pages
4. Follow GitHub's custom domain guide: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

## Troubleshooting

### Site not loading?
- Wait 1-2 minutes after enabling GitHub Pages
- Check that repository is **Public**
- Verify GitHub Pages is enabled in Settings

### Annotations not working?
- Make sure all files in `annotations_js/` are committed and pushed
- Check browser console for errors (F12)
- Verify file paths are correct

### Images not showing?
- Ensure `culture_india-white.png` is in the root directory
- Check that image path in HTML is correct (`culture_india-white.png`)

## Updating Your Site

To make changes:

```bash
# Make your changes to HTML/CSS/JS files

# Add changes
git add .

# Commit
git commit -m "Update: description of changes"

# Push
git push origin main
```

Changes will appear on your site within 1-2 minutes.

## Questions?

For more information about GitHub Pages:
- Documentation: https://docs.github.com/en/pages
- Jekyll themes: https://pages.github.com/themes/

