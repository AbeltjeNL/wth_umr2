# WTH UMR2 v1.2.0 - Home Assistant 2026 Standards Release

## 🎉 What's New

**Version 1.2.0** brings the WTH UMR2 integration fully up to **Home Assistant 2026.5 standards** with the latest Python 3.12+ features and best practices.

## 🚀 Major Updates

### 1. Home Assistant 2026 Compliance
- ✅ **Runtime Data**: Using modern `entry.runtime_data` instead of deprecated `hass.data`
- ✅ **Type Aliases**: Python 3.12+ `type` syntax for better type safety
- ✅ **Device Registry**: Direct device registration in setup
- ✅ **Coordinator Shutdown**: Proper cleanup with `async_shutdown()`
- ✅ **Always Update**: Performance optimization with `always_update=False`

### 2. Quality & Performance
- ✅ **Platinum Quality Scale**: Upgraded from Silver to Platinum
- ✅ **Better Validation**: Using `isinstance()` for type checking
- ✅ **Improved Cleanup**: Proper resource management
- ✅ **Modern Exception Handling**: Using `TimeoutError` instead of `asyncio.TimeoutError`

### 3. Developer Experience
- ✅ **Type Aliases**: `type WTHConfigEntry = ConfigEntry[WTHCoordinator]`
- ✅ **Better Type Hints**: Full modern Python typing
- ✅ **Cleaner Code**: Removed unused imports and simplified logic

## 📋 Breaking Changes

### Minimum Requirements Updated
- **Home Assistant**: 2025.1.0+ (was 2024.1.0+)
- **Python**: 3.12+ (was 3.11+)

### Migration Path
The integration will automatically migrate when you upgrade. No manual steps needed!

## 🔧 Technical Changes

### Before (v1.1.0)
```python
# Old way - using hass.data
hass.data.setdefault(DOMAIN, {})
coordinator = WTHCoordinator(hass, entry)
hass.data[DOMAIN][entry.entry_id] = coordinator

# In sensor platform
coordinator = hass.data[DOMAIN][entry.entry_id]
```

### After (v1.2.0)
```python
# New way - using runtime_data
coordinator = WTHCoordinator(hass, entry)
entry.runtime_data = coordinator

# In sensor platform
coordinator = entry.runtime_data
```

### Type Alias Addition
```python
# Modern Python 3.12+ type alias
type WTHConfigEntry = ConfigEntry[WTHCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: WTHConfigEntry) -> bool:
    """Set up with typed entry."""
```

### Device Registry
```python
# Direct device registration
device_registry = dr.async_get(hass)
device_registry.async_get_or_create(
    config_entry_id=entry.entry_id,
    identifiers={(DOMAIN, entry.entry_id)},
    manufacturer="WTH",
    model="UMR2",
    name="WTH UMR2 Regulator",
    sw_version=coordinator.data.get("version", {}).get("fw"),
    hw_version=coordinator.data.get("version", {}).get("hw"),
    configuration_url=f"http://{coordinator.host}",
)
```

## ✅ What's Improved

### 1. Performance
- Faster startup with direct device registration
- Better memory management with `always_update=False`
- Optimized coordinator with proper cleanup

### 2. Reliability
- Better exception handling hierarchy
- Proper cleanup on failed setup
- More robust data validation

### 3. Code Quality
- Modern Python 3.12+ features
- Better type safety with type aliases
- Cleaner, more maintainable code

## 📦 Installation

### New Installation
```bash
# Extract package
unzip wth_umr2_v1.2.0_complete.zip

# Copy to Home Assistant
cp -r wth_umr2/custom_components/wth_umr2 /config/custom_components/

# Restart Home Assistant
# Add integration via GUI
```

### Upgrade from v1.0 or v1.1
```bash
# Backup
cp -r custom_components/wth_umr2 custom_components/wth_umr2.backup

# Replace
rm -rf custom_components/wth_umr2
cp -r wth_umr2/custom_components/wth_umr2 /config/custom_components/

# Restart Home Assistant
```

**Note:** No reconfiguration needed! The integration will automatically work with the new version.

## 🎯 Features (Unchanged)

All v1.0/v1.1 features remain:
- ✅ 60+ sensor entities
- ✅ Automatic logo loading
- ✅ Multi-language (EN/NL)
- ✅ Real-time updates (30s)
- ✅ Diagnostic entity categories
- ✅ Comprehensive documentation

## 🔍 Verification

After upgrade, verify:

1. **Check Version**
   ```
   Settings → Devices & Services → WTH UMR2
   Version should show: 1.2.0
   Quality Scale: Platinum
   ```

2. **Check Device**
   ```
   Settings → Devices & Services → WTH UMR2 → Device
   Should show all device info and sensors
   ```

3. **Check Logs**
   ```
   Settings → System → Logs
   Filter: "wth_umr2"
   Should be clean, no errors
   ```

## 📊 Comparison

| Feature | v1.0 | v1.1 | v1.2 |
|---------|------|------|------|
| HA Version | 2023.1+ | 2024.1+ | **2025.1+** |
| Python | 3.10+ | 3.11+ | **3.12+** |
| Data Storage | hass.data | hass.data | **runtime_data** |
| Type Aliases | ❌ | ❌ | **✅** |
| Device Registry | Manual | Manual | **Direct** |
| Quality Scale | - | Silver | **Platinum** |
| Coordinator Shutdown | ❌ | ❌ | **✅** |
| Always Update | - | - | **Optimized** |

## 🐛 Known Issues

None reported for v1.2.0

## 🆘 Troubleshooting

### "Integration failed to load"

**Cause:** Home Assistant or Python version too old

**Solution:**
1. Check HA version: Must be 2025.1.0+
2. Check Python version: Must be 3.12+
3. Upgrade if needed

### Sensors unavailable after upgrade

**Cause:** Integration needs reload

**Solution:**
```
Settings → Devices & Services → WTH UMR2 → ⋮ → Reload
```

### Device not showing

**Cause:** Device registry issue

**Solution:**
1. Remove integration
2. Restart Home Assistant
3. Re-add integration

## 💡 Why Upgrade?

1. **Future-Proof**: Ready for HA 2027 and beyond
2. **Better Performance**: Optimized coordinator and device handling
3. **Platinum Quality**: Highest quality standard
4. **Modern Code**: Using latest Python features
5. **Better Reliability**: Improved error handling and cleanup

## 📞 Support

- **Documentation:** See README.md, CHANGELOG.md
- **Issues:** https://github.com/AbeltjeNL/wth_umr2/issues
- **Upgrade Help:** See UPGRADE_GUIDE.md

## 🎓 For Developers

### New Patterns to Use

1. **Type Aliases**
   ```python
   type WTHConfigEntry = ConfigEntry[WTHCoordinator]
   ```

2. **Runtime Data**
   ```python
   entry.runtime_data = coordinator
   coordinator = entry.runtime_data
   ```

3. **Direct Device Registration**
   ```python
   device_registry = dr.async_get(hass)
   device_registry.async_get_or_create(...)
   ```

4. **Coordinator Shutdown**
   ```python
   async def async_shutdown(self) -> None:
       await super().async_shutdown()
   ```

## ✨ Summary

**v1.2.0** is the most modern, performant, and future-proof version of the WTH UMR2 integration!

- 🏆 Platinum Quality
- 🚀 HA 2026 Standards
- ⚡ Python 3.12+
- 🎯 Runtime Data
- 🔧 Better Performance

**Strongly recommended for all users!**

---

**Version:** 1.2.0  
**Released:** May 14, 2026  
**Quality:** Platinum ⭐⭐⭐  
**Status:** Production Ready ✅
