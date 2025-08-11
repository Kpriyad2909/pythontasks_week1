contacts = {}
while True:
 options = ("1.Add a new contact","2.Delete a contact ", "3.Search contact by name"
,"4.Display all contacts in sorted order ", "5.Exit")
 for item in options:
    print(item.lower())
 option = input("choose an option(only number): ")

# 1.Add a new contact
 if option == '1':
     new_name = str(input("Enter the name: ")).lower()
     new_number = input("Enter the number: ").lower()
     if new_name in contacts or new_number in contacts:
         print("contact updated successfully".upper())
     elif new_number.isdigit() and len(new_number) != 10:
          print("number is not valid".upper())  
     else:
         contacts.update({new_name:new_number})
         print("contact updated successfully".upper())
# 2.Delete a contact
 elif option == '2':
     delete = input("Contact to be deleted:")
     if delete in contacts:
         contacts.pop(delete)
         print("contact deleted successfully".upper())
     else:
         print("contact not found".upper())

# 3.Search contact by name
 elif option == '3':
     Search = input("Enter the contact: ")
     if Search in contacts:
         print(f"PLEASE FIND THE CONTACT DETAILS -> {Search.title()}: {contacts[Search]}")
     else:
         print("contact not found".upper())

# 4.Display all contacts in sorted order
 elif option == '4':
   if not contacts:
       print("contact not found".upper())
   else:
       sort_contacts = dict(sorted(contacts.items()))
       print("SORTED CONTACTS:")
       for new_name,new_number in sort_contacts.items():
        print(f"{new_name.title()}: {new_number}")

# 5.Exit
 elif option == '5':
     exit()

 else:
     print("Invalid Choose the right Option".upper())
  



