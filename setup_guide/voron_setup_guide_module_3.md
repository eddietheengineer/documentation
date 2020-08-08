**Voron Design Setup Guide**

**Module 3**

**Klipper/Firmware Configuration**

 





Introduction/Notes	1

Definitions	1

Klipper Installation	2

Installing Klipper on your MCU Boards	2

Configuring Octoprint to use Klipper	2

Setting up Voron Printer Configuration FIle	3

Common Klipper Errors	4

Klipper Troubleshooting	5

Klipper Configuration Checks	6

Endstop Check	6

Stepper Motor Check	6

XY Homing Check	6

Define (0,0) Point	7

Z Endstop Pin Location Definition	8

Probe Check	8

Probe Accuracy	8

Quad Gantry Leveling (or Z Tilt)	8

PID Tune Heated Bed	9

PID Tune Hotend	9

Running Quad Gantry Level with Hot Chamber	9

Z Offset Adjustment	9

Extruder Calibration	10

Fine Tuning Z Height	10

Slicer Setup and First Print	11

Cura Installation	11

First Print	11

Appendix	12

Appendix 1 - Notepad++ Configuration Editing (Windows)	12

Appendix 2 - bbEdit Configuration Editing (macOS)	12

Appendix 3 - Recommended Octoprint Plugins	13

Appendix 5 - Other Accessories	13

Appendix 6 - Contributors	13

**Introduction/Notes**

Welcome to the latest version of the Voron/Klipper setup documentation! This version is very similar to previous editions, but the wording has been modified to be more generic to different controller boards. Now that the BigTreeTech SKR 1.4 board is used in addition to the SKR 1.3 (and it’s possible in the future other boards will be added as alternates) it makes sense to separate out the specific controller wiring/configurations into separate modules. 



**Any time you see the word “MCU”, you can replace it with your preferred controller (SKR 1.3, SKR 1.4, etc).** 



Also, the previous SKR guide has been split in to two parts. 



**Definitions**

Raspberry Pi - Main “brains” of your printer, does all the calculations

MCU - The controller board (SKR 1.3/SKR 1.4/etc) - receives commands from the Raspberry Pi and 		executes them

Stepper Driver - Takes step and direction commands from the MCU and sends current to the stepper motor to move it



**Klipper Installation**

