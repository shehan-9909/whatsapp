clear
from twilio.rest import Client
import sys
import os
#shehan lahiru
#Dont copyright 

print("\033[0;36m "" ░P░A░N░D░O░R░A░")
print("\033[0;36m "" ")
print("\033[0;36m "" ωнαтsαρρ sραм")
print("")
print("\033[0;36m "" ")
token = input("Enter token")
id = input ("Enter usar id")
t = input("Enter send message: ")
p = input("Enter a number: ")
def main():
    os.system("clear")
    account_sid = id
    auth_token = token
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         from_='whatsapp:+14155238886',
                         body= t,
                         to=p
                 )


    os.system('figlet END  PROGERAM')
    again()


def again():
    again = input('\033[1;0;40m\nDo You want use again (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()
