from maquina_sincrona import *
from inputData import *
import pandas as pd

#Define dicionario para data frame

data = {
    'h'   : [],
    'kd'  : [],
    'kc'  : [],
    'ke'  : [],
    'Eh0' : [],
    'Eha' : [],
    'kh'  : []

}




def main():

    #Calcula o numero de ranhuras por polo e por fase 
    q = qRanhuras(nr, nf, p)
    #Calcula numero de espiras eficaz
    Nef = nEficaz(nr, q)


    delt = passoRanhura(nr, p)
    for h in range(1,18):

        #Calcula fator de encurtamento, distribuição e atenuação
        kc = fatorEncurtamento(delt, h)
        kd = fatorDistribuicao(q, delt, h)
        ke = kd* kc

        #Calcula tensão eficaz não atenuada

        Eh0 = Einduzida(Nef, Bm, D, L, p, f)
        Eha = Eh0 * ke

        kh = (1/h) * ke

        #Adiciona valores ao dicionário 
        data['h'].append(h) 
        data['kd'].append(kd)
        data['kc'].append(kc)
        
        data['ke'].append(ke)
        data['Eh0'].append(Eh0)
        data['Eha'].append(Eha)
        data['kh'].append(kh)

    df = pd.DataFrame(data)
    subdfF = df[(df['h'] > 3) & (df['h'] % 2 != 0)].copy()
    subdfL = subdfF[subdfF['h'] % 3 != 0].copy()

    somaKhF = conteudoHarmonico(subdfF['kh'])
    somaKhL = conteudoHarmonico(subdfL['kh']) 
    print("Vh de fase:", somaKhF)
    print("Vh de Linha:", somaKhL)
    print(subdfF)


    
    print(subdfL)
    subdfL.to_excel('output.xlsx', index=False)

if __name__ == "__main__":
    main()
