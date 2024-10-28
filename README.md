
# Data Logger and Communication System

## Overview
This project simulates an embedded data logging system that acquires environmental data from sensors (temperature, humidity), logs the data, and sends it to a host computer over serial communication.

## Structure
- **Hardware**: Circuit schematics, PCB layout, and Bill of Materials (BoM).
- **Firmware**: Code for reading sensors, logging data, and serial communication.
- **Scripts**: Python scripts for logging and visualizing data on a host computer.
- **Docs**: Documentation for project setup and troubleshooting.

## Setup
1. Build the hardware circuit using `schematics/circuit_diagram.png`.
2. Upload firmware to the microcontroller using `firmware_uploader.sh`.
3. Run `data_logger.py` on the host computer to log data.
