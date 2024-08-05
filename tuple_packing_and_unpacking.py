orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

def unpack_orders(orders):
    for order in orders:
        name,item,amount = order
        print(f"{name} ordered {int(amount)} {item}{"'s" if amount > 1 else ''}")

if __name__ == '__main__':
    unpack_orders(orders)