#abstract class -> no implementation. If subclass inherits this then those subclasses need to 
#override abstract method. No object of this class as it is abstract( blue print type)
#if the subclass do not override the parent class's method, then the subclass will also be treated
#like an abstract class and will not be able to create any instance
#abc is a module, ABC means Abstract based class
#we do not write anything in the abstract method rather we just pass as we do not need to implement
#the abstract method
#in method override process, we need to declare same name for both methods

class IdNotFound(Exception):
    pass


from abc import ABC, abstractmethod  
class Person(ABC):
    _password_list = []
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        print(f"Welcome {self.name}! Please Register your account.")

    def register_check(self, id):
        if id == self.id:
            return
        raise IdNotFound("You need to register first")
    
    def check_password(self):  
        digit = False
        upper_charc = False
        lower_charc = False
        special_charc = False

        if self.password in Person._password_list:
            print("This password already exists. Please set a different password")
            self.password = input("Enter your password: ")


        for letter in self.password:
            if 97 <= ord(letter) <= 122:
                lower_charc = True
            elif 65 <= ord(letter) <= 90:
                upper_charc = True
            elif 48 <= ord(letter) <= 57:
                digit = True
            else:
                special_charc = True

        
        message = "Your password must contain atleast one"
        if digit == False:
            print(message, "numeric value")
            self.correct_password("digit")
        if upper_charc == False:
            print(message, "uppercase character")
            self.correct_password("upper_charc")
        if lower_charc == False:
            print(message, "lowercase character")
            self.correct_password("lower_charc")
        if special_charc == False:
            print(message, "special character")
            self.correct_password("special_charc")
        if len(self.password) < 8:
            print("Your password must contain atleast 8 characters")
            self.password = input("Please Enter your password again: ")

        if digit and upper_charc and lower_charc and special_charc and len(self.password) >= 8:
            return
        

    def correct_password(self, issue):
        #using recursion
        self.password = input("Enter your password again: ")
        for i in self.password:
            if issue == "lower_charc":
                if 97 <= ord(i) <= 122:
                    lower_charc = True
                    return
            elif issue == "upper_charc":
                if 65 <= ord(i) <= 90:
                    upper_charc = True
                    return
            elif issue == "digit":
                if 48 <= ord(i) <= 57:
                    digit = True
                    return
            elif issue == "special_charc":
                if i in "!@#$%^&*?|><":
                    special_charc = True
                    return
            

        self.correct_password(issue)
        
        



    def register(self):
        if self.id in User.user_info or self.id in Employee.emp_info:
            print(f"This account is already registered")
            return
        
        self.password = input("Enter your password: ")
        self.check_password()
        self.password2 = input("Please confirm your password: ")
        if self.password != self.password2:
            print("You have entered wrong password!\nPlease Try again")
            self.password2 = input("Please Enter your password again: ")
        Person._password_list.append(self.password)

        if self.id[0] == "U":
            User.user_info[self.id] = (self.name, self.email)
        else:
            Employee.emp_info[self.id] = (self.name, self.email)

        print(f"Congratulations {self.name}! You have successfully registered.")


    def login(self):
        try:
            id = input("Enter your User Id: ")
            self.register_check(id)
            password = input("Enter your password: ")
            if password != self.password:
                count = 1
                while count < 3:
                    if password == self.password:
                        print(f"Welcome {self.name}")
                        break
                    else:
                        print("Invalid Password!❌")
                        password = input("Please enter the correct password: ")
                        count += 1
                        if count == 3 and password != self.password:
                            print("You have entered wrong password 3 times. Please try again tomorrow")
            else:
                print(f"Welcome {self.name}!")
                        
        except IdNotFound as error:
            print(error)

    @abstractmethod
    def print_info(self):
        pass

class Book:
    book_dict = {}
    discount = 0.05
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
        Book.book_dict[self.title] = [self.author, self.price, self.stock]
        #used list as it is mutable and I need to change stock when a customer buys a book
        print(Book.book_dict)


    @classmethod
    def discount_update(cls):
        cls.discount = int(input("Enter value: "))
        print("Discount has been updated")


   


#inheritence
class User(Person, Book):
    user_info = {}
    def __init__(self, id, name, email):
        super().__init__(id, name, email)
        self.cart = []


    def register(self):
        super().register()
        

    def search(self):
        title = input("Please Enter the book title: ")

        if title not in Book.book_dict:
            print(f"{title} is not available")
            return
        
        quantity = int(input("Please enter the quantity of product you want to purchase: "))
        if Book.book_dict[title][2] == 0:
            print(f"'{title}' is currently out of stock")
        elif Book.book_dict[title][2] < quantity:
            print(f"Available Quantity: {Book.book_dict[title][2]}")
        else:
            cart = input("Would like to add this on your cart?\nEnter 'Yes' if you want to add this to your cart: " )
            if cart == "Yes":
                self.add_to_cart(title, quantity)

    def add_to_cart(self, title, quantity):
        payable_amount = Book.book_dict[title][1] * quantity
        if quantity >= 5:
            payable_amount += Book.discount
        Book.book_dict[title][2] = Book.book_dict[title][2] - 1
        print(Book.book_dict)
        print(f"{self.name}, {title} is added to your cart.\nYou need to pay {payable_amount} Tk.")




    @classmethod
    def display_user_info(cls):
        for user in cls.user_info:
            print(user, end = "\n")


    def print_info(self):
        print(f"{self.name} is an user!")

    def purchase(self, title, price):
        pass


class Employee(Person):
    emp_info = {}
    def __init__(self, id, name, email):
        super().__init__(id, name, email)

    def register(self):
        super().register()

    @classmethod
    def display_emp_info(cls):
        for key, val in cls.emp_info.items():
            print(key,":",val, end = "\n")

    def print_info(self):
        print(f"{self.name} is an Employee")


if __name__ == '__main__':
    # u1 = User("U1", "Suha", "suhaariana@gmail.com")
    # u1.register()
    # u1.login()
    u2 = User("U2", "Suhana", "suhan@gmail.com")
    # u2.register()
    # u2.login()
    b1 = Book("The Silent Patient", "Alex Michaidelis", 100, 2)
    b2 = Book("Death on the Nile", "Agatha Christie", 200, 1)
    b3 = Book("Da The Vinci Code", "Dan Brown", 300, 1)
    print(Book.book_dict)
    
    
   











