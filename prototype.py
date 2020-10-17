import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        existing = self._objects.get(name)
        clone_obj = copy.deepcopy(existing)
        clone_obj.__dict__.update(attr)
        return clone_obj


class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return f'{self.name} | {self.color} | {self.options}'


c = Car()
print(c)
prototype = Prototype()
prototype.register_object('car', c)

another_c = prototype.clone('car', **dict(color="Green"))
print(another_c)
