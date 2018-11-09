def login():
    filename = open('users.txt')
    users = filename.readlines()
    dict1 = {}
    for i in users:
        Key, Value = i.strip().split(':')
        dict1[Key]= Value
    print(dict1)
    userName = input('Enter username: ')
    if userName in dict1.keys():
        password = input('Enter password :')
        if password == dict1[userName]:
            print("You can login")
        else:
            print("You have entered a wrong password")
    else:
        print('You have enter a wrong username')
if __name__ =="__main__":
    login()