import time

def main():
    while True:
      menu()
      opcao = int(input("Informe a opção desejada: "))

      if opcao == 1:
        cont_progressivo()

      elif opcao == 2:
        tempo_incial = int(input("digite o tempo para iniciar (em segundos) o cronometro: "))
        cont_regressivo(tempo_incial)

      elif opcao == 3:
        print("Finalizado")
        break
      else:
        print("Opção invalida. Tente novamente")


def menu():
   print(''' Escolha a opção desejada:

    1 - contador progressivo
    2 - contador regressivo
    3 - sair
    ''')

def cont_regressivo(tempo_inicial):
    horas = tempo_inicial // 3600
    minutos = (tempo_inicial % 3600) // 60
    segundos = tempo_inicial % 60

    while horas >= 0 and minutos >= 0 and segundos >= 0:
        print(f'{horas:02}:{minutos:02}:{segundos:02}', end = "\r")
        time.sleep(1)
        segundos -= 1
        if segundos < 0:
            segundos = 59
            minutos -= 1
        if minutos < 0:
            minutos = 59
            horas -= 1
      
    print("Tempo finalizado")


def cont_progressivo():
    horas = 0
    minutos = 0
    segundos = 0

    while horas < 12:
        print(f'Tempo decorrido: {horas:02}:{minutos:02}:{segundos:02}', end = " \r ")
        time.sleep(1)
        segundos += 1
        if segundos > 59:
            segundos = 0
            minutos += 1
        if minutos > 59:
            minutos = 0
            horas += 1



if __name__ == '__main__':
    main()