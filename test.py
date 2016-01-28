import json
#
#
# def parse_document(jl, d):
#     for i in jl:
#         if d.has_key(i['token']):
#             aux = d.get(i['token'])
#         else:
#             aux = list()
#         aux.append(i['tag'])
#         d[i['token']] = aux
#     return
#
#
# r = dict()
# arch = open('corpus_formateado.txt','r')
# # o = repr(str('[{"token":"Buda_Gautama_De_Wikipedia","tag":"NP"},{"token":",","tag":"Fc"},{"token":"la","tag":"DA"},{"token":"enciclopedia","tag":"NC"},{"token":"libre","tag":"AQ"},{"token":"Buda_Gautama_Buddha","tag":"NP"},{"token":"in","tag":"NC"},{"token":"Sarnath_Museum","tag":"NP"},{"token":"(","tag":"Fp"},{"token":"Dhammajak_Mutra","tag":"NP"},{"token":")","tag":"Fp"},{"token":".","tag":"Fp"},{"token":"jpg","tag":"NC"},{"token":"Estatua_de_el_Buda_Gautama","tag":"NP"},{"token":"de","tag":"SP"},{"token":"el","tag":"DA"},{"token":"siglo","tag":"NC"},{"token":"IV","tag":"NP"},{"token":"a","tag":"SP"},{"token":".","tag":"Fp"}],[{"token":"C.","tag":"NP"},{"token":"en","tag":"SP"},{"token":"la","tag":"DA"},{"token":"ciudad","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Sarnath","tag":"NP"},{"token":",","tag":"Fc"},{"token":"distrito","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Benar\u00e9s","tag":"NP"},{"token":",","tag":"Fc"},{"token":"estado","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Uttar_Pradesh","tag":"NP"},{"token":",","tag":"Fc"},{"token":"India","tag":"NP"},{"token":".","tag":"Fp"}]'))
#
#
# l = arch.readline()[:-1]
# jt = json.loads(json.dumps(eval(l)))
# print jt
#
#
#
# arch.close()

arch = open('corpus_formateado2.txt','r')
jt = list()
for line in arch:
    if line != "":
        jt.append(json.loads(json.dumps(eval(line))))
print len(jt)
for it in jt:
    print type(it)
arch.close()
