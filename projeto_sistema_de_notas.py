import os


#professor este trabalho não está completo, meu desempenho não foi bom o suficiente, mas confesso que aprendi bastante com ele. sei que ele não vale a pontuacao, mas estou lhe enviando pq sei que o senho dará feddeback de como poderei melhorar
#evitei o maximo usar IA's, pois acho que mais ajuda que atrapalha quando não o conhecimento.


alunos = [{'nome':'', 'nota': '', 'assiduidade':'', # nao sabia a forma correta da sintaxe para nao ficar mostrando dados fixos deixei aspas sem nenhum do valor.
            'desempenho1':'',  'desempenho2':''}]


def exibir_opcoes_do_programa ():
    print("1- cadastrar aluno\n2- editar dados do aluno\n3 - impressão de relatório de alunos\n4- impressão por filtro\n0- sair " )
    

    #utilizei o try para tentar forçar o progrtama a ler todos os valores de opçao comop inteiro.
#caso o usuário coloque um str, em vez de mostrar a msg de erro , irá chamar a funçao opcao invalida
def opcao_invalida():
    print ('opção inválida!\n')
    input('digite uma tecla para voltar ao menu principal. ')
    main()

def situacao_dos_alunos():
    print('1- relatorio geral\n2-relatorio por filtro')
    opcao = int(input('escolha o numero da opcao: '))
    if opcao==1:
        os.system('cls')
        print('relatório dos alunos:\n')
        for aluno in alunos:
            nome_do_aluno = aluno['nome']
            media = aluno ['nota']
            media_frequencia = aluno['assiduidade']
            aprovado = aluno['desempenho1']
            reprovado = aluno['desempenho2']
            print(f'{nome_do_aluno} {media} {media_frequencia} {aprovado} {reprovado}')

        input('\ndigite uma tecla para voltar ao menu principal ')
        main()

            


    elif opcao==2:
        imprimir_por_condicao()
                 
def imprimir_por_condicao():      #aqui ficou com bug que não consegui resolver quando quero imprimir por outros filtros, 
                                   #só consegue imprimir por aprovado ou reprovado ou o nome. este trecho peguei a sintaxe da IA's e não cosegui resolver o bug. (não copiei, talvez não apresente que foi de IA)    
            
  
    situacao=input ('digite a condicao que deseja filtrar: nome - media - frequencia:    ').strip() 

    for aluno in alunos:
        
        if situacao == aluno['nome'] or situacao in [aluno['nota'],aluno['desempenho1'] , aluno['assiduidade'],aluno['desempenho2']] :
            print(f"aluno: {aluno['nome']} | nota: {aluno['nota']} | presencas {aluno['assiduidade']}  | {aluno['desempenho1']} | {aluno['desempenho2']}")
      
              
    input('\ndigite uma tecla para voltar ao menu principal ')
    main()
              
       
def editar_alunos():                    #não cosegui subescrever o valor via input ao dicionario, ficou de forma manual( não era o pedido nem o ideal)
    print('\n1- adcionar nota\n2- adicionar frequencia\n3- adicionar carga horaria\n')
    opcao = int(input('digite o numero\n'))
    
    if opcao ==1:
                
        
        print('adicione as notas:')
        
        nota1=float(input('digite a primeira nota: '))
        nota2=float(input('digite a segunda nota: ' ))
        print(f'notas {nota1} e {nota2}')
        media = (nota1 + nota2)/2
        print('media ',media)

       

    elif opcao ==2:
        print('adicione frequencia')
        frequencia=int(input('digite quantas aulas o aluno compareceu\n'))
        print (frequencia,' aulas')

        


    elif opcao ==3: 
        print ('quantas horas aulas tem a disciplina? ')
        disciplina = int(input('digite as horas\n'))

        print (disciplina, ' hrs/aula')

        

        
       
        


    input('\ndigite uma tecla para voltar ao menu principal ')
    main()
    
def adicionar_novo_aluno():
    
        
    os.system('cls')
    print('cadastro de alunos:\n ')

    nome_do_aluno= input ('digite o nome do aluno que deseja cadastrar:\n ')
    nota1=float(input('digite a nota 1\n')) 
    nota2=float(input('digite a nota 2:\n'))
    media=(nota1 + nota2)/2
    print('media', media)
    carga_horaria = int(input('quantas horas aulas tem a disciplina? '))
    frequencia= int(input('digite as presencas do aluno: '))
    media_frequencia = (frequencia/carga_horaria)*100

    print(f'percentual de presenca {media_frequencia:.1f}')
        
    media = float(input(f'digite a media do aluno {nome_do_aluno}:\n'))
    media_frequencia =float(input(f'digite a percentual de presencas do aluno {nome_do_aluno}\n'))
    aprovado= input(f'escreva aprovado se o estudante foi aprovado  {nome_do_aluno}\n')
    reprovado=input(f'escreva reprovado se o aluno foi reprovado {nome_do_aluno}')
    dados_do_aluno= {'nome':nome_do_aluno, 'nota' :media, 'assiduidade' :media_frequencia, 'desempenho1':aprovado, 'desempenho2':reprovado}

    
    alunos.append(dados_do_aluno)
   
    print(f'o estudante {nome_do_aluno} foi adicionado a base dados.')
    input('\ndigite uma tecla para voltar ao menu principal\n')
    main()

def escolher_opcao():

    try: 
        opcao = int(input ('escolha o número da opção: '))

        print('opção escolhida: ',opcao)


        if opcao == 1:
            print('cadastre o aluno:\n')
            adicionar_novo_aluno()
        
        elif opcao == 3:
            print('edite dados do aluno: ')
            editar_alunos()
        elif opcao == 4:
            situacao_dos_alunos()

        #elif opcao == 5: (este tentei deixar incluso noa opcao 4)
         #   print('imprimir por filtro: ')
        elif opcao == 0:
            print ('fechar programa')
            finalizar()
           
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar():
    os.system('cls') # utilizei para não deixar o terminal com muita informação
    print('Programa finalizado!')   

def main():
    os.system('cls')
    exibir_opcoes_do_programa() 
    escolher_opcao()
    opcao_invalida()
    finalizar()
#utilizei pq quero que ele seja meu arquivo principal e organizando que quero que as funçoes executem 
if __name__ == '__main__': 
    main()


