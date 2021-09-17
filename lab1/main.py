

replace_dict = {}
keys = "jhñkuwy"
values = "iinlvvz"
for (k , i) in zip(keys , values):
    replace_dict[k] = i

# 1 

def replace(string):
    global replace_dict
    replaced = ""
    for i in string:
        if i in replace_dict.keys():
            replaced += replace_dict[i]
        else:
            replaced += i
    return replaced

# 2

def remove_tildes(string):
    tildes = 'áéíóú'
    vals = 'aeiou'
    result = ""
    for i in string:
        change = False
        for j in range(len(tildes)):
            if i == tildes[j]:
                result += vals[j]
                change = True
                break
        if not change:
            result += i
    return result

# 3

def caps(string):
    result = ""
    for i in string:
        if i >= chr(97) and i <= chr(122):
            result += chr(ord(i)-32)
        else:
            result += i
    return result

#4

def remove_characters(string):
    result = ""
    rm_chars = ".,;:_-!¿?¡ \n"
    for i in string:
        ignore = False
        for j in rm_chars:
            if i == j:
                ignore = True
                break
        if not ignore:
            result += i
    return result


#5 

def frecuencias(archivo):
    p5 = open(archivo,'r', encoding="utf-8")
    content = p5.read()
    p5.close()

    freqs = {}
    for i in range(65,91):
        freqs[chr(i)] = 0
    for i in content:
        if i >= chr(65) and i <= chr(91):
            freqs[i] += 1

    return freqs

# 6 
def trigramas(string):
    tri_freq = {}
    for i in range(len(string)-2):
        if string[i:i+3] in tri_freq.keys():
            tri_freq[string[i:i+3]][0] += 1
            tri_freq[string[i:i+3]][1] += [i]
        else:
            tri_freq[string[i:i+3]] = [1,[i]]
    for i in tri_freq.keys():
        distances = []
        for j in range(tri_freq[i][0]-1):
            distances += [(tri_freq[i][1][j+1] - tri_freq[i][1][j]) - 2 ] 
        tri_freq[i][1] = distances

    result  = {}
    for i in tri_freq.keys():
        if tri_freq[i][0] > 1:
            result[i] = [tri_freq[i][0], tri_freq[i][1]]
    return (list(sorted(result.items(), key=lambda item: item[1], reverse = True)))


# 20 caracteres 

def AQUI(string):
    result = ""
    for i in range(len(string)):
        if not i % 20:
            result += "AQUI"
        result += string[i]

    while len(result)%4:
        result += "X"

    return result



i = open("input.txt",'r',encoding="utf-8")
mytext = i.read()
i.close()

mytext = replace(mytext)
mytext = remove_tildes(mytext)
mytext = caps(mytext)
mytext = remove_characters(mytext)

mytext.encode(encoding="utf-8")

o = open("HERALDOSNEGROS_pre.txt",'w',encoding="utf-8")
o.write(mytext)
o.close()

file_freqs = frecuencias("HERALDOSNEGROS_pre.txt")

# 5 primeros

sort_freqs = sorted(file_freqs.items(), key=lambda item: item[1], reverse = True)
for i in range(5):
    print(sort_freqs[i][0],"=",sort_freqs[i][1], end=' ')
print()

# trigrama mas repetida
trig = trigramas(mytext)[0]
print(trig[0],trig[1][0]," veces. Distancias: ",trig[1][1])


# utf
print("utf-8")
for i in mytext:
    print(ord(i.encode("utf-8")),end='')
print()

# con aqui
print("AQUI")
mytext = AQUI(mytext)
print(mytext)