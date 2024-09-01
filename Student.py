from Person import Person
import input_utility

class Student(Person):
    def __init__(self, id_number, name, age, field_of_study, year_of_study, score_avg):
        super().__init__(id_number, name, age)
        self.field_of_study = field_of_study
        self.year_of_study = year_of_study
        self.score_avg = score_avg
    
    @staticmethod
    def createStudent():
        while True:
            try:
                person = Person.createPerson()
                field_of_study = input("Enter Field Of Study: ")
                year_of_study = input_utility.validateNumber(input("Enter Year Of Study: "), "Year Of Study")
                score_avg = input_utility.validateNumber(input("Enter score average: "), "score average")
                return Student(person.getID(), person.getName(), person.getAge(), field_of_study, year_of_study, score_avg)
            except ValueError:
                    continue
            
    def getFieldOfStudy(self):
        return self.field_of_study
    
    def getYearOfStudy(self):
        return self.year_of_study
    
    def getScoreAvg(self):
        return self.score_avg

    def printStudent(self):
        print(self.getPersonString() + ", The field of study is " + self.getFieldOfStudy() + " , the year of study is " + str(self.getYearOfStudy()) + " and the average is " + str(self.getScoreAvg()))

    def printMyself(self):
        self.printStudent()

########################################## TESTS #################################################

if __name__ == "__main__":
    test_id = 101  
    test_name = "test_name"
    test_age = 80
    test_field_of_study = "Science"
    test_year_of_study = 2
    test_score_avg = 90

    student = Student(test_id, test_name, test_age, test_field_of_study, test_year_of_study, test_score_avg)
    if student.getID() != test_id:
        print("Error: ID should be " + str(test_id) + " but i got " + str(student.getID()))
    if student.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " but i got " + str(student.getAge()))
    if student.getName() != test_name:
        print("Error: Name should be " + test_name + " but i got " + student.getName())
    if student.getFieldOfStudy() != test_field_of_study:
        print("Error: Field Of Study should be " + test_field_of_study + " but i got " + str(student.getFieldOfStudy()))
    if student.getYearOfStudy() != test_year_of_study:
        print("Error: Year Of Study should be " + str(test_year_of_study) + " but i got " + str(student.getYearOfStudy()))
    if student.getScoreAvg() != test_score_avg:
        print("Error: Score Average should be " + str(test_score_avg) + " but i got " + str(student.getScoreAvg()))
