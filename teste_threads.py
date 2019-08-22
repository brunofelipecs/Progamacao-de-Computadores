from datetime import datetime

inicio = datetime.now()

def fatorial(valor):

    fat = valor

    for aux in range(1,valor):

        fat *= aux

    return fat



def primo(valor):

    primo = 0

    for div in range(1,valor+1):

        if(valor % div == 0):

            primo += 1

    if primo == 2: return True

    else: return False




valor = int(input("Informe um número: "))



arq = open('VALORES_PRIMOS.TXT', 'w')

arq2 = open('VALORE_NAO_PRIMOS.TXT', 'w')

arq3 = open('TEMPO_GASTO.TXT', 'w')

for i in range(1,valor+1):

    if primo(i) == True:

        arq.write("{0} é primo e seu fatorial é: {1}!\n\n".format(i, fatorial(i)))

        arq.write("-" * 100)

        arq.write("\n\n")

    else:

        arq2.write("{0} não é primo!\n\n".format(i))

        arq2.write("-" * 100)

        arq2.write("\n\n")



arq3.write("{0}:{1}:{2}\n".format(inicio.hour, inicio.minute, inicio.second))


arq.close()

arq2.close()


fim = datetime.now()

arq3.write("{0}:{1}:{2}\n".format(fim.hour, fim.minute, fim.second))

tempo = fim - inicio

arq3.write(str(tempo))
arq3.close()
