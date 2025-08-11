class dictionary:
    # methods
    def cms(self):
     self.contacts={}
     while True:
      self.options = ("1.Add a new contact","2.Delete a contact ", "3.Search contact by name"
      ,"4.Display all contacts in sorted order ", "5.Exit")
      for item in self.options:
          print(item.lower())
      self.option = input("choose an option(only number): ")
      # Conditions are used to access the selected option via methods
      if self.option == '1':
          self.addnewcontact()
      elif self.option == '2':
          self.deletecontact()
      elif self.option == '3':
          self.findcontact()
      elif self.option == '4':
          self.sortedcontacts()
      elif self.option == '5':
          self.exit()
      else:
          print("Invalid,choose the right option".upper())
# child class
class child(dictionary):
# 1.Add a new contact
    def addnewcontact(self):
            self.name = str(input("Enter the name: ")).lower()
            self.number = input("Enter the number: ").lower()
            if self.name in self.contacts or self.number in self.contacts:
                print("contact updated successfully".upper())
            elif self.number.isdigit() and len(self.number) != 10:
                   print("number is not valid".upper())  
            else:
                self.contacts.update({self.name:self.number})
                print("contact updated successfully".upper())
# 2.Delete a contact
    def deletecontact(self):
           self.delete = input("Contact to be deleted:")
           if self.delete in self.contacts:
               self.contacts.pop(self.delete)
               print("contact deleted successfully".upper())
           else:
               print("contact not found".upper())
# 3.Search contact by name
    def findcontact(self):
          self.Search = input("Enter the contact: ")
          if self.Search in self.contacts:
             print(f"PLEASE FIND THE CONTACT DETAILS -> {self.Search.title()}: {self.contacts[self.Search]}")
          else:
             print("contact not found".upper())
# 4.Display all contacts in sorted order
    def sortedcontacts(self):
          if not self.contacts:
            print("contact not found".upper())
          else:
            sort_contacts = dict(sorted(self.contacts.items()))
            print("SORTED CONTACTS:")
            for self.name,self.number in sort_contacts.items():
                print(f"{self.name.title()}: {self.number}")
# 5.Exit
    def exit(self):
            print("EXITING")
            exit()

dic = child() 
dic.cms()




  





 