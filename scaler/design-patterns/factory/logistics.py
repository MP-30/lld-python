from abc import ABC
class Transport(ABC):

    def deliver(self):
        ...
# concrete objects
class Truck(Transport):
    def deliver(self):
        return "Delivering by land in a box"

class Ship(Transport):
    def deliver(self):
        return "Delivering by see in a container"

class Airplane(Transport):
    def deliver(self):
        return "Delivering by air in a package"

class Auto(Transport):
    def deliver(self):
        return "Delivering by road in a vehicle"

class TransportFactoryAbc(ABC):
    @staticmethod
    def create_trasport(self):
        pass

class TransportFactory(TransportFactoryAbc):
    @staticmethod
    def create_transport(type):
        if type == 'road':
            return Auto()
        elif type == 'sea':
            return Ship()
        elif type == 'air':
            return Airplane()
        return None

if __name__ == "__main__":
    transport_way = "sea"
    transport = TransportFactory.create_transport(transport_way)
    print(transport.deliver())