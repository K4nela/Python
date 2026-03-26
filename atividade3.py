def questao1():
    print("\n--- Questão 1: Mesclar Intervalos ---")
    intervalos = [(1, 4), (2, 5), (7, 9)]
    intervalos.sort()
    
    resultado = []
    for intervalo in intervalos:
        if not resultado or intervalo[0] > resultado[-1][1]:
            resultado.append(intervalo)
        else:
            resultado[-1] = (resultado[-1][0], max(resultado[-1][1], intervalo[1]))
    
    print("Entrada:", intervalos)
    print("Saída:", resultado)


def questao2():
    print("\n--- Questão 2: Frequência mínima ---")
    lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    minimo = 3
    
    frequencia = {}
    for num in lista:
        frequencia[num] = frequencia.get(num, 0) + 1
    
    resultado = [num for num, freq in frequencia.items() if freq >= minimo]
    
    print("Lista:", lista)
    print("Mínimo:", minimo)
    print("Resultado:", resultado)


def questao3():
    print("\n--- Questão 3: Subconjunto com soma alvo ---")
    lista = [3, 34, 4, 12, 5, 2]
    alvo = 9
    
    def backtrack(i, soma):
        if soma == alvo:
            return True
        if i >= len(lista) or soma > alvo:
            return False
        
        return backtrack(i + 1, soma + lista[i]) or backtrack(i + 1, soma)
    
    print("Lista:", lista)
    print("Alvo:", alvo)
    print("Existe subconjunto?", backtrack(0, 0))


def questao4():
    print("\n--- Questão 4: Verificação de parênteses ---")
    expressao = input("Digite a expressão: ")
    pilha = []
    
    for char in expressao:
        if char == "(":
            pilha.append(char)
        elif char == ")":
            if not pilha:
                print("Resultado: Erro")
                return
            pilha.pop()
    
    if not pilha:
        print("Resultado: OK")
    else:
        print("Resultado: Erro")


def questao5():
    print("\n--- Questão 5: Operações com conjuntos ---")
    lista1 = [1, 2, 3, 4]
    lista2 = [3, 4, 5, 6]
    
    set1 = set(lista1)
    set2 = set(lista2)
    
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Comuns:", set1 & set2)
    print("Só na primeira:", set1 - set2)
    print("Só na segunda:", set2 - set1)
    print("Sem repetidos:", set1 | set2)
    print("Primeira sem repetidos da segunda:", set1 - set2)


def questao6():
    print("\n--- Questão 6: Crivo de Eratóstenes ---")
    n = 1000
    primos = [1] * n
    
    primos[0] = primos[1] = 0
    
    for i in range(2, n):
        if primos[i] == 1:
            for j in range(i * 2, n, i):
                primos[j] = 0
    
    print("Números primos de 2 até 999:")
    for i in range(2, n):
        if primos[i] == 1:
            print(i, end=" ")
    print()  # quebra de linha final

questao1()
questao2()
questao3()
questao4()
questao5()
questao6()
