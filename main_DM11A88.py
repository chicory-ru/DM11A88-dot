from pyb import SPI,Pin,Timer
"""
DM11A88 8x8
pyboard: X8 - DI
         X6 - CLK
         X5 - LAT
"""
def update(reg1, reg2):
    global x5
    x5.low()
    spi.send(reg1)
    spi.send(reg2)
    x5.high()

spi = SPI(1, SPI.MASTER, baudrate=30000, polarity=0, phase=0, bits=8)
x5 = Pin('X5', Pin.OUT_PP)
tim = Timer(4, freq=1)
bits = (0,1,2,4,8,16,32,64,128)
reg1, reg2 = 0, 0

imgLOVE = (22,23,26,27,31,34,35,38,41,48,52,57,63,66,74,75)
img0 = (24,25,33,36,43,46,53,56,63,66,74,75)
img1 = (25,34,35,45,55,65,75)
img2 = (24,25,33,36,46,55,64,73,74,75,76)
img3 = (24,25,33,36,45,56,63,66,74,75)
img4 = (23,26,33,36,43,44,45,46,56,66,76)
img5 = (23,24,25,26,33,44,45,56,63,66,74,75)
img6 = (25,34,43,44,45,53,56,63,66,74,75)
img7 = (23,24,25,26,36,45,55,65,75)
img8 = (24,25,33,36,44,45,53,56,63,66,74,75)
img9 = (24,25,33,36,44,45,46,56,65,74)

animation = (img9,img8,img7,img6,img5,img4,img3,img2,img1,img0,imgLOVE)

for ani in animation:
    while tim.counter() < 18000:
        if ani == imgLOVE:
            tim.counter(0)
        for i in ani:
            reg1 = bits[-(i//10)]
            reg2 = bits[(i%10)]
            update(~reg1, reg2)
    tim.counter(0)
update(0,0)
