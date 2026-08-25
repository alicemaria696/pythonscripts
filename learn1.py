import bcrypt
print("helllo world this is git from my college id")

class role:
    def role_display(self):
        i = 0
        tuple = ("admin", "soc", "management", "it", "finance", "marketing")
        for t in tuple:
            i += 1
            print(f"the role in the system are {i} {t}")
        print("please enter the role of your choice from the above list")
        user_choice = input("enter the role of your choice: ")
        if user_choice == "admin":
            print("you have access to all the data")
        elif user_choice == "soc":
            print("you have access to the data of your department")
        elif user_choice == "management":
            print("you have access to the data of your department")
        elif user_choice == "it":
            print("you have access to the data of your department")
        elif user_choice == "finance":
            print("you have access to the data of your department")
        elif user_choice == "marketing":
            print("you have access to the data of your department")
        else:
            print("you have no access to the data")

class user:
    def user_details(self):
        ut = []
        un = input("enter your name: ")
        ue = input("enter your email: ")
        up = input("enter your password: ")
        up = bcrypt.hashpw(up.encode('utf-8'), bcrypt.gensalt())
        
        for i in range(1):
            ut.append(un)
            ut.append(ue)
            ut.append(up)
        print("your details are saved successfully")
        print("your name is: ", ut)
        
class cyberark_login_jwt_pvwa_signin:
    def __init__(self, username, password, role):
        self.username = username,
        self.password = password,
        self.role = role,
        
    payload = {
        username: "username",
        password: "password",
        role: "role"
    }
        
    
        
  
if __name__ == "__main__":
    r = role()
    r.role_display()
    u = user()
    u.user_details()
        
            
            
    