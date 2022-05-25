#Ramiro da Silva Souza 150919.

#Função que captura e retorna o inicio do arquivo. Desde a abertura do HTML
# até a abertura da primeira linha do <theader>
def inicioHtml():
    ## Abre o arquivo html que foi passado;
    arquivo = open("test_results.html", "r")

    ##Variável que recebe as linhas do arquivo aberto.
    info = arquivo.readlines()

    ##variavel que armazenará todas as linhas sem caracteres desnecessários como o " ".
    linhas = []

    ##Looping que é usado para retirada de espaços desnecessários de cada valor armazenado no array.
    for i in range(0, len(info)):
        linhaAtual = info[i]
        linhas.append(linhaAtual)
    linhas[5] = """<style type="text/css">"""
    ##Variável que armazenará o inicio do arquivo, desde a abertura do html, até a abertura do header da tabela.
    inicioArquivo = []
    ##Captura das linhas que parte desde a abertura do html até o header da tabela.
    for i in range(0, 70):
        inicioArquivo.append(linhas[i])

    inicioArquivo = "".join(inicioArquivo)
    arquivo.close()

    return inicioArquivo

#Função que captura e organiza o fechamento do HTML.
def fechamentoHtml():
    ## Abre o arquivo html que foi passado;
    arquivo = open("test_results.html", "r")

    ##Variável que recebe as linhas do arquivo aberto.
    info = arquivo.readlines()

    ##variavel que armazenará todas as linhas sem caracteres desnecessários como o " ".
    linhas = []

    ##Looping que é usado para retirada de espaços desnecessários de cada valor armazenado no array.
    for i in range(0, len(info) - 1):
        linhaAtual = info[i]
        remover = " "
        for j in range(0, len(remover)):
            linhaAtual = linhaAtual.replace(remover[j], "")
        linhas.append(linhaAtual)
    ##Variável que armazenará o inicio do arquivo, desde a abertura do html, até a abertura do header da tabela.
    finalArquivo = []
    ##Captura das linhas que parte desde a abertura do html até o header da tabela.
    for i in range(123, 120, -1):
        finalArquivo.append(linhas[i])

    #operações para inverter a ordem das tags no array para correta formatação.
    body = finalArquivo[0]
    finalArquivo[0] = finalArquivo[2]
    finalArquivo[2] = body
    #operação que transforma o array da abertura do arquivo para string.
    finalArquivo = "".join(finalArquivo)
    return finalArquivo

#Função que captura o header da tabela HTML juntamente com as informações que são passadas na tabela
def headerTabela():
    arquivo = open("exportar.csv", "r")

    info = arquivo.readlines()
    #definição do header como sendo a primeira linha da tabela
    header = info[0]
    #header quebrado em um array com um split em ;.
    header = header.split(";")

    linhaTabela = ['<tr>', '</tr>']
    #definição da coluna da tabela
    colunaTabela = ['<td class="test-result-table-header-cell">', '</td>']
    headerFormatado = []
    #array que vai receber todos os elementos do header
    headerFormatado.append(linhaTabela[0])
    for i in range(0, len(header)):
        headerFormatado.append(colunaTabela[0])
        headerFormatado.append(header[i])
        headerFormatado.append(colunaTabela[1])
    headerFormatado.append(linhaTabela[1])
    headerFormatado.append("</thead>")
    #transformação do array em string para escrever no html.
    headerFormatadoString = "".join(headerFormatado)

    arquivo.close()
    return headerFormatadoString

#Função que captura as demais informações da tabela e realiza a conversão para HTML
def corpoTabela():
    arquivo = open("exportar.csv", "r")

    info = arquivo.readlines()
    header = info[0]
    corpo = []
    linhas = []
    corpoFormatado = []

    linhaTabela = ['<tr>', '</tr>']
    colunaTabela = ['<td>', '</td>','<td class="test-cast-status-box-ok">', '<td class="test-result-step-result-cell-failure">']

    #variável responsável por saber quando que será utilizado o fechamento de linha no arquivo.
    cont = 0
    corpoFormatado = []

    #captação do corpo na variavel corpo. Começará na segunda linha.
    for i in range(1, len(info)):
        corpo.append(info[i])

    #array que separará os elementos a partir do elemento ";"
    for i in range(0, len(corpo)):
        linhas.append(corpo[i].split(";"))


    corpoFormatado.append("<tbody>")

    #Laço que será responsavel por montar o corpo com todas as informações do arquivo "test_results" no arquivo "index.html".
    for i in range(0, len(linhas)):
        for j in range(0,len(linhas[i])):
            if(cont == 0):
                corpoFormatado.append(linhaTabela[0])
                corpoFormatado.append(colunaTabela[0])
                corpoFormatado.append(linhas[i][j])
            else:
                #Se a coluna atual for a de porcentagem, irá avaliar qual cor de background colocar.
                if(j == 4):
                    remover = '" '
                    for x in range(len(remover)):
                        linhas[i][j] = linhas[i][j].replace(linhas[i][j][x], "")
                    porcentagem = float(linhas[i][j])
                    if(porcentagem >= 10):
                        corpoFormatado.append(colunaTabela[2])
                        corpoFormatado.append(str(porcentagem))
                    else:
                        corpoFormatado.append(colunaTabela[3])
                        corpoFormatado.append(str(porcentagem))
                if(j!=4):
                    corpoFormatado.append(colunaTabela[0])
                if(j != 5 and j != 4):
                    corpoFormatado.append(linhas[i][j])

            if(cont == 5):
                corpoFormatado.append(linhas[i][j])
                corpoFormatado.append(colunaTabela[1])

            else:
                corpoFormatado.append(colunaTabela[1])
            cont += 1
            if(cont > 5):
                cont = 0

    #conversao do array do corpo para string, para a gravação no arquivo.
    corpoFormatado = "".join(corpoFormatado)
    arquivo.close()
    return corpoFormatado

#Função que escreve o novo arquivo HTML.
def novoArquivo():
    arquivo = open("index.html", "w+")

    #array que terá atribuído todos os retornos de construção do arquivo html.
    html = []

    html.append(inicioHtml())
    html.append(headerTabela())
    html.append(corpoTabela())
    html.append(fechamentoHtml())

    #Transformação do array em string para a gravação no arquivo html.
    html = "".join(html)

    arquivo.write(html)
    arquivo.close()

    return 0


novoArquivo()