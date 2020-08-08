**Appendix 4 - SKR Bootloader Update**

Source: https://github.com/Arksine/LPC17xx-DFU-Bootloader/releases



The current SKR 1.3 boards ship with the Marlin bootloader which does not allow Klipper to update the firmware via USB. This means that when you update Klipper, if the MCU firmware needs to be updated, you would typically need to create the new firmware image, manually transfer it to the SKR microSD card on both SKR boards, and power cycle. This is not ideal because it’s difficult to access the SKR boards below your printer.



Fortunately there is a great way to fix this! You can now update your SKR 1.3 boot loader to the smoothieware bootloader, which allows you to update the MCU firmware at any time via USB. To do this, perform the following steps:



1. Verify that your SKR jumper settings are correct as defined in SKR 1.3 Board Configuration section. Specifically make sure that the jumper is connected between "INT" and "5V" on both of your SKR boards. 
2. Download the file “betterBootleader.bin” file to your computer, and rename it “firmware.bin”
3. Power down your printer and remove the microSD card from each of your SKR 1.3 boards. 
4. Connect one of the microSD cards to your computer and transfer the firmware.bin file to it. Eject the microSD card and disconnect it from your computer.
5. Repeat step 4 with your second microSD card.

With the still powered off, insert one microSD card into each SKR 1.3 board. 

Power up your printer. After waiting 30 seconds, momentarily press the reset button once on each SKR 1.3 board. The reset button is located at the corner of the board between the thermistor inputs and the display outputs. Wait the entire 30s, or your bootloader may become corrupted.

SSH in to your Raspberry Pi and run **ls -l /dev/serial/by-path/** Check to see if the board IDs match what you have in your Klipper printer.cfg file. If they do not match your previous configuration, go through the process to identify which ID matches which MCU as defined in the “Setting Up Voron Printer Config File” section.