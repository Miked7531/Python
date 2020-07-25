#parent class
class User:
    name = "Bob"
    email = "bob@yahoo.com"
    password = "bobbylovescoding"

    def getLoginInfo(self):
        entry_name = input("Enter name here: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")


#child class Customer
class Customer(User):
    class_cost = 40.00
    hours = "Unlimited"
    premium_number = "1337"

#swap password with premium

    def getLoginInfo(self):
        entry_name = input("Enter name here: ")
        entry_email = input("Enter your email: ")
        entry_premium = input("Enter your premium membership code: ")
        if (entry_email == self.email and entry_premium == self.premium_number):
            print("Welcome premium member, {}!".format(entry_name))
        else:
            print("Premium number or email is incorrect")

#2nd child class
class Club(User):
    fee = 50.00
    hours = "all day baby"
    club_name = "Super Fitness"

#swap password with club name   
            
    def getClubRewards(self):
        entry_name = input("Enter name here: ")
        entry_email = input("Enter your email: ")
        entry_club = input("Enter club name: ")
        if (entry_email == self.email and entry_club == self.club_name):
            print("Super Fitness welcomes, {}!".format(entry_name))
        else:
            print("Invalid club name")
            
#invokes the methods for each class
customer = User()
customer.getLoginInfo()

clubc = Customer()
clubc.getLoginInfo()

cluba = Club()
cluba.getClubRewards()
