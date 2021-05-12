"""
Singleton basically makes every instance of specific class the same. Any changes made to any insance of a singleton class, will result in changes of every other object which has the same class.
"""

#Defining Metaclass
class CarMeta(type):

    _instances = {}

    #Making the object with same class instance
    def __call__(obj, *args, **kwargs):
        if obj not in obj._instances:
            instance = super().__call__(*args, **kwargs)
            obj._instances[obj] = instance
        return obj._instances[obj]


class CarModelX(metaclass=CarMeta):

    #For example, lets say the car has invalid amount of wheels from the beggining
    _wheels = 3

    def how_many_wheels(self):
        print(self._wheels, " wheels")


if __name__ == "__main__":

    CarOne = CarModelX()
    CarTwo = CarModelX()
    CarThree = CarModelX()

    #Lets check the amount of wheels:
    print("Car one has:")
    CarOne.how_many_wheels()

    print("Car two has:")
    CarTwo.how_many_wheels()

    print("Car three has:")
    CarThree.how_many_wheels()

    print("------------------")

    """
    Because we are using singleton pattern, we don't need to change wheel variable of every single class individually, we can do it with any CarModelX object instance.
    """

    CarOne._wheels = 4

    print("Car one has:")
    CarOne.how_many_wheels()

    print("Car two has:")
    CarTwo.how_many_wheels()

    print("Car three has:")
    CarThree.how_many_wheels()

  
    #We can make sure they contain the same instance by:
    print(id(CarOne), id(CarTwo), id(CarThree))
  


