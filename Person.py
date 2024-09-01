import input_utility

class Person:
    def __init__(self, id_number, name, age):
        self._id_number = id_number
        self._name = name
        self._age = age
    
    @staticmethod
    def createPerson():
        while True:
            try:
                id_number = input_utility.validateNumber(input("ID: "), "id")
                name = input("Name: ")
                age = input_utility.validateNumber(input("Age: "), "age")
                return Person(id_number, name, age)
            except ValueError:
                continue

    def getID(self):
        return self._id_number
    
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def setID(self, id_number):
        self._id_number = id_number

    def setName(self, name):
        self._name = name
    
    def setAge(self, age):
        self._age = age

    def getPersonString(self):
        return "ID: " + str(self.getID()) + ", Name: " + self.getName() + " , Age: " + str(self.getAge())
    
    def printMyself(self):
       print(self.getPersonString())


########################################## TESTS #################################################
 # __main__ = You are running Person.py (The class file definition), else You are running Person as a moudule
if __name__ == "__main__":
    test_id = 105    
    test_name = "test_name"
    test_age = 80
    person = Person(test_id, test_name, test_age)
    if person.getID() != test_id:
        print("Error: ID should be " + str(test_id) + " but i got " + str(person.getID()))
    if person.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but i got " + str(person.getAge()))
    if person.getName() != test_name:
        print("Error: Name should be " + test_name + " but i got " + person.getName())
