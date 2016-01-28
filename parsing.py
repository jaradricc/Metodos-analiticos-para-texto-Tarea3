# -*- encoding: utf-8 -*-
# 1. Para cada documentoeliminé la palabra inicial: ''"document":'
# 2. eliminé las comas sobrantes utilizando sed s/",}"/"}"/g
# 3. Para leer cada línea en python usé el siguiente ejemplo:
#
# import json
# jt = json.loads(json.dumps([{"token":"Buda_Gautama_De_Wikipedia","tag":"NP"},{"token":",","tag":"Fc"},{"token":"la","tag":"DA"},{"token":"enciclopedia","tag":"NC"},{"token":"libre","tag":"AQ"},{"token":"Buda_Gautama_Buddha","tag":"NP"},{"token":"in","tag":"NC"},{"token":"Sarnath_Museum","tag":"NP"},{"token":"(","tag":"Fp"},{"token":"Dhammajak_Mutra","tag":"NP"},{"token":")","tag":"Fp"},{"token":".","tag":"Fp"},{"token":"jpg","tag":"NC"},{"token":"Estatua_de_el_Buda_Gautama","tag":"NP"},{"token":"de","tag":"SP"},{"token":"el","tag":"DA"},{"token":"siglo","tag":"NC"},{"token":"IV","tag":"NP"},{"token":"a","tag":"SP"},{"token":".","tag":"Fp"}],[{"token":"C.","tag":"NP"},{"token":"en","tag":"SP"},{"token":"la","tag":"DA"},{"token":"ciudad","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Sarnath","tag":"NP"},{"token":",","tag":"Fc"},{"token":"distrito","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Benar\u00e9s","tag":"NP"},{"token":",","tag":"Fc"},{"token":"estado","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Uttar_Pradesh","tag":"NP"},{"token":",","tag":"Fc"},{"token":"India","tag":"NP"},{"token":".","tag":"Fp"}]))
#
# 4. Para contar los tags de cada documento, utilicé la siguiente línea:
#
# Counter(elem['tag'] for elem in jt)
#
# 5. Para eliminar las líneas en blanco, ejecutamos en bash : sed '/^$/d' corpus_formateado.txt > corpus_formateado2.txt


def parse_document(jl, d):
    for i in jl:
        if d.has_key(i['token']):
            aux = d.get(i['token'])
        else:
            aux = list()
        aux.append(i['tag'])
        d[i['token']] = aux
    return

def get_tags(d):
    t = list()
    for k, v in d.items():
        for it in v:
            if it not in t:
                t.append(it)
    return t

import json
r = dict()

arch = open('corpus_formateado2.txt', 'r')
for line in arch:
    if line != "":
        jt =json.loads(json.dumps(eval(line)))
        parse_document(jt,r)
arch.close()
# jt = json.loads(json.dumps([{"token":"Buda_Gautama_De_Wikipedia","tag":"NP"},{"token":",","tag":"Fc"},{"token":"la","tag":"DA"},{"token":"enciclopedia","tag":"NC"},{"token":"libre","tag":"AQ"},{"token":"Buda_Gautama_Buddha","tag":"NP"},{"token":"in","tag":"NC"},{"token":"Sarnath_Museum","tag":"NP"},{"token":"(","tag":"Fp"},{"token":"Dhammajak_Mutra","tag":"NP"},{"token":")","tag":"Fp"},{"token":".","tag":"Fp"},{"token":"jpg","tag":"NC"},{"token":"Estatua_de_el_Buda_Gautama","tag":"NP"},{"token":"de","tag":"SP"},{"token":"el","tag":"DA"},{"token":"siglo","tag":"NC"},{"token":"IV","tag":"NP"},{"token":"a","tag":"SP"},{"token":".","tag":"Fp"}],[{"token":"C.","tag":"NP"},{"token":"en","tag":"SP"},{"token":"la","tag":"DA"},{"token":"ciudad","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Sarnath","tag":"NP"},{"token":",","tag":"Fc"},{"token":"distrito","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Benar\u00e9s","tag":"NP"},{"token":",","tag":"Fc"},{"token":"estado","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Uttar_Pradesh","tag":"NP"},{"token":",","tag":"Fc"},{"token":"India","tag":"NP"},{"token":".","tag":"Fp"}]))
#print jt
#
# r= dict()
# parse_document(jt, r)

for key, values in r.items():
    print key, values
print '\n'

t = get_tags(r)
print 'tags: ', t
