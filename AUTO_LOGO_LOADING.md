# Automatic Logo Loading - Technical Documentation

## Overview

The WTH UMR2 integration now automatically loads logos from local storage and makes them available throughout Home Assistant.

## Implementation

### 1. HTTP API Endpoint

The integration creates a public API endpoint to serve logo files:

```
/api/wth_umr2/logo/{filename}
```

**Available files:**
- `/api/wth_umr2/logo/icon.png` (128x128)
- `/api/wth_umr2/logo/icon@2x.png` (256x256)
- `/api/wth_umr2/logo/logo.png` (256x256)
- `/api/wth_umr2/logo/icon.svg` (vector)

**Features:**
- ✅ No authentication required (public access)
- ✅ Cached for 24 hours
- ✅ CORS enabled
- ✅ Security: Only serves whitelisted files

### 2. Automatic WWW Directory Setup

On integration startup, logos are automatically copied to:

```
config/www/wth_umr2/
├── icon.png
├── icon@2x.png
├── logo.png
└── icon.svg
```

**Access via:**
- `/local/wth_umr2/logo.png`
- `/local/wth_umr2/icon.png`
- `/local/wth_umr2/icon@2x.png`
- `/local/wth_umr2/icon.svg`

### 3. Config Flow Integration

The setup wizard includes logo display in the description using markdown:

```markdown
![WTH Logo]({logo_url})

Enter the IP address of your WTH UMR2 regulator.
```

The `{logo_url}` placeholder is replaced with `/api/wth_umr2/logo/logo.png`

## How to Use

### In Dashboard Cards

```yaml
type: picture
image: /local/wth_umr2/logo.png
tap_action:
  action: none
```

Or via API:

```yaml
type: picture
image: /api/wth_umr2/logo/logo.png
tap_action:
  action: none
```

### In Custom Cards

```yaml
type: custom:button-card
entity: sensor.wth_umr2_regulator_main_state
name: WTH UMR2
icon: mdi:radiator
styles:
  card:
    - background-image: url('/local/wth_umr2/logo.png')
    - background-size: contain
    - background-position: center
```

### In Templates

```yaml
type: markdown
content: |
  ![WTH Logo](/local/wth_umr2/logo.png)
  
  ## WTH UMR2 Status
  - State: {{ states('sensor.wth_umr2_regulator_main_state') }}
  - Mode: {{ states('sensor.wth_umr2_regulator_operating_mode') }}
```

## Verification

### 1. Check API Endpoint

Open in browser:
```
http://YOUR_HA_IP:8123/api/wth_umr2/logo/logo.png
```

You should see the WTH logo.

### 2. Check WWW Directory

Verify files exist:
```bash
ls -la config/www/wth_umr2/
```

Should show:
- icon.png
- icon@2x.png  
- logo.png
- icon.svg

### 3. Check Logs

Look for this message in Home Assistant logs:
```
INFO (MainThread) [custom_components.wth_umr2] WTH UMR2 logos installed to /local/wth_umr2/
```

## Integration List Icon

The integration list shows the MDI icon `mdi:radiator` because custom integrations cannot override this without being in the Home Assistant Brands repository.

**What shows:**
- Integration list: 🔥 (mdi:radiator)
- Setup wizard: WTH logo (via markdown)
- Dashboard cards: WTH logo (when configured)
- Device page: Standard device info

**To get custom icon in integration list:**
Submit to Home Assistant Brands repository (see brands_submission folder).

## Troubleshooting

### Logo Not Loading

1. **Check integration loaded:**
   ```
   Settings → System → Logs
   Search: "wth_umr2"
   ```

2. **Verify API endpoint:**
   ```
   http://YOUR_HA_IP:8123/api/wth_umr2/logo/logo.png
   ```

3. **Check www directory:**
   ```bash
   ls config/www/wth_umr2/
   ```

4. **Restart Home Assistant:**
   ```
   Settings → System → Restart
   ```

### WWW Directory Not Created

If logos aren't copied to www folder:

1. Check permissions on www directory
2. Manually create: `mkdir -p config/www/wth_umr2`
3. Copy files from: `custom_components/wth_umr2/*.png`
4. Restart Home Assistant

### Logo Not Showing in Setup Wizard

The setup wizard logo display depends on Home Assistant's markdown rendering support. This may vary by version.

**Workaround:** Logo is still available via API and www directory for dashboard use.

## Code Reference

### Logo Serving View

```python
class WTHLogoView(HomeAssistantView):
    """View to serve WTH logo files."""
    
    requires_auth = False
    url = "/api/wth_umr2/logo/{filename}"
    name = "api:wth_umr2:logo"
```

### WWW Setup

```python
def _setup_www_directory(hass: HomeAssistant) -> None:
    """Set up www directory with logos."""
    www_dir = os.path.join(hass.config.path("www"), "wth_umr2")
    os.makedirs(www_dir, exist_ok=True)
    # Copy logo files...
```

## Security

- ✅ Only whitelisted files served
- ✅ No path traversal possible
- ✅ No authentication required (logos are public)
- ✅ CORS enabled for cross-origin requests
- ✅ Files cached to reduce server load

## Performance

- Logo files cached for 24 hours
- Small file sizes (4-13KB)
- No external requests needed
- Served from local storage

## Browser Compatibility

- ✅ All modern browsers
- ✅ Mobile apps
- ✅ Home Assistant iOS/Android apps
- ✅ Desktop browsers

## Future Enhancements

Potential improvements:
- [ ] Dark mode logo variant
- [ ] Animated logo support
- [ ] Logo customization options
- [ ] Integration list icon override (requires HA core changes)

## Summary

✅ **Logos are automatically loaded from integration**
✅ **Available via HTTP API endpoint**
✅ **Automatically copied to www directory**
✅ **Ready to use in dashboard cards**
✅ **No manual setup required**

Just install the integration and the logos are ready to use!
