#10.4_ chop() принимает список, модифицирует его,
#удаляя первый и последний элементы, и возвращает None.

def chop(t):
    del t[1:-1]
    
t = [1, 2, 3, 4, 5]
chop(t)
print(t)