# WTH UMR2 v1.1.0 - Complete Release Package

## 📦 Package Information

**Version:** 1.1.0  
**Release Date:** May 14, 2026  
**Package:** `wth_umr2_v1.1.0_complete.zip` (184KB)  
**Compatibility:** Home Assistant 2024.1.0+, Python 3.11+

## ✨ What's Included

### Core Integration Files
```
custom_components/wth_umr2/
├── __init__.py                 # Main integration (Updated)
├── config_flow.py              # GUI setup (Updated)
├── sensor.py                   # Sensor platform (Updated)
├── const.py                    # Constants
├── manifest.json               # Integration metadata (v1.1.0)
├── strings.json                # UI strings (Updated)
├── panel.py                    # Panel support
└── translations/
    ├── en.json                 # English (Updated)
    └── nl.json                 # Dutch (Updated)
```

### Logo Files (Auto-Loading)
```
custom_components/wth_umr2/
├── icon.png                    # 128x128 icon
├── icon@2x.png                 # 256x256 HD icon
├── logo.png                    # 256x256 logo
└── icon.svg                    # Vector logo
```

### Documentation (17 Files)
- **README.md** - Main documentation
- **README_NL.md** - Nederlandse documentatie
- **CHANGELOG.md** - Version history (NEW)
- **UPGRADE_GUIDE.md** - Upgrade instructions (NEW)
- **INSTALLATION.md** - Installation guide
- **QUICK_START.md** - Quick start guide
- **EXAMPLES.md** - Dashboard examples
- **AUTO_LOGO_LOADING.md** - Logo technical docs
- **DASHBOARD_CARDS_WITH_LOGO.md** - 8 card examples
- Plus 8 more guides...

### Additional Files
- **LICENSE** - MIT License
- **hacs.json** - HACS compatibility
- **requirements_dev.txt** - Development requirements (NEW)
- **.gitignore** - Git ignore rules
- **brands_submission/** - Ready for HA Brands submission

## 🚀 Key Improvements in v1.1.0

### 1. Updated to Latest HA Standards
- ✅ Modern async patterns with `asyncio.timeout()`
- ✅ Python 3.11+ type hints
- ✅ Proper exception chaining
- ✅ ConfigEntryNotReady support
- ✅ Integration reload support

### 2. Better Error Handling
- ✅ Specific timeout detection
- ✅ Detailed error messages
- ✅ Better connection failure feedback
- ✅ Response validation

### 3. Entity Organization
- ✅ Diagnostic entities properly categorized
- ✅ Communication sensors marked as diagnostic
- ✅ Device sensors marked as diagnostic
- ✅ Cleaner device page organization

### 4. Performance Improvements
- ✅ FileResponse for logo serving (less memory)
- ✅ Path library for modern file handling
- ✅ Better resource cleanup
- ✅ Optimized coordinator

### 5. Enhanced Quality
- ✅ Quality scale: Silver
- ✅ Issue tracker in manifest
- ✅ Comprehensive type hints
- ✅ Better code documentation

## 📊 Statistics

| Metric | Count |
|--------|-------|
| **Total Files** | 49 |
| **Python Files** | 4 |
| **Documentation Files** | 17 |
| **Translation Files** | 2 |
| **Logo Files** | 8 |
| **Total Lines of Code** | ~1,500 |
| **Sensor Entities** | 60+ |
| **Languages** | 2 (EN, NL) |

## 🎯 Installation

### New Installation

1. **Download** `wth_umr2_v1.1.0_complete.zip`
2. **Extract** to your Home Assistant config directory:
   ```bash
   unzip wth_umr2_v1.1.0_complete.zip
   cp -r wth_umr2/custom_components/wth_umr2 /config/custom_components/
   ```
3. **Restart** Home Assistant
4. **Add Integration**:
   - Settings → Devices & Services → Add Integration
   - Search: "WTH UMR2 Regulator"
   - Enter IP address: `192.168.178.69`

### Upgrade from v1.0

See **UPGRADE_GUIDE.md** for detailed instructions.

**Quick upgrade:**
```bash
# Backup
cp -r custom_components/wth_umr2 custom_components/wth_umr2.backup

# Replace
rm -rf custom_components/wth_umr2
cp -r wth_umr2/custom_components/wth_umr2 /config/custom_components/

# Restart Home Assistant
```

## ✅ Features

### Sensors (60+)
- **System Status** (7 sensors)
  - Main state, mode, display, LED, heat/cool/PWM factors

- **Outputs** (3 sensors)
  - Heater output, cooler output, pump speed

- **Thermostats** (16 sensors)
  - 8 zones with temperature and state

- **Valves** (10 sensors)
  - Position sensors for all valves

- **Inputs** (13 sensors)
  - Max/return/condens inputs, 10 temperature sensors

- **Communications** (15 sensors - DIAGNOSTIC)
  - Fanlink, RF, Modbus, Bluetooth, Ethernet status
  - 10 Fanlink device sensors

### Automatic Logo Loading
- ✅ HTTP API: `/api/wth_umr2/logo/{filename}`
- ✅ WWW Directory: `/local/wth_umr2/`
- ✅ Auto-copy on startup
- ✅ Ready for dashboard cards

### Multi-Language
- ✅ English (en)
- ✅ Nederlands (nl)

## 🔧 Requirements

### Minimum
- **Home Assistant:** 2024.1.0 or newer
- **Python:** 3.11 or newer
- **Network:** Local network access to WTH UMR2 device

### Recommended
- **Home Assistant:** Latest stable version
- **Python:** 3.12+
- **Network:** Static IP for WTH UMR2 device

## 📝 Quick Reference

### Entity Naming
```
sensor.wth_umr2_regulator_main_state
sensor.wth_umr2_regulator_thermostat_1_temperature
sensor.wth_umr2_regulator_valve_3
```

### Logo Paths
```yaml
# In dashboard cards:
image: /local/wth_umr2/logo.png

# Or via API:
image: /api/wth_umr2/logo/logo.png
```

### Device Configuration
```
IP Address: 192.168.178.69
API URL: http://192.168.178.69/get.json?f=$.status.*
Update Interval: 30 seconds
```

## 🐛 Known Issues

None reported for v1.1.0

## 📞 Support

- **Documentation:** See included markdown files
- **Issues:** https://github.com/AbeltjeNL/wth_umr2/issues
- **Discussions:** https://github.com/AbeltjeNL/wth_umr2/discussions

## 📄 License

MIT License - See LICENSE file

## 🙏 Credits

- **Developer:** AbeltjeNL
- **Logo:** WTH (used with permission)
- **Platform:** Home Assistant

## 📋 Checklist

Before installation, verify:
- [ ] Home Assistant 2024.1.0 or newer
- [ ] Python 3.11 or newer
- [ ] WTH UMR2 device on network
- [ ] Device IP address known
- [ ] Backup of existing configuration

## 🎉 Ready to Install!

Everything you need is in this package. Just extract, copy, restart, and configure!

---

**Package:** wth_umr2_v1.1.0_complete.zip  
**Size:** 184KB  
**Files:** 49  
**Version:** 1.1.0  
**Status:** Ready for Production ✅
