import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"]
units_sold = [25, 60, 35, 80, 45]
prices = [150000, 85000, 60000, 12000, 5000]

revenue = [units_sold[i] * prices[i] for i in range(len(products))]

plt.figure(figsize=(9, 5))
plt.bar(products, revenue)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (PKR)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("product_revenue.png")
plt.show()

best_product = products[revenue.index(max(revenue))]
print("Total revenue: PKR", sum(revenue))
print("Highest revenue product:", best_product)
