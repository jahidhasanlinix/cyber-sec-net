import secrets
import string

def pwd_gen(pwd_len):

    char = string.ascii_letters + string.digits

    sec_pwd = ''.join(secrets.choice(char) for i in range(pwd_len))

    return sec_pwd

def main():

    user_pwd_len = int(input("Enter number of digits password: "))

    print("Password Generated for: ", pwd_gen(user_pwd_len))

main()