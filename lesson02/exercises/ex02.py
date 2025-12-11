# Mỗi sản phẩm là 1 tuple (product_id, name, price)
products = [
    (1, "Ban Phim", 250_000),
    (2, "Chuot", 150_000),
    (3, "Man Hinh", 3_000_000),
    (4, "Tai Nghe", 500_000),
]

# Danh sách đơn hàng (list dict)
orders = [
    {"order_id": "HD01", "items": [1, 2, 4]},
    {"order_id": "HD02", "items": [2, 3]},
    {"order_id": "HD03", "items": [1, 4]},
]

# a
print("\na.")

product_map = {}

for product_id, name, price in products:
    product_map[product_id] = {"name": name, "price": price}

print(product_map)

# b Tính tổng tiền mỗi hóa đơn
for order in orders:
    total = 0
    for product_id in order["items"]:
        total += product_map[product_id]["price"]
    order["total"] = total

# c
print("\nc. In ra danh sách hóa đơn theo format:")
for order in orders:
    print(
        f"{order['order_id']}: "
        f"{len(order['items'])} san pham, "
        f"Tong tien = {order['total']:,}"
    )

# d
all_products_sold = set()

for order in orders:
    all_products_sold.update(order["items"])

print("\nd. So luong san pham khac nhau da ban:", len(all_products_sold))





