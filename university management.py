
students = {
    "fatima": "1564",
        "rehmat": "abcd"
        }

       
        def login():
            user = input("Enter username: ")
                pwd = input("Enter password: ")
                    if user in students and students[user] == pwd:
                            print("Login successful!\n")
                                    menu()
                                        else:
                                                print("Login failed.\n")

                                                
                                                def add_student():
                                                    user = input("New username: ")
                                                        if user in students:
                                                                print("User already exists.\n")
                                                                    else:
                                                                            pwd = input("New password: ")
                                                                                    students[user] = pwd
                                                                                            print("Student added.\n")

                                                                                            
                                                                                            def delete_student():
                                                                                                user = input("Username to delete: ")
                                                                                                    if user in students:
                                                                                                            del students[user]
                                                                                                                    print("Student deleted.\n")
                                                                                                                        else:
                                                                                                                                print("Student not found.\n")

                                                                                                                                
                                                                                                                                def view_students():
                                                                                                                                    print("All students:")
                                                                                                                                        for user in students:
                                                                                                                                                print("-", user)
                                                                                                                                                    print()

                                                                                                                                                    
                                                                                                                                                    def menu():
                                                                                                                                                        while True:
                                                                                                                                                                print("1. Add Student")
                                                                                                                                                                        print("2. Delete Student")
                                                                                                                                                                                print("3. View Students")
                                                                                                                                                                                        print("4. Logout")
                                                                                                                                                                                                choice = input("Choose option: ")
                                                                                                                                                                                                        
                                                                                                                                                                                                                if choice == "1":
                                                                                                                                                                                                                            add_student()
                                                                                                                                                                                                                                    elif choice == "2":
                                                                                                                                                                                                                                                delete_student()
                                                                                                                                                                                                                                                        elif choice == "3":
                                                                                                                                                                                                                                                                    view_students()
                                                                                                                                                                                                                                                                            elif choice == "4":
                                                                                                                                                                                                                                                                                        print("Logged out.\n")
                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                                                        print("Invalid choice.\n")

                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                        while True:
                                                                                                                                                                                                                                                                                                                            print("=== Student System ===")
                                                                                                                                                                                                                                                                                                                                print("1. Login")
                                                                                                                                                                                                                                                                                                                                    print("2. Exit")
                                                                                                                                                                                                                                                                                                                                        option = input("Select: ")
                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                if option == "1":
                                                                                                                                                                                                                                                                                                                                                        login()
                                                                                                                                                                                                                                                                                                                                                            elif option == "2":
                                                                                                                                                                                                                                                                                                                                                                    print("Goodbye!")
                                                                                                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                                                                                        print("Invalid option.\n")


                                                                                                                                                                                                                                                                                                                                                                                        

                                                                                                                                                                                                                                                                                                                                                                                        

                                                                                                                                                                                                                                                                                                                                                                                  

                                                                                                                                                                                                                                                                                                                                                                                   

                                                                                                                                                                                                                                                                                                                                                                                   

                                                                                                                                                                                                                                                                                                                                                                                  


                                                                                                                                                                                                                                                                                                                                                                                  

