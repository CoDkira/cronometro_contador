def main():
    calculadora = []    
 
    def menu():
        print('''Escolha a operação a ser realizada
            
            1 - soma
            2 - subtração
            3 - multiplicação
            4 - divisão
            5 - raiz quadrada
            6 - exponenciação
            7 - porcentagem
            8 - finalizar
            ''')

    def soma(num1, num2):
        return num1 + num2
    
    def subtracao(num1, num2):  
        return num1 - num2
    
    def multiplicacao(num1, num2): 
        return num1 * num2  
    
    def divisao(num1, num2):
        return num1 / num2
    
    def raiz_quadrada(num1):  
        return num1 ** 0.5
    
    def exponenciacao(num1, num2):
        return num1 ** num2
    
    def porcentagem(num1, num2):
        return num1 * num2 / 100
        
    def obter_numero(mensagem):    
         while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print("Por favor, insira um número válido.")



    while True:
        menu()
        try:
            opcao = int(input("Informe a opção desejada: "))
        except ValueError:
            print("Por favor, insira uma opção válida.")
            continue
        
        if opcao == 1:
           num1 = int(input("Informe o primeiro numero: "))
           num2 = int(input("Informe o segundo numero: "))
           resultado = soma(num1, num2)
           print(f"o resultado da operação é: {resultado}")
           calculadora.append(resultado)
           
        elif opcao == 2:
            num1 = int(input("Informe o primeiro numero: "))
            num2 = int(input("Informe o segundo numero: "))
            if num2 == 0:
                print("nao é possivel dividir por 0")
            resultado = subtracao(num1, num2)        
            print(f"o resultado da operação é: {resultado}")
            calculadora.append(resultado)
            
        elif opcao == 3:
            num1 = int(input("Informe o primeiro numero: "))
            num2 = int(input("Informe o segundo numero: "))
            resultado = multiplicacao(num1, num2)
            print(f"o resultado da operação é: {resultado}")
            calculadora.append(resultado)
            
        elif opcao == 4:
            num1 = int(input("Informe o primeiro numero: "))
            num2 = int(input("Informe o segundo numero: "))       
            resultado = divisao(num1, num2)
            print(f"o resultado da operação é: {resultado}")
            calculadora.append(resultado)
            
        elif opcao == 5:
            num1 = int(input("Informe o primeiro numero: "))
            resultado = raiz_quadrada(num1)
            print(f"o resultado da operação é: {resultado}")
            calculadora.append(resultado)
            
        elif opcao == 6:
            num1 = int(input("Informe o primeiro numero: "))
            num2 = int(input("Informe o segundo numero: "))
            resultado = exponenciacao(num1, num2)
            print(f"o resultado da operação é: {resultado}")
            calculadora.append(resultado)
        
        elif opcao == 7:
            num1 = int(input("Informe a porcentagem desejada: "))
            num2 = int(input("Informe o numero: "))    
            resultado = porcentagem(num1, num2)
            print(f"o resultado da operação é: {resultado}")
            calculadora.append(resultado)
            
        elif opcao == 8:
            print("finalizado")
            break
        
        else:
            print("Opção invalida")
            
if __name__ == "__main__":
    main()
                    