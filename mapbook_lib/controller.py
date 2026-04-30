def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f'Twój znajomy {user['username']} z miejscowości {user["location"]} opublikował {user['posts']} wiadomości. Ostatnia wiadomość: {user["usermessage"][-1]}.')

def add_user(users_data: list)-> None:
    name = input('Podaj Imie: ')
    location = input('Podaj lokalizacje: ')
    posts = int(input('Podaj ilość postów: '))
    usermessage = ['']
    users_data.append({"username": name, 'location': location, 'posts': posts,
         'usermessage': usermessage})

def remove_user(users_data: list) -> None:
    name = input('Podaj imie użytkownika do usunięcia: ')
    for user in users_data:
        if user["username"] == name:
            users_data.remove(user)


