import pandas as pd
import os
from Person import Person
from Employee import Employee
from Student import Student
from PersonKind import PersonKind
from input_utility import validateNumber

def mainProgram():
    # flag to exit
    exit_flag = False
    total_ages = 0

    while not exit_flag:
        try:
            printMenu()
            user_choice = validateNumber(input("Please enter your choice: "), "selection")
            
            match user_choice:
                case 1:
                    total_ages += saveNewEntry()
                case 2:
                    searchById()
                case 3:
                    printAgesAverage(total_ages)
                case 4:
                    printAllNames()
                case 5:
                    printAllIds()
                case 6:
                    printAllEntries()
                case 7:
                    printEntryByIndex()
                case 8:
                    saveDataToCSV()
                case 9:
                    yes_no_input = input("Are you sure? (y/n) ")
                    while yes_no_input != "n" and yes_no_input != "y":
                        yes_no_input = input("Are you sure? (y/n) ")
                    if yes_no_input == "n":
                        continue
                    else:
                        exit_flag = True
                        print("Goodbye!")
                case _:
                    if user_choice is not None:
                        print("Error: Option [" + str(user_choice) + "] does not exist. Please try again")
        except ValueError:
            continue
        except KeyboardInterrupt:
            print("Exit the program..")
            exit_flag = True

# Print Menu
def printMenu():
    main_menu = """1. Save a new entry 
2. Search by ID
3. Print ages average 
4. Print all names
5. Print all IDs
6. Print all entries
7. Print entry by index 
8. Save all data
9. Exit"""
    print(main_menu)

def getObjectClass(object):
    return object.__class__.__name__

# handle input from user and return person object
def getNewUserDataFromUser():
    person_type = input("Choose Person Type: " + " | ".join(kind.name.lower() for kind in PersonKind) + ": ")
    if person_type.upper() in PersonKind.__members__:
        # create the desired method according to the person type
        method_name  = "create" + person_type.capitalize()
        class_name = person_type.capitalize()
        # retrieve the appropriate class from the global namespace
        class_instance = globals()[class_name]

        # dynamically create the object according to the right class
        person_obj = getattr(class_instance, method_name)()
        return person_obj
    else:
        print("Invalid Choice try again..")
        return
    
# Print Database Entry
def printEntry(person):
    person.printMyself()
    print("Object Type: " + getObjectClass(person))

# function to get all instance attributes dynamically
def getInstanceAttributes(obj):
    # Use __dict__ to get instance variables and remove leading underscores
    # __dict__ return a dictionary of all the instance attributes. the keys is the attr name and the value is the attr value. 
    attributes = {attr_name.lstrip('_'): attr_value for attr_name, attr_value in obj.__dict__.items()}
    attributes["type"] = type(obj).__name__  # Add the object type
    return attributes

# handle save to csv operation
def saveDataToCSV():
    output_file_name = input("What is your output file name? ")
    dir_path = "C:/Users/Yarin/OneDrive/Python/Chapter3/Project"
    csv_path = os.path.join(dir_path, output_file_name)

    df = createDataFrame()
    # save the data frame to csv file
    try:
        df.to_csv(csv_path, index=False)
    except (FileNotFoundError, OSError):
        print("File not found in the directory: " + dir_path)

def createDataFrame():
    # Convert the database to person dict where the keys are the person id and the values are dict that contain values
    # create persons_dict dynamically according to instance attributes
    persons_dict = {
        id_number: getInstanceAttributes(person)
        for id_number, person in database.items()
    }
    # Convert persons_dict to DataFrame
    df = pd.DataFrame.from_dict(persons_dict, orient="index")
    df.fillna("", inplace=True)
    return df

# 1
def saveNewEntry():
    person = getNewUserDataFromUser() # Person obj
    #check that person has data
    if person != None:
        if not person.getID() in database:
            # save to the db the person object as value
            database[person.getID()] = person
            print("ID [" + str(person.getID()) + "] saved successfuly")
            return person.getAge()
        else:
            print("Error: ID already exists: {'name': '" + database[person.getID()].getName() + "' 'age': "  + str(database[person.getID()].getAge()) + "}")
            return 0
    else:
        return 0
      
# 2
def searchById():
    try:
        requested_id = validateNumber(input("Please enter the ID you want to look for: "), "id")
        if requested_id in database:
            entry = database[requested_id]
            printEntry(entry)
        else: # ID number not exists
            print("Error: ID " + requested_id + " is not saved")
    except ValueError:
        return

# 3
def printAgesAverage(ages_sum):
    count = len(database)
    # can't divide by zero --> print 0
    if count == 0:
        print(0)
        return
    average = ages_sum / count
    print(average)
    
# 4
def printAllNames():
    for index, key in enumerate(database):
        name = database[key].getName()
        print(str(index) + ". " + name)

# 5    
def printAllIds():
    for index, key in enumerate(database):
        print(str(index) + ". " + str(key))

# 6
def printAllEntries():
    for index, key in enumerate(database):
        print(str(index) + ". ")
        printEntry(database[key])
  
# 7
def printEntryByIndex():
    max_index = len(database) - 1
    try:
        requested_index = validateNumber(input("Please enter the index of the entry you want to print: "), "index")
        # The user type out of range index
        if requested_index > max_index:
            print("Error: Index out of range. the maximum index allowed is " + str(max_index))
            return
        requested_key = None
        # find the key
        for index, key in enumerate(database):
            if index == requested_index:
                requested_key = key
        value = database[requested_key]
        printEntry(value)
    except ValueError:
        return
    
# dict = { key = id , value = Person Obj } 
database = {}
mainProgram()

