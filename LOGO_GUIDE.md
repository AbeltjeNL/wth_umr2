# Logo Integration Guide

## Where the WTH Logo Appears in Home Assistant

The WTH logo has been integrated into the Home Assistant integration and will appear in several key locations:

### 1. Integration Discovery & Setup

When adding the integration:

**Location**: Settings → Devices & Services → Add Integration → Search "WTH"

**What you'll see**:
```
┌─────────────────────────────────────────┐
│                                         │
│          [WTH Logo]                     │
│                                         │
│      WTH UMR2 Regulator                 │
│                                         │
│   Connect to WTH UMR2 Regulator        │
│                                         │
│   IP Address: [192.168.178.69    ]     │
│                                         │
│              [Submit]                   │
│                                         │
└─────────────────────────────────────────┘
```

### 2. Integration Card

**Location**: Settings → Devices & Services → WTH UMR2 Regulator

**What you'll see**:
```
┌─────────────────────────────────────────┐
│  [WTH Logo]  WTH UMR2 Regulator        │
│                                         │
│  1 device                              │
│  60+ entities                          │
│                                         │
│  Configured IP: 192.168.178.69         │
│                                         │
│  [Options] [⋮]                         │
└─────────────────────────────────────────┘
```

### 3. Device Information Page

**Location**: Settings → Devices & Services → WTH UMR2 Regulator → Device

**What you'll see**:
```
┌─────────────────────────────────────────┐
│                                         │
│          [WTH Logo]                     │
│                                         │
│      WTH UMR2 Regulator                │
│                                         │
│  Manufacturer: WTH                      │
│  Model: UMR2                            │
│  Firmware: 00.01                        │
│  Hardware: 00.01                        │
│                                         │
│  [Open Configuration] ↗                 │
│  http://192.168.178.69                  │
│                                         │
│  ───── Entities ─────                   │
│  ☑ Main State                           │
│  ☑ Operating Mode                       │
│  ☑ Heat Factor                          │
│  ... (60+ more)                         │
└─────────────────────────────────────────┘
```

### 4. Mobile App

The logo also appears in the Home Assistant mobile app:
- Integration list
- Device cards
- Setup flow
- Settings pages

## Logo Files

Two versions are included:

- **logo.png** (15KB)
  - Primary logo file
  - Used in main UI elements
  - Red WTH branding

- **icon.png** (15KB)
  - Icon version of logo
  - Used in smaller UI elements
  - Same as logo.png

## Logo Specifications

- **Format**: PNG
- **Size**: 15KB
- **Dimensions**: Optimized for Home Assistant display
- **Colors**: Red (#FF0000) WTH branding on white background
- **Transparency**: White background

## Language-Specific Display

### English Interface
```
┌─────────────────────────────────────────┐
│          [WTH Logo]                     │
│                                         │
│   Connect to WTH UMR2 Regulator        │
│   Enter the IP address of your WTH     │
│   UMR2 regulator.                       │
│                                         │
│   IP Address: [              ]          │
└─────────────────────────────────────────┘
```

### Dutch Interface (Nederlands)
```
┌─────────────────────────────────────────┐
│          [WTH Logo]                     │
│                                         │
│   Verbind met WTH UMR2 Regulator       │
│   Voer het IP-adres van uw WTH UMR2    │
│   regulator in.                         │
│                                         │
│   IP-adres: [              ]            │
└─────────────────────────────────────────┘
```

## Testing the Logo

After installation, verify the logo appears correctly:

1. **Clear Browser Cache**
   - Force refresh (Ctrl+Shift+R / Cmd+Shift+R)
   - Or clear cache in browser settings

2. **Check Integration List**
   - Go to Settings → Devices & Services
   - Look for WTH logo next to integration name

3. **View Device Page**
   - Click on WTH UMR2 Regulator integration
   - Check if logo appears at top of device card

4. **Test Mobile App**
   - Open Home Assistant mobile app
   - Navigate to integrations
   - Verify logo displays correctly

## Troubleshooting Logo Display

### Logo Not Showing
- Clear browser cache
- Restart Home Assistant
- Check files exist:
  - `custom_components/wth_umr2/logo.png`
  - `custom_components/wth_umr2/icon.png`

### Logo Appears Stretched
- Files are correct format (PNG)
- Home Assistant will auto-scale appropriately

### Logo Shows as Broken Image
- Verify file permissions (readable)
- Check file isn't corrupted
- Re-copy logo files from package

## Notes

- The logo is embedded in the integration package
- No external URLs or downloads required
- Logo displays instantly after installation
- Works offline (local files only)
- Consistent across all Home Assistant interfaces

## Credits

WTH logo is trademark of WTH. Used with permission for this integration.
