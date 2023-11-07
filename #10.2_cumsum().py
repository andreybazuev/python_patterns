#10.2_cumsum()берет список чисел и возвращает
#кумулятивную сумму; то есть новый список, где i-й элемент — это сумма
#первых элементов i +1 из исходного списка.
def cumsum(t):
    cs = []
    s = 0
    for i in t:
        s += i
        cs.append(s)
    return cs    

t = [1, 2, 3, 4]
print (cumsum(t))
