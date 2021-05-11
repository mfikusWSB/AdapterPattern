class CantFit(Exception):
    pass

class WrongAdapter(Exception):
    pass



class Socket():

    def voltage(self):
        return 230

    def plug(self):
        return "europlug"

    def live(self):
        return 1
    
    def neutral(self):
        return -1

class Adapter():
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

        if self.__socket.plug() != "europlug":
            raise CantFit("Can't fit adapter into socket!")
        
        if self.__socket.voltage() > 240:
            raise WrongAdapter("wrong adapter!")
            

    def voltage(self):
        return 120

    def plug(self):
        return "usaplug"


class Microwave():
    __plug = "usaplug"
    __input_voltage = 120
    __power = None
    def __init__(self, power):
        self.__power = power

    def cook(self):
        if self.__power.plug() != self.__plug:
            print("It wont fit!")
        elif self.__power.voltage() > self.__input_voltage:
            print("Oh no! It exploded!")
        else:
            print("cookin' food")

socket = Socket()
adapter = Adapter(socket)
device = Microwave(adapter)

device.cook()

