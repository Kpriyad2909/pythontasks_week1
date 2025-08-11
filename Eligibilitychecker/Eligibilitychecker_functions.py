# Using Functions
# Prompt for User's Full name
Fullname = str(input("Enter your Full Name:"))
# Validate that age is a valid number.
while True:
    Input_Age = input("Enter the age:")
    if Input_Age.isdigit():
        Age = int(Input_Age)
        if (0 <= Age <= 120):
            break
        else:
            print("Enter a valid age between 0 and 120")
    else:
        print("Enter a valid age as digits")
print("-------Valid age-------") 
# Prompt for User's Gender
Gender = input("Enter your Gender(Male/Female/Other):").lower()
#prints Users name
print(f"Hello {Fullname.title()}!")
# Functions
def voting_eligibility(Age):
    return "You are eligible for voting" if Age >= 18 else "You are not Eligible for voting"

def driving_eligibility(Age):
    return "You are eligible for driving" if Age >= 18 else "You are not Eligible for driving"

def retirement_eligibility(Age,Gender):
    if Age >= 60 and Gender == 'male':
        return "You are eligible for retirement"
    elif Age >= 58 and Gender == 'female':
        return "You are eligible for retirement"
    elif Age >= 60 and Gender == 'other':
        return "You are eligible for retirement"
    return "You are not eligible for retirement"
# Result(functions)
print(voting_eligibility(Age))
print(driving_eligibility(Age))
print(retirement_eligibility(Age,Gender))

"""i = 0
while i < 3:
 User_age = input("Enter the age:")
 if User_age.isdigit():
    Age = int(User_age)
    print("Valid age")
    break
 elif i < 2:
    print("Please enter valid age") 
 i+=1
else:
    print("Invalid age and hence exiting")
    exit()""" 



