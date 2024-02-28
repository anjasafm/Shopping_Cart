import unittest
'''
import the unittest module for testing
'''
from shopping_cart_app import CartItem, ShoppingCart
'''
import the CartItem and ShoppingCart classes from the shopping_cart_app file/mobule that will be tested
'''
class TestCartItem(unittest.TestCase):
    '''
    class definition for CartItem testing
    '''
    def test_cartitem(self):
        '''
        testing the initialization function of the CartItem class
        '''
        item = CartItem("Mouse", 500)                # input test data into the CartItem class in the form of a Mouse worth 500
        self.assertEqual(item.product_name, "Mouse")    # assertequal to ensure that previously attempted values for input are the same
        self.assertEqual(item.product_price, 500)      # assertequal to ensure that the values you are trying to enter have the same value

class TestShoppingCart(unittest.TestCase):
    '''
    define a class for testing the ShoppingCart class
    '''
    def setUp(self):
        '''
        a method start function that is always executed before testing begins
        '''
        self.cart = ShoppingCart()                      # declare a new variable containing the ShoppingCart class

    def test_input(self):
        '''
        defines a function to test the input function
        '''
        self.cart.input_item("Mouse", 500)                               # input item for testing
        self.assertEqual(len(self.cart.product_data), 1 )                    # look for whether the value in the product_data variable exists or not (if it exists it means it was entered successfully, if not it fails)
        self.assertEqual(self.cart.product_data[0].product_name, "Mouse")    # Look for the value that was entered into product_name
        self.assertEqual(self.cart.product_data[0].product_price, 500)      # look for the value that was entered into product_price

    def test_remove(self):
        '''
        defines a function for test remove/delete
        '''
        self.cart.input_item("Mouse", 500)                               # input items for testing
        self.cart.remove_item("Mouse")                                     # deletes the previously entered value
        self.assertEqual(len(self.cart.product_data), 0)                     # Check by looking for the value in product_data. If it is successfully deleted, there will be no values/variables in it

    def test_total(self):
        '''
        defines a function to test calculating the total price of item
        '''
        self.cart.input_item("Mouse", 500)                               # input goods for testing
        self.cart.input_item("Keyboard", 650)                                 # input goods for testing
        self.assertEqual(self.cart.shopping_total(), 1150)                  # check by equating the value in the total shopping with the total number of checks
    
    def tearDown(self):
        '''
        function to delete all data that is dummy for the testing above
        '''
        del self.cart                                                       # execute to delete the data in the self.cart variable

if __name__ == '__main__':
    '''
    run all test scripts
    '''
    unittest.main(argv=['ignore','-v'], exit=False)
