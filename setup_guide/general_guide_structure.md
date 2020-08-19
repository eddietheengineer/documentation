# General Documentation Structure

Format idea is as follows:



1. Introduction
2. Generic Wiring Information (applies to all boards/printers)
3. Octoprint Installation
4. Klipper Initial Installation (git pull, run install script)
5. Flash Controller with Klipper firmware (unique per controller, same for all printers with same controller)
   1. SKR 1.3
   2. SKR 1.4
   3. SKR mini e3 V1.2
   4. SKR mini e3 V2.0
   5. FYSETC S6?
   6. FLY?
6. Wiring/Config Setup (unique per controller/printer)
   1. Voron 0
      1. mini e3 V1.2
      2. mini e3 V2.0
   2. Voron 1
      1. SKR 1.3
      2. SKR 1.4
      3. FYSETC S6?
   3. Voron 2
      1. RAMPS
      2. SKR 1.3
      3. SKR 1.4
      4. FLY?
   4. Voron Switchwire
      1. mini e3 V1.2
      2. mini e3 V2.0
7. Initial Startup Checks
   1. Endstop Check
   2. Stepper Motor Buzz
   3. XY Homing Check
   4. Define 0,0 point
   5. Z Endstop Pin Definition
   6. Probe Check
   7. Probe Accuracy?
   8. QGL/Z Tilt?
   9. PID Tune Heated Bed/Hotend
   10. Z Offset Adjustment
   11. Extruder Calibration
8. Slicer Setup/First Print
   1. Cura or PS?
   2. Voron Cube STL, settings?
   3. Proper preheat sequence, checks?
   4. What happens if...
      1. Layer Shift
      2. Over Extrusion
      3. Etc
9. Advanced Tuning
   1. Input Shaper
   2. Pressure Advance
   3. ?
10. Appendix
    1. Hall Effect Wiring/Guide
    2. PT100 Wiring/Guide (MAX31865)
    3. PT100 Wiring/Guide (INA826)
    4. ?