# WTH UMR2 Integration v1.0 - Release Notes

![WTH Logo](custom_components/wth_umr2/logo.png)

## 🎉 What's New in Version 1.0

### Visual Enhancements
- ✅ **Official WTH Logo** integrated into the Home Assistant GUI
- ✅ Logo appears in:
  - Integration setup screen
  - Device card
  - Integration list
  - All related UI elements

### Localization
- ✅ **Dutch Language Support** (nl.json)
  - Complete translation of all UI strings
  - Native language setup experience for Dutch users
  - README_NL.md with full Dutch documentation

### Metadata Updates
- ✅ **Version**: Changed to 1.0 (from 1.0.0)
- ✅ **Code Owner**: Set to @AbeltjeNL
- ✅ **Repository**: https://github.com/AbeltjeNL/wth_umr2
- ✅ **License**: MIT License included

### Device Information Enhancements
- ✅ **Hardware Version**: Now displayed in device info
- ✅ **Configuration URL**: Direct link to device web interface (http://IP_ADDRESS)
- ✅ **Device ID**: Properly extracted from JSON response

### Project Files
- ✅ **LICENSE**: MIT License file added
- ✅ **.gitignore**: Proper Python/Home Assistant gitignore
- ✅ **hacs.json**: HACS compatibility metadata
- ✅ **README_NL.md**: Complete Dutch documentation

## 📦 Package Contents

```
wth_umr2/
├── .gitignore                          # Git ignore rules
├── hacs.json                           # HACS metadata
├── LICENSE                             # MIT License
├── README.md                           # English documentation
├── README_NL.md                        # Nederlandse documentatie
├── INSTALLATION.md                     # Installation guide
├── EXAMPLES.md                         # Usage examples
├── QUICK_START.md                      # Quick start guide
└── custom_components/
    └── wth_umr2/
        ├── __init__.py                 # Main integration
        ├── config_flow.py              # GUI setup flow
        ├── const.py                    # Constants
        ├── manifest.json               # Integration metadata (v1.0)
        ├── sensor.py                   # Sensor platform (60+ sensors)
        ├── strings.json                # Base UI strings
        ├── logo.png                    # WTH logo for GUI
        ├── icon.png                    # Icon version of logo
        └── translations/
            ├── en.json                 # English translations
            └── nl.json                 # Dutch translations (NEW!)
```

## 🌍 Language Support

### English (en)
- Full integration setup
- All sensor names and descriptions
- Error messages and help text

### Nederlands (nl) 🆕
- Volledige integratie setup
- Alle sensornamen en beschrijvingen
- Foutmeldingen en help teksten

The integration automatically detects your Home Assistant language and shows the appropriate translation.

## 🖼️ Logo Integration

The WTH logo is now displayed in:

1. **Add Integration Screen**
   - Logo appears when searching for "WTH UMR2"
   - Professional branded appearance

2. **Device Card**
   - Logo shown in device information
   - Consistent branding throughout

3. **Integration Settings**
   - Logo in integration list
   - Easy visual identification

## 🔧 Technical Details

### Version Number Change
- Old: `1.0.0` (semantic versioning)
- New: `1.0` (simplified versioning)

### Ownership
- **Code Owner**: @AbeltjeNL
- **Repository**: https://github.com/AbeltjeNL/wth_umr2
- **License**: MIT

### Device Information
Enhanced device info now includes:
```python
{
    "identifiers": {("wth_umr2", "entry_id")},
    "name": "WTH UMR2 Regulator",
    "manufacturer": "WTH",
    "model": "UMR2",
    "sw_version": "00.01",           # From device
    "hw_version": "00.01",           # From device (NEW!)
    "configuration_url": "http://192.168.178.69"  # (NEW!)
}
```

## 📥 Installation

### Method 1: Manual Installation
1. Download `wth_umr2_integration_v1.0.zip`
2. Extract to `custom_components/`
3. Restart Home Assistant
4. Add integration via GUI

### Method 2: HACS (Future)
Once added to HACS default repositories:
1. Open HACS
2. Search "WTH UMR2"
3. Click Install
4. Restart

## 🆙 Upgrading from Pre-1.0

If you installed a previous version:

1. **Backup** your Home Assistant configuration
2. **Remove** old integration via GUI (Settings → Devices & Services)
3. **Delete** old `custom_components/wth_umr2` folder
4. **Install** new version
5. **Add** integration again
6. Your previous configuration will be automatically restored

## ✨ What's Next?

Future enhancements under consideration:
- Binary sensors for on/off states
- Climate platform for thermostat control
- Switch platform for valve control
- Service calls for device control
- Energy monitoring integration
- More language translations

## 🐛 Known Issues

None reported for v1.0

## 📞 Support

- **Issues**: https://github.com/AbeltjeNL/wth_umr2/issues
- **Discussions**: https://github.com/AbeltjeNL/wth_umr2/discussions
- **Email**: [Your support email if desired]

## 🙏 Credits

- **Developer**: AbeltjeNL
- **Logo**: WTH (used with permission)
- **Testing**: Community contributors

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Version**: 1.0  
**Release Date**: January 27, 2026  
**Maintainer**: @AbeltjeNL
