# 📸 How to Add Your Project Images

Follow these steps to add your screenshots to the repository:

## Step 1: Prepare Your Images

You need 5 images:
1. **logo.png** - Your SKINAURA logo (the metallic rose gold logo with face icon)
2. **homepage.png** - Screenshot of your homepage/web interface
3. **upload.png** - Screenshot of the image upload interface
4. **results.png** - Screenshot showing disease prediction results
5. **chatbot.png** - Screenshot of the AI chatbot interaction

## Step 2: Save Images to the Correct Location

Save all images to: `skin_analyzer/images/`

**File names must be exactly:**
- `logo.png`
- `homepage.png`
- `upload.png`
- `results.png`
- `chatbot.png`

## Step 3: Add Images to Git

Open PowerShell in `D:\SkinAura` and run:

```powershell
# Add images
git add skin_analyzer/images/*.png

# Commit
git commit -m "Add project screenshots and images"

# Push to GitHub
git push origin main
```

## Step 4: Verify on GitHub

Visit: https://github.com/bhavika2203/SkinAura

The images should now appear in the README!

## Image Requirements

- **Format**: PNG or JPG
- **Recommended Size**: 
  - Logo: 200x200px to 400x400px
  - Screenshots: 1200x800px or larger
- **File Size**: Keep under 1MB each for faster loading
- **Quality**: Use clear, high-quality images

## Alternative: Using GitHub's Image Hosting

If your images are too large, you can:
1. Upload images to GitHub Issues (create a dummy issue, upload images, get URLs)
2. Use the image URLs in README instead of local paths
3. Or use a service like imgur.com

## Quick Copy-Paste Commands

```powershell
# Navigate to images folder
cd skin_analyzer\images

# Copy your images here, then:
cd ..\..
git add skin_analyzer/images/*.png
git commit -m "Add project screenshots"
git push origin main
```

---

**Note**: Make sure your image files are named exactly as shown above, or the README won't display them correctly!

