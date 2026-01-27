# WTH Logo Display in Home Assistant - Complete Guide

## Current Status

The WTH logo has been properly prepared and included in the integration with the following files:

- `icon.png` (128x128) - Standard resolution
- `icon@2x.png` (256x256) - High resolution (Retina)
- `logo.png` (256x256) - Brand logo
- `icon.svg` - Vector version

## How Home Assistant Displays Integration Logos

### Official Integrations
Official Home Assistant integrations get their logos from the [Home Assistant Brands](https://github.com/home-assistant/brands) repository. These logos appear automatically in:
- Integration setup flow
- Integration list (Settings → Devices & Services)
- Device cards
- Entity cards

### Custom Integrations (Like WTH UMR2)
Custom integrations have limited logo display options. Here's what works:

## ✅ What DOES Work

### 1. MDI Icon in Integration List
The integration will show with the `mdi:radiator` icon in the integration list because we've set:
```json
"icon": "mdi:radiator"
```

### 2. Device Cards
The device information includes links and proper identification with manufacturer info.

### 3. Entity Cards
Individual entities can show custom icons.

## ❌ What DOESN'T Work (For Custom Integrations)

### Integration Logo in Setup Flow
Custom integrations cannot display a custom logo during the setup flow without being in the Brands repository.

## 🔧 Solutions & Workarounds

### Option 1: Add to Home Assistant Brands (Recommended for Public Release)

To get the WTH logo to appear officially:

1. **Fork the Brands Repository**
   ```bash
   git clone https://github.com/home-assistant/brands.git
   ```

2. **Add WTH Logo**
   - Create folder: `brands/custom_integrations/wth_umr2/`
   - Add files:
     - `icon.png` (256x256 or 512x512)
     - `icon@2x.png` (512x512 or 1024x1024)
     - `logo.png` (same sizes)

3. **Create brand.json**
   ```json
   {
     "domain": "wth_umr2",
     "name": "WTH UMR2 Regulator",
     "integrations": ["wth_umr2"]
   }
   ```

4. **Submit Pull Request**
   - Submit PR to Home Assistant Brands repository
   - Once approved, logo will appear for all users automatically

### Option 2: Local Brands Override

Users can manually add the logo to their Home Assistant instance:

1. **Create brands folder** in Home Assistant config:
   ```
   config/custom_components/wth_umr2/brands/
   ```

2. **Copy logo files** to this folder

3. **Restart Home Assistant**

However, this only works for that specific installation.

### Option 3: Custom Frontend Card (Advanced)

Create a custom Lovelace card that displays the WTH logo with your devices.

### Option 4: Use Device Configuration URL

We've added a configuration URL in the device info:
```python
"configuration_url": f"http://{self.coordinator.host}"
```

This provides a direct link to the device's web interface from Home Assistant.

## 📝 What We've Already Done

✅ Created all required icon files in correct sizes:
- `icon.png` (128x128)
- `icon@2x.png` (256x256)  
- `logo.png` (256x256)
- `icon.svg` (vector)

✅ Set MDI fallback icon:
```json
"icon": "mdi:radiator"
```

✅ Created proper device info with manufacturer and model

✅ Added configuration URL for easy device access

## 🎯 For End Users: How to See the WTH Logo

Since this is a custom integration, the full WTH logo won't appear in the integration list automatically. However, you can:

### 1. Manual Logo Installation (Optional)

If you want to see the WTH logo in Home Assistant:

1. Copy the logo files from the integration folder:
   ```
   custom_components/wth_umr2/icon.png
   custom_components/wth_umr2/icon@2x.png
   custom_components/wth_umr2/logo.png
   ```

2. Create directory in your HA config:
   ```
   mkdir -p www/community/wth_umr2/
   ```

3. Copy files there:
   ```bash
   cp custom_components/wth_umr2/*.png www/community/wth_umr2/
   ```

4. Use in custom cards with:
   ```yaml
   type: picture-entity
   entity: sensor.wth_umr2_regulator_main_state
   image: /local/community/wth_umr2/logo.png
   ```

### 2. Create a Custom Dashboard Card

```yaml
type: vertical-stack
cards:
  - type: picture
    image: /local/community/wth_umr2/logo.png
    tap_action:
      action: none
  - type: entities
    title: WTH UMR2 Status
    entities:
      - sensor.wth_umr2_regulator_main_state
      - sensor.wth_umr2_regulator_operating_mode
      - sensor.wth_umr2_regulator_heat_factor
```

### 3. Use the Device Page

The device page will show:
- Manufacturer: WTH
- Model: UMR2
- Direct link to device web interface
- All sensors organized

## 🚀 For Integration Developers

### To Get Logo in Official HA

1. **Submit to Brands Repo**
   - Follow process above
   - PR to https://github.com/home-assistant/brands
   - Wait for approval

2. **Alternative: HACS Integration**
   - Logo can be displayed in HACS
   - Add logo to your GitHub repo
   - HACS will show it in the integration list

## 📊 Logo File Requirements

For best results, logos should be:

- **Format**: PNG with transparency
- **Sizes**: 
  - icon.png: 128x128 or 256x256
  - icon@2x.png: 256x256 or 512x512
  - logo.png: 256x256 or 512x512
- **Color**: Works on both light and dark backgrounds
- **File size**: < 50KB per file

Our WTH logos meet all these requirements:
- ✅ PNG format with transparency
- ✅ Proper sizes (128x128 and 256x256)
- ✅ Red logo works on light backgrounds
- ✅ File sizes: 4-13KB (well under limit)

## 🔮 Future Improvements

Potential enhancements:
- Submit to HA Brands repository
- Create dark mode version of logo (white text)
- Add to HACS default repositories
- Create custom frontend panel with logo

## ⚠️ Important Note

**This is a limitation of Home Assistant, not the integration.**

- Official integrations: Logo appears automatically
- Custom integrations: Logo requires manual setup or Brands submission

The WTH UMR2 integration has all the logo files properly prepared and ready. They just need to be either:
1. Added to Home Assistant Brands (for automatic display), or
2. Manually installed by users (as shown above)

## 📞 Support

For questions about logo display:
- Check Home Assistant Brands: https://github.com/home-assistant/brands
- Integration issues: https://github.com/AbeltjeNL/wth_umr2/issues
