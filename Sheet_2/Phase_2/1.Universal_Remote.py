from abc import ABC, abstractmethod

class Remote(ABC):
    @abstractmethod
    def TurnOn(self):
        pass

class Light(Remote):
    def TurnOn(self):
        print("Light Turned On")

class TV(Remote):
    def TurnOn(self):
        print("TV Turned On")

class AC(Remote):
    def TurnOn(self):
        print("AC Turned On")

def main():
    remote1 = Light()
    remote1.TurnOn()

    remote2 = TV()
    remote2.TurnOn()

    remote3 = AC()
    remote3.TurnOn()

main()