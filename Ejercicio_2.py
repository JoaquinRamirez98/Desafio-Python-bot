import pandas as pd
import unittest

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity": [3, 10, 0, 5]
})


def is_product_available(product_name, quantity):
    row = _PRODUCT_DF[_PRODUCT_DF['product_name'] == product_name]
    if row.empty:
        return False
    return row['quantity'].iloc[0] >= quantity

#Test unitarios para verificar el funcionamiento
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
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