References: [Klipper Installation Instructions](https://github.com/KevinOConnor/klipper/blob/master/docs/Installation.md) [SKR Installation Instructions](https://3dprintbeginner.com/install-klipper-on-skr-1-3-speed-up-your-prints/)



**Installing Klipper on your MCU Boards**

- Install OctoPi on your Raspberry Pi (guide here: https://octoprint.org/download/)
- Once it is installed, ssh in to your Raspberry Pi using [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/) on Windows or the Terminal on macOS

​	

​	ssh pi@octopi OR ssh [pi@192.168.1.X](mailto:pi@192.168.1.X) (Or whatever ip address your Raspberry Pi has)



- Enter password, the default one is “raspberry”. It is recommended to change this for security using

​	sudo raspi-config 

​	Change the password via “Change User Password”



- Once you are at the command line of the Raspberry Pi, run the following commands:

​	git clone https://github.com/KevinOConnor/klipper

​	./klipper/scripts/install-octopi.sh



- When the install script has completed, run the following commands:

​	cd ~/klipper/

​	make menuconfig



**In this menu structure, you’ll want to pick a few things based on your MCU type. Please follow the steps listed in the Module 2 that applies to your control board.**



- Turn on your power supply to power up your SKR 1.3 boards



**Important:** If you do not power your SKR with 12-24V, Klipper will be unable to communicate with the TMC drivers via UART and it will automatically shut down.



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

- Download the respective Voron configuration file from the following link (or attached with this file):



​	https://github.com/VoronDesign/VoronUsers/tree/master/firmware_configurations/klipper/eddie



- Using WinSCP, Cyberduck, Notepad++ NppFTP, or BBEdit, transfer the downloaded file to your raspberry pi in the following folder:

​	~/klipper/config/ 



- Run the following command to copy the Voron configuration into your printer config:

​	cp ~/klipper/config/FILENAME_OF_VORON_CONFIG.cfg ~/printer.cfg



**Note:** There are many ways of editing your config file. Using the built-in Nano editor through SSH is simple, but it is not user friendly. Notepad++ with the NppFTP plugin (Windows) or bbEdit (MacOS) are better alternatives. Instructions on how to use them are in the appendix. 



- Review the configuration file by typing:

​	nano ~/printer.cfg



You’ll notice that near the top of the file, there are two sections titled [mcu] and [mcu z]. These sections are where we define that we will be using the SKR 1.3 controllers, and identifying the controllers so that Klipper knows which components are connected to what controller. First of all, we need to identify what the Raspberry Pi calls each of the controllers so we can correctly list them in the configuration.



- Take the USB cable from the SKR 1.3 with the X, Y, and E steppers connected to it and plug this in to one of the USB ports on your Raspberry Pi, then run the following command:

​	ls -l /dev/serial/by-path/



You should see something similar to this: 

- Copy the corresponding text from your terminal window **platform-3f980000.usb-usb-0:1.5:1.0** and paste it in a text file temporarily. 



- Open your configuration file (nano ~/printer.cfg) and navigate to the [mcu] section. After the text “serial: /dev/serial/by-path/” paste your SKR path so that the line becomes:



​	serial: /dev/serial/by-path/platform-3f980000.usb-usb-0:1.5:1.0



- Exit the text editor using CNTL-X, and save when asked.



- Take the USB cable from the SKR 1.3 with the Z steppers connected to it and plug this in to another USB port on your Raspberry Pi. \



- Rerun the command “ls -l /dev/serial/by-path/” and note that there are two devices listed, one with a different path than your previous SKR 1.3. Copy this text and save it.



- Open your configuration file and add in your copied text under [mcu z] so it looks something like:

​	serial: /dev/serial/by-path/platform-3f980000.usb-usb-0:1.4:1.0



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



**Klipper Configuration Checks**

The moment you’ve been waiting for—your printer finally coming to life! Klipper has a very helpful configuration check guide that will help make sure that everything is operating properly. Please follow the steps detailed at the URL below:



https://github.com/KevinOConnor/klipper/blob/master/docs/Config_checks.md



**Endstop Check**

Make sure that none of the X, Y, or Z Endstops are being pressed, and then send a 	QUERY_ENDSTOPS command via the Octoprint command line. The terminal window should respond with the following:



Send: QUERY_ENDSTOPS

Recv: x:open y:open z:open



If any of them say “triggered” instead of “open”, double check to make sure none of them are pressed. Next, manually press the X endstop, send the QUERY_ENDSTOPS command again, and make sure that the X endstop says “triggered” and the Y and Z endstops stay open. Repeat with the Y and Z endstops. 



You may find that one of your Endstops has inverted logic (it displays “open” when it is pressed, and “triggered” when it is not). In this case, go to your printer’s config file and add or remove the ! In front of the pin. For instance, if your X endstop was inverted, you would add a ! In front of your pin number as follows:



endstop_pin: P1.28 —> !P1.28



**Stepper Motor Check**

To verify that each stepper motor is operating correctly, send the following command:

​	STEPPER_BUZZ STEPPER=stepper_x

Run this again for each of the motors (stepper_y, stepper_z, stepper_z1, stepper_z2, and stepper_z3). Z motors should go UP first then down. If the stepper motors do not move, check wiring for loose connectors.



**XY Homing Check**

It’s time to start by homing X and Y! You’ll want to be able to quickly stop your printer in case something goes wrong (ie, the tool head goes in the wrong direction). There are a few ways of doing this—one is to use the E-stop button on your display (if you have one installed). Test the button and see what happens—Klipper should shut down, but the Raspberry Pi and Octoprint will still be running, but disconnected from Klipper. Press “Connect” in the upper left corner of Klipper, and then in the Octoprint terminal window send a FIRMWARE_RESTART command to get your printer back up and running. 



The alternative to this is to have your laptop right next to the printer with “restart” already in the terminal command line in Octoprint. When you start homing your printer, if it goes in the wrong direction—quickly send the restart command and it will stop the printer. 



The final “nuclear” option is to power off the entire printer if something goes wrong. This is not ideal because doing this may corrupt the files on the SD card and you would have to reinstall everything from scratch. 



Now that you know how to stop the printer if something goes wrong, send a G28 X Y command to your printer. This will only home X and Y, not Z. The tool head should move to the right until it hits the X endstop, and then move to the back of the printer until it hits the Y endstop. In a CoreXY configuration, each motor has to move in order to get the toolhead to go in only an X or Y direction (think of an Etch a Sketch). 



If the toolhead does not go in the correct direction, refer to the table below to figure out how to correct it. If you need to invert one of the motors, invert the direction pin (put a ! before the pin). If the motors are going in the directions that match the lower row, swap your X and Y connectors.



[stepper x] => Motor B

[stepper y] => Motor A 

**Define (0,0) Point**

Home XY

Move the nozzle to the front left corner of the bed. If you can’t reach it, move the bed on the extrusions, but make sure whatever bed position you end up with you can still reach the Z switch. Once you can get the nozzle close to the front left corner of the bed, send an M114 command. If X and Y are not ~0-5mm, update “position_max” and “position_endstop” for both [stepper_x] and [stepper_y]:

​	For X: New = Current – Get Position X Result

​	For Y: New = Current – Get Position Y Result

If you update anything in your configuration file, save the file and then restart Klipper using FIRMWARE_RESTART.



**Z Endstop Pin Location Definition**

Run another G28 X Y

Move the nozzle using Octoprint until it is directly above the Z Endstop switch. Send an M114 command and record the X and Y values. Update your homing routine (homing_override] or [safe_z_home] with these values, then restart Klipper. Run a full G28 and make sure that the printer properly homes X, Y, and Z. If your toolhead is not over the center of the bed at the end of G28, check the printer config file and uncomment the section in [homing_override] that lists your bed size.



**Probe Check**

With the probe in the center of the bed, reconfirm that the probe is working correctly. When it is far from the bed, QUERY_PROBE should return “open”. When a metal object is close to the probe, QUERY_PROBE should return “triggered”. Slowly reduce your Z height and run QUERY_PROBE each time until QUERY_PROBE returns “triggered”—make sure the nozzle is not touching the print surface (and has clearance). If the signal is inverted, add a “!” In front of the pin definition (ie, pin: !z:P1.24). 



**Probe Accuracy**

With the bed and hotend cold (for now), move the probe to the center of the bed and run PROBE_ACCURACY. It will probe the bed 10 times in a row, and output a standard deviation value at the end. Make sure that the sensed distance is not trending (gradually decreasing or increasing over the 10 probes) and that the standard deviation is less than 0.003mm. 



Example of unstable PROBE_ACCURACY (trending downward during warm up). 



Send: PROBE_ACCURACY

Recv: // PROBE_ACCURACY at X:125.000 Y:125.000 Z:7.173 (samples=10 retract=2.000 speed=2.0

Send: M105

Recv: // probe at 125.000,125.000 is z=4.975000

Recv: // probe at 125.000,125.000 is z=4.960000

Recv: // probe at 125.000,125.000 is z=4.955000

Recv: // probe at 125.000,125.000 is z=4.952500

Recv: // probe at 125.000,125.000 is z=4.950000

Recv: // probe at 125.000,125.000 is z=4.947500

Recv: // probe at 125.000,125.000 is z=4.942500

Recv: // probe at 125.000,125.000 is z=4.937500

Recv: // probe at 125.000,125.000 is z=4.937500

Recv: // probe at 125.000,125.000 is z=4.932500

Recv: // probe accuracy results: maximum 4.975000, minimum 4.932500, range 0.042500, average 4.949000, median 4.948750, standard deviation 0.011948



**Quad Gantry Leveling (or Z Tilt)**

Run Quad_Gantry_Level or Z_Tilt (V2.2 or V1.6). If the script errors out due to an “out of bounds” error, disable your stepper motors and slowly move your gantry or bed by hand until it is approximately flat. Re home your printer (G28) and then rerun the sequence. You may have to run it more than once—make sure that the adjustment value for each stepper motor converges to 0. If it diverges, check to make sure you have your stepper motors wired to the correct stepper driver (check documentation). 







**PID Tune Heated Bed**

Move nozzle to the center of the bed and approximately 5-10mm above the bed surface, then run:



PID_CALIBRATE HEATER=heater_bed TARGET=100



It will perform a PID calibration routine that will last about 10 minutes. Once it is finished, type SAVE_CONFIG which will save the parameters into your configuration file.



**PID Tune Hotend**

Set the part cooling fans to 25% (M106 S64) and then run:



PID_CALIBRATE HEATER=extruder TARGET=245



It will perform a PID calibration routine that will last about 5 minutes. Once it is finished, type SAVE_CONFIG which will save the parameters into your configuration file.



**Running Quad Gantry Level with Hot Chamber**

Run a G28 command to home the printer since SAVE_CONFIG restarts your printer. 



**Important**: This will be the first time that you have run a Quad Gantry Leveling at a high chamber temperature. To make sure that your probe has stabilized with the heated bed at 100C and the extruder at 240C, run PROBE_ACCURACY with the nozzle in the center of the bed. If the values are trending (increasing or decreasing) throughout the 10 probes, or the standard deviation is greater than 0.003mm, wait another 5 minutes and try again. Once the readings are stable, run QUAD_GANTRY_LEVEL. Make a note of how long it took for your probe readings to stabilize and remember this for the next time you start your print—you’ll typically want to wait 10-20 minutes from a cold printer to your first print to make sure temperatures stabilize.



**Z Offset Adjustment**

If you did not run PID tuning, set your extruder to 245C and heated bed to 100C and let the printer heat up for 15 minutes.



Run a G28, and then a Quad_Gantry_Level, and then another G28.

Move the nozzle to the center of the bed



Run Z_ENDSTOP_CALIBRATE



Slowly move the nozzle toward the bed by using

​	TESTZ Z=-1

Until the nozzle is relatively close to the bed, and then stepping down with 

​	TESTZ Z=-0.1

Until the nozzle touches a piece of paper on top of the build plate. If you go far down, you can move the nozzle back up with:

​	TESTZ Z=0.1

Once you are satisfied with the nozzle height, type “ACCEPT” and then “SAVE_CONFIG”. 



If you get an error (out of bounds), send Z_ENDSTOP_CALIBRATE, ACCEPT, and then SAVE_CONFIG. This will redefine the 0 bed height so you will be able to get closer. However, if you get this error it likely means that the shaft for your Z Endstop is too long, and may catch on the print head during a print. It is best to cut the shaft so that it is flush with the top surface of your PEI.



**Extruder Calibration**

Before your first print, you need to make sure that your extruder extrudes the correct amount of material. With the hotend at temperature, make a mark between your roll of filament and your extruder, 120mm away from the entrance to your extruder. In Octoprint, extrude 50mm 2 times (for a total of 100mm—Klipper doesn’t allow you to extrude more than 50mm at a time), then measure from the entrance of your extruder to the mark you made previously. In a perfect world, it would measure 20mm (120mm - 20mm = 100mm), but it usually won’t be. Take the value you have in your configuration file and update it using the following:



New Config Value = Old Config Value * (Actual Extruded Amount/Target Extruded Amount)



Note that a higher configuration value means that less filament is being extruded.



Paste the new value into your configuration file, restart Klipper, and try again. Once your extrusion amount is within 0.5% of the target value (ie, 99.5-100.5mm for a target 100mm of extruded filament), your extruder is calibrated!



**Fine Tuning Z Height**

As a reference, if you adjust the Z offset during a print using the Tune menu on your display, you can update your printer configuration with this new value. Remember that higher values for your Z_endstop_position mean that the nozzle will be closer to the bed. 



New Position = Old Position - Tune Adjustment

New Position = Old Position - (-0.050) = Old Position + 0.050



**Slicer Setup and First Print**

**Cura Installation**

For your first print, use the latest version of Cura, but do not open it at first. Download the latest Voron Cura setup files pinned in #slicers_and_print_help, and then extract the zip folder into C:\Program Files\Ultimaker Cura X.X\resources.



Once that is complete, open Cura and under “non-networked printer” find the Voron tab and select the size of your printer. All the settings should be pre-populated for you.



**First Print**

Download the “voron_design_cube_v6.stl” from the Voron Github page (Voron-2/STLs/TEST_PRINTS), and open the file in Cura. Use the default slicer settings, but make sure the hotend temperature and bed temperature is correct for the filament you are using. A good starting point is 240C hotend temperature, 100C heated bed temperature, and 92% flow for ABS. 



Slice the file and save the .gcode file to your desktop (if you haven’t set up the Octoprint Plugin). Navigate to Octoprint in your web browser, and upload the file to Octoprint. Press “Print” and closely watch the beginning of the print. If your nozzle is too far or close to the bed, on your printer display press the knob, navigate to “Tune”, and adjust the Z offset distance (+ is further from the bed, - is closer). 



Once you are printing (with your printer fully assembled), take a quick video, upload it to the Voron subreddit and eat a well deserved bowl of cereal!



 

​	

**Appendix**

**Appendix 1 - Notepad++ Configuration Editing (Windows)**

1.  Install Notepad++ from: https://notepad-plus-plus.org
2.  Under the “Plugins” tab, select “Plugins Admin”
3.  Search for “NppFTP”, select the check box, and click “Install” 
4.  Restart Notepad++ if necessary
5.  On the right, there will be a new section. Click the gear icon and select “Profile Settings” 
6.  In the bottom left, select “Add New” and name the profile as you wish
7.  In the Hostname dialog, enter the IP address of your Raspberry Pi
8.  In Connection Type, select SFTP
9.  Port: 22 

\10. Username: pi

\11. Password: *** (default is raspberry)

\12. Close the dialog box, select the blue symbol, and select the name of the profile you created 

\13.  Notepad++ will connect to your Raspberry Pi and display the file structure

\14.  Navigate to /home/pi and open printer.cfg

\15.  Make any applicable edits and then save the file



Remember to restart klipper from the Octoprint terminal to see your changes take affect!



**Appendix 2 - bbEdit Configuration Editing (macOS)**

1. Install bbEdit. The free version works great! https://www.barebones.com/products/bbedit/
2. Under File, select Open from FTP/SFTP Server…”  

\3.  Under Server, type in your Raspberry Pi’s IP address (will be different)

\4.  Select SFTP

\5.  Enter “pi” as the user

\6.  Enter your password, it will be “raspberry” unless you changed it.

\7.  Select Continue



\8.  Find “printer.cfg” in the file browser and double click to open the file

\9.  Make any necessary edits and save the file



Remember to restart klipper from the Octoprint terminal to see your changes take affect! 



**Appendix 3 - Recommended Octoprint Plugins**

- ​	OctoKlipper
- ​	Themeify
- ​	TerminalCommands
- ​	Bed Level Visualizer
- ​	Print Time Genius



**Appendix 5 - Other Accessories**

To add LED lights inside the enclosure, wire up the (+) side of the LEDs to a power supply that matches the LED rated voltage, and the (-) side of the LEDs to one of the H-Bed (Heated Bed) connectors on either MCU. Define this output in your klipper configuration file and install an Octoprint plugin to control these LEDs. 



**Appendix 6 - Contributors**

- eddie V2.058
- chron V2.226
- Iakabos V2.067
- fermion V2.202
- Timmitt V2.003
- insurgus V2.278
- Defib V2.213
- newb
- mjoaris

