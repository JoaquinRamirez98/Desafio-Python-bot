import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity": [3, 10, 0, 5]
})


def is_product_available(product_name, quantity):
    while True:
        row = _PRODUCT_DF[_PRODUCT_DF['product_name'] == product_name]

        if row.empty or row['quantity'].iloc[0] < quantity:
            print(f"El producto '{product_name}' no está disponible o no hay suficiente stock.")

            decision = input("¿Desea probar con otro producto? (s/n): ").lower()

            if decision == 's':
                product_name = input("Ingrese el nombre del nuevo producto: ")
                continue
            else:
                return False
        else:
            return True


if __name__ == '__main__':
    is_chocolate_available = is_product_available('Chocolate', 5)
    print(is_chocolate_available)
