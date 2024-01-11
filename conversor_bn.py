'''
Laboratório de Algoritmos
        Mudança de Bases Numéricas
'''
# Função para verificar se o número digitado pelo usuário contém caracteres especiais
def verifique_caracter_especial(numero):
    if numero.isalpha():
        return True
    elif numero.isdecimal():
        return True
    elif numero.isalnum():
        return True
    else:
        return False

# Função que recebe o número digitado (em string) e converte para valores inteiros dentro de uma lista  
def numero_em_lista(numero):
    numero = numero.upper()
    lista = []
    letras = [['A',10],['B',11],['C',12],['D',13],['E',14],['F',15],['G',16],['H',17],['I',18],['J',19],['K',20],['L',21],['M',22],
              ['N',23],['O',24],['P',25],['Q',26],['R',27],['S',28],['T',29],['U',30],['V',31],['W',32],['X',33],['Y',34],['Z',35]]
    for algarismo in numero:
        iterador1 = 0
        iterador2 = 0
        while iterador1 < 10 or iterador2 < 26:
                if str(iterador1) == algarismo:
                    algarismo = int(algarismo)
                    lista.append(algarismo)
                    break
                elif letras[iterador2][0] == algarismo:
                    algarismo = int(letras[iterador2][1])
                    lista.append(algarismo)
                    break
                else:
                    iterador1 += 1
                    iterador2 += 1
    return lista

# Função que verifica se algum algarismo digitado é maior do que a base de origem
def verifique_num_maior_que_base(base_origem,lista):
    for elemento in lista:
        if elemento >= base_origem:
            return False


def converta_para_base_10(base_origem,lista):
    # A lista será convertida para um número inteiro na base 10
    n = len(lista)
    valor_convertido = 0
    for algarismo in lista:
        # Fórmula para converter um número de uma base qualquer para a base 10
        valor_convertido += algarismo * (base_origem)**(n-1)
        n-=1
    return valor_convertido


def converta_para_base_destino (num_base_10,base_destino):
    letras = [['A',10],['B',11],['C',12],['D',13],['E',14],['F',15],['G',16],['H',17],['I',18],['J',19],['K',20],['L',21],['M',22],
              ['N',23],['O',24],['P',25],['Q',26],['R',27],['S',28],['T',29],['U',30],['V',31],['W',32],['X',33],['Y',34],['Z',35]]
    # A seguir, estrutura para obter os restos das divisões sucessivas que irão compor o resultado
    restos = []
    inteiro = num_base_10
    while inteiro > 0:
        resto = num_base_10 % base_destino
        inteiro = inteiro // base_destino
        num_base_10 = inteiro
        restos.append(resto)
    # Estrutura para inverter a ordem dos restos:
    posicao = len(restos) - 1
    inv_restos = []
    for elem in range(len(restos)):
        inv_restos.append(restos[posicao])
        posicao -= 1
    # Estrutura para converter valores em strings
    for indice in range(len(inv_restos)):
        if inv_restos[indice] >= 10:
            i = 0
            while i < 26:
                if inv_restos[indice] == letras[i][1]:
                    inv_restos[indice] = letras[i][0]
                    break
                else:
                    i += 1
        else:
            inv_restos[indice] = str(inv_restos[indice])
    # Resultado fora da lista, em string
    valor_convertido = ''
    valor_convertido = valor_convertido.join(inv_restos)
    return valor_convertido
    
def conversao_total (base_origem,numero,base_destino):
    if base_origem >= 2 and base_origem <= 36 and base_destino >= 2 and base_destino <= 36:
        verificacao1 = verifique_caracter_especial(numero)
        if verificacao1 == False:
            return 'Valor Inválido'
        else:
            verificacao2 = numero_em_lista(numero)
            se_menor_que_base = verifique_num_maior_que_base(base_origem,verificacao2)
            if se_menor_que_base == False:
                return 'Valor Inválido'
            else:
                numero_na_base_10 = converta_para_base_10(base_origem,verificacao2)
                resultado_final = (converta_para_base_destino(numero_na_base_10,base_destino))
        return resultado_final
    else:
        return 'Valor Inválido'

print("------ Código de Conversão de Bases Numéricas ------")
base_origem = int(input("Digite o número da base de origem: "))
numero = input("Digite um número na base indicada: ")
base_destino = int(input("Digite a base de destino: "))

print(conversao_total(base_origem,numero,base_destino))