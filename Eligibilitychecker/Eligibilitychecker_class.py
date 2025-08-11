# using class and objects
class application:
# constructor
   def __init__(self):
    self.name = input('Enter the Full name:')
    # checks the valid age
    while True:
     self.Age = input('enter the Age:')
     if self.Age.isdigit():
              self.age = int(self.Age)
              if (0 <= self.age <= 120):
                break
              else:
                print("Enter a valid age between 0 and 120")
     else:
        print("Enter a valid age as digits")
    print("-------Valid age-------")
    # prompt for gender
    self.Gender = input("Enter your Gender(Male/Female/Other):").lower()
    # prints users name
    print(f"Hello {self.name.title()}!")
    # other methods
   def voting_eligibility(self):
       print("You are eligible for voting") if self.age >= 18 else ("You are not eligible for voting")

   def driving_eligibility(self):
       print("You are eligible for driving")if self.age >= 18 else ("You are not eligible for driving")

   def retirement_eligibility(self):
       if self.age >= 60 and self.Gender == 'male':
           print("You are eligible for retirement")
       elif self.age >= 58 and self.Gender == 'female':
           print("You are eligible for retirement")
       elif self.age >= 60 and self.Gender == 'other':
           print("You are eligible for retirement")
       else:
           print("You are not eligible for retirement")
#object initialization - a1
a1 = application() #class
a1.voting_eligibility() #method
a1.driving_eligibility()
a1.retirement_eligibility()