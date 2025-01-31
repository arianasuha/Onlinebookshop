#abstract class -> no implementation. If subclass inherits this then those subclasses need to 
#override abstract method. No object of this class as it is abstract( blue print type)
#if the subclass do not override the parent class's method, then the subclass will also be treated
#like an abstract class and will not be able to create any instance
#abc is a module, ABC means Abstract based class
#we do not write anything in the abstract method rather we just pass as we do not need to implement
#the abstract method
#in method override process, we need to declare same name for both methods

class IdNotFound(Exception):
    
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

from abc import ABC, abstractmethod  
class person(ABC):
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password  #encapsulation
        print(f"Welcome to the Bookstore!")

    def register_check(self, id):
        if id == self.id:
            return
        raise IdNotFound("You need to register first")


    def register(self):
        if self.id in User.user_info or self.id in Employee.emp_info:
            print(f"This account is already registered")
            return
    
        if self.id[0] == "U":
            User.user_info[self.id] = (self.name, self.email, self.password)
        else:
            Employee.emp_info[self.id] = (self.name, self.email, self.password)

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
        Book.book_dict[self.title] = self.price        


#inheritence
class User(person, Book):
    user_info = {}
    def __init__(self, id, name, email, password):
        super().__init__(id, name, email, password)
        self.cart = []


    def register(self):
        super().register()

    def add_to_cart(self, book, quantity):
        if book.stock >= quantity:
            self.cart.append([book.title, book.price])
            print(f"{book} added to cart, {self.name}")
        else:
            print(f"Sorry, {book} is Out of stock!")


    @classmethod
    def display_user_info(cls):
        for user in cls.user_info:
            print(user, end = "\n")


    def print_info(self):
        print(f"{self.name} is an user!")

    def purchase(self, title, price):
        pass


class Employee(person):
    emp_info = {}
    def __init__(self, id, name, email, password):
        super().__init__(id, name, email, password)

    def register(self):
        super().register()

    @classmethod
    def display_emp_info(cls):
        for key, val in cls.emp_info.items():
            print(key,":",val, end = "\n")

    def print_info(self):
        print(f"{self.name} is an Employee")


if __name__ == '__main__':
    u1 = User("U1", "Suha", "suhaariana@gmail.com", "12345678")
    u1.register()
    u1.login()











