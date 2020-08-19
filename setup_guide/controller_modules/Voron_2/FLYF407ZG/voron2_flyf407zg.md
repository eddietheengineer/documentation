# Controller Module - Voron 2 - FLYF407ZG

Reference: [FLYF407ZG Documentation](https://github.com/FLYmaker/FLYF407ZG)

This module details how to configure and wire your FLYF407ZG board for a Voron 2.4 printer.

## Jumper Configuration (TMC 2209 Drivers)

Under each stepper driver, set two jumpers as shown on the following picture ([source](https://github.com/FLYmaker/FLYF407ZG/issues/2)):

![flyf407zg_uart_jumpers](../../../images/voron2_flyf407zg_uart_jumpers.png?raw=true)

Remove all other jumpers on the board.

## Wiring

![voron2_flyf407zg_mcu_1](../../../images/voron2_flyf407zg_mcu_1.png?raw=true)

![voron2_flyf407zg_mcu_2](../../../images/voron2_flyf407zg_mcu_2.png?raw=true)

## Klipper Firmware Compilation

After you've installed Klipper, we need to
compile firmware.

Run `make menuconfig` and select options as shown on the following picture:

![flyf407zg_klipper_menuconfig](../../../images/flyf407zg_klipper_menuconfig.png?raw=true)

Run `make`.

Copy `out/klipper.bin` file to MicroSD card. Rename it to `firmware.bin`.

Insert the SD-card into SD-slot on the board. Power off the board, wait 10 seconds, power on and wait 30 seconds.

Pull out SD-card and check files. If you see file `FLY.CUR` the firmware is flashed successfully.

## Klipper Configuration File

[klipper.cfg](klipper.cfg)
