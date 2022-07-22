import csv,pickle,json
import email
from contato import Contato

def csv_para_contato(caminho, encoding='latin_1'):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            id, nome, email = linha
            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos

def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)

def pickle_para_contatos(caminho):
    with open(caminho, 'rb') as arquivo:
        contatos = pickle.load(arquivo)

    return contatos

def contatos_para_json(contatos, caminho):
    with open(caminho, 'w') as arquivo:
        json.dump(contatos, arquivo, default=_contatos_para_json)

def _contatos_para_json(contato):
    return contato.__dict__


def json_para_contatos(caminho):
    contatos = []
    
    with open(caminho) as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:
            c = Contato(**contato)
            contatos.append(c)
    
    return contatos
# if __name__ == '__main__':
#     caminho = r'C:\Users\Márcio\Desktop\estudos\alura\python_abertura_manipulacao_arquivos\contatos_v2.csv'
#     csv_para_contato(caminho, encoding= 'latin_1')


