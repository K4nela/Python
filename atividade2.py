def questao1():
    palavra = input("Digite uma palavra: ")
    palavraInv = palavra[::-1]

    if palavraInv == palavra:
        print(f"'{palavra}' é um palíndromo!")
    else:
        print(f"'{palavra}' não é um palíndromo")

def questao2():
        hr = int(input("Digite a hora (0 - 23): "))
        ch = int(input("Digite se esta chovendo (1 - sim; 0 - nao): "))
        fl = int(input("Digite o fluxo (0 - baixo; 1 - medio; 2 - alto): "))
        tempo = 0
        
        print(f"hora: {hr}\nchuva: {ch}\nfluxo: {fl}")
        
        if(7 <= hr <= 9) or (17 <= hr <= 19):
                tempo = 60
        else: 
                tempo = 30
                
        if(ch == 1):
                tempo *= 1.20
        
        if(fl == 2):
                tempo += 15
        elif(fl == 0):
                tempo -=10
        else:
                tempo += 0
        
        print(int(tempo))
                
def questao3():
        entrada1 = input("Digite uma palavra ou frase: ")
        entrada2 = input("Digite outra: ")
        
        if sorted(entrada1) == sorted(entrada2):
                print("São anagramas!")
        else:
                print("Não são anagramas!")
                
def questao4():
        lista = ["Papagaio", "Computador", "Mesa", "Cavalete", "Armário"]
        opcao = input(f"Digite uma palavra da lista para saber sua posição:\n{lista}\nPesquisa: ")   
        
        for i in range(len(lista)):
                if opcao == lista[i]:
                        print(f"Posição = {i}")
                        break                        
                
def questao5():
        a = int(input("Digite um número inteiro: "))
        b = int(input("Digite um número inteiro: "))
        p = int(input("Digite um número de pssos: "))
        
        if p == 0:
                print("Erro")
        
        if a < b:
                for i in range(a, b+1, abs(p)):
                        print(i)
                        
        elif a > p:
                for i in range(a, b-1, -abs(p)):
                        print(i)
        else: 
                print("Erro")
                

def questao6():
        estado = False
        triagem = False
        encaminho = False
        estadoAt = " "
        estadoTr = " "
        estadoEn = " "
        estadoFi = " "
        opcao = " "
        
        while True:
                print("=========MENU=========")
                print(f"1 - abrir atendimento {estadoAt}")
                print(f"2 - triagem {estadoTr}")
                print(f"3 - encaminhar {estadoEn}")                
                print(f"4 - finalizar {estadoFi}")
                print(f"s - sair")
                print("======================")
                
                opcao = input("Digite a opcao: ")
                
                match(opcao):
                        case "1":
                                estadoAt = "[Aberto]"
                                estado = True
                        
                        case "2": 
                                if estado == True:
                                        triagem = True
                                        estadoTr = "[Triagem iniciada]"
                                else:
                                        print("Atendimento não está aberto!")
                                        
                        
                        case "3":
                                if triagem == True:
                                        encaminho = True
                                        estadoEn = "[Encaminhado]"
                                else: 
                                        print("Triagem não iniciada!")
                                        
                        case "4":
                                if encaminho == True:
                                        estado = False
                                        estadoAt = " "
                                        estadoTr = " "
                                        estadoEn = " "
                                        estadoFi = " "
                                        print("Finalizado")
                                else:
                                        print("Encaminhamento não iniciado!")
                                        
                        case "s":
                                print("Saindo...")
                                break
                        
                        case _:
                                print("Opção inválida")
                                        
questao6()