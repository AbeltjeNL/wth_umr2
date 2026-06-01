# Upgrade Guide: v1.1 to v1.2

## Quick Upgrade

**Good news:** Upgrading from v1.1 to v1.2 is seamless! No configuration changes needed.

```bash
# 1. Backup (recommended)
cp -r custom_components/wth_umr2 custom_components/wth_umr2.backup

# 2. Replace files
rm -rf custom_components/wth_umr2
cp -r /path/to/new/wth_umr2/custom_components/wth_umr2 custom_components/

# 3. Restart Home Assistant
```

That's it! Your integration will automatically work with v1.2.

## What Changed

### Requirements
- **Home Assistant:** 2025.1.0+ (was 2024.1.0+)
- **Python:** 3.12+ (was 3.11+)

### Under the Hood
- Using `entry.runtime_data` instead of `hass.data`
- Modern type aliases with Python 3.12+
- Direct device registry registration
- Better performance and cleanup

### User Impact
**None!** Everything works the same from your perspective.

## Verification Steps

### 1. Check Integration Version
```
Settings → Devices & Services → WTH UMR2 Regulator
```
Should show **Version 1.2.0**

### 2. Check Quality Scale
In the integration card, you should see quality scale upgraded to **Platinum**

### 3. Verify All Sensors Working
```
Settings → Devices & Services → WTH UMR2 → Device
```
All 60+ sensors should be present and updating

### 4. Check Logs
```
Settings → System → Logs
Filter: "wth_umr2"
```
Should be clean with no errors

## Troubleshooting

### Integration Won't Load

**Error:** "Integration failed to load"

**Cause:** Home Assistant or Python version too old

**Fix:**
1. Check your HA version:
   ```
   Settings → About
   ```
   Must be 2025.1.0 or newer

2. Check Python version via terminal/SSH:
   ```bash
   python3 --version
   ```
   Must be 3.12 or newer

3. If versions are old, upgrade Home Assistant first

### Sensors Showing Unavailable

**Fix:**
```
Settings → Devices & Services → WTH UMR2 → ⋮ → Reload
```

### Device Not Showing

**Fix:**
1. Remove integration
2. Restart Home Assistant  
3. Re-add integration with same IP address

## Rollback (If Needed)

If you encounter issues:

```bash
# Restore backup
rm -rf custom_components/wth_umr2
cp -r custom_components/wth_umr2.backup custom_components/wth_umr2

# Restart Home Assistant
```

Then report the issue: https://github.com/AbeltjeNL/wth_umr2/issues

## Benefits of v1.2

✅ **Better Performance** - Optimized coordinator  
✅ **Future-Proof** - HA 2026 standards  
✅ **Platinum Quality** - Highest quality rating  
✅ **Better Cleanup** - Proper resource management  
✅ **Modern Code** - Python 3.12+ features  

## Compatibility Matrix

| Component | v1.1 | v1.2 |
|-----------|------|------|
| Home Assistant | 2024.1+ | 2025.1+ |
| Python | 3.11+ | 3.12+ |
| Data Storage | hass.data | runtime_data |
| Type Aliases | ❌ | ✅ |
| Quality | Silver | Platinum |

## FAQ

**Q: Do I need to reconfigure the integration?**  
A: No, all settings are preserved.

**Q: Will my automations break?**  
A: No, all entity IDs remain the same.

**Q: Will my dashboard cards work?**  
A: Yes, everything remains compatible.

**Q: Should I upgrade?**  
A: Yes! v1.2 is faster, more reliable, and future-proof.

**Q: Can I skip v1.1 and go straight from v1.0 to v1.2?**  
A: Yes! The upgrade process is the same.

## Summary

✅ **Easy upgrade** - Just replace files and restart  
✅ **No configuration needed** - Everything automatic  
✅ **No breaking changes** - Fully compatible  
✅ **Better performance** - Optimized and modern  
✅ **Strongly recommended** - Future-proof your setup  

Enjoy v1.2! 🎉
