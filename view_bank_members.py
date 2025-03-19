#!/usr/bin/env python3
"""
Interactive Bank Member Viewer
Author: SNN
Unique ID: VIEW20241105  <- Watermark Here!

This script allows users to interactively view stored bank member details from the CSV file (data/bank_members.csv).
It loads the data, displays a list of bank member names, and prompts the user to select a member by name to view their account details.
Type 'exit' to quit the program.
"""

import os
import csv

def ensure_data_folder():
    """Ensure that the 'data' folder exists."""
    if not os.path.exists("data"):
        print("Error: 'data' folder not found. Please run the data generation script first.")
        exit(1)

def load_bank_members_from_csv(filename="data/bank_members.csv"):
    """
    Load bank member data from the CSV file and return a dictionary.
    Each key is a member's name (in lowercase) and the value is a dictionary containing:
      - Personal details (Unique ID, Name, Age, ID Number, Date of Entry, Occupation)
      - A list of associated accounts (each with registration date, account number, type, and balance)
    """
    members = {}
    try:
        with open(filename, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["Name"]
                key = name.lower()
                if key not in members:
                    members[key] = {
                        "Unique ID": row["Unique ID"],
                        "Name": row["Name"],
                        "Age": row["Age"],
                        "ID Number": row["ID Number"],
                        "Date of Entry": row["Date of Entry"],
                        "Occupation": row["Occupation"],
                        "Accounts": []
                    }
                # Append account information for this member
                account_info = {
                    "Account Date": row["Account Date"],
                    "Account Number": row["Account Number"],
                    "Account Type": row["Account Type"],
                    "Account Balance": row["Account Balance"]
                }
                members[key]["Accounts"].append(account_info)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit(1)
    return members

def display_member_names(members):
    """Print the list of bank member names available in the CSV file."""
    print("\nList of Bank Members:")
    for key in sorted(members.keys()):
        print(" -", members[key]["Name"])

def display_member_details(member):
    """Print the detailed information for a bank member along with their account details."""
    print("\nMember Details:")
    print(f"Unique ID: {member['Unique ID']}")
    print(f"Name: {member['Name']}")
    print(f"Age: {member['Age']}")
    print(f"ID Number: {member['ID Number']}")
    print(f"Date of Entry: {member['Date of Entry']}")
    print(f"Occupation: {member['Occupation']}")
    print("Accounts:")
    for account in member["Accounts"]:
        print(f"  - Account Number: {account['Account Number']}")
        print(f"    Type: {account['Account Type']}")
        print(f"    Registration Date: {account['Account Date']}")
        print(f"    Balance: ${float(account['Account Balance']):.2f}")
        print("")

def main():
    ensure_data_folder()
    csv_filename = "data/bank_members.csv"
    members = load_bank_members_from_csv(csv_filename)
    
    # Display the list of available bank member names
    display_member_names(members)
    
    # Interactive loop: prompt user to select a member to view details or exit
    while True:
        user_input = input("\nEnter the name of the bank member to display their account details (or type 'exit' to quit): ").strip()
        if user_input.lower() == "exit":
            print("Exiting program.")
            break
        key = user_input.lower()
        if key in members:
            display_member_details(members[key])
        else:
            print(f"No bank member found with the name '{user_input}'. Please try again.")

if __name__ == "__main__":
    main()
