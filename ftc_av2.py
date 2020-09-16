'''Várias strings, a serem lidas da entrada padrão, até que uma string vazia seja recebida. 
Cada string é composta pelos símbolos [,],(,),{,} ou espaço em branco.'''


def is_matched (expr):
    lefty = '({['
    righty = ')}]'
    s = ArrayStack ()
    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False
    return s.is_empty()

'''  Para cada linha da entrada, retornar: casada e correta, nao casada e casada e
incorreta. Para as strings que incorrem neste último caso, também apresentar ao final a
versão casada e correta das mesmas. É importante ressaltar que todos os espaços em branco

1

Elloá B. Guedes (ebgcosta@uea.edu.br, www.elloaguedes.com)
Fundamentos Teóricos da Computação

devem ser ignorados antes da checagem especificada e também nas saídas casadas e corretas
após o conserto. Se após a remoção dos espaços restar apenas uma string vazia, tem-se que
esta é casada e correta por vacuidade.
Para fins de simplificação, sempre há uma única versão correta das strings que precisarem de
conserto. Entradas como ([][][][]) que podem ensejar saídas como ()[][][][] ou também
[][][][]() não serão fornecidas como entrada.
Para resolver o problema em questão, você deve utilizar a linguagem de programação Python 3
e obrigatoriamente fazer uso da estrutura de dados pilha, a qual também pode ser implementada
com o auxílio de uma lista, ficando à critério de cada aluno conforme preferir. Os exemplos a seguir
auxiliam a ilustrar entradas e saídas para o problema considerado.
'''