your_account = []  # Stores user data

# Function for user registration and login
def registration():
    print(r"""
  __________________________________________________________
 /                                                            \
|   / \__                                                      |
|  (    @\___    Welcome To PAWFECT PALS!!!                   |
|  /         O   Rescue a friend, gain a forever companion. 🐾  |
| /   (_____/                                                  |
|/_____/   U                                                   |
 \____________________________________________________________/
""")

    while True:
        ask_user = input("\nLogin or Signup: ").strip().lower()

        if ask_user in ["signup", "sign up"]:
            user_name = input("Enter your Name: ")
            
            #Email Loop
            while True:
                user_email = input("Enter your email address: ")
                if "@gmail.com" in user_email:
                    break
                else:
                    print("Invalid email! It must contain '@gmail.com' Please try again.")
            
            while True:
                user_password = input("Enter your password: ")
                if any(char.isupper() for char in user_password) and any(char.isdigit() for char in user_password):
                    break
                else:
                    print("Password must contain at least one uppercase letter and one number. Please try again.")     
        
            user_age = int(input("Enter your age: "))

            if user_age < 18:
                print("\nApologies, we cannot accept users under 18.")
                continue

            personal_info = {
                "name": user_name,
                "email": user_email,
                "password": user_password,
                "age": user_age
            }

            your_account.append(personal_info)
            print("\nYou are now registered!!")

        elif ask_user in ["login", "log in"]:
            if not your_account:
                print("\nNo registered users yet! Please sign up first.")
                continue

            user_email = input("Enter your email address: ")
            user_password = input("Enter your password: ")

            for user in your_account:
                if user["email"] == user_email and user["password"] == user_password:
                    print(f"\nWelcome {user['name']}!")
                    return  # Login successful, exit function
            else:
                print("\nWrong credentials! Please try again.")

        else:
            print("\nInvalid input. Please type 'Login' or 'Signup'.")

# List of pets for adoption
pets = [
    {'id': 1, 'name': 'Buddy', 'breed': 'Golden Retriever', 'age': 3, 'adopted': False},
    {'id': 2, 'name': 'Mittens', 'breed': 'Tabby Cat', 'age': 2, 'adopted': False},
    {'id': 3, 'name': 'Bella', 'breed': 'Bulldog', 'age': 5, 'adopted': False},
    {'id': 4, 'name': 'Oreo', 'breed': 'Syberian Husky', 'age': 3, 'adopted': False},
    {'id': 5, 'name': 'Orion Pax', 'breed': 'Cybertronian', 'age': 5, 'adopted': False},
    {'id': 6, 'name': 'Angstrom', 'breed': 'Viltrumite', 'age': 5, 'adopted': False},
    {'id': 7, 'name': 'Reznor', 'breed': 'Tilapia  Cat', 'age': 2, 'adopted': False},
    {'id': 8, 'name': 'Rixton', 'breed': 'Aspin', 'age': 5, 'adopted': False},
    {'id': 9, 'name': 'Roger', 'breed': 'Alaskan Malamute', 'age': 2, 'adopted': False},
    {'id': 10, 'name': 'Asteroid Destroyer', 'breed': 'Persian Cat', 'age': 3, 'adopted': False},
]

# Function to display available pets
def display_pets():
    print("\nAvailable Pets for Adoption:")
    for pet in pets:
        status = "Adopted" if pet['adopted'] else "Available"
        print(f"{pet['id']}. {pet['name']} - {pet['breed']} ({pet['age']} years old) [{status}]")

# Function to adopt a pet
def adopt_pet():
    display_pets()
    pet_id = int(input("\nEnter the ID of the pet you want to adopt: "))
    pet = next((p for p in pets if p['id'] == pet_id), None)

    if pet and not pet['adopted']:
        pet['adopted'] = True
        print(f"\nYou have successfully adopted {pet['name']}!")
        print("\n========== Adoption Receipt ==========")
        print(f"Pet Name     : {pet['name']}")
        print(f"Breed        : {pet['breed']}")
        print(f"Age          : {pet['age']} years")
        print("Thank you for giving a loving home!")
        print("======================================")
    else:
        print("\nPet not found or already adopted.")

# Function to search for pets by breed
def search_pets():
    breed = input("\nEnter the breed to search for: ")
    print(f"\nSearching for pets with breed '{breed}'...")

    found_pets = [pet for pet in pets if breed.lower() in pet['breed'].lower() and not pet['adopted']]
    if found_pets:
        for pet in found_pets:
            print(f"{pet['name']} - {pet['breed']} ({pet['age']} years old)")
    else:
        print(f"\nNo available pets found with the breed '{breed}'.")

# Main menu function
def main():
    registration()  # Require login first
    while True:
        print("\n===== Pet Adoption Console =====")
        print("1. View Available Pets")
        print("2. Adopt a Pet")
        print("3. Search Pets by Breed")
        print("4. Exit")

        choice = input("\nChoose an option (1/2/3/4): ")

        if choice == '1':
            display_pets()
        elif choice == '2':
            adopt_pet()
        elif choice == '3':
            search_pets()
        elif choice == '4':
            print("\nThank you for visiting PAWFECT PALS! Have a great day! 🐶🐱✨")
            break
        else:
            print("\nInvalid option. Please choose 1, 2, 3, or 4.")

# Run the application
if __name__ == '__main__':
    main()