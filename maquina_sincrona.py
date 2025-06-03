import numpy as np


def ns(f, p):
    '''
    Retorna rotação síncrona em rpm
    @param: 
    f: frequência [Hz]
    p: pares de polos.
    '''
    return (60*f)/p

def passoPolar(p):
    '''
    passoPolar(p)
    Retorna passo polar em graus geométricos.
    '''
    return 360/(2*p)

def passoRanhura(nr,p):
    '''
    
    passoRanhura(nr,p)
    retorna o Passo de ranhura em graus elétricos.
    @param:
    nr: número total de ranhuras.
    p: pares de polos.
    '''
    return 360 *p /(nr)

def qRanhuras(nr, nf, p):
    '''
    qRanhuras(nr, nf)
    Retorna o número de ranhuras por polo e fase
    @param:
    nr: número total de ranhuras.
    nf: número de fases.
    p: pares de polos.
    '''
    return nr /(nf * 2*p)

def nEficaz(nr, q):
    '''
    Retorna o número eficaz de espiras sem encurtamento e sem distribuição.
    '''
    return nr/ q


def fatorEncurtamento(delt, h):
    '''
    Retorna o fator de encurtamento para um encurtamento delta na harmônica h.

    '''
    theta = delt/2
    theta = theta * (np.pi/180)
    
    return abs(np.cos(h*theta))

def fatorDistribuicao(q, delt,h):
    '''
    Retorna o fator de Distribuição para uma distribuição de q por polo e fase e encurtamento del na harmônica h
    '''
    theta = delt /2
    theta = theta * (np.pi/180)

    kd = np.sin(q*h*theta) / (q*np.sin(h*theta))

    return abs(kd)


def Einduzida(Nef, Bm, D, L, p, f):
    '''
    Retorna a tensão induzida eficaz por fase sem encurtamento e sem distribuição.
    @param:
    Nef: Número eficaz de espiras 
    Bm: Densidade de fluxo máximo no entreferro.
    D: Diâmetro da máquina.
    L: Altura da máquina.
    p: Pares de polos.
    '''
    E = (2*Nef*Bm * np.pi * D* L * f) / (np.sqrt(2) * p)
    return  E

def conteudoHarmonico(kh):
   return sum(kh)

