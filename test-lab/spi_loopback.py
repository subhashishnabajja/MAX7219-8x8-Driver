import spidev
import time

spi = spidev.SpiDev()
# spidev_test.c uses /dev/spidev1.1
spi.open(0,0) #use spi Port 1, device (CS) 1

while True:
    try:
        response = spi.xfer2([0x0F, 0x01])
        print(response)
        time.sleep(1)
    except KeyboardInterrupt:
        spi.close()