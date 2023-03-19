# MAX7219 Sample Drive

This repository contains the code required to drive a max7219 8x8 LED matrix using a Raspberry Pi (with `spidev`). **The code written is extremely rigid and should not be used in any form of production applications**.

## Pypi Link

<a href="https://pypi.org/project/max7219-driver/0.0.1/" target="_blank">PyPi Package Link</a>    

## Installation

    pip install max7219-driver

## Connections

The following are the table lists the connetion

| LED | Physical Pin (Raspberry Pi)  |
|-----|------------------------------|
| VCC| 2 or 4|
| GND| 6|
| DIN| 19|
| CLK| 23|
| CS | 24|


## Driving the led matrix

You can either modiy the `test.py` file, or paste the `max7219` folder into your project directory. 

The following are the methods available.

1. `bootstrap()` - Initialize the matrix to display fonts.
2. `CLEAR_DISPLAY()` - Clears the entire display.
3. `setBitmap(bitMap)` - Display the provided `bitMap`. (Can be used to display special characters or symbols)
4. `show(string, delay = 0)` - Display the given string with a word delay of the `delay`.
5. `close()` - Closes the `spi` connection  
