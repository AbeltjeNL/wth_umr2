# Upgrade Guide: v1.0 to v1.1

## Overview

Version 1.1.0 brings the WTH UMR2 integration up to the latest Home Assistant standards with improved performance, better error handling, and enhanced organization.

## Breaking Changes

### Minimum Requirements
- **Home Assistant**: 2024.1.0 or newer required
- **Python**: 3.11 or newer (for async timeout support)

### Entity Organization
Communication and device status sensors are now marked as **DIAGNOSTIC** entities:
- Fanlink Status
- RF Status  
- Modbus Status
- Bluetooth Status
- Ethernet Status
- Fanlink Device 1-10

These will now appear in the "Diagnostic" section of your device page by default.

## What's New

### 1. Better Error Messages
You'll now see more specific error messages:
- ✅ **Timeout errors** - When the device doesn't respond in time
- ✅ **Connection errors** - When the device can't be reached
- ✅ **Invalid response errors** - When the device returns unexpected data

### 2. Improved Performance
- Faster logo serving (uses FileResponse instead of loading into memory)
- More efficient file handling with Path library
- Better resource cleanup

### 3. Enhanced Reliability
- Better handling of network issues
- Improved coordinator error recovery
- Proper exception chaining for better debugging

### 4. Entity Categories
Diagnostic sensors are now properly categorized, making your device page cleaner and more organized.

## Upgrade Steps

### Option 1: HACS Update (If using HACS)
1. Go to HACS → Integrations
2. Find "WTH UMR2 Regulator"
3. Click "Update"
4. Restart Home Assistant

### Option 2: Manual Update
1. **Backup your configuration**
   ```bash
   cp -r custom_components/wth_umr2 custom_components/wth_umr2.backup
   ```

2. **Download new version**
   - Download the latest release
   - Extract to temporary location

3. **Replace files**
   ```bash
   # Remove old version
   rm -rf custom_components/wth_umr2
   
   # Copy new version
   cp -r path/to/new/wth_umr2 custom_components/
   ```

4. **Restart Home Assistant**
   - Settings → System → Restart

5. **Verify installation**
   - Check logs for any errors
   - Verify all sensors are updating
   - Test dashboard cards

## Post-Upgrade Verification

### 1. Check Integration Status
```
Settings → Devices & Services → WTH UMR2 Regulator
```
- Status should be "Loaded"
- Version should show 1.1.0

### 2. Verify Sensors
All sensors should still be present and updating:
- Main status sensors ✓
- Thermostat sensors ✓
- Valve sensors ✓
- Temperature sensors ✓
- Diagnostic sensors (now in diagnostic category) ✓

### 3. Check Diagnostic Entities
Go to your device page:
```
Settings → Devices & Services → WTH UMR2 → Your Device
```
Scroll to "Diagnostic" section - you should see:
- Communication status sensors
- Fanlink device sensors

### 4. Test Error Handling
Try intentionally entering a wrong IP:
```
Settings → Devices & Services → WTH UMR2 → Configure
```
You should see clear, specific error messages.

## Troubleshooting

### Integration Won't Load

**Symptom**: Integration shows as "Failed to load"

**Solution**:
1. Check Home Assistant version (must be 2024.1.0+)
2. Check Python version (must be 3.11+)
3. Check logs for specific error
   ```
   Settings → System → Logs
   Filter: "wth_umr2"
   ```

### Sensors Not Updating

**Symptom**: Sensors show as "Unavailable"

**Solution**:
1. Check device connectivity
   ```
   ping 192.168.178.69
   ```
2. Verify device JSON endpoint
   ```
   curl http://192.168.178.69/get.json?f=$.status.*
   ```
3. Restart integration
   ```
   Settings → Devices & Services → WTH UMR2 → ⋮ → Reload
   ```

### Diagnostic Entities Missing

**Symptom**: Can't find communication status sensors

**Solution**:
They're now in the "Diagnostic" section of your device page. Toggle "Show disabled entities" if needed.

### Logo Not Loading

**Symptom**: Logo doesn't appear in dashboard

**Solution**:
1. Clear browser cache (Ctrl+Shift+R)
2. Verify files exist
   ```bash
   ls /config/www/wth_umr2/
   ```
3. Check API endpoint
   ```
   http://YOUR_HA_IP:8123/api/wth_umr2/logo/logo.png
   ```

## Rollback (If Needed)

If you encounter issues and need to rollback:

1. **Restore backup**
   ```bash
   rm -rf custom_components/wth_umr2
   cp -r custom_components/wth_umr2.backup custom_components/wth_umr2
   ```

2. **Restart Home Assistant**

3. **Report issue**
   - https://github.com/AbeltjeNL/wth_umr2/issues
   - Include logs and error messages

## Benefits of Upgrading

✅ **Better performance** - Faster, more efficient
✅ **Clearer errors** - Know exactly what went wrong
✅ **Better organization** - Diagnostic entities properly categorized
✅ **Future-proof** - Ready for upcoming HA versions
✅ **More reliable** - Improved error recovery

## Compatibility

| Component | v1.0 | v1.1 |
|-----------|------|------|
| Home Assistant | 2023.1+ | 2024.1+ |
| Python | 3.10+ | 3.11+ |
| Entity Categories | ❌ | ✅ |
| Modern Async | ⚠️ | ✅ |
| Type Hints | Basic | Complete |

## Questions?

- Documentation: See README.md
- Issues: https://github.com/AbeltjeNL/wth_umr2/issues
- Changelog: See CHANGELOG.md

---

**Recommendation**: We strongly recommend upgrading to v1.1.0 for the improved reliability and performance.
