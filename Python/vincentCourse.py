# Mortgage function
def mortgage(p, r, t, n=12):
    '''p: payment, r: rate, t: term = years, n=months in a year.'''
    interstRatePerMonth = p * (r/n)
    mortgae = round(interstRatePerMonth  / ( 1- (1+r/n)**-(n*t)  ),0)
    return mortgae
    
# print(mortgage(960000,0.06,30))

# #---------------------------------------------------------------------

# # String operation 

# "text{0}" .format()
def InstaHeader(Followers, Following, Likes):
    print("Followers {0} | Following {1} | Likes {2}".format(Followers, Following, Likes))  
# print(InstaHeader(100,10,"1M"))

#     # string * 3
#     # string += " name"
# first_name = "Muhammad"
# first_name += " Mostey"
# letter = "k"
# multi_letters = letter*3
# print(multi_letters)

# #---------------------------------------------------------------------

# logical operators and or not 

# #---------------------------------------------------------------------
# # Drawing Tringles 

# # *
# # **
# # ***
# for step in range (1, 4):
#     print("*"*step)

# #    *
# #   ***
# #  *****
def pyramid(n):
    stars = 1
    while stars <= n:
        empty = n - stars
        side = int(empty / 2)
        print(side*" " ,stars*"*", side*" ")
        stars += 2
# pyramid(10)



# #---------------------------------------------------------------------
# Cart and Items implementation using python, with features adding and removing items to a cart, and calculate cart total.
# using interface to not make cart [] variable accessable to user we put it private by prefixing the name with __
# to avoid things like AhmedStore.cart.append(Item("bug",-100))
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Store:
    def __init__(self):
        self.__cart = []
        

    def addToCart(self, itemObject):
        return self.__cart.append(itemObject)


    def removeItemFromCart (self, ItemObjectName):
        for cartItem in self.__cart:
            if cartItem.name == ItemObjectName: 
                return self.__cart.remove(cartItem)  
            
            
    def calculateCartTotal(self):
        total = 0.0
        for item in self.__cart:
            total += item.price
            
        return total

    def displayCart(self):
        for LineNumber in range(0, len(self.__cart)):
            print(LineNumber, self.__cart[LineNumber].name)
# # Testing cart
# store = Store()
# store.addToCart(Item("pen", 1))
# store.addToCart(Item("pencil", 0.5))


# print("Hello! Welcome to Our Store")
# while True:
    
#     store.displayCart()
#     print("Cart Total Amount: ", store.calculateCartTotal(), "\n")
    
#     print("Press a to add an item")
#     print("Press r to remove an item")
#     print("Press x to exit")
    
#     userInput = input("Please enter a command: ").lower()
#     if userInput == "x":
#         break
    
#     elif userInput == "a":
#         itemName = input("Please give the item's name: ")
#         itemPrice = float(input("Please provide a price: "))
#         store.addToCart(Item(itemName, itemPrice))
        
#     elif userInput == "r":
#         itemName = input("Please give the item's name: ")
#         store.removeItemFromCart(itemName)
#     else:
#         print("Please Enter a valid command(a: add, r: remove, x: exit)")
                

# #---------------------------------------------------------------------

class Character:
    def __init__(self, name, eyes, hair):
        self.name = name
        self.eyes = eyes
        self.hair = hair
        
        
Player1 = Character("Hunjur", "brown", "long") 

# #---------------------------------------------------------------------
# def __str__(self): // print of obj will return this fun not obj address at the memory
# Tringle area = base * height / 2
# Polymorphism sub-classes class subClassname(parentClassName) // needs using super().__init__(length, length) under def __init__(length):

class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height
    
    def preimeter(self):
        return (self.base * 2) + (self.height * 2)



class Rectangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)



class Square(Shape):
    def __init__(self, length):
        super().__init__(length, length)


class Trinagle(Shape):
    def __init__(self, base, height, a, b, c):
            super().__init__(base, height)
            self.a = a
            self.b = b
            self.c = c
            
    def area(self):
        return self.base * self.height / 2
    
    def preimeter(self):
        return self.a + self.b + self.c
    
        
# shapes = [Square(2), Rectangle(4,2), Trinagle(2,3,10,20,30)]        
# print(shapes[2].area()) 
       
# # overriding vs overloading in java vs Python 
# # overriding - Runtime Polymorphism (Method Overriding) Example:
# # Shape class has a draw method with two parameters. The Rectangle and Circle subclasses override this method with additional parameters specific to each shape. but with same method names as parent.
# # in java using childClass extends parentClass {}. in python childClass(ParentClass):.

# # overriding example in Java:
# class Shape {
#     // Method with two parameters
#     void draw(int width, int height) {
#         System.out.println("Drawing shape with width " + width + " and height " + height);
#     }
# }

# class Rectangle extends Shape {
#     // Overriding the draw method with additional parameters
#     @Override
#     void draw(int width, int height, String color) {
#         System.out.println("Drawing rectangle with width " + width + ", height " + height + ", and color " + color);
#     }
# }

# # overriding and using super keyword in java:
# class Animal {
#     String sound = "Generic animal sound";

#     void makeSound() {
#         System.out.println(sound);
#     }
# }

# class Dog extends Animal {
#     String sound = "Bark";

#     @Override
#     void makeSound() {
#         // Call the makeSound method from the parent class using super
#         super.makeSound();

#         // Add additional functionality specific to Dog
#         System.out.println("Dog barks loudly: " + sound);
#     }
# }

# # overriding and using super keyword in python:

# class Animal:
#     def __init__(self):
#         self.sound = "Generic animal sound"

#     def make_sound(self):
#         print(self.sound)

# class Dog(Animal):
#     def __init__(self):
#         # Call the constructor of the parent class
#         super().__init__()
#         self.sound = "Bark"

#     def make_sound(self):
#         # Call the make_sound method from the parent class using super
#         super().make_sound()

#         # Add additional functionality specific to Dog
#         print(f"Dog barks loudly: {self.sound}")





# #overloading - Compile-time Polymorphism (Method Overloading):
# # writing same method within a class that let to call the method by choosing what are the parameters that's been overloaded with in the method declaration params 

# # overloading example in Java:
# public class Printer {
#     // Method with an integer parameter
#     public void print(int number) {
#         System.out.println("Printing integer: " + number);
#     }

#     // Overloaded method with a double parameter
#     public void print(double number) {
#         System.out.println("Printing double: " + number);
#     }

#     // Overloaded method with a String parameter
#     public void print(String text) {
#         System.out.println("Printing string: " + text);
#     }


    
# # overloading example in python:
# class Calculator:
#     def add(self, a, b=0, c=0):
#         return a + b + c

# # Creating an object
# calculator = Calculator()

# # Calling overloaded methods (using default parameter values)
# result1 = calculator.add(2)
# result2 = calculator.add(2, 3)
# result3 = calculator.add(2, 3, 4)


# #---------------------------------------------------------------------

# Lists Operations
# tools = ["Screwdriver", "Hammer", "Nail", "Saw", "Scissors", "Tape measure"]
# print("\n", "list items at the beginning: ", tools, "\n")

# tools.insert(0, "wrench")
# print("list itmes after insert(0, 'wrench'): ", tools, "\n")

# tools.remove("Nail")
# print("list itmes after remove('Nail') ", tools, "\n")

# tools.pop()
# print("list itmes after pop() ", tools, "\n")

# tools.pop(2)
# print("list itmes after pop(2) index that will be removed or poped: ", tools, "\n")

# tools.clear()
# print("list itmes after clear(): ", tools, "\n")

# #---------------------------------------------------------------------