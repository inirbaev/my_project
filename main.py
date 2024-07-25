import mysql.connector


while True:
    command = input("Command: ")
    if command == 'help':
        print('login')
        print('register')
        print()

    if command == 'login':
        login = input("Login: ")
        password = input("Password: ")
        mydb = mysql.connector.connect(
            host='bzd5rg7mowmfjo4qvaji-mysql.services.clever-cloud.com',
            user='uot2ukcx5pvpvwml',
            password='VjIWzs0uQcWAZuS3LOmw',
            database='bzd5rg7mowmfjo4qvaji'
        )

        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM users WHERE login = "' + login + '" AND password = "'+password+'"')
        myresult = mycursor.fetchall()
        if len(myresult) != 0:
            print("Welcome")
            print()
        else:
            print("Wrong login or password")
            print()

    if command == 'register':
        login = input("Login: ")
        password = input("Password: ")
        mydb = mysql.connector.connect(
            host='bzd5rg7mowmfjo4qvaji-mysql.services.clever-cloud.com',
            user='uot2ukcx5pvpvwml',
            password='VjIWzs0uQcWAZuS3LOmw',
            database='bzd5rg7mowmfjo4qvaji'
        )

        mycursor = mydb.cursor()
        mycursor.execute('INSERT INTO users (login, password) VALUES ("'+login+'", "'+password+'")')
        mydb.commit()
        print('registred')
        print()

    if command == 'exit':
        break

    if command == 'author':
        print('Ali Inirbaev')

    if command == 'version':
        print('1.0')