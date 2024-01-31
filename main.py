notas = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E','F', 'F#', 'G', 'G#']
testes = 1
bar = 'E'
if(testes != 1):
    casa = int(input("digite a nota: "))
def foo(casa, bar):
    for i in notas:
        if(i == bar):
            nota = notas.index(i)

    contadora = 0
    notaDigitada = ''
    while(contadora < casa):
        if(nota + casa > 11):
            casa = (nota + casa) % 12
            notaDigitada = notas[casa]
            break
        nota_casa = nota + casa
        notaDigitada = notas[nota_casa]
        contadora += 1

    return notaDigitada

def tecnicas(tec):
    if(tec == 'b'):
        return '↑'
    elif(tec == 'h'):
        return '→'
    elif(tec == 'r'):
        return '↓'
    elif(tec == 'p'):
        return '←'
    else:
        return tec
    
StringFinal = ''
    
def trataString(str):
    global StringFinal
    novosTracos = 0
    removeTracos = 0
    if(str == 'breakRow'):
        novaString = '\n'
        StringFinal += novaString
        return
    novaString = str[0:2]
    i=1
    while True:
        i+=1
        if(str[i]):
            if(str[i].isnumeric()):
                if(str[i+1].isnumeric()):
                    numero = str[i] + str[i+1]
                    i +=1
                    novosTracos += 1
                else:
                    numero = str[i]
                retorno = foo(int(numero), str[0])
                if(len(retorno) > 1):
                    removeTracos += 1
                novaString += retorno
            #identifica as tecnicas
            elif (str[i].isalpha()):
                novaString += tecnicas(str[i])
            else:
                if(str[i+1] == '-'):
                    while(novosTracos > 0):
                        novaString += '-'
                        novosTracos -= 1
                    while(removeTracos > 0):
                        novaString = novaString[:-1]
                        removeTracos -= 1
                novaString += str[i]

            
            if(str[i] == '|'):
                novaString += '\n'
                StringFinal += novaString
                break
            else:
                continue

    
with open('file.txt', 'r') as tab:
    lido = tab.readline()
    while lido:
        if(len(lido) < 2):
            trataString('breakRow')
            lido = tab.readline()
            continue
        trataString(lido)
        lido = tab.readline()


print(StringFinal)

with open('output.txt', 'w', encoding='utf-8') as tab:
    tab.write(StringFinal)