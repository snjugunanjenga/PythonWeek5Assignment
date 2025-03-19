#!/usr/bin/env python3
"""
Banking Encapsulation Demonstration
Author: SNN
Unique ID: BANK20241105  <- Watermark Here!

This script demonstrates encapsulation in a banking context.
It simulates 20 bank members, each with personal details and one or more bank accounts.
Account balances are encapsulated (hidden) and accessed via getter methods.
The program allows the user to repeatedly select a member by name to view account details, 
or type 'exit' to quit. All data is saved to a CSV file in the 'data' folder.
"""

import os
import csv
import random
from datetime import datetime, timedelta

# ---------------- Helper Functions ----------------

def ensure_data_folder():
    """Ensure that the 'data' folder exists."""
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Created 'data' folder.")

def generate_random_date(start_year=2020, end_year=2023):
    """Generate a random date between start_year and end_year."""
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randrange(delta.days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def generate_account_number():
    """Generate a random 10-digit account number as a string."""
    return ''.join(random.choices("0123456789", k=10))

# ---------------- Account Class ----------------

class Account:
    def __init__(self, date_of_registration, account_number, account_type, account_balance):
        self.date_of_registration = date_of_registration
        self.account_number = account_number
        self.account_type = account_type
        self._account_balance = account_balance  # Encapsulated attribute

    @property
    def account_balance(self):
        """Getter for the account balance."""
        return self._account_balance

    def display_account_info(self):
        """Return a string displaying account details."""
        return (f"Account Number: {self.account_number} | Type: {self.account_type} | "
                f"Registered: {self.date_of_registration} | Balance: ${self.account_balance:.2f}")

# ---------------- BankMember Class ----------------

class BankMember:
    def __init__(self, unique_ID, name, age, id_number, date_of_entry, occupation):
        self.unique_ID = unique_ID
        self.name = name
        self.age = age
        self.id_number = id_number
        self.date_of_entry = date_of_entry
        self.occupation = occupation
        self.accounts = []  # List to hold multiple Account objects

    def add_account(self, account):
        """Add an account to the member's list of accounts."""
        self.accounts.append(account)

    def display_member_info(self):
        """Return a string displaying the member's details and their account info."""
        info = (f"Unique ID: {self.unique_ID}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"ID Number: {self.id_number}\n"
                f"Date of Entry: {self.date_of_entry}\n"
                f"Occupation: {self.occupation}\n"
                f"Accounts:\n")
        for acc in self.accounts:
            info += "  - " + acc.display_account_info() + "\n"
        return info

# ---------------- Main Program ----------------

def create_dummy_bank_members():
    """Create 20 dummy bank members with random account data."""
    names = [
        "Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah", "Ian", "Julia",
        "Kevin", "Laura", "Michael", "Nina", "Oscar", "Paula", "Quentin", "Rachel", "Steven", "Tina"
    ]
    occupations = ["Engineer", "Teacher", "Doctor", "Lawyer", "Artist", "Scientist", "Nurse", "Manager", "Clerk", "Designer"]
    account_types = ["Savings", "Current", "Business", "Joint_Account", "SACCO_Savings"]
    bank_members = []
    
    for i, name in enumerate(names, start=1):
        unique_ID = f"BM{i:03d}"
        age = random.randint(21, 70)
        id_number = ''.join(random.choices("0123456789", k=8))
        date_of_entry = generate_random_date(2015, 2020)
        occupation = random.choice(occupations)
        member = BankMember(unique_ID, name, age, id_number, date_of_entry, occupation)
        
        # Each member gets between 1 to 3 accounts
        for _ in range(random.randint(1, 3)):
            date_of_registration = generate_random_date(2018, 2023)
            account_number = generate_account_number()
            account_type = random.choice(account_types)
            account_balance = round(random.uniform(100.0, 10000.0), 2)
            account = Account(date_of_registration, account_number, account_type, account_balance)
            member.add_account(account)
        
        bank_members.append(member)
    
    return bank_members

def save_bank_members_to_csv(members, filename="data/bank_members.csv"):
    """Save all bank member details along with their accounts to a CSV file."""
    ensure_data_folder()
    with open(filename, "w", newline="") as csvfile:
        fieldnames = [
            "Unique ID", "Name", "Age", "ID Number", "Date of Entry", "Occupation",
            "Account Date", "Account Number", "Account Type", "Account Balance"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for member in members:
            for account in member.accounts:
                writer.writerow({
                    "Unique ID": member.unique_ID,
                    "Name": member.name,
                    "Age": member.age,
                    "ID Number": member.id_number,
                    "Date of Entry": member.date_of_entry,
                    "Occupation": member.occupation,
                    "Account Date": account.date_of_registration,
                    "Account Number": account.account_number,
                    "Account Type": account.account_type,
                    "Account Balance": account.account_balance
                })

def main():
    # Create dummy data for 20 bank members
    members = create_dummy_bank_members()
    
    # Display the list of member names
    print("List of Bank Members:")
    for member in members:
        print(f" - {member.name}")
    
    # Allow user to repeatedly view member details until they choose to exit
    while True:
        chosen_name = input("\nEnter the name of the bank member to display their account details (or type 'exit' to quit): ").strip()
        if chosen_name.lower() == "exit":
            break
        selected_member = next((member for member in members if member.name.lower() == chosen_name.lower()), None)
        if selected_member:
            print("\nMember Details:")
            print(selected_member.display_member_info())
        else:
            print(f"No bank member found with the name '{chosen_name}'.")
    
    # Save all bank member data to CSV
    save_bank_members_to_csv(members)
    print("\nBank member data saved to 'data/bank_members.csv'.")

if __name__ == "__main__":
    main()
