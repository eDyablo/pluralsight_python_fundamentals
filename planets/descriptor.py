from weakref import WeakKeyDictionary


class Positive:
    def __init__(self):
        self._instance_data = WeakKeyDictionary()

    def __get__(self, instance, _):
        if instance is None:
            return self
        return self._instance_data[instance]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Value {} is not positive".format(value))
        self._instance_data[instance] = value

    def __delete__(self, _):
        raise AttributeError("Cannot delete attribute")
