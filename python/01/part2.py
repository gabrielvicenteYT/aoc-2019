def cost(n):
    result = 0
    while n >= 9:
        n = n // 3 - 2
        result += n
    return result


print(sum(cost(int(x)) for x in open("data.txt")))
