flag = b'WXN{'

letter_list = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y ' \
              'Z 0 1 2 3 4 5 6 7 8 9 } _'.split(' ')

found = False

i = 4

for target in [354029087, 1915420169, 3254692394, 2815960165, 4110859573, 3306584243, 1848860968]:

    for a in letter_list:
        for b in letter_list:
            # print(a+b)
            flag_copy = flag + bytes(a + b, 'utf8')

            if int('\n'.join(str(_) for _ in [(lambda s: (int(__import__('hashlib').sha224(s).hexdigest(), 16) ^ int(__import__('hashlib').sha256(s).hexdigest(), 16) ^ int(__import__('hashlib').sha384(s).hexdigest(), 16) ^ int(__import__('hashlib').sha512(s).hexdigest(), 16)) & 0xFFFFFFFF)(flag_copy[i:i + 2])])) == target:
                # print('found')
                flag = flag_copy
                found = True
                break
        if found:
            break
    if not found:
        print('bullshit'+str(target))
        print(flag)
    found = False
    i += 2
print(str(flag, 'utf'))
