from collections import Counter
from pprint import pprint

normal     = 'MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'
falciforme = 'MVHLTPVEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH'

massa_aminoacido = {
            "A": 71.03711 , "C": 103.00919, "D": 115.02694, "E": 129.04259, 
            "F": 147.06841, "G": 57.02146 , "H": 137.05891, "I": 113.08406,
            "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
            "P": 97.05276 , "Q": 128.05858, "R": 156.10111, "S": 87.03203 ,
            "T": 101.04768, "V": 99.06841 , "W": 186.07931, "Y": 163.06333
}

massa_normal = 0
for aa in normal:
    massa = massa_aminoacido[aa]
    massa_normal += massa

massa_falciforme = 0
for ss in falciforme:
    massa = massa_aminoacido[ss]
    massa_falciforme += massa
print('Massa Normal (A)    : ',massa_normal)
print('Massa Falciforme (S): ',massa_falciforme)

cod_genetico = {
        "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", 
        "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V", 
        "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
        "UUG": "L", "CUG": "L", "GGG": "G", "GUG": "V", 
        "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A", 
        "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
        "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A", 
        "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", 
        "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
        "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", 
        "CAA": "Q", "AAA": "K", "GAA": "E", "CAG": "Q", 
        "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R",
        "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R", 
        "AGC": "S", "GGC": "G", "CGA": "R", "AGA": "R", 
        "GGA": "G", "UGG": "W", "CGG": "R", "AGG": "R",
        "AUG": "M", "UGA": "stop", "UAG": "stop", "UAA": "stop"
}

conta_codons = Counter(cod_genetico.values())
pprint(conta_codons)

qtd_rna = 1

for aa in normal:
    possibilidades_codons = conta_codons[aa]
    qtd_rna *= possibilidades_codons
print('aa:', qtd_rna * 3)