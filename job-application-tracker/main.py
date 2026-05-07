import os

def add_application():
    company = input("Company Name: ")
    position = input("Position: ")
    status = input("Status (Applied/Interview/Rejected): ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{company},{position},{status}\n")

    print("Application saved successfully!\n")



def view_applications():
    if not os.path.exists(FILE_NAME):
        print("No applications found.\n")
        return

    with open(FILE_NAME, "r") as file:
        applications = file.readlines()

    if not applications:
        print("No applications saved yet.\n")
        return

    print("\n--- APPLICATIONS ---")

    for app in applications:
        company, position, status = app.strip().split(",")
        print(f"Company: {company}")
        print(f"Position: {position}")
        print(f"Status: {status}")
        print("---------------------")



def main():
    while True:
        print("1. Add Application")
        print("2. View Applications")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")


main()