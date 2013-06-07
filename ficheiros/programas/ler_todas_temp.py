# Temperaturas de cidades de Portugal
# Novembro 2012
import matplotlib.pyplot #as plt
plt = matplotlib.pyplot

def le_todas_temperaturas(fich):
    """
    Extrai os dados de temperaturas relativos a Portugal.
    """
    with open(fich,'r')  as f_ent:
        portugal = list()
        dados = le_uma_temperatura(f_ent)
        while dados != -1:
            portugal.append(dados)
            dados = le_uma_temperatura(f_ent)
    f_ent.close()
    return portugal

def le_uma_temperatura(f_ent):
    """
    Ler dados da temperatura de uma cidade.
    Devolve -1 se  fim de ficheiro
    """
    linha = f_ent.readline()
    while (linha !='') and (linha == '\n'):
        linha = f_ent.readline()
    if linha == '':
        return -1
    else:
        linha = linha[:-1].split()
        return [float(dado) for dado in linha]
    
def mostra_todas(xetiq,yetiq,tit,dados):
    plt.xlabel(xetiq)
    plt.ylabel(yetiq)
    plt.title(tit)
    for cidade in dados:
        plt.plot(cidade)




def main(ficheiro):
    dados = le_todas_temperaturas(ficheiro)
    mostra_todas('Meses','Temperatura','Temperaturas Médias das Cidades',dados)
    plt.show()

if __name__ == '__main__':
    main('/data/temperaturas.txt')
   

