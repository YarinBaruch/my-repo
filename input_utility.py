# handle input that isn't number and print error
def printNumberError(user_input, error_event):
    print("Error: " + error_event + " must be a number. " + user_input + " is not a number")

# check if the input is'nt number
def validateNumber(user_input, input_type):
    try:
        return int(user_input)
    except ValueError:
        printNumberError(user_input, input_type)
        raise ValueError


