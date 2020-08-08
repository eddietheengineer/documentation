# Slicer Setup and First Print

**Cura Installation**

For your first print, use the latest version of Cura, but do not open it at first. Download the latest Voron Cura setup files pinned in #slicers_and_print_help, and then extract the zip folder into C:\Program Files\Ultimaker Cura X.X\resources.



Once that is complete, open Cura and under “non-networked printer” find the Voron tab and select the size of your printer. All the settings should be pre-populated for you.



**First Print**

Download the “voron_design_cube_v6.stl” from the Voron Github page (Voron-2/STLs/TEST_PRINTS), and open the file in Cura. Use the default slicer settings, but make sure the hotend temperature and bed temperature is correct for the filament you are using. A good starting point is 240C hotend temperature, 100C heated bed temperature, and 92% flow for ABS. 



Slice the file and save the .gcode file to your desktop (if you haven’t set up the Octoprint Plugin). Navigate to Octoprint in your web browser, and upload the file to Octoprint. Press “Print” and closely watch the beginning of the print. If your nozzle is too far or close to the bed, on your printer display press the knob, navigate to “Tune”, and adjust the Z offset distance (+ is further from the bed, - is closer). 



Once you are printing (with your printer fully assembled), take a quick video, upload it to the Voron subreddit and eat a well deserved bowl of cereal!