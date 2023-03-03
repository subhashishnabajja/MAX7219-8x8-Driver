import spidev
from time import sleep 



spi = spidev.SpiDev()

spi.open(0, 0)

spi.max_speed_hz = 1600

spi.xfer([0x0c, 0x01])
spi.xfer([0x0f, 0x00])
spi.xfer([0x09, 0x00])
spi.xfer([0x0b, 0x07])

spi.xfer([0x01, 0b01010101])

sleep(1)

spi.close()