# criar um contador com base em letras de textos
from collections import Counter

def cria_lista_palavras(texto):
    aparicoes = Counter(texto.lower())
    return aparicoes

def conta_caracteres(texto):
    aparicoes = cria_lista_palavras(texto)
    total_letras = sum(aparicoes.values())
    return (total_letras)

def calcula_frequencia(texto):
    aparicoes = cria_lista_palavras(texto)
    total_caracteres = conta_caracteres(texto)
    tuplas = [(letra, frequencia/total_caracteres) for letra, frequencia in aparicoes.items()]
    return Counter(dict(tuplas))

if __name__ == '__main__':

    texto1 = 'David Soares é analista editorial da consultoria tributária IOB e contabilista com MBA em IFRS (Normas Internacionais de Contabilidade pela Fundação Instituto de Pesquisas Contábeis, Atuariais e Financeiras (Fipecafi). Autor do Livro: Estrutura Conceitual Básica para a Elaboração e Apresentação das Demonstrações Contábeis, e coautor do livro Imposto de Renda de “A” a “Z”.'

    texto2 = """O SEO envolve muitas estratégias para aumentar a posição de classificação de uma página da web nos resultados de mecanismos de busca. Quanto melhor for o SEO de sua página, mais fácil será para as pessoas encontrarem seu site e acessarem o seu conteúdo.
Imagine que você tenha uma página que vende produtos Geeks. Quando qualquer pessoa interessada em comprar algo relacionado a seus produtos pesquisar na internet sobre um produto deste nicho é importante que sua página apareça entre os primeiros resultados da busca, e isso é possível com uma boa estratégia de SEO. Assim, é fundamental ter uma boa pontuação de SEO se o seu objetivo é obter um maior número de pessoas visualizando seu site, já que mais visitantes podem significar um aumento no número de vendas do seu negócio, por exemplo.
Os mecanismos de buscas estão cada vez mais inteligentes, pois, ajustam constantemente seus algoritmos. Contudo, eles acabam ficando limitados por quais informações você fornece e como fornece em seus sites. Uma forma de solucionar essa limitação é melhorar a indexação do seu conteúdo nos mecanismos de pesquisa. Para isso, o método mais comum é o uso de meta-tags que ajudam os algoritmos a caracterizarem o conteúdo de suas páginas da web."""

    freq_letras_texto = calcula_frequencia(texto1)
    most_common = freq_letras_texto.most_common(10)
    # print(most_common)
    for k, v in most_common:
        print(k, '==>', f'{(v*100):.2f}%')
    # print(freq_letras_texto.most_common(10))