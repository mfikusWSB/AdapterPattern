#VERY simple decorator pattern example

class UndecoratedObject:
    def __init__(self, string):
        self.str = string

    def get_string(self):
        return self.str


class DecoratedObject:
    def __init__(self, obj):
        self.undecorated_object = obj

    def get_string(self):
        return self.undecorated_object.get_string().replace("undecorated", "decorated")


undecorated = UndecoratedObject("Hello, I am undecorated object!")
print(undecorated.get_string())

decorated = DecoratedObject(undecorated)
print(decorated.get_string())
