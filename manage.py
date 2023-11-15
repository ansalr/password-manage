from cryptography.fernet import Fernet


def load_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key

password = input("what is passowrd? ")
key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,psd = data.split('|')
            print('user : ',user,'\nPassword : ',psd)

def add():
    user_name = input('user name : ')
    user_password = input('user password : ')

    with open('password.txt','a') as f:
        f.write(user_name +'|'+ user_password + '\n')



while True:
    mode = input("""To add password enter 'add' \nTo view old password enter 'view' \nTo quit enter 'q'\nEnter mode : """).lower()

    if mode == 'q':
        break

    elif mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print("invalid mode !! ")
        continue
