from typing import ClassVar


class Vehicle:
    def __init__(self, make, model, y, w, nm=False, tsm=0):
        self.Make = make
        self.Model = model
        self.Year = y
        self.Weight = w
        self.NeedsMaintenance = nm
        self.TripsSinceMaintenance = tsm

    # getters
    def getMake(self):
        return self.Make

    def getModel(self):
        return self.Model

    def getYear(self):
        return self.Year

    def getWeight(self):
        return self.Weight

    def getNeedsMaintenance(self):
        return self.NeedsMaintenance

    def getTripsSinceMaintenance(self):
        return self.TripsSinceMaintenance

    # setters
    def setMake(self, xmake):
        self.Make = xmake

    def setModel(self, xmodel):
        self.Model = xmodel

    def setYear(self, year):
        self.Year = year

    def setWeight(self, weight):
        self.Weight = weight

    def setNeedsMaintenance(self, needsmaintenance):
        self.NeedsMaintenance = needsmaintenance

    def setTripsSinceMaintenance(self, tripssincemaintenance):
        self.TripsSinceMaintenance = tripssincemaintenance

    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False


class Cars(Vehicle):
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance, Drive=False):
        Vehicle.__init__(self, Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance, Drive)
        self.Drive = Drive

    def drive(self):
        self.Drive = True

    def stop(self):
        if self.Drive:
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
            self.Drive = False

    # drive and stop car
    def randomly_car(car):
        random = 0
        times = random.randint(1, 101)
        for i in range(times):
            car.drive()
            car.stop()

    # print car attributes
    def printCarSpecs(car):
        print("Make", car.make)
        print("Model", car.model)
        print("Year", car.year)
        print("Weight", car.weight)
        print("Needs Maintenance", car.nm)
        print("Trips Since Maintenance", car.tsm)

    # three cars
    car1 = Vehicle("Toyota", "GR Supra", "2020", "1518")
    car2 = Vehicle("Mercedes-Benz", "G-class", "2020", "2650")
    car3 = Vehicle("Lexus", "ES 350 F Sport", "2019", "1655")

    # randomly driving cars
    randomly_car(car1)
    randomly_car(car2)
    randomly_car(car3)

    # printing cars
    printCarSpecs(car1)
    printCarSpecs(car2)
    printCarSpecs(car3)
