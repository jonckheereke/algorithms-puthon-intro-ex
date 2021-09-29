class led:
    def __init__(self,pin):
        self.pinNumber = pin
        self.isOn = False
    def on(self):
        self.isOn = True
    def off(self):
        self.isOn = False
    def toggle(self):
        self.isOn = not self.isOn
    def state(self):
        return self.isOn

class binaryCounter:
    def __init__ (self, led0, led1, led2, led3):
        self.led0 = led0
        self.led1 = led1
        self.led2 = led2
        self.led3 = led3
        self.value = 0
    def setValue(self, value):
        self.value = value
        self.value %= 15
        if((self.value % 2) != 0):
            self.led0.on()
        else:
            self.led0.off()
        if ((int(self.value / 2) % 2) != 0):
            self.led1.on()
        else:
            self.led1.off()
        if ((int(self.value / 4) % 2) != 0):
            self.led2.on()
        else:
            self.led2.off()
        if ((int(self.value / 8 % 2) != 0)):
            self.led3.on()
        else:
            self.led3.off()
    def increment(self, value):
        self.value += value
    def decrement(self, value):
        self.value -= value
    def states(self):
        self.setValue(self.value)
        stringToReturn = "LED3 = {}, LED2 = {}, LED1 = {}, LED0 = {}"
        return stringToReturn.format(self.led3.state(), self.led2.state(), self.led1.state(), self.led0.state())

binaryValue = binaryCounter(led(1),led(2),led(3),led(4))
binaryValue.setValue(14)
print(binaryValue.states())
binaryValue.decrement(8) 
print(binaryValue.states())
binaryValue.increment(3)
print(binaryValue.states())