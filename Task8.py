contacts=[]
while True:
    def add_contact():
        name=input("input your name!")
        phone=input("input your phone!")
        email=input("input your email!")
        contacts.append([name.lower(),phone,email.lower()])
        print("Contact Has Been Added")

    def show():
        x=1
        for i , contact in enumerate(contacts):
            print(f"{i+1}. {contact[0]}-{contact[1]}-{contact[2]}")

    def search():
        search  = input("type name or phone to search:")
        for i, contact in enumerate(contacts):
            if (search.lower() in contact):
                print(f"{i+1}{contact[0]}-{contact[1]}-{contact[2]}")

    def delete():
        n=input("do you want to delet by name or index? ").lower()
        if (n =="name"):
            na =input("enter name:")
            for contact in contacts:
                if na.lower() ==contact[0]:
                    contacts.remove(contact)
                    print("contact was deleted successfully")
        elif(n =="index"):
            index = int(input("enter index:"))
            contacts.remove(contacts[index-1])
        else:
            print("contact wasn't found")

    print("for adding new contact.1")
    print("for displaying contacts.2")
    print("for searching for a contact.3")
    print("for deleting a contact.4")
    print("Exit.5")
    choice=input("type number of operation")
    if choice=="1":
        add_contact()
    elif choice=="2":
        show()
    elif choice=="3":
        search()
    elif choice=="4":  
        delete() 
    else:
        print("please try again") 