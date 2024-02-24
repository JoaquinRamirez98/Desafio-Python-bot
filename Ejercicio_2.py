import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity": [3, 10, 0, 5]
})

def is_product_available(product_name, quantity):
    row = _PRODUCT_DF[_PRODUCT_DF['product_name'] == product_name]
    if row.empty:
        return False
    return row['quantity'].iloc[0] >= quantity

if __name__ == '__main__':
    product_name_input = input("Ingrese el nombre del producto: ")
    quantity_input = int(input("Ingrese la cantidad deseada: "))

    if is_product_available(product_name_input, quantity_input):
        print(f"¡Producto '{product_name_input}' disponible en la cantidad solicitada!")
    else:
        print(f"Lo siento, no hay suficiente stock para el producto '{product_name_input}'.")

    # Código adicional para ejecutar cuando se ejecuta el script directamente
