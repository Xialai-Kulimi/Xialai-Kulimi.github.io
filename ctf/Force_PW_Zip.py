import os
import Crypto

file_name = raw_input('What is file\'s name?')

char_list = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z ' \
            '0 1 2 3 4 5 6 7 8 9 ` ~ ! @ # $ % ^ & * ( ) _ + = - [ ] { } ; : , < . > / ? \' \" \ |'.split(' ')

char_dict = {}

a = 0
for letter in char_list:
    char_dict[letter] = a
    a += 1

print('Char num:', len(char_list))

for letter in char_list:
    os.system('unzip -P ' + letter + ' ' + file_name)

password = ''
while True:

    os.system('unzip -P ' + password + ' ' + file_name)
