f = open("ly.txt", "r")
ly = str.lower(f.read())
x = 0
#clip_dict = {'u': 'i', 'n': 'm'}
key = str.lower('ETAONRISHDLFCMUGYPWBVKJXQZ')
keydict = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
realdict = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, len(ly)):
    #x = ly[i]
    try:
        keydict[ord(ly[i])-97] += 1
    except:
        pass
    #print(x, end="")

print(keydict)

for i in range(0, 26):
    x = 0
    #realdict[i] = 0
    for j in range(0, 26):
         if keydict[j] > x:
             x = keydict[j]
             realdict[i] = j
    keydict[realdict[i]] = 0

print(realdict)
print(ly)
for i in range(0, len(ly)):
    for j in range(0, 26):
        if ord(ly[i])-97 == realdict[j]:
            print(key[j], end="")
