# -*- encoding: utf-8 -*-

import numpy
import json

def parse_document(jl, d):    #Recibe una linea decodificada de json y un diccionario para actualizarlo.
    for i in jl:
        if d.has_key(i['token']):
            aux = d.get(i['token'])
        else:
            aux = list()
        aux.append(i['tag'])
        d[i['token']] = aux
    return

def get_amatrix_and_init(jl, t, am, iniciales):  #recibe una línea decodificada de json, un set de tags disponibles, la matriz de ocurrencias de tags y un arreglo con la ocurrencia de cada tag como inicial
    ant = ''
    for i in jl:
        if ant == '':
            iniciales[t.index(i['tag'])] += 1
        else:
            am[t.index(i['tag'])][t.index(ant)] += 1
        ant = i['tag']

    return

def get_tags(d):
    t = list()
    for k, v in d.items():
        for it in v:
            if it not in t:
                t.append(it)
    return t

def get_bmatrix(d,t):   #Recibe un diccionario de tokens con lista de tags de cada token y un set de tags disponibles
    bm = numpy.ones((len(d),len(t)))  #Inicializamos una matriz de tamaño (#tokens, #tags)
    for i, ii in zip(d.items(), bm):
        tot = float(len(i[1]))   #Número total de veces que aparece el token i[0]
        for tag in i[1]:
            ii[t.index(tag)] += tot            # ii es el renglón a editar de la matriz bm, el indice al que debemos sumar corresponde  la posicion en la lista de tags (t)
    for i in range(len(bm)):
        aux = sum(bm[i])
        bm[i] = bm[i] / aux
    return bm



numpy.set_printoptions(threshold='nan')  #Esto es para que imprima completa la matriz ( o arreglos de numpy )
r = dict()  #diccionario de tokens con lista de tags.

#Leemos el corpus de documentos y agregamos al diccionario.

arch = open('corpus_formateado2.txt', 'r')
for line in arch:
    if line != "":
        jt = json.loads(json.dumps(eval(line)))
        parse_document(jt,r)
arch.close()
#

# imprimimos diccionario
# for key, values in r.items():
#     print key, values
# print '\n'
#
# Obtenemos una lista de tags
t = get_tags(r)
# print 'tags: ', t
#
#Obtenemos matriz B.
bm = get_bmatrix(r,t)
#
#Imprimimos la matriz B
print '\nMatriz B:\n', bm
#
# generamos la matriz A y el arreglo de tags iniciales
iniciales = numpy.ones(len(t))
am = numpy.ones((len(t), len(t)))
arch = open('corpus_formateado2.txt', 'r')
for line in arch:
    if line != "":
        jt = json.loads(json.dumps(eval(line)))
        get_amatrix_and_init(jt, t, am, iniciales)
arch.close()

#
#procesamos la matriz A para que sean probabilidades al igual que el vector iniciales
for i in range(len(am)):
    aux = sum(am[i])
    am[i] = am[i] / float(aux)

iniciales = iniciales / sum(iniciales)
#
#imprimimos la matriz A y los iniciales:
print '\nMatriz A:\n', am
print '\nIniciales:\n', iniciales
