import random
import sys
import os
import time 
os.system('clear')
print('''
\033[0;33m    I--------------I   
\033[0;33m    I--------------I          \033[0;31m   ██████╗ ██████╗ ██████╗  ██████╗███╗   ██╗ █████╗      ██╗  ██╗
\033[0;33m   .-'            '-.         \033[0;31m ██╔════╝██╔═══██╗██╔══██╗██╔═══██╗████╗  ██║██╔══██╗     ╚██╗██╔╝
\033[0;33m  / --.-.--,---,.--.,\        \033[0;31m ██║     ██║   ██║██████╔╝██║   ██║██╔██╗ ██║███████║█████╗╚███╔╝
\033[0;33m /--.-.--,---,.--.,-- \       \033[0;31m ██║     ██║   ██║██╔══██╗██║   ██║██║╚██╗██║██╔══██║╚════╝██╔██╗
\033[0;33m |--------------------|       \033[0;31m ╚██████╗╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║  ██║     ██╔╝ ██╗
\033[0;33m |       OUR          |       \033[0;31m  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═╝  ╚═╝
\033[0;33m |                    |
\033[0;33m |  SCRIPTS - LIKE    |                        \033[0;31m ███╗   ███╗ █████╗ ██╗██╗
\033[0;33m |                    |                        \033[0;31m ████╗ ████║██╔══██╗██║██║
\033[0;33m |     MEDICINE       |                        \033[0;31m ██╔████╔██║███████║██║██║
\033[0;33m |                    |                        \033[0;31m ██║╚██╔╝██║██╔══██║██║██║ 
\033[0;33m | [ Pharmacy Only ]  |                        \033[0;31m ██║ ╚═╝ ██║██║  ██║██║███████╗
\033[0;33m |____________________|                        \033[0;31m ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
\033[0;33m |.,--.-.--,---,.--.-.|   
\033[0;33m |--.-.--,---,.--.,--.|
\033[0;33m '--------------------'                             
                                                                                                                       
''')                                                                                               
print('''
                           \033[0;32m ╔--─────────────────────────────────--╗
                           \033[0;32m |      [#] : Coded By Max-IQ          |
                           \033[0;32m |                                     |
                           \033[0;32m |      FB :facebook.com/GOV.iraq2     |
                           \033[0;32m ╚--─────────────────────────────────--╝
''')                                                                                               
                                                                                  

chars2 = '0123456789abcdefghijklmnpqrstuvwxyz' 

print('=========================================')
email2 = input ('Write email domain here exm:(@gmail.com)# ')
user   = input('write The visible letters in email#  ')
user2  = user 
amount = input('Type number of email# ')
amount = int(amount)
length2 = input('How Much star in email# ')
email = (email2)
length2 = int(length2)
print ('We start nOw')
time.sleep(2)


print('==================================')

for password in range(amount):
    password = ''
    
    
    for item in range(length2):
         password = ''
    for item in range(length2):
        password += random.choice(chars2)



    print (user+password+email)
    with open('email.txt', 'a') as x:
     x.write(user2 + password + email +'\n')


