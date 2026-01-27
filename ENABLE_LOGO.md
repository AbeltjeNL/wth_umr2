# Enable WTH Logo Display - Step by Step

## Quick Setup (5 minutes)

This guide shows you how to make the WTH logo appear in your Home Assistant interface.

## Why Doesn't the Logo Show Automatically?

Home Assistant only shows logos automatically for integrations in the official [Brands repository](https://github.com/home-assistant/brands). Custom integrations like WTH UMR2 need manual setup.

## Method 1: Dashboard Logo (Easiest)

### Step 1: Copy Logo to www Folder

1. **Via File Editor or SSH:**
   ```bash
   # Create directory
   mkdir -p /config/www/wth_umr2
   
   # Copy logo files
   cp /config/custom_components/wth_umr2/logo.png /config/www/wth_umr2/
   cp /config/custom_components/wth_umr2/icon.png /config/www/wth_umr2/
   ```

2. **Via Samba/Network Share:**
   - Navigate to `config/www/`
   - Create folder `wth_umr2`
   - Copy `logo.png` and `icon.png` from `custom_components/wth_umr2/` to `www/wth_umr2/`

### Step 2: Add Logo to Dashboard

Create a new card in your dashboard:

```yaml
type: vertical-stack
cards:
  - type: picture
    image: /local/wth_umr2/logo.png
    tap_action:
      action: navigate
      navigation_path: /config/devices/device/YOUR_DEVICE_ID
  - type: entities
    title: WTH UMR2 Regulator
    entities:
      - sensor.wth_umr2_regulator_main_state
      - sensor.wth_umr2_regulator_operating_mode
      - sensor.wth_umr2_regulator_heat_factor
      - sensor.wth_umr2_regulator_pump_speed
```

**Result:** You'll see the WTH logo above your sensor status!

## Method 2: Submit to Home Assistant Brands (For Everyone)

If you want the logo to appear automatically for all users:

### Step 1: Fork Brands Repository

```bash
# Fork https://github.com/home-assistant/brands on GitHub
git clone https://github.com/YOUR_USERNAME/brands.git
cd brands
```

### Step 2: Create Integration Folder

```bash
mkdir -p custom_integrations/wth_umr2
cd custom_integrations/wth_umr2
```

### Step 3: Copy Logo Files

Copy these files from the WTH UMR2 integration:
- `icon.png` (rename to `icon.png` - 256x256)
- `icon@2x.png` (keep name - 512x512 preferred, or use 256x256)
- `logo.png` (keep name - 256x256)

### Step 4: Create brand.json

```json
{
  "domain": "wth_umr2",
  "name": "WTH UMR2 Regulator",
  "integrations": ["wth_umr2"]
}
```

### Step 5: Submit Pull Request

1. Commit your changes
2. Push to your fork
3. Create PR to home-assistant/brands
4. Wait for review and approval

**Once approved:** Logo will appear automatically for everyone!

## Method 3: Custom Lovelace Card with Logo

Create a custom card template:

```yaml
type: custom:button-card
entity: sensor.wth_umr2_regulator_main_state
name: WTH UMR2
icon: mdi:radiator
show_state: true
show_name: true
styles:
  card:
    - background-image: url('/local/wth_umr2/logo.png')
    - background-size: contain
    - background-repeat: no-repeat
    - background-position: top center
    - padding-top: 80px
  name:
    - padding-top: 10px
```

## Method 4: Picture Elements Card

Create an advanced dashboard with the logo:

```yaml
type: picture-elements
image: /local/wth_umr2/logo.png
elements:
  - type: state-label
    entity: sensor.wth_umr2_regulator_main_state
    style:
      top: 80%
      left: 50%
      color: white
      font-size: 20px
  - type: state-label
    entity: sensor.wth_umr2_regulator_heat_factor
    prefix: 'Heat: '
    suffix: '%'
    style:
      top: 90%
      left: 50%
      color: white
```

## Verification

After setup, you should see:

✅ WTH logo in your dashboard cards (Method 1, 3, 4)
✅ Device info shows "Manufacturer: WTH, Model: UMR2"
✅ Configuration URL links to device web interface
✅ All 60+ sensors available

## Current Icon in Integration List

Until the logo is added to Home Assistant Brands, the integration list will show:
- Icon: 🔥 (mdi:radiator)
- Name: WTH UMR2 Regulator

This is normal for custom integrations.

## Troubleshooting

### Logo Not Showing in Dashboard

1. **Check file path:**
   ```
   /config/www/wth_umr2/logo.png
   ```

2. **Verify file is accessible:**
   - Navigate to: `http://YOUR_HA_IP:8123/local/wth_umr2/logo.png`
   - You should see the WTH logo

3. **Clear browser cache:**
   - Press Ctrl+Shift+R (Cmd+Shift+R on Mac)
   - Or clear cache in browser settings

4. **Restart Home Assistant:**
   - Settings → System → Restart

### Dashboard Card Not Updating

1. Force refresh the dashboard
2. Check YAML syntax
3. Verify entity IDs are correct

## File Locations Reference

```
config/
├── custom_components/
│   └── wth_umr2/
│       ├── icon.png          # 128x128 icon
│       ├── icon@2x.png       # 256x256 high-res icon
│       └── logo.png          # 256x256 logo
└── www/                      # Public web folder
    └── wth_umr2/            # Create this
        ├── logo.png         # Copy here
        └── icon.png         # Copy here
```

## Summary

- ✅ Logo files are included in the integration
- ✅ Logo files are properly sized and optimized
- ⚠️ Manual setup needed for display (Home Assistant limitation)
- 🎯 Use Method 1 for quick dashboard logo
- 🌟 Use Method 2 to help everyone (submit to Brands)

## Need Help?

- Integration issues: https://github.com/AbeltjeNL/wth_umr2/issues
- Home Assistant Brands: https://github.com/home-assistant/brands
- Home Assistant Community: https://community.home-assistant.io/
