import contatos_util as ctt

pasta = r"C:\Users\Márcio\Desktop\estudos\alura\python_abertura_manipulacao_arquivos\\"
# arquivo_contatos = open(pasta + 'contatos_v2.csv', encoding='latin_1')

###################################################################################################################
# arquivo_contatos = open(pasta + 'contatos_v2.csv', encoding='latin_1', mode='a')
# nova_linha = '11,Carol,carol@carol.com.br\n'
# arquivo_contatos.write(nova_linha)
# arquivo_contatos.close()

# arquivo_contatos = open(pasta + 'contatos_v2.csv', encoding='latin_1', mode='r')

# conteudo = arquivo_contatos.readlines()     **lê todas as linhas do arquivo. Pode ser ruim para desemprenho, pois pode consumir toda memória.


###################################################################################################################


# conteudo = arquivo_contatos.readline() # pode ler até caracteres específos ou quantidades

# loop sobre o arquivo é uma forma eficiente de mostraro seu conteúdo
# for line in arquivo_contatos:
#     print(line, end='')


###################################################################################################################
# escrita de aquivos
# ao abir um arquivo, podemos selecionar o modo escrita direto na abertura com o método open(file, [encoding=encoding], [mode='[ w (write)]'|'[ a (actualize)]'])
# arquivo_contatos = open(pasta + 'contatos_v2.csv', encoding='latin_1', mode='a')
# contatos = ['12,Ana,ana@ana.com.br,', 
#             '13,Jonas,jonas@jonas.com.br',
#             '14,Luiza,luiza@luiza.com.br'
#             ]
# for contato in contatos:
#     arquivo_contatos.write(f'{contato}+\n')

# arquivo_contatos.flush()

# arquivo_contatos = open(pasta + 'contatos_v2.csv', encoding='latin_1', mode='r')

# for line in arquivo_contatos:
#     print(line)

###################################################################################################################

# try:
#     arquivo_contatos = open(pasta + 'contatos_erro.csv', encoding='latin_1', mode='r')

#     for linha in arquivo_contatos:
#         print(linha, end='')
# # para fechar o arquivo independente do que aconteça no bloco try
# except FileNotFoundError:
#     print('\n**** Arquivo não encontrado. ****\n')
# # except NameError:
# #     print('\n**** Arquivo não encontrado. ****\n')

# finally:
#     arquivo_contatos.close()    

###################################################################################################################

# o statement with serve para casos em que seja necessário uma operação inicial e a finalização da mesma, como na abertura e fechamento de um arquivo.
caminho = r'C:\Users\Márcio\Desktop\estudos\alura\python_abertura_manipulacao_arquivos\contatos.p'

try:
    # contatos = ctt.csv_para_contato('contatos.csv')
    # ctt.contatos_para_pickle(contatos, 'contatos.p')
    
    # contatos = ctt.pickle_para_contatos(caminho)
    caminho = r'C:\Users\Márcio\Desktop\estudos\alura\python_abertura_manipulacao_arquivos\contatos.json'
    # ctt.contatos_para_json(contatos, caminho)

    contatos = ctt.json_para_contatos(caminho)

    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')

except FileNotFoundError:
    print('\n**** Arquivo não encontrado. ****\n') 
