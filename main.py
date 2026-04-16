users: list = [
    {"username": "Oliwia", 'location':'Łódź','posts':1, 'usermessage':['życzenia','kocham legie','sprzedam opla', 'kiwi']},
    {"username": "Paweł", 'location':'Ostróda','posts':2, 'usermessage':['życzenia1','kocham legie1','sprzedam opla1']},
    {"username": "Eliza", 'location':'Radom','posts':3, 'usermessage':['życzenia2','kocham legie2']},
    {"username": "Filip", 'location':'Dęblin','posts':4, 'usermessage':['życzenia3','kocham legie3','sprzedam opla3', 'kiwi']},
]

for user in users[1:]:
    print(f'Twój znajomy {user['username']} z miejscowości {user["location"]} opublikował {user['posts']} wiadomości. Ostatnia wiadomość: {user["usermessage"][-1]}.')
#     twój znajomy filip z miejscowości Dęblin opublikował jeden post o treści: życzenia
