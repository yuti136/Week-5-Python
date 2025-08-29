class Car:
    def move(self):
        print("Driving on the road")

class Plane:
    def move(self):
        print("Flying in the sky")

class Boat:
    def move(self):
        print("Sailing on the water")

class Animal:
    def move(self):
        print("Walking on the ground")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat(), Animal()]

for v in vehicles:
    v.move()
