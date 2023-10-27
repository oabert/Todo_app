"""filepath as constant var"""
FILEPATH = 'todos_list.txt'


def get_read_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_input, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_input)


"""called only when functions.py executed directly, not as imported file"""
if __name__ == "__main__":
    print("Hello, I am locked in functions.py message")