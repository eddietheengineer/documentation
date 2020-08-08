**SKR 1.3 Board Configuration**

**Jumper Configuration**

For both SKR 1.3 boards with TMC 2208 or TMC 2209 drivers:

- Remove the four jumpers from below the drivers on all boards
- Put single jumper for each driver's UART connection
- Remove all jumpers from end stop pins, otherwise end stops will not work properly
- Make sure power jumper is between INT and +5V (should be default from factory). If this is not installed correctly you may have power issues with your Raspberry Pi which can cause throttling. 

**Stepper Driver Installation**

- **Warning!** Always be sure to orient drivers correctly when installing. If you plug the drivers in backwards, they may permanently be damaged. Enable (EN) and Direction (DIR) pins should both be on the side closest to the microcontroller and the side OPPOSITE the plug that the stepper motor connects to. Another way of orienting the drivers is to make sure the red plastic shown below should align with the red pins on your SKR board. The orientation shown below on the left is correct for TMC 2209 drivers relative to the image above.
- Place included heatsink on top of stepper driver copper pad and provide adequate cooling during operation or you may experience layer shifts or other undesirable behaviors. This is even more important with TMC 2208s as they have higher RDSon and generate more heat for the same stepper motor current.
- **Note:** if you do not have BigTreeTech TMC2209s, the pinout is different. See link [here](https://www.anet3d-forum.de/viewtopic.php?f=82&t=4776)  

**Wire Terminals**

One key difference between RAMPS 1.4 boards and the SKR 1.3 is that RAMPS boards use Dupont terminals, but SKR 1.3 boards use JST-XH terminals. This will mean that you will need to purchase a JST-XH connector kit with 2 pin (thermistor and fan), 3 pin (endstop), and 4 pin (stepper motor) connectors. Unlike Dupont connectors, JST-XH terminals are keyed and will only fit in one orientation so pay close attention while crimping to make sure you do not make a mistake. 



For wiring the stepper motors, keep the same wire color sequence that your stepper motors came with and make sure you use the same sequence for all of your stepper motors. If you have the spec motors from StepperOnline, the wires should in the the color order shown in the SKR 1.3 wiring diagrams on the following pages.



**Important:** If you find out your motors are going the wrong way once you start up your printer for the first time, you do not need to repin your connectors. You can invert the DIR (direction) pins in your configuration by adding or removing ! in front of pin and it will work properly.



**Inductive Probe Wiring**

The PL-08N inductive probe that is used for Z Tilt Adjust (V1) or Quad Gantry Leveling (V2) needs to be powered with 12-24V, not the standard 5V that is used for typical end stop switches. This is critical because if it is powered with 5V its sense distance will be so low that the nozzle will crash in to the build surface.  



The issue with this is that the output signal from the sensor is approximately the same voltage as the sensor is powered with. This means if you power the sensor with 24V, it will send 24V to a pin on the micro that is supposed to never have more than 5V applied to it. This is where the BAT85 diode comes in to play. It is oriented so that when the probe signal wire is HIGH (12-24V), no current will flow to the SKR input pin, so the SKR pin will read HIGH voltage due to the internal pull-up resistor. If the probe signal is LOW (0V), current will flow from the SKR board through the diode, through the Probe to GND, which will pull the SKR pin LOW. Below is a circuit diagram explaining this: 

**Endstop Wiring**

There are two ways of wiring your endstops, one is NC (normally closed) and the other is NO (normally open). For normally closed configurations, the endstop switch allows current to flow through it when it is not triggered. For normally open configurations, the end stop switch only allows current to flow through it when it is triggered. 



While both of these configurations will work fine in an ideal world, NC configurations are more robust because if a wire breaks or a terminal becomes disconnected, the printer will think that the end stop has triggered and the printer will stop movement before the toolhead crashes in to the frame or the bed. 



Wiring mechanical end stop switches for NC operation is easy, as they generally have three pins exposed. With a multimeter, probe each combination of the three pins until you find a pair that has continuity (0 ohm resistance) when the switch is not triggered, but does not have continuity (infinite resistance) when the switch is triggered. The outer two pins are often the NC pins, but verify prior to installation.



For the inductive probe, you will need to make sure that you purchase a NC probe, not a NO probe. You cannot change the configuration of the probe—it comes fixed from the factory in a specific configuration. If you happen to receive a NO probe it will still work but you may risk crashing the nozzle in to the bed if a wire breaks. 



**MCU 1 Wiring (X, Y, E, Hot End)**

- Place stepper drivers for X, Y, and E in positions X, Y, and E0
- Plug in stepper motors for X, Y, and E in positions X, Y, and E0
- Plug Hot End thermistor to thermistor TH0 (P0.24)
- Plug Hot End heater in to HE0 (P2.7)
- Plug Hot End Fan in to HE1 (P2.4)
- Plug Part Cooling Fan in to Fan (P2.3)
- Connect X end stop to +X connector (P1.28)
- Connect Y end stop to +Y connector (P1.26)
- Wire 24V and 0V from DC power supply to Power In
- Connect USB Cable to your SKR 1.3, but do not connect it yet to your Raspberry Pi 

Note: Do not follow jumper positions shown in this image, refer to Page 2**MCU Z Wiring (Z, Bed, Exhaust Fan)**

- Place stepper drivers for Z0, Z1, Z2, and Z3 into positions X, Y, Z, and E0
- Plug in stepper motors for Z0, Z1, Z2, and Z3 into positions X, Y, Z, and E0
- Plug Bed Heater Temp in to TB (P0.23)
- Plug in Exhaust Fan in to HE0 (P2.7)
- Plug in Controller Fan in to HE1 (P2.4)
- Plug SSR Control for Heated Bed in to Fan (P2.3)
- Plug Z Endstop Switch into -Z (P1.25)
- Plug Probe GND and Signal (with BAT85 diode) in to +Z (P1.24
- Plug display wires in to EXP1 and EXP2
- Wire 24V and 0V from DC power supply to Power In
- Connect USB Cable to your SKR 1.3, but do not connect it yet to your Raspberry Pi 

Note: Do not follow jumper positions shown in this image—refer to Page 2