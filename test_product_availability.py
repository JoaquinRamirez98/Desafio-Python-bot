import unittest
from Ejercicio_2 import is_product_available  
class TestProductAvailability(unittest.TestCase):

    def test_is_product_chocolate_available(self):
        self.assertTrue(
            is_product_available('Chocolate', 3),
            msg="Test"
        )

    def test_is_not_product_chocolate_available(self):
        self.assertFalse(
            is_product_available('Chocolate', 5),
            msg="Test"
        )

if __name__ == '__main__':
    unittest.main()
