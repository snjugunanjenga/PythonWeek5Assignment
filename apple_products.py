#!/usr/bin/env python3
"""
Apple Product Class Demonstration
Author: SNN
Unique ID: DNN19600118  <- Watermark Here!
 
Week 5 Assignment 1: Apple Products Class Design

Description:
- Defines an AppleProduct base class with attributes like model name, storage capacity, color, price, and operating system.
- Creates subclasses (iPhone, iPad, MacBook) that inherit from AppleProduct and add unique attributes and behaviors.
- Generates 10 examples of different Apple products.
- Saves product details to a CSV file in the "data" folder as 'apple_products.csv'.
"""

import os
import csv

def ensure_data_folder():
    """Ensure that the 'data' folder exists."""
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Created 'data' folder.")

class AppleProduct:
    def __init__(self, product_type, model_name, storage_capacity, color, price, operating_system):
        self.product_type = product_type
        self.model_name = model_name
        self.storage_capacity = storage_capacity
        self.color = color
        self.price = price
        self.operating_system = operating_system

    def display_info(self):
        return (f"{self.product_type} | Model: {self.model_name} | Storage: {self.storage_capacity} | "
                f"Color: {self.color} | Price: ${self.price} | OS: {self.operating_system}")

    def calculate_discounted_price(self, discount_percent):
        """Calculate and return the discounted price if discount is 20% or higher; else return original price."""
        if discount_percent >= 20:
            discount_amount = self.price * (discount_percent / 100)
            return self.price - discount_amount
        return self.price

class iPhone(AppleProduct):
    def __init__(self, model_name, storage_capacity, color, price, operating_system, camera_resolution):
        super().__init__("iPhone", model_name, storage_capacity, color, price, operating_system)
        self.camera_resolution = camera_resolution

    def take_photo(self):
        return f"{self.model_name} takes a stunning photo with its {self.camera_resolution} camera."

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} | Camera: {self.camera_resolution}"

class iPad(AppleProduct):
    def __init__(self, model_name, storage_capacity, color, price, operating_system, has_apple_pencil):
        super().__init__("iPad", model_name, storage_capacity, color, price, operating_system)
        self.has_apple_pencil = has_apple_pencil

    def draw(self):
        return f"{self.model_name} is perfect for drawing" + (" with Apple Pencil support." if self.has_apple_pencil else ".")

    def display_info(self):
        base_info = super().display_info()
        pencil_info = "Apple Pencil Supported" if self.has_apple_pencil else "No Apple Pencil Support"
        return f"{base_info} | {pencil_info}"

class MacBook(AppleProduct):
    def __init__(self, model_name, storage_capacity, color, price, operating_system, processor):
        super().__init__("MacBook", model_name, storage_capacity, color, price, operating_system)
        self.processor = processor

    def run_application(self):
        return f"{self.model_name} is running applications seamlessly on its {self.processor} processor."

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} | Processor: {self.processor}"

def save_apple_products_to_csv(products, filename="data/apple_products.csv"):
    """Save the list of AppleProduct objects to a CSV file in the data folder."""
    ensure_data_folder()
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["Product Type", "Model Name", "Storage Capacity", "Color", "Price", "Operating System", "Details"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow({
                "Product Type": product.product_type,
                "Model Name": product.model_name,
                "Storage Capacity": product.storage_capacity,
                "Color": product.color,
                "Price": product.price,
                "Operating System": product.operating_system,
                "Details": product.display_info()
            })

def main():
    # Create 10 examples of Apple products
    products = [
        iPhone("iPhone 12", "128GB", "Black", 799, "iOS 14", "12MP"),
        iPhone("iPhone 13", "256GB", "White", 899, "iOS 15", "12MP Dual"),
        iPhone("iPhone SE", "64GB", "Red", 399, "iOS 15", "12MP"),
        iPhone("iPhone 14 Pro", "512GB", "Deep Purple", 1099, "iOS 16", "48MP"),
        iPad("iPad Pro", "256GB", "Space Gray", 1099, "iPadOS 15", True),
        iPad("iPad Air", "64GB", "Silver", 599, "iPadOS 15", False),
        iPad("iPad Mini", "64GB", "Gold", 499, "iPadOS 15", False),
        MacBook("MacBook Air", "256GB", "Gold", 999, "macOS Monterey", "M1"),
        MacBook("MacBook Pro 13", "512GB", "Space Gray", 1299, "macOS Monterey", "M1"),
        MacBook("MacBook Pro 16", "1TB", "Silver", 2399, "macOS Monterey", "Intel i9")
    ]

    # Display each product's info and demonstrate unique behavior
    for product in products:
        print(product.display_info())
        if isinstance(product, iPhone):
            print(product.take_photo())
        elif isinstance(product, iPad):
            print(product.draw())
        elif isinstance(product, MacBook):
            print(product.run_application())
        print("-" * 50)

    # Save all products to CSV
    save_apple_products_to_csv(products)
    print("Apple product data saved to 'data/apple_products.csv'.")

if __name__ == "__main__":
    main()
