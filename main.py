notas = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E','F', 'F#', 'G', 'G#']
testes = 1
# bar = input("digite a corda: ")
bar = 'E'
if(testes != 1):
    casa = int(input("digite a nota: "))
# vamos começar pensando na corda mais grossa E
#provavelmente isso faz mais sentido ser uma função, e o 'E' vai ser passado como um parametro
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

    # print(notaDigitada)
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
        # print('\n')
        novaString = '\n'
        StringFinal += novaString
        return
    novaString = str[0:2]
    i=2
    while True:
        # print(str[i])
        i+=1
        #identifica inteiros
        if(str[i]):
            if(str[i].isnumeric()):
                if(str[i+1].isnumeric()):
                    numero = str[i] + str[i+1]
                    i +=1
                    novosTracos += 1
                    #novaString += '-' #isso aqui que está adicionando um tracinho no lugar errado, fazer isso apenas quando o proximo caracter for == '|'
                else:
                    numero = str[i]
                retorno = foo(int(numero), str[0])
                if(len(retorno) > 1):
                    removeTracos += 1
                novaString += retorno
            #identifica as tecnicas
            elif (str[i].isalpha()):
                novaString += tecnicas(str[i])
            #retorna os espaços
            # elif(str[i+1] == '|'):
            #     while(novosTracos > 0):
            #         novaString += '-'
            #         novosTracos -= 1
            #         break
            else:
                if(str[i+1] == '|'):
                    while(novosTracos > 0):
                        novaString += '-'
                        novosTracos -= 1
                    while(removeTracos > 0):
                        novaString = novaString[:-1]
                        removeTracos -= 1
                novaString += str[i]

            
            if(str[i] == '|'):
                # print(novaString)
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