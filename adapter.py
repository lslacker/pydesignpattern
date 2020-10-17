class Korean:
    def __init__(self):
        self.name = 'Korean'

    def speak_korean(self):
        return 'an-neyong?'


class British:
    def __init__(self):
        self.name = 'British'


    def speak_english(self):
        return 'Hello!'


class Adapter:

    def __init__(self, obj, **adapted_method):
        self._object = obj

        #add a new dictionary item that established the mapping between the generic method name
        # speak() and the concrete method e.g. speak_english, speak_koren if the mapping say so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)

# list to store speak objects
objects = []

# create a Korean objects
korean = Korean()
# create a British objects
british = British()


objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print(f'{obj.name} says {obj.speak()}')
