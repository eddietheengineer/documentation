# Controller Module - Voron 2 - SKR 1.3

This module details how to configure and wire your SKR 1.3 boards for a Voron 2.4 printer.

**Jumper Configuration**

For both SKR 1.3 boards with TMC 2208 or TMC 2209 drivers:

- Remove the four jumpers from below the drivers on all boards (shown in red)
- Put single jumper for each driver's UART connection (shown in green)
- Remove all jumpers from end stop pins, otherwise end stops will not work properly
- Make sure power jumper is between INT and +5V (should be default from factory). If this is not installed correctly you may have power issues with your Raspberry Pi which can cause throttling.

![skr13_jumper](https://github.com/jdlongenecker/documentation/blob/master/setup_guide/images/skr13_jumper.png?raw=true)

![voron2_skr13_mcu_xye](https://github.com/jdlongenecker/documentation/blob/master/setup_guide/images/voron2_skr13_mcu_xye.png?raw=true)

![voron2_skr13_mcu_z](https://github.com/jdlongenecker/documentation/blob/master/setup_guide/images/voron2_skr13_mcu_z.png?raw=true)

## Klipper Firmware Generation

After you've installed Klipper, we need to 

In this menu structure, you’ll want to pick a few things. Make sure your Micro-controller Architecture is LPC176x, and your processor model is the lpc1768 with 100Mhz. 

When your configuration matches the image below, select Exit and “Yes” if you are asked to save the configuration.