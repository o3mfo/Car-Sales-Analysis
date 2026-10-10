
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path(__file__).resolve().parent / "cars1000.xlsx"
cars = pd.read_excel(file_path)

# cars = pd.read_excel("Car_Sales_Analysis/cars1000.xlsx")

# Data Cleaning - تنظيف البيانات

print(cars.isnull().sum())
print(cars.duplicated().sum())

print("-" * 30)

# Data Analysis - تحليل البيانات

sales = cars.groupby("Brand")["Price"].sum()
print(sales.sort_values(ascending=False))

print(cars["Price"].mean())
print(cars["Price"].sum())
print(cars["Price"].max())
print(cars["Brand"].value_counts())
print(cars["Model"].value_counts())

# Data Visualization - تصور البيانات

cars["Brand"].value_counts().plot(kind="bar")
plt.title("Car Sales by Brand")
plt.tight_layout()
# plt.savefig("car_sales_by_brand.png")
plt.show()

sales = cars.groupby("Brand")["Price"].sum()
sales.sort_values(ascending=False).plot(kind="bar")
plt.title("Total Sales Value by Brand")
plt.tight_layout()
# plt.savefig("sales_value_by_brand.png")
plt.show()

cars["Brand"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Car Sales Share by Brand")
plt.tight_layout()
# plt.savefig("car_sales_share_by_brand.png")
plt.show()