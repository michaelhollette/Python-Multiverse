from scooter import Scooter
from user import User

class ScooterApp:
    def __init__(self):
        self.stations = {
            "Liverpool Street": [],
            "Camden Market": [],
            "Kings Cross Station" : [],
        }
        self.registeredUsers = {}
    
    def registerUser (self, username, password, age):
        try:
            if username not in self.registeredUsers and age >= 18:
                new_user = User(username, password, age)
                self.registeredUsers[username] = new_user
                print(f"{username} has been registered")
                return new_user
            elif age < 18:
                raise Exception(f"{username} is too young to register")
            else:
                raise Exception(f"{username} has already been registered")
        except Exception as e:
            print(str(e))
    
    def loginUser(self, username, password):
        try:
            if username not in self.registeredUsers:
                raise Exception("Username or password is incorrect")
            for key, user_obj in self.registeredUsers.items():
                if username == key:
                        user_obj.login(password)
                        if user_obj.loggedIn == True:
                            print(f"{user_obj.username} has been logged in")
                        else:
                            raise Exception("Username or password is incorrect")
        except Exception as e:
            print(str(e))
        
    def logoutUser(self, username):
        try:
            for key, user_obj in self.registeredUsers.items():
                if username == key and user_obj.loggedIn == True:
                    user_obj.logout()
                    print(f"{user_obj.username} is logged out")
                    return
                elif username == key and user_obj.loggedIn == False:
                    raise Exception(f"{username} is not logged in")
                    
                else:
                    raise Exception(f"user '{username}' does not exist")
        except Exception as e:
            print(str(e))
    
    def createScooter(self, station):
        try:
            if station not in self.stations:
                raise Exception(f"{station} does not exist")
            for stop in self.stations:
                if station == stop:
                    new_scooter = Scooter(station)
                    self.stations[stop].append(new_scooter)
                    print("Created new scooter")
                    return new_scooter
        except Exception as e:
            print(str(e))
    
    def dockScooter(self, scooter, station):
        try:
            if station not in self.stations:
                raise Exception(f"Station '{station}' does not exist")
            for stop, scooter_list in self.stations.items():
                if stop == station:
                    if scooter not in scooter_list:
                        self.stations[stop].append(scooter)
                    else:
                        raise Exception(f"Scooter is already at station {station}")
                    print("Scooter is docked")
        except Exception as e:
            print(str(e))
    
    def rentScooter(self, scooter, user):
        try:
            for stop, scooter_list in self.stations.items():
                if scooter in scooter_list:
                    self.stations[stop].remove(scooter)
                    scooter.user = user
                    print("scooter is rented")
                    return
            raise Exception("Scooter is already rented")
        except Exception as e:
            print(str(e))

    def print(self):
        print("Registered users are:")
        for user in self.registeredUsers:
            print(user)
        for station in self.stations:
            print(f"At {station}, there are {len(self.stations[station])} scooters")


        







                
            

app = ScooterApp()
app.registerUser("michael", "password123", 24)
app.registerUser("marcus", "password123", 14)

app.registerUser("michael", "password123", 24)

print(app.registeredUsers)

app.loginUser("michael", "password123")
app.logoutUser("michael")
app.logoutUser("michael")
app.logoutUser("marcus")

app.createScooter('Liverpool Street')
app.createScooter('Manchester Piccadilly')
print(app.stations)
app.dockScooter(app.createScooter("Camden Market"), "Camden Market")
print(app.stations)

app.dockScooter(app.rentScooter(app.createScooter("Camden Market"), app.registerUser("david","password1234", 26)), "Camden Market")

app.print()