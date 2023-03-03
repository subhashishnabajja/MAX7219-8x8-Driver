import spidev
from time import sleep
import max7219.font as font





def toMhz(hz:int):
    return hz * 1000 * 1000

def toByte(array):
    return bin(int("0b" + "".join(str(x) for x in array), 2))

class LedMatrix:

    def __init__(self, open:int, port:int):
        self.spi = spidev.SpiDev()

        self.rows = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]

        # Initiailize spi and open spi
        self.spi.open(open, port)

        # Configure spi
        self.spi.max_speed_hz = toMhz(6)

        

    def bootstrap(self):
        # Go to normal operation mode
        self.SHUTDOWN_REGISTER(0x01)

        # Disable test mode
        self.DISPLAY_TEST_REGISTER()

        # Disable decode mode
        self.DECODE_MODE_REGISTER()

        # Set scan limit 
        self.SCAN_LIMIT_REGISTER(0x01)

        self.CLEAR_DISPLAY()


    def SHUTDOWN_REGISTER(self, mode:int = 0x00):
        self.spi.xfer([0x0f, mode])

    def DISPLAY_TEST_REGISTER(self, mode:int = 0x00):
        self.spi.xfer([0x0f, mode])

    def SCAN_LIMIT_REGISTER(self, range:int = 0x07):
        self.spi.xfer([0x0b, range])

    def DECODE_MODE_REGISTER(self, mode:int = 0x00):
        self.spi.xfer([0x09, mode])

    def CLEAR_DISPLAY(self):
        self.setBitmap([
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            0b00000000,
            ])

    def setBitmap(self, bitMap):
        for i in range(8):
            self.spi.xfer([self.rows[i], bitMap[i]])

    def show(self, string:str, delay:int = 0):
        for char in  string:
            if char == " ":
                self.CLEAR_DISPLAY()
            else:    
                self.setBitmap(font.fonts[char])

            sleep(delay)

    def close(self):

        return self.spi.close()



