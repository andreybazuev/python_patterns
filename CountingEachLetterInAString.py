
#считаем сколько раз в строке встречается каждая буква  
def histogram(s):
    d = dict() #создаем пустой словарь
    for c in s: #для каждой буквы в строке 
        
        """if c not in d: #проверяем есть ли она в словаре
            d[c] = 1 #если нет, добавляем ключ со знач 1
        else:
            d[c] += 1 #иначе тикает счетчик"""

        d[c] = d.get(c, 0) + 1 # или так без условия. 
        #каждой новой букве в строке добавляется в словарь d ключ и значение 1, 
        # если ключ и значение есть - добавляется к значению + 1)

    return d

#h = histogram('аабббввввВ')
#print (h)