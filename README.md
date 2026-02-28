# Arduino Real-Time Energy Monitor & Telemetry
An end-to-end hardware-to-software pipeline for monitoring power consumption and calculating total energy usage.

##  Technical Overview
This project interfaces an **Arduino Uno** with a serial data pipeline to capture voltage/current metrics. It utilizes a **Python** backend for long-term data logging and numerical analysis.

### Key Engineering Features:
* **Hardware Layer:** C++ firmware for high-frequency analog sampling and 1602 LCD real-time display.
* **Data Pipeline:** Python (PySerial) bridge to transition data from embedded hardware to a Windows/Linux filesystem.
* **Mathematical Analysis:** Implements the **Trapezoidal Rule** via NumPy to integrate instantaneous power over time, providing accurate Watt-hour (Wh) calculations.
* **Visualization:** Matplotlib integration for plotting power profiles and identifying peak consumption periods.

##  Tech Stack
* **Embedded:** C++, Arduino IDE
* **Software:** Python 3.10+, NumPy, Matplotlib
* **Tools:** Git, WSL (Ubuntu), VS Code
