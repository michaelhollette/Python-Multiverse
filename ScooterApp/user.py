class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age
        self.loggedIn = False

    def login(self, password):
        try:
            if password == self.password:
                self.loggedIn = True
            else:
                raise Exception("Incorrect password")
        except Exception as e:
            print (e)
    
    def logout(self):
        self.loggedIn = False