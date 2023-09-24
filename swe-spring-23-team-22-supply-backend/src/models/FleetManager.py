import sys
sys.path.insert(0, '/home/team22/repos/supply-backend/src')

class FleetManager:
    def __init__(self, _id, email, username, password, fName, lName):
        self._id = _id
        self.email = email
        self.username = username
        self.password = password
        self.fName = fName
        self.lName = lName

    ##### SETTERS #####

    def setId(self, _id):
        self._id = _id

    def setEmail(self, email):
        self.email = email

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def setFName(self, fName):
        self.fName = fName

    def setLName(self, lName):
        self.lName = lName

    ##### GETTERS #####

    def getId(self):
        return self._id

    def getEmail(self):
        return self.email

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getFName(self):
        return self.fName

    def getLName(self):
        return self.lName

    def __str__(self):
        return f"Fleet Manager ID: {self._id}\nEmail: {self.email}\nUsername: {self.username}\nPassword: {self.password}\nFirst Name: {self.fName}\nLast Name: {self.lName}"