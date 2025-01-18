import os

def add_contact(name, phone, email):
    """Додає новий контакт до файлу."""
    with open("contacts.txt", "a") as file:
        file.write(f"Ім'я: {name}, Телефон: {phone}, Електронна пошта: {email}\n")
    print("Контакт успішно додано!")

def view_contacts():
    """Переглядає всі контакти з файлу."""
    if not os.path.exists("contacts.txt"):
        print("Файл контактів не знайдено.")
        return

    with open("contacts.txt", "r") as file:
        contacts = file.readlines()
        if not contacts:
            print("Контакти не знайдено.")
        else:
            print("Список контактів:")
            for contact in contacts:
                print(contact.strip())

def main():
    """Головна функція програми."""
    while True:
        print("\nВиберіть дію:")
        print("1. Додати новий контакт")
        print("2. Переглянути список контактів")
        print("3. Вийти")

        choice = input("Ваш вибір (1/2/3): ")

        if choice == "1":
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            email = input("Введіть електронну пошту: ")
            add_contact(name, phone, email)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()