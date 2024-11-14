class Scooter:
    next_serial = 1

    def __init__(self, station):
        self.station = station
        self.user = None
        self.serial = Scooter.next_serial
        Scooter.next_serial += 1
        self.charge = 100
        self.isBroken = False

    def rent(self, user):
        if (self.charge > 20 and self.isBroken == False):
            self.user = user
            self.station = None
        elif self.charge < 20:
            raise Exception("Scooter needs to charge")
        elif self.isBroken:
            raise Exception("Scooter needs repair")
        

  

    def dock(self, station):
        self.station = station
        self.user = None


