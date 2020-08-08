# Controller Module - Voron 2 - SKR 1.4

Reference: [BigTreeTech SKR 1.4 Documentation](https://github.com/bigtreetech/BIGTREETECH-SKR-V1.3/tree/master/BTT%20SKR%20V1.4)

This module details how to configure and wire your SKR 1.4 boards for a Voron 2.4 printer.

## Jumper Configuration (TMC 2209 Drivers)

1. On each TMC 2209 driver you will be using, cut the pin off of the driver as shown below. ([Image Source](https://github.com/bigtreetech/BIGTREETECH-SKR-V1.3/blob/master/BTT%20SKR%20V1.4/Hardware/BTT%20SKR%20V1.4%20Instruction%20Manual.pdf))

   ![skr_14_TMC2209_pin_remove](../../images/skr_14_TMC2209_pin_remove.png)

2. Under each stepper driver, remove all jumpers (shown in red) except for a single jumper per driver as shown in green. ([Image Source](https://github.com/bigtreetech/BIGTREETECH-SKR-V1.3/blob/master/BTT%20SKR%20V1.4/Hardware/UART.jpg))

   ![skr_14_UART_jumper](../../images/skr_14_UART_jumper.png)

   

3. Verify that the red jumper near the center of the board is connected between VDD and the center pin. This powers the SKR board off of the 24V power supply.

4. As a final check, review the diagram below:

![skr14_jumper](https://github.com/jdlongenecker/documentation/blob/master/setup_guide/images/skr14_jumper.png?raw=true)





![voron2_skr14_mcu_xye](https://github.com/jdlongenecker/documentation/blob/master/setup_guide/images/voron2_skr14_mcu_xye.png?raw=true)

![voron2_skr14_mcu_z](https://github.com/jdlongenecker/documentation/blob/master/setup_guide/images/voron2_skr14_mcu_z.png?raw=true)

