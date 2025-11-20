
from datetime import date

donors = {}
users = {
    "treasurer": {"username": "treasurer", "password": "12345"},
    "leader": {"username": "leader", "password": "admin"}
}

def add_donation():
    name = input("Enter donor name: ")
    amount = float(input("Enter donation amount: ₱"))
    donation_date = input("Enter donation date (YYYY-MM-DD): ") or str(date.today())

    if name not in donors:
        donors[name] = []

    donors[name].append({"amount": amount, "date": donation_date})

    print("\n--- DONATION RECORDED ---")
    print(f"Name: {name}")
    print(f"Amount Donated: ₱{amount:.2f}")
    print(f"Date Donated: {donation_date}")

    print(f"\nThank you, {name}, for donating ₱{amount:.2f} on {donation_date}!\n")

def edit_donation():
    if not donors:
        print("No donations to edit yet.")
        return

    print("\n--- Donor List ---")
    all_entries = []
    index = 1

    for donor, entries in donors.items():
        for entry in entries:
            print(f"{index}. {donor} - ₱{entry['amount']:.2f} | Date: {entry['date']}")
            all_entries.append((donor, entry))
            index += 1

    choice = int(input("\nEnter number to edit: "))
    donor_name, donation_entry = all_entries[choice - 1]

    new_name = input("New donor name (Enter to keep): ") or donor_name
    new_amount = input("New amount (Enter to keep): ")
    new_date = input("New date (YYYY-MM-DD or Enter to keep): ") or donation_entry["date"]

    if new_amount:
        donation_entry["amount"] = float(new_amount)
    donation_entry["date"] = new_date

    if new_name != donor_name:
        if new_name not in donors:
            donors[new_name] = []
        donors[new_name].append(donation_entry)
        donors[donor_name].remove(donation_entry)
        if not donors[donor_name]:
            del donors[donor_name]

    print("Donation updated successfully!")

def view_donors():
    if not donors:
        print("No donations yet.")
        return

    print("\n--- DONOR LIST ---")
    for donor, entries in donors.items():
        print(f"\nDonor: {donor}")
        total = sum(e["amount"] for e in entries)
        for entry in entries:
            print(f"  - ₱{entry['amount']:.2f} on {entry['date']}")
        print(f"Total: ₱{total:.2f}")

def treasurer_menu():
    while True:
        print("\n--- Treasurer Menu ---")
        print("1. Add Donation")
        print("2. View Donors")
        print("3. View Total Donations")
        print("4. Edit Donor Info")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            add_donation()
        elif choice == "2":
            view_donors()
        elif choice == "3":
            total = sum(entry["amount"] for entries in donors.values() for entry in entries)
            print(f"Total Funds Collected: ₱{total:.2f}")
        elif choice == "4":
            edit_donation()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

def leader_menu():
    while True:
        print("\n--- Organization Leader Menu ---")
        print("1. View Donors")
        print("2. View Total Funds")
        print("3. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            view_donors()
        elif choice == "2":
            total = sum(entry["amount"] for entries in donors.values() for entry in entries)
            print(f"Total Funds Raised: ₱{total:.2f}")
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

def login(role):
    print(f"\n--- {role.capitalize()} Login ---")
    username = input("Username: ")
    password = input("Password: ")

    if username == users[role]["username"] and password == users[role]["password"]:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Incorrect username or password.")
        return False

while True:
    print("\n===== Donation Tracking System =====")
    print("1. Treasurer")
    print("2. Organization Leader")
    print("3. Exit")

    role = input("Choose your role: ")

    if role == "1":
        if login("treasurer"):
            treasurer_menu()
    elif role == "2":
        if login("leader"):
            leader_menu()
    elif role == "3":
        print("Exiting system... Thank you!")
        break
    else:
        print("Invalid choice, please try again.")