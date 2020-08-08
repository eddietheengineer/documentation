# 4. Klipper Installation

References:

[Klipper Installation Instructions](https://github.com/KevinOConnor/klipper/blob/master/docs/Installation.md) 

[SKR Installation Instructions](https://3dprintbeginner.com/install-klipper-on-skr-1-3-speed-up-your-prints/)



**Installing Klipper on your MCU Boards**

- Install OctoPi on your Raspberry Pi (guide here: https://octoprint.org/download/)
- Once it is installed, connect to your Raspberry Pi using Windows [SSH commands](https://www.howtogeek.com/336775/how-to-enable-and-use-windows-10s-built-in-ssh-commands/) or [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/) or for macOS, use Terminal.

​	```ssh pi@octopi```

OR 

​	```ssh pi@192.168.1.x```

- Enter password, the default one is “raspberry”. It is recommended to change this for security using

​	```sudo raspi-config```

​	and then select "Change User Password" and follow the prompts.

- Once you are back at the command line of the Raspberry Pi, run the following commands:

​	```git clone https://github.com/KevinOConnor/klipper```

​	```./klipper/scripts/install-octopi.sh```

- When the install script has completed, run the following commands:

​	```cd ~/klipper/```

​	```make menuconfig```



**Configuring Octoprint to use Klipper**

Reference: [KevinOConnor - klipper/docs/Installation.md](https://github.com/KevinOConnor/klipper/blob/master/docs/Installation.md#configuring-octoprint-to-use-klipper)

The OctoPrint web server needs to be configured to communicate with the Klipper host software. 

Using a web browser, login to the OctoPrint web page and then configure the following items:

- Navigate to the Settings tab (the wrench icon at the top of the page)

- Under "Serial Connection" in "Additional serial ports" add "/tmp/printer" then click "Save"

- Open Settings tab and under "Serial Connection" change the "Serial Port" setting to "/tmp/printer"

- In the Settings tab, navigate to the "Behavior" sub-tab and select the "Cancel any ongoing prints but stay connected to the printer" option, then click “Save”

- From the main page, under the "Connection" section (at the top left of the page) make sure the "Serial Port" is set to "/tmp/printer" and click "Connect". (If "/tmp/printer" is not an available selection then try reloading the page)

- Once connected, navigate to the "Terminal" tab and type "status" (without the quotes) into the command entry box and click "Send". The terminal window will likely report there is an error opening the config file - that means OctoPrint is successfully communicating with Klipper.		 



**Setting up Voron Printer Configuration FIle**

- Download the respective Voron configuration file from the controller module that applies to your printer and control board.

- Using WinSCP, Cyberduck, Notepad++ NppFTP, or BBEdit, transfer the downloaded file to your raspberry pi in the following folder:

​	```~/klipper/config/``` 

- Run the following command to copy the Voron configuration into your printer config:

​	```cp ~/klipper/config/FILENAME_OF_VORON_CONFIG.cfg ~/printer.cfg```

**Note:** There are many ways of editing your config file. Using the built-in Nano editor through SSH is simple, but it is not user friendly. Notepad++ with the NppFTP plugin (Windows) or bbEdit (MacOS) are better alternatives. Instructions on how to use them are in the appendix. 

- Review the configuration file by typing:

​	```nano ~/printer.cfg```

You’ll notice that near the top of the file, there are two sections titled [mcu] and [mcu z]. These sections are where we define that we will be using the SKR 1.3 controllers, and identifying the controllers so that Klipper knows which components are connected to what controller. First of all, we need to identify what the Raspberry Pi calls each of the controllers so we can correctly list them in the configuration.

- Take the USB cable from the SKR 1.3 with the X, Y, and E steppers connected to it and plug this in to one of the USB ports on your Raspberry Pi, then run the following command:

​	```ls -l /dev/serial/by-path/```

You should see something similar to this: 

- Copy the corresponding text from your terminal window **platform-3f980000.usb-usb-0:1.5:1.0** and paste it in a text file temporarily. 

- Open your configuration file (nano ~/printer.cfg) and navigate to the [mcu] section. After the text “serial: /dev/serial/by-path/” paste your SKR path so that the line becomes:

​	```serial: /dev/serial/by-path/platform-3f980000.usb-usb-0:1.5:1.0```

- Exit the text editor using CNTL-X, and save when asked.

- Take the USB cable from the SKR 1.3 with the Z steppers connected to it and plug this in to another USB port on your Raspberry Pi. \

- Rerun the command “ls -l /dev/serial/by-path/” and note that there are two devices listed, one with a different path than your previous SKR 1.3. Copy this text and save it.

- Open your configuration file and add in your copied text under [mcu z] so it looks something like:

​	```serial: /dev/serial/by-path/platform-3f980000.usb-usb-0:1.4:1.0```

- Save the configuration file as before. 

- Under Octoprint’s Terminal tab type:

​	FIRMWARE_RESTART and press enter send the command to restart Klipper. 

**NOTE:** **Pay close attention and complete the remaining configuration checks. If you do not complete these steps, your printer will not run!**

1. Open your printer.cfg file again, and scan through the file. Under [stepper_x], uncomment the position_endstop and position_max that corresponds to your printer size. Under [tmcXXXX stepper_x], replace XXXX with either 2208 or 2209 to match the type of TMC drivers that you have. For example, [tmc2209 stepper_x] for TMC 2209 drivers.

1. Repeat step 1 for your [stepper_y] motor. 
2. Under [stepper_z], uncomment position_max for your printer type. You will need to update the TMC configuration with your stepper type for all four Z motors (Z, Z1, Z2, and Z3). 
3. Under [extruder] verify that your sensor_type is correct. Do not worry about step_distance and pid values for now, they will be updated later in the setup process. Update [tmcXXXX extruder] to match the type of stepper driver you have for your extruder.
4. Under [heater_bed], verify that your sensor type is correct.
5. Under [quad_gantry_level], uncomment the “gantry_corners” and “points” sections for your printer size.
6. Under Display, uncomment the display section that matches your display.

Save the configuration file.

- Under Octoprint’s Terminal tab type:

​	FIRMWARE_RESTART and press enter send the command to restart Klipper. 

The terminal window should show a status “Ready”—if not, type “status” in to the terminal command and press enter. If Klipper says that it is not ready, it will generally notify you if there is a configuration issue that needs to be fixed.

**Common Klipper Errors**

**TMC UART Error:** This appears when the communication between the TMC drivers and the SKR 1.3 is not working. Typically this means that you have not powered the SKR board with 12-24V (TMC drivers didn’t boot), you haven’t plugged in the TMC steppers to the correct spots, or you forgot to add or remove a jumper as detailed above.

**ADC Error:** ADC stands for “Analog to Digital Converter” and is what is used to convert thermistor readings to temperatures for your hotend and heated bed. As a safety precaution, if Klipper is expecting a thermistor to be plugged in but it is reading an invalid reading (no thermistor = open, or 0 ohms for a shorted wire as closed), it will go in to this shut down mode. Double check to make sure your thermistors are plugged in to the correct SKR 1.3 boards and plugs. 

**Unable to connect:** Once the underlying issue is corrected, use the "FIRMWARE_RESTART" command to reset the firmware, reload the config, and restart the host software.

​	Check MCU IDs match your printer.cfg 

​								"*Make sure you get the paths right”*

**Klipper Troubleshooting**

**Retrieve Log File:** The Klippy log file (/tmp/klippy.log) contains debugging information. 

​	M112 command in the OctoPrint terminal window immediately after the undesirable event 

There is a logextract.py script that may be useful when analyzing a micro-controller shutdown or similar problem. 

​	mkdir work_directory

​	cd work_directory

​	cp /tmp/klippy.log .

​	~/klipper/scripts/logextract.py ./klippy.log

The script will extract the printer config file and MCU shutdown information to work_directory.
