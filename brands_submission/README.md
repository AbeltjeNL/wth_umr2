# WTH UMR2 - Home Assistant Brands Submission

This folder contains all files needed to submit the WTH UMR2 integration to the [Home Assistant Brands](https://github.com/home-assistant/brands) repository.

## Contents

```
wth_umr2/
├── brand.json          # Brand metadata
├── icon.png            # 256x256 icon
├── icon@2x.png         # 512x512 high-res icon
├── logo.png            # 256x256 logo
└── logo@2x.png         # 512x512 high-res logo
```

## Submission Process

### 1. Fork the Brands Repository

Visit: https://github.com/home-assistant/brands

Click "Fork" in the top right

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/brands.git
cd brands
```

### 3. Copy WTH UMR2 Folder

```bash
# Copy the entire wth_umr2 folder to custom_integrations/
cp -r /path/to/wth_umr2/brands_submission/wth_umr2 custom_integrations/
```

Your structure should look like:
```
brands/
└── custom_integrations/
    └── wth_umr2/
        ├── brand.json
        ├── icon.png
        ├── icon@2x.png
        ├── logo.png
        └── logo@2x.png
```

### 4. Commit and Push

```bash
git add custom_integrations/wth_umr2
git commit -m "Add WTH UMR2 Regulator brand"
git push origin main
```

### 5. Create Pull Request

1. Go to your fork on GitHub
2. Click "Pull Request"
3. Title: "Add WTH UMR2 Regulator"
4. Description:
   ```
   Adding brand assets for WTH UMR2 Regulator custom integration.
   
   - Integration: WTH UMR2 Regulator
   - Domain: wth_umr2
   - Type: Heating system regulator
   - Repository: https://github.com/AbeltjeNL/wth_umr2
   
   Logo source: Official WTH brand logo
   ```
5. Submit PR

### 6. Wait for Review

The Home Assistant team will review your submission. They check:
- ✅ Image quality and sizes
- ✅ File formats (PNG)
- ✅ brand.json correctness
- ✅ Logo usage rights

### 7. After Approval

Once merged, the WTH logo will appear automatically for all users!

## Image Specifications

All images meet Home Assistant requirements:

| File | Size | Format | Optimized |
|------|------|--------|-----------|
| icon.png | 256x256 | PNG | ✅ |
| icon@2x.png | 512x512 | PNG | ✅ |
| logo.png | 256x256 | PNG | ✅ |
| logo@2x.png | 512x512 | PNG | ✅ |

## brand.json

```json
{
  "domain": "wth_umr2",
  "name": "WTH UMR2 Regulator",
  "integrations": ["wth_umr2"]
}
```

## Logo Usage

The WTH logo is used with permission for this integration. Ensure you have rights to use the logo before submitting.

## Alternative: Community Submission

If you don't want to submit yourself, you can:
1. Open an issue at: https://github.com/home-assistant/brands/issues
2. Title: "Add WTH UMR2 Regulator brand"
3. Attach this folder or link to the integration repo

## Support

- Integration: https://github.com/AbeltjeNL/wth_umr2
- Brands Repo: https://github.com/home-assistant/brands
- Questions: Open an issue in the WTH UMR2 repo

## Timeline

After PR approval:
- Merge: Within days/weeks
- Availability: Next Home Assistant Brands update
- Auto-display: For all users with WTH UMR2 integration

---

**Ready to submit!** Follow the steps above to get the WTH logo showing automatically in Home Assistant.
