# ============ CADASTRO ================
print(' Seja Bem - Vindo!🤖 ')
print(' Eu sou o Evon seu Assisente Virtual')
print(' STATUS' '\033[32m - ONLINE! \033[0m')
print('Vou te Listar as Nossas Opções Disponivéis e você Selecione a Desejada OK?')
ok = input(' Digite OK para Prosseguir:  ')

# ======= SISTEM  ==========
import time

while True:
    if ok.lower() == 'ok':
        print(' Que Ótimo!, Vamos Prosseguir JÁ!')
        print(' Aguarde...')
        time.sleep(5)
        print('\033[32mFINALIZANDO...\033[0m')
        print('CARREGAMENTO CONCLUIDO!🚨')
        break
    else:
        print('RESPOSTA INVALIDA')
        ok = input(' Digite OK para Prosseguir:  ')

# ======== INICIAL =========
print('Queremos te Conhecer!')

nomeini = input(' Como podemos te Chamar?:  ')
idade =int(input(f' Olá Sr(a) {nomeini}, digite a sua idade: '))
hobby = input('Algo que Você Gosta de Fazer? ')
con = input('Como nos Conheceu?: ')

# ======= COMEÇO - LISTA ==========
print(' DISPONÍVEIS ')

lista_disp = [None, 1, 2, 3, 4, 5]

lista_disp[1] = ' [1] Criar Usuario: '
print(lista_disp[1])

lista_disp[2] = ' [2] Ver Usuario: '
print(lista_disp[2])

lista_disp[3] = ' [3] Procurar Usuario: '
print(lista_disp[3])

lista_disp[4] = ' [4] Excluir Usuario: '
print(lista_disp[4])

lista_disp[5] = ' [5] SAIR '
print(lista_disp[5])

# ======= ESCOLHA =================
# ======= SISTEM ESCOLHA ==========

nome = 'nome'

while True:
    escolha = int(input(' Digite a sua Escolha: '))

    if escolha == 1:
        print(' Crie seu Usuario: ')

        nome = input('Informe o seu Usuario: ')
        senha = input(' Informe a sua Senha: ')
        email = input(' Informe seu Email EX: admin@gmail.com: ')

        print(' Confirme sua Senha para Seguirmos')
        confss = input('Confirme sua Senha: ')

        if confss == senha:
            print('  Conta Criada!, Obrigado. ')

        else:
            print(' Senha Incorreta ')

    elif escolha == 2:
        pergunta = input(
            ' Fala Usuario! aqui é o Evon🤖 oque Você Deseja Fazer? '
        )

        if pergunta == 'Ver Usuario' or pergunta == '2':
            print('Nome:', nome)
            print('Idade do Usuario:', idade)
            print('Hobby:', hobby)
            print('Por onde nos Conheceu?', con)

        else:
            print('Opção Invalida')

            
    if escolha == 3:
        print('Você irá Obter a sua Resposta...')
        nomee = 'Alex'
        nomeee = 'alex'
        procura =input((' Digite o Nome da Pessoa que Você Deseja buscar:  '))
        if procura.lower() == 'alex':
            print('Usuário encontrado:', procura)
            print('Idade 23 ( FÍCTCIO )')
            print('Hobby: Fazer Dinheiro ')
        else:
            print('usuario não Encontrado')
    else: 
        print('Opção Invalida')

    if escolha == 4:
        print('Usuario Excluido')
    elif escolha == 5:
        print ('Até Logo!👋')
        break
    else:
        print('Opção Invalida')

# ===========================================