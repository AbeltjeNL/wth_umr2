# 🚀 WTH UMR2 v1.3.0 - Installation Quick Guide

## ✅ You Have Everything You Need!

This package contains **everything** for a complete WTH UMR2 integration with Home Assistant 2026.3+ brand system support.

---

## 📦 Package Contents

**File:** `wth_umr2_v1.3.0_HA2026_complete.zip` (175KB)

- ✅ **Integration Code** - HA 2026.3+ brand system ready
- ✅ **Brand Folder** - Official logos and icons
- ✅ **Documentation** - 24 markdown files
- ✅ **Translations** - English + Dutch (Complete)
- ✅ **Examples** - 8 dashboard cards
- ✅ **Brands Package** - Ready for HA brands submission

**Total:** 54 files, fully tested and production-ready!

---

## 🎨 What's New - Brand System

**Home Assistant 2026.3+** has a new brand system where custom integrations include their own logos:

```
custom_components/wth_umr2/
└── brand/                  ← NEW!
    ├── brand.json
    ├── icon.png
    ├── icon@2x.png
    ├── logo.png
    └── logo@2x.png         ← HD 512×512 logo
```

**Result:** Logos automatically appear in Home Assistant UI! 🎉

---

## ⚡ Quick Install (3 Steps)

### Step 1: Extract Package
```bash
unzip wth_umr2_v1.3.0_HA2026_complete.zip
```

### Step 2: Copy to Home Assistant
```bash
cp -r wth_umr2/custom_components/wth_umr2 /config/custom_components/
```

### Step 3: Restart & Configure
1. Restart Home Assistant
   ```
   Settings → System → Restart
   ```

2. Add Integration
   ```
   Settings → Devices & Services → Add Integration
   Search: "WTH UMR2"
   IP Address: YOUR.WTH.IP.ADDRESS
   Submit
   ```

**Done!** ✅ Logo automatically appears!

---

## 🌐 Language Support

Your language is automatically selected based on your Home Assistant settings:

```
Settings → System → General → Language
```

**Available:**
- 🇬🇧 **English** - Full support
- 🇳🇱 **Nederlands** - Volledig ondersteund

All text, errors, and messages are automatically translated!

---

## 🎯 What You Get

### Immediately After Setup

- ✅ **60+ Sensors** - All device data accessible
- ✅ **Logo Display** - Automatic via `/api/brands/integration/`
- ✅ **Device Info** - Firmware, hardware, configuration URL
- ✅ **Real-time Updates** - Every 30 seconds
- ✅ **Multi-Language** - English & Dutch support
- ✅ **Organized Entities** - Diagnostic sensors categorized

### Logo Displays In

- 🎨 Integration list in Devices & Services
- 🎨 Device page header
- 🎨 Configuration flow (if adding new device)
- 🎨 Dashboard cards (if you add them)

---

## 📋 Requirements Check

Before installing, verify:

- [ ] **Home Assistant:** 2025.1.0 or newer
  - Best with 2026.3+ for brand system
- [ ] **Python:** 3.12 or newer  
- [ ] **WTH UMR2:** On your network
- [ ] **IP Address:** Known and accessible

### Check Your Versions

**Home Assistant:**
```
Settings → About
Version should be 2025.1.0 or higher
```

**Python (via SSH/Terminal):**
```bash
python3 --version
# Should show: Python 3.12.x or higher
```

**Device Connection:**
```bash
ping 192.168.178.69
# Should respond
```

---

## 🎨 Add Logo to Dashboard (Optional)

The logo automatically appears in HA, but you can also add cards:

```yaml
type: vertical-stack
cards:
  - type: picture
    image: /api/brands/integration/wth_umr2/logo.png
    title: WTH UMR2

  - type: entities
    title: Status
    entities:
      - sensor.wth_umr2_regulator_main_state
      - sensor.wth_umr2_regulator_operating_mode
```

See **DASHBOARD_CARDS_WITH_LOGO.md** for 8 more examples!

---

## ✅ Verification After Install

### 1. Check Integration Shows Logo
```
Settings → Devices & Services
Look for: WTH UMR2 Regulator (with logo)
```

### 2. Check Device
```
Settings → Devices & Services → WTH UMR2 → Device
Should show:
- Device info (manufacturer, model, versions)
- 60+ sensor entities
- All updating with current data
```

### 3. Check Brand API
```
Browser: http://YOUR_HA:8123/api/brands/integration/wth_umr2/logo.png
Should display: WTH logo
```

### 4. Check Logs
```
Settings → System → Logs
Filter: "wth_umr2"
Should be: Clean (no errors)
```

### 5. Check Language
```
Settings → System → General
Language: Select "Nederlands" to see Dutch
Go back to Devices & Services
Text should be in Dutch
```

---

## 🔄 Upgrading from v1.2.0?

