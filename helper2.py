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


def parse_command(full_command):
    split_command = full_command.split(' ', 1)
    primary_command = split_command[0]
    data = split_command[1] if len(split_command) > 1 else ""

    function_to_execute = None
    for func, cmds in COMMANDS.items():
        if primary_command in cmds:
            function_to_execute = func
            break

    if not function_to_execute and len(full_command.split()) > 1:
        potential_two_word_command = " ".join(full_command.split()[:2])
        for func, cmds in COMMANDS.items():
            if potential_two_word_command in cmds:
                function_to_execute = func
                break

    return function_to_execute, data


COMMANDS = {
    hello: ['hello'],
    add_contact: ['add'],
    change_phone: ['change'],
    get_phone: ['phone'],
    show_all: ['show all'],
    good_bye: ['good bye', 'close', 'exit']
}

phonebook = {}

def main():
    print("Bot Assistant is here to help you!")
    while True:
        full_command = input("Enter a command: ").strip().lower()
        function_to_execute, data = parse_command(full_command)

        
        
        if function_to_execute:
            if function_to_execute in [hello, show_all, good_bye]:
                response = function_to_execute()
            else:
                response = function_to_execute(data)
            print(response)
            if function_to_execute == good_bye:
                break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()