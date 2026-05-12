import random

products = ['Laptop','Monitor','Keyboard','Mouse','Webcam','Headset','Docking Station','USB Hub','Desk Lamp','Surge Protector'
]
# print(random.choice(products))
# selected_products = random.sample(products,3)
# print(selected_products)

# random.shuffle(products)
# print(products)

transaction_count = random.randint(50,300)

print(f'Daily transaction count: {transaction_count}')