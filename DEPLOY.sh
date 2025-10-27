#!/bin/bash

# Deployment script for GitHub Pages
# Run this script from the cultural-misrepresentations directory

echo "🚀 Starting GitHub Pages deployment..."

# Step 1: Initialize git (if not already done)
if [ ! -d .git ]; then
    echo "📦 Initializing git repository..."
    git init
else
    echo "✅ Git repository already initialized"
fi

# Step 2: Add all files
echo "📝 Adding files to git..."
git add .

# Step 3: Commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Cultural Representation of AI-generated Stories"

# Step 4: Set main branch
echo "🌿 Setting main branch..."
git branch -M main

# Step 5: Add remote (you'll need to create the repository first)
echo ""
echo "⚠️  NEXT STEPS:"
echo "1. Go to https://github.com/cultural-misrepresentations"
echo "2. Click the '+' icon in the top right"
echo "3. Select 'New repository'"
echo "4. Repository name: cultural-misrepresentations (or your preferred name)"
echo "5. Description: Cultural Representation of AI-generated Stories"
echo "6. Make it PUBLIC (required for free GitHub Pages)"
echo "7. DO NOT initialize with README, .gitignore, or license"
echo "8. Click 'Create repository'"
echo ""
echo "After creating the repository, run:"
echo "git remote add origin https://github.com/cultural-misrepresentations/REPOSITORY_NAME.git"
echo "git push -u origin main"
echo ""
echo "Then enable GitHub Pages:"
echo "1. Go to repository Settings > Pages"
echo "2. Source: main branch, / (root) folder"
echo "3. Click Save"
echo ""
echo "Your site will be live at:"
echo "https://cultural-misrepresentations.github.io/REPOSITORY_NAME/"

