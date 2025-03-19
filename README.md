# Python OOP Assignments and Encapsulation Demonstration

**Author: SNN**

This repository contains various Python programs demonstrating key Object-Oriented Programming (OOP) principles: **Class Design, Inheritance, Polymorphism, and Encapsulation**.

## Table of Contents
- [Assignment 1: Apple Products (Class Design & Inheritance)](#assignment-1-apple-products-class-design--inheritance)
- [Assignment 2: Movable Objects (Polymorphism)](#assignment-2-movable-objects-polymorphism)
- [Encapsulation in Banking System](#encapsulation-in-banking-system)
- [Interactive Bank Member Viewer](#interactive-bank-member-viewer)

---
## Assignment 1: Apple Products (Class Design & Inheritance)

### **File:** `apple_products.py`
**Description:**
This script models Apple products (iPhones, iPads, and MacBooks) using **inheritance**. A base class `AppleProduct` defines common attributes, while subclasses (`iPhone`, `iPad`, and `MacBook`) introduce unique characteristics.

### **Key Features:**
- **Class Hierarchy:**
  - `AppleProduct` (Base class)
  - `iPhone` (Child class with camera-specific attributes)
  - `iPad` (Child class with stylus support features)
  - `MacBook` (Child class with processor details)
- **CSV Data Handling:**
  - Saves a list of Apple products into a CSV file `data/apple_products.csv`.
- **Watermark:** `DNN19600118` embedded to identify original work.

### **How to Run:**
```sh
python apple_products.py
```
This will:
- Generate and display details of various Apple products.
- Save the data into `data/apple_products.csv`.

---
## Assignment 2: Movable Objects (Polymorphism)

### **File:** `movements.py`
**Description:**
This program demonstrates **polymorphism** by defining various objects (both living and non-living) that move in different ways.

### **Key Features:**
- **Base Class:** `Movements` with an abstract `move()` method.
- **Subclasses Implementing Different Movements:**
  - `Man`: Moves by **walking** 🚶
  - `Dog`: Moves by **running** 🐕
  - `Cat`: Moves by **jumping** 🐈
  - `Crocodile`: Moves by **crawling** 🐊
  - `Bird`: Moves by **flying** 🕊️
  - `Car`: Moves by **driving** 🚗
  - `Train`: Moves by **rail transport** 🚆
  - `Plane`: Moves by **flying** ✈️
  - `Ship`: Moves by **sailing** 🚢
  - `Drone`: Moves by **hovering** 🚁
- **CSV Data Handling:** Saves all movement types into `data/movable_objects.csv`.
- **Watermark:** `DNN18011960` embedded.

### **How to Run:**
```sh
python movements.py
```
This will:
- Display movement styles of all objects.
- Save the data into `data/movable_objects.csv`.

---
## Encapsulation in Banking System

### **File:** `banking_encapsulation.py`
**Description:**
This script demonstrates **encapsulation** by storing and restricting access to bank account details.

### **Key Features:**
- **Encapsulation:**
  - `BankMember` class holds personal details (name, age, ID, etc.).
  - `BankAccount` class restricts direct access to **account balances**.
- **Data Storage:**
  - Bank members and their accounts are saved into `data/bank_memberss.csv`.
- **Watermark:** Unique ID `BNK20241105`.

### **How to Run:**
```sh
python banking_encapsulation.py
```
This will:
- Generate random bank members and accounts.
- Save details into `data/bank_members.csv`.

---
## Interactive Bank Member Viewer

### **File:** `view_bank_members.py`
**Description:**
This script allows users to **view stored bank member details interactively** by selecting a name from the generated list.

### **Key Features:**
- **User Interaction:** Prompts the user to input a member name.
- **CSV Data Reading:** Fetches details from `data/bank_members.csv`.
- **Encapsulation Enforcement:** Ensures account balances are displayed securely.

### **How to Run:**
```sh
python view_bank_members.py
```
Users can:
- View details of multiple bank members.
- Exit the program anytime.

---
## Conclusion
This repository demonstrates essential **OOP principles (Encapsulation, Inheritance, and Polymorphism)** through real-world examples.

For improvements or contributions, feel free to submit a pull request! 🚀

