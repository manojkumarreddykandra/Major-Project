import keyring 
import getpass
def add_password(website, username, password):
           keyring.set_password(“password_manager”, website, password)
           print(f”Password for {website} saved successfully!”)
def get_password(website): 
          try:
             password = keyring.get_password(“password_manager”, website)
            print(f”Password for {website}: {password}”)
            except keyring.errors.PasswordDeleteError: 
                print(f”Password for {website} not found.”)
def main(): 
    while True:
            print(“\nPassword Manager”) 
            print(“1. Add password”)
            print(“2. Get password”) 
            print(“3. Exit”)
            choice = input(“Enter your choice: “)
            if choice == “1”:
                    website = input(“Enter website: “)
                    username = input(“Enter username: “) 
                    password = getpass.getpass(“Enter password: “) 
                    add_password(website, username, password)
            elif choice == “2”:
                         website = input(“Enter website: “)
                        get_password(website) 
            elif choice == “3”:
                       break 
            else:
               print(“Invalid choice. Please try again.”)


if   name	== “  main  ”:






