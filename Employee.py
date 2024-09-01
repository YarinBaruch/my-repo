from Person import Person
import input_utility

class Employee(Person):
    def __init__(self, id_number, name, age, field_of_work, salary):
        super().__init__(id_number, name, age)
        self._field_of_work = field_of_work
        self.salary = salary

    @staticmethod
    def createEmployee():
        while True:
            try:
                person = Person.createPerson()
                field_of_work = input("Enter Field Of Work: : ")
                salary = input_utility.validateNumber(input("Enter Salary: "), "salary")
                return Employee(person.getID(), person.getName(), person.getAge(), field_of_work, salary)
            except ValueError:
                    continue
            
    def getFieldOfWork(self):
        return self._field_of_work
    
    def getSalary(self):
        return self.salary

    def printEmployee(self):
        print(self.getPersonString() + ", The field of work is " + self.getFieldOfWork() + " , the salary is " + str(self.getSalary()))

    def printMyself(self):
        self.printEmployee()

########################################## TESTS #################################################

if __name__ == "__main__":
    test_id = 101  
    test_name = "test_name"
    test_age = 80
    test_field_of_work = "Software Developer"
    test_salary = 30000
    
    employee = Employee(test_id, test_name, test_age, test_field_of_work, test_salary)
    if employee.getID() != test_id:
        print("Error: ID should be " + str(test_id) + " but i got " + str(employee.getID()))
    if employee.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but i got " + str(employee.getAge()))
    if employee.getName() != test_name:
        print("Error: Name should be " + test_name + " but i got " + employee.getName())
    if employee.getFieldOfWork() != test_field_of_work:
        print("Error: Field Of Work should be " + test_field_of_work + " but i got " + employee.getFieldOfWork())
    if employee.getSalary() != test_salary:
        print("Error: Salary should be " + str(test_salary) + " but i got " + str(employee.getSalary()))
   