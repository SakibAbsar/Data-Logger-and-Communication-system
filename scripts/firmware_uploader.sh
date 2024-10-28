
#!/bin/bash
# Script to upload firmware to Arduino
arduino-cli compile --fqbn arduino:avr:uno firmware/main_firmware.ino
arduino-cli upload -p /dev/ttyUSB0 --fqbn arduino:avr:uno firmware/main_firmware.ino
