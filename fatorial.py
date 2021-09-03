n = input('insira um número ')
count = int(n)
result = 1
while (count >= 2):

    result *= count
    count -= 1

print (result)
