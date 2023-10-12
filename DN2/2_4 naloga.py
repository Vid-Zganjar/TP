def prastevilo(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

st = [x for x in range(1, 51) if prastevilo(x)]

print("Prastevilo od 1 do 50:")
print(st)
