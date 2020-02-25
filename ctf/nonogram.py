import nonogram_solver

# {"ver":[[2],[2],[2],[2]],"hor":[[0,1],[1],[1,2],[1,2]]}
f = open('a', 'r')
strs = f.read().split('a\n')

hor = '{"ver":['

for line in strs[1].split('\n'):
    hor = hor + '['
    for num in line.split(' '):
        hor = hor + str(num) + ','
    hor = hor[0:-1] + '],'

hor = hor[0:-1] + '],"hor":['

for line in strs[0].split('\n'):
    hor = hor + '['
    for num in line.split(' '):
        hor = hor + str(num) + ','
    hor = hor[0:-1] + '],'

hor = hor[0:-1] + ']}'

print(hor)

print(nonogram_solver)
