#!/bin/bash

# Replace with your device ID
DEVICE_ID="258a:0049"

# Find the device path
DEVICE_PATH=$(lsusb | grep "$DEVICE_ID" | awk '{print "/dev/bus/usb/" $2 "/" $4}' | sed 's/://')

# If the device path exists
if [ -e "$DEVICE_PATH" ]; then
    echo "Resetting keyboard at $DEVICE_PATH"
    sudo usbreset "$DEVICE_ID"
else
    echo "Keyboard device not found."
fi
