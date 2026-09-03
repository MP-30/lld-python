from abc import ABC
class Transport(ABC):

    def deliver(self):
        ...

class Truck(Transport):
    def deliver(self):
        return "Delivering by land in a box"
class Ship(Transport):
    def deliver(self):
        return "Delivering by see in a container"

class Airplane(Transport):
    def deliver(self):
        return "Delivering by air in a package"
