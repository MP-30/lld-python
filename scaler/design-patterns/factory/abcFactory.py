from abc import ABC

class Transportation(ABC):
    def deliver(self):
        raise NotImplementedError("This method should be overridden")
class Packaging(ABC):
    def pack(self):
        raise NotImplementedError

# concrete objects
class Truck(Transportation):
    def deliver(self):
        return "Delivering by land in a box"

class Ship(Transportation):
    def deliver(self):
        return "Delivering by see in a container"

class Airplane(Transportation):
    def deliver(self):
        return "Delivering by air in a package"

class Auto(Transportation):
    def deliver(self):
        return "Delivering by road in a vehicle"

class Box(Packaging):
    def pack(self):
        return "Packing in a box"
class Container(Packaging):
    def pack(self):
        return "Packing in a container"

class LogisticFactoryAbc(ABC):
    @staticmethod
    def create_transportation(type):
        raise NotImplementedError
    @staticmethod
    def create_packaging(type):
        raise NotImplementedError

class RoadFactory(LogisticFactoryAbc):
    @staticmethod
    def create_transportation(type):
        if type == "truck":
            return Truck()
        elif type == "auto":
            return Auto()
        else:
            return None
    @staticmethod
    def create_packaging(type):
        if type == "box":
            return Box()
        else:
            return None

class SeaFactory(LogisticFactoryAbc):
    @staticmethod
    def create_transportation(type):
        if type == "sea":
            return Ship()

        else:
            return None

    @staticmethod
    def create_packaging(type):
        if type == "box":
            return Box()
        else:
            return None

class LogisticProvider:
    @staticmethod
    def getFactory(type):
        if type == "road":
            return RoadFactory()
        elif type == "sea":
            return SeaFactory()
        else:
            raise ValueError

if __name__ == "__main__":
    transport_way = "road"
    factory = LogisticProvider.getFactory(transport_way)
    transport = factory.create_transportation("truck")
    packaging = factory.create_packaging("box")

    print(transport.deliver())
    print(packaging.pack())