from entities.smartphone import Smartphone
from entities.plane import Plane

def main():
    # Creating an instance of Smartphone
    smartphone = Smartphone("Apple", "iPhone 14", "20 hours")
    print(smartphone.get_specs())
    smartphone.make_call("123-456-7890")

    # Creating an instance of Plane
    plane = Plane("Boeing", "747")
    print(f"Plane Model: {plane.model}")
    plane.move()

if __name__ == "__main__":
    main()