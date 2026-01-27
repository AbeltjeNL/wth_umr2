# Installation Guide - WTH UMR2 Home Assistant Integration

## Prerequisites

- Home Assistant 2023.1 or newer
- WTH UMR2 Regulator connected to your network
- IP address of your WTH UMR2 device

## Step-by-Step Installation

### Method 1: Manual Installation

#### 1. Prepare the Integration Files

1. Download or clone this repository
2. Locate the `custom_components/wth_umr2` folder

#### 2. Copy Files to Home Assistant

**Option A: Via Samba/Network Share**
1. Access your Home Assistant configuration folder via network share
2. Navigate to (or create) the `custom_components` folder
3. Copy the entire `wth_umr2` folder into `custom_components`
4. Your folder structure should look like:
   ```
   config/
   └── custom_components/
       └── wth_umr2/
           ├── __init__.py
           ├── config_flow.py
           ├── const.py
           ├── manifest.json
           ├── sensor.py
           ├── strings.json
           └── translations/
               └── en.json
   ```

**Option B: Via SSH/Terminal**
1. Access Home Assistant via SSH or Terminal
2. Navigate to your config directory:
   ```bash
   cd /config
   ```
3. Create custom_components if it doesn't exist:
   ```bash
   mkdir -p custom_components
   ```
4. Copy the wth_umr2 folder:
   ```bash
   cp -r /path/to/wth_umr2 custom_components/
   ```

**Option C: Via File Editor Add-on**
1. Install the "File Editor" add-on if not already installed
2. Create the folder structure manually
3. Copy the contents of each file from the repository

#### 3. Restart Home Assistant

1. Go to **Settings** → **System**
2. Click **Restart** (top right)
3. Wait for Home Assistant to restart completely

#### 4. Verify Installation

1. Check the Home Assistant logs for any errors:
   - Go to **Settings** → **System** → **Logs**
   - Look for messages containing "wth_umr2"
2. If you see any errors, check the file permissions and structure

### Method 2: HACS Installation (Future)

Once this integration is added to HACS:

1. Open HACS
2. Click on "Integrations"
3. Search for "WTH UMR2"
4. Click "Download"
5. Restart Home Assistant

## Configuration

### 1. Find Your WTH UMR2 IP Address

You can find the IP address of your WTH UMR2 in several ways:

**Option A: From the Device**
- The IP address should be visible in the device's settings or display

**Option B: From Your Router**
- Log into your router's admin interface
- Look for connected devices
- Find the device with MAC address matching your WTH UMR2
- The MAC address can be found in the JSON data (in your case: `00:A0:50:0F:1F:03`)

**Option C: Network Scanner**
- Use a network scanning tool like Fing or Advanced IP Scanner
- Scan your local network
- Look for a device at the identified IP

### 2. Test the Connection

Before configuring in Home Assistant, verify the device is accessible:

1. Open a web browser
2. Navigate to: `http://YOUR_IP_ADDRESS/get.json?f=$.status.*`
3. You should see JSON data similar to the example provided
4. If you get an error, check:
   - IP address is correct
   - Device is powered on
   - Device is on the same network as Home Assistant
   - No firewall blocking the connection

### 3. Add Integration in Home Assistant

1. In Home Assistant, go to **Settings** → **Devices & Services**
2. Click the **+ ADD INTEGRATION** button (bottom right)
3. Search for "WTH UMR2 Regulator"
4. Click on it to start the setup
5. Enter your WTH UMR2 IP address (e.g., `192.168.178.69`)
6. Click **Submit**

The integration will:
- Test the connection
- Retrieve device information
- Create all sensor entities
- Add the device to your system

### 4. Verify Entities

1. Go to **Settings** → **Devices & Services**
2. Click on the **WTH UMR2 Regulator** integration
3. You should see:
   - 1 Device (WTH UMR2 Regulator)
   - 60+ Entities (all sensors)

## Troubleshooting

### Integration Not Found

**Symptoms**: "WTH UMR2" doesn't appear when searching for integrations

**Solutions**:
1. Verify the files are in the correct location: `config/custom_components/wth_umr2/`
2. Check file permissions (should be readable by Home Assistant)
3. Restart Home Assistant again
4. Clear your browser cache
5. Check the logs for any Python errors

### Cannot Connect to Device

**Symptoms**: Error message "Failed to connect to the device"

**Solutions**:
1. Verify IP address is correct
2. Ping the device from Home Assistant host:
   ```bash
   ping 192.168.178.69
   ```
3. Check if the JSON endpoint is accessible in a browser
4. Ensure no firewall is blocking port 80
5. Verify the device is on the same network/VLAN as Home Assistant

### Invalid Response Error

**Symptoms**: Error message "The device returned an invalid response"

**Solutions**:
1. Check the JSON endpoint URL in a browser
2. Verify the device is a WTH UMR2 (not another device at that IP)
3. Ensure the firmware version is compatible
4. Try accessing the root URL: `http://YOUR_IP/`

### Missing Sensors

**Symptoms**: Some expected sensors don't appear

**Possible Reasons**:
1. Temperature sensors showing 0.0°C are hidden (not connected)
2. Some valves may not be in use (will show 0%)
3. Communication interfaces not in use won't have devices

This is normal behavior - the integration only shows active/configured components.

### Sensors Not Updating

**Symptoms**: Sensor values are stale or not changing

**Solutions**:
1. Check the device is still accessible
2. Verify network connectivity
3. Check Home Assistant logs for errors
4. Restart the integration:
   - Go to **Settings** → **Devices & Services**
   - Click on WTH UMR2 integration
   - Click the three dots → **Reload**

## Logs and Debugging

### Enable Debug Logging

To get detailed logs for troubleshooting:

1. Edit your `configuration.yaml`:
   ```yaml
   logger:
     default: info
     logs:
       custom_components.wth_umr2: debug
   ```

2. Restart Home Assistant

3. Check logs at **Settings** → **System** → **Logs**

### Common Log Messages

- `Error communicating with API`: Network connectivity issue
- `Error fetching data: 404`: Wrong URL or device not responding
- `JSON decode error`: Invalid JSON response from device

## Network Configuration

### Static IP Address (Recommended)

For reliable operation, assign a static IP to your WTH UMR2:

**Option A: Router DHCP Reservation**
1. Log into your router
2. Find DHCP settings
3. Create a reservation for MAC: `00:A0:50:0F:1F:03`
4. Assign the desired IP address

**Option B: Device Configuration**
1. Access the WTH UMR2 configuration
2. Disable DHCP
3. Set a static IP address
4. Set subnet mask, gateway, and DNS

### Firewall Rules

If you have a firewall, ensure:
- Allow TCP port 80 from Home Assistant to WTH UMR2
- No VLAN isolation between Home Assistant and WTH UMR2

## Updating the Integration

When a new version is released:

### Manual Update
1. Download the new version
2. Replace the files in `custom_components/wth_umr2/`
3. Restart Home Assistant

### HACS Update
1. Open HACS
2. Go to Integrations
3. Click "Update" next to WTH UMR2

## Uninstalling

To remove the integration:

1. Go to **Settings** → **Devices & Services**
2. Find **WTH UMR2 Regulator**
3. Click the three dots → **Delete**
4. Confirm deletion
5. (Optional) Remove the `custom_components/wth_umr2` folder
6. Restart Home Assistant

## Getting Help

If you encounter issues:

1. Check this installation guide thoroughly
2. Review the main README.md
3. Check the Home Assistant logs
4. Verify your device JSON endpoint is working
5. Open an issue on GitHub with:
   - Home Assistant version
   - Integration version
   - Error messages from logs
   - Steps to reproduce the problem
