username = input('What is your username? ')
password = input('What is your password? ')
password_lenght = len(password)
hidden_password = '*' * password_lenght

print(f'{username}, your password, {hidden_password}, length is {password_lenght}')
