# imx6qdl-sabresd

Python 3

Tkinter library (python3-tk on Ubuntu/Debian)

sudo apt install python3-tk


project simulates the boot LED sequence for the i.MX6QDL Sabre-SD board using two approaches:

C Program (imx6qdl_sabre_led) – Console-based simulation of 16 LEDs representing boot stages.

Python GUI (led_gui.py) – Graphical simulation with a 4x4 LED grid showing each stage of the boot process.


=========================================================================
Boot LED Flow Summary
========================================================================

Power ON → LED0

U-Boot stage → LED1–LED4

Kernel boot → LED5–LED8

RootFS mount → LED9–LED11

Services init → LED12–LED14 (Wi-Fi / Bluetooth / Ethernet)

System Ready → LED15
============================================================================
