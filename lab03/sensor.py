por = float(input())
n = int(input())

max = -1000000000
sum = 0

err = 0
sumpor = 0

for i in range(0,n):
    g = input()
    if g == 'error':
        err += 1
    else:
        g = float(g)
        if g > max:
            max = g
        if g > por:
            sumpor += 1
        sum += g
print(n)
print(err)
print(sumpor)
print(round(max,1))
print( round(sum/(n-err),1) )
