f = open('decode.py', 'r')
a = f.read()
print(a)
a = a.replace('weight', 'FLAG')
f.close()
f = open('decode.py', 'w')
f.write(a)