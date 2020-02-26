import hashlib
m = hashlib.md5()
data = b"240610708"
m.update(data)
ans = m.hexdigest()

a = 240610708

while True:
    a += 1
    m.update(bytes(str(a), 'utf8'))
    if ans == m.hexdigest():
        print(a)
        break