### Quick Upgrade
```bash
# Backup
cp -r custom_components/wth_umr2 custom_components/wth_umr2.backup

# Replace
rm -rf custom_components/wth_umr2
cp -r wth_umr2/custom_components/wth_umr2 /config/custom_components/

# Restart Home Assistant
```

**No reconfiguration needed!** Everything migrates automatically.

### What's Different in v1.3.0

- ✅ Brand folder system (HA 2026.3+ standard)
- ✅ Logos served via `/api/brands/integration/` (official API)
- ✅ No custom logo endpoint
- ✅ Simpler, cleaner code
- ✅ Better logo quality (HD images included)
- ✅ Full language support

See **RELEASE_v1.3.0.md** for detailed changes.

---

## 📚 Documentation Included

### Quick Start
1. **This file** - Installation guide
2. **README.md** - Features and overview
3. **RELEASE_v1.3.0.md** - What's new

### Installation & Setup
4. **INSTALLATION.md** - Detailed guide
5. **QUICK_START.md** - 5-minute setup
6. **UPGRADE_GUIDE.md** - General upgrade info

### Usage
7. **DASHBOARD_CARDS_WITH_LOGO.md** - 8 ready cards
8. **EXAMPLES.md** - Automation ideas
9. **README_NL.md** - Dutch documentation

### Reference
10. **CHANGELOG.md** - Version history
11. **PACKAGE_SUMMARY.md** - Technical details
12. Plus 12 more guides

---

## 🐛 Troubleshooting

### Logo Not Showing

**Problem:** Logo doesn't appear in integration list

**Solution:**
1. Verify HA 2026.3+ or 2025.1+ is installed
2. Restart Home Assistant
3. Clear browser cache (Ctrl+Shift+R)
4. Check logs for errors

### Language Not Changing

**Problem:** Still shows English when you select Dutch

**Solution:**
1. Go to: Settings → System → General
2. Select: Language → Nederlands
3. Wait for page to reload
4. Go to Devices & Services
5. Check if text is now in Dutch

### Can't Find Integration

**Problem:** Can't find "WTH UMR2" when adding integration

**Solution:**
1. Verify files copied to `custom_components/wth_umr2/`
2. Restart Home Assistant completely
3. Clear browser cache (Ctrl+Shift+R)
4. Try again

### Can't Connect to Device

**Problem:** "Cannot connect" error during setup

**Solution:**
1. Verify IP address is correct
2. Test device: `curl http://192.168.178.69/get.json?f=$.status.*`
3. Check device is powered on
4. Ensure same network as Home Assistant

### Python/HA Version Too Old

**Problem:** "Integration failed to load"

**Solution:**
1. Check HA version (must be 2025.1.0+)
2. Check Python (must be 3.12+)
3. Upgrade if needed

---

## 🎯 Next Steps

After successful installation:

1. ✅ **Customize Entities**
   - Rename thermostats
   - Settings → Devices & Services → WTH UMR2 → Device → Entity

2. ✅ **Create Dashboard**
   - Add logo and status cards
   - See DASHBOARD_CARDS_WITH_LOGO.md

3. ✅ **Setup Automations**
   - Alert on device offline
   - Monitor temperature changes
   - Track heating runtime

4. ✅ **Explore Documentation**
   - Read EXAMPLES.md for ideas
   - Check CHANGELOG.md for all features

---

## 💡 Pro Tips

1. **Static IP:** Set static IP for WTH UMR2 device
2. **Entity Names:** Customize sensor names for your zones
3. **Dashboard:** Start with examples in DASHBOARD_CARDS_WITH_LOGO.md
4. **Backup:** Backup config before major changes
5. **Docs:** Keep included documentation handy

---

## 🆘 Need Help?

- 📖 **Documentation:** See included markdown files
- 🐛 **Issues:** https://github.com/AbeltjeNL/wth_umr2/issues
- 💬 **Discussions:** https://github.com/AbeltjeNL/wth_umr2/discussions

---

## ✨ Why v1.3.0 is Great

- 🏆 **Platinum Quality** - Highest HA standard
- 🚀 **HA 2026.3+ Ready** - Official brand system
- 🌐 **Multi-Language** - English + Dutch
- 🎨 **Beautiful Logos** - Auto-displayed in UI
- ⚡ **Fast** - Official HA image serving
- 🔒 **Secure** - Uses HA's official APIs

---

## 🎉 You're Ready!

Everything you need is in this package:

✅ Latest integration code  
✅ Complete documentation  
✅ Ready-to-use examples  
✅ Automatic logo display  
✅ Multi-language support (EN + NL)  

**Just install and enjoy!** 🚀

---

**Package:** wth_umr2_v1.3.0_HA2026_complete.zip  
**Version:** 1.3.0  
**Quality:** Platinum ⭐  
**Files:** 54  
**Size:** 175KB  
**Languages:** English + Dutch  
**Status:** Production Ready ✅
