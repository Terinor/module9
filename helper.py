def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Name not found."
        except ValueError:
            return "Wrong input format. Provide name and phone number separated by a space."
        except IndexError:
            return "Provide all required data."
    return inner

phonebook = {}

@input_error
def add_contact(data):
    name, phone = data.split()
    phonebook[name] = phone
    return "Contact added."

@input_error
def change_phone(data):
    name, new_phone = data.split()
    if name not in phonebook:
        raise KeyError
    phonebook[name] = new_phone
    return "Phone number updated."

@input_error
def get_phone(name):
    return phonebook[name]

@input_error
def show_all():
    result = ""
    for name, phone in phonebook.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def hello():
    return "How can I help you?"

def good_bye():
    return "Good bye!"

# Словник для управління командами
COMMANDS = {
    "hello": hello,
    "add": add_contact,
    "change": change_phone,
    "phone": get_phone,
    "show all": show_all,
    "good bye": good_bye,
    "close": good_bye,
    "exit": good_bye
}

def main():
    print("Bot Assistant is here to help you!")
    while True:
        command = input("Enter a command: ").strip().lower()

        # Якщо команда з двох слів
        command_name = " ".join(command.split()[:2])
        if command_name not in COMMANDS:
            command_name = command.split()[0]  # використовуємо лише перше слово
        data = " ".join(command.split()[len(command_name.split()):])

        # Якщо команда в словнику, виконуємо її
        if command_name in COMMANDS:
            response = COMMANDS[command_name](data) if data else COMMANDS[command_name]()
            print(response)

            if command_name in ["good bye", "close", "exit"]:
                break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
