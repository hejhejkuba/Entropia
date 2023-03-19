def decode_gamma_elias(code):
    # znajdź pozycję pierwszej jedynki
    pos = 0
    while code[pos] == '0':
        pos += 1

    # oblicz długość prefiksu kodu gamma eliasa
    prefix_len = pos + 1

    # odczytaj wartość prefiksu
    prefix = code[:prefix_len]
    value = int('1' + code[prefix_len:prefix_len + pos], 2)

    # odczytaj drugą wartość
    code = code[prefix_len + pos:]
    pos = 0
    while code[pos] == '0':
        pos += 1
    prefix_len = pos + 1
    value2 = int('1' + code[prefix_len:prefix_len + pos], 2)

    return (value, value2)


# przykładowe użycie
code = '00010100001011'
print(code)
value, value2 = decode_gamma_elias(code)
if(value==10):
    print("A")
elif(value==11):
    print("B")
elif(value==12):
    print("C")
elif(value==13):
    print("D")
else:
    print(value)
if(value2==10):
    print("A")
elif(value2==11):
    print("B")
elif(value2==12):
    print("C")
elif(value2==13):
    print("D")
else:
    print(value2)