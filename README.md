# Generación de matrices A y B además de un vector de tags iniciales.

1. Para cada documentoeliminé la palabra inicial: ''"document":'
2. eliminé las comas sobrantes utilizando sed s/",}"/"}"/g
3. Para leer cada línea en python use el siguiente ejemplo:
```python
import json
jt = json.loads(json.dumps([{"token":"Buda_Gautama_De_Wikipedia","tag":"NP"},{"token":",","tag":"Fc"},{"token":"la","tag":"DA"},{"token":"enciclopedia","tag":"NC"},{"token":"libre","tag":"AQ"},{"token":"Buda_Gautama_Buddha","tag":"NP"},{"token":"in","tag":"NC"},{"token":"Sarnath_Museum","tag":"NP"},{"token":"(","tag":"Fp"},{"token":"Dhammajak_Mutra","tag":"NP"},{"token":")","tag":"Fp"},{"token":".","tag":"Fp"},{"token":"jpg","tag":"NC"},{"token":"Estatua_de_el_Buda_Gautama","tag":"NP"},{"token":"de","tag":"SP"},{"token":"el","tag":"DA"},{"token":"siglo","tag":"NC"},{"token":"IV","tag":"NP"},{"token":"a","tag":"SP"},{"token":".","tag":"Fp"}],[{"token":"C.","tag":"NP"},{"token":"en","tag":"SP"},{"token":"la","tag":"DA"},{"token":"ciudad","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Sarnath","tag":"NP"},{"token":",","tag":"Fc"},{"token":"distrito","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Benar\u00e9s","tag":"NP"},{"token":",","tag":"Fc"},{"token":"estado","tag":"NC"},{"token":"de","tag":"SP"},{"token":"Uttar_Pradesh","tag":"NP"},{"token":",","tag":"Fc"},{"token":"India","tag":"NP"},{"token":".","tag":"Fp"}]))
```
Con ésto, generamos una lista de diccionarios.
4. Para eliminar las líneas en blanco, ejecutamos en bash : sed '/^$/d' corpus_formateado.txt > corpus_formateado2.txt

# v2.0:
# Viterbi algorithm
* Smoothing added to avoid probabilities equal to zero (lambda = 1 used for facilities).
* There was implemented a method called viterbi which requires:
    * A matrix
    * B matrix
    * Pi array with probabilities of tags to be initial.
    * array of tags available (ordered according with matrices)
    * array of tokens available (ordered according with matrices)
    * a string with the chain of words to tag.
