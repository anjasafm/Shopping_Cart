'''
========================================

This program creates a simple Shopping Cart, made to reflect the concepts of Conditionals, Loops, Functions, Object-Oriented Programming, Python Unit Tests, and Computational Thinking

========================================
'''

class CartItem:
    '''
    Creating CartItem class
    '''
    def __init__(self, product_name, product_price):      # __init__ the function is for initiation the attributes
        '''
        Creating Object for Class CartItem
        '''

        self.product_name = product_name                  # creating new variable for product_name
        self.product_price = product_price                # creating new variable for product_price

class ShoppingCart:
    '''
    Creating ShoppingCart class
    '''
    def __init__(self):    
        '''
        Creating Object for Class ShoppingCart
        '''                             
        self.product_data = []                           # Creating empty list for data looping basket

    def input_item(self, product_name, product_price ):   # Creating input function   
        '''
        Function input for append new looping data to empty basket
        '''
        for item in self.product_data:                   # check whether there are items with the same item name in the shopping cart                  
            if item.product_name == product_name:         # if present will update the declared variable
                item.product_price = product_price
                return
        self.product_data.append(CartItem(product_name,int(product_price))) # append is used to add a new Cart Item object to the self.product_data list
        print(f"Item {product_name} has been successfully added to the basket.")  # prints information if the item was added successfully

    def remove_item(self, item_name):
        '''
        This Function for delete items in data list
        '''
        for item in self.product_data:                   # check the item data for the conditions in which it will be operated
            if item.product_name == item_name:         # if there is an item name it will be the product name
                self.product_data.remove(item)           # remove used to delete items in the data previously entered
                print(f"Item {item_name} successfully removed from shopping cart.") # prints information if the item was successfully deleted
                return                                  # save the return value
    def cart_display(self):
        '''
        function to display items that have previously been entered
        '''
        print("Items in Cart: ")                  # print information on the number of items in the basket
        for item in self.product_data:                   
            print(f"{item.product_name} - Rp {item.product_price}")   # print what items have been entered and how much the price
        
    def shopping_total(self):
        '''
        Function to calculate the total price of goods in product_data
        '''
        total = 0                                       # total = 0 is prepared to accommodate the total value of the added results between item 1 and the others
        for item in self.product_data:                   
            total += item.product_price                  # variable total to add price
        return total                                    # return to return the value
        
def menu_user():
    '''
    Function to be the main menu in this simple application
    '''
    print("\n")
    print("==============================================")
    print("WELCOME TO H8 STORE, HAPPY SHOPPING!")
    print("==============================================")
    print("\nMain Menu:")                                          # tampilan menu yang nanti akan ditampilkan ke user
    print("1. Add Items")
    print("2. Delete Items")
    print("3. Show Items In Cart")
    print("4. View Total Price")
    print("5. Exit")
    print("\n")

if __name__ == "__main__":
    '''
    It is a way to be able to run programs independently
    '''
    cart = ShoppingCart()                                   # create a new variable called cart from the ShoppingCart Class

    while True:                                             # to run the condition if the condition is true then the program will run
        menu_user()
        select_input = input("Choose: ")                          # declare a variable to store user choices

        try:                                                # to check the value entered by the user
            menu_select = int(select_input)                       # creates a new variable for the call and the value filled in is an integer
            if menu_select < 1 or menu_select > 5:        # conditions for options that the user can input
                raise ValueError                            # to initiate an error exception
        except ValueError:                                  # to provide conditions if the user inputs an inappropriate value
            print("Your input is not correct, please re-enter it!")   # prints a statement if the input entered is incorrect
            continue

        if select_input == '1':                                    # for the condition if the user inputs select_input 1     
            item_name = input("Enter the Item Name: ")    # input data for the name of the item to be entered
            item_price = input("Enter Price: ")         # input the price data for the goods to be entered
            cart.input_item(item_name, item_price)      # will call the ShoppingCart class to run the input_item function

        elif select_input == '2':                                  # for the condition if the user inputs select_input 2
            item_name = input("Enter the name of the item you want to delete: ")   # prints a command for the user to input the name of the item to be deleted
            cart.remove_item(item_name)                   # calls the ShoppingCart class to run the remove_item function

        elif select_input == '3':                                  # for the condition if the user inputs select_input 3
            cart.cart_display()                         # calls the ShoppingCart class to run the cart_display function and then prints the items that have been input

        elif select_input == '4':                                  # for the condition if the user inputs select_input 4
            total = cart.shopping_total()                    # calls the ShoppingCart class to run the shopping_total function to calculate the total that has been input
            print(f"Total Price:  Rp {total}")            #   print the total expenditure that has been calculated previously
        elif select_input == '5':                                  # for the condition if the user inputs select_inputan 5 to exit the program
            print("See you! Thank you for shopping at the H8 Store! ") # print a farewell greeting
            break