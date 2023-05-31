print("""
---------------------** APRESENTACAO **-------------------------------
          Olá, Bem-vindo ao Projeto Localiza&Auxilia!
  
Aqui pretendemos te auxiliar da melhor maneira de como se informar sobre 
a melhor situacao de producao alimentícia de onde voce habita. Portanto 
faremos uma série de perguntas relacionadas a sua vida pessoal.

Dicas de uso:
- Para perguntas de sim ou não, usar 'S' para sim e 'N' para não!;
- Para perguntas que envolvam qualquer tipo de lista, responder com o número de desejo.
""")

def dados():
  
  print("------------------------------------------------------------")
  print("nos informe, por gentileza")
  nome = input(" seu nome: ")
  data_nasc = input(" sua data de nascimento: ")
  print("-------------------------------------")
  print(f'''Seu nome: {nome}, e sua data de nascimento: {data_nasc}''')
  confirmacao = input("Estão corretos?:")
  
  while confirmacao != "S" and confirmacao != "N":
    print("Resposta inválida! Responder apenas com 'S' para sim e 'N' para não.") 
    print(f'''Seu nome: {nome}, e sua data de nascimento: {data_nasc}''')
    confirmacao = input("Estão corretos?:")
  
  return confirmacao

def localizao_macro(confirmacao):
  
  if confirmacao == "S":
    print("------------------------------------------------------------")
    print("Certo! Daremos sequência a pesquisa.")
  
  while confirmacao == "N":
    print("""Por favor preencha novamente os campos abaixo!""")
    print("nos informe, por gentileza")
    nome = input(" seu nome: ")
    data_nasc = input(" sua data de nascimento: ")
    print(f'''Seu nome: {nome}, e sua data de nascimento: {data_nasc}''')
    confirmacao = input("Estão corretos?:")
  
  print("""Agora nos informe o continente que você habita:
1 - América 
2 - Oceania
3 - Áfirca
4 - Ásia
5 - Europa """)
  
  continente = int(input("Continente:"))

  while continente not in range(1, 6):
    print("Apenas número de 1 a 5!")
    print("""Agora nos informe o continente que você habita:
1 - América 
2 - Oceania
3 - Áfirca
4 - Ásia
5 - Europa """)
    continente = int(input("Continente:"))
    
  print("------------------------------------------------------------")
  
  match continente:
    
    case 1:
      print("""Certo! dentro da américa, temos três opções de países representando cada país uma divisão da américa, sendo elas:
1 - Brasil
2 - Cuba
3 - Estados Unidos
""")

    case 2:
        print("""Certo! Nosso projeto permite do continente da Oceania apenas a Austrália, pois é um país de dimensões continentais, abrangendo muitos contextos.
    4 - Austrália""")

    case 3:
      print("""
Pela sua imensa extensão longitudinal, da África abrangeremos 3 países, com 3 predominâncias climáticas e de biomas diferntes, sendo eles:
5 - Egito
6 - República Democrática do Congo
7 - África do Sul
    """)
    
    case 4:
      print("""Certo! Nosso projeto permite do continente Asiático apenas a China, pois é um país de dimensões continentais, abrangendo muitos contextos.
    8 - China
    """)
      
    case 5:
      print("""Pela sua grande quantidade de países e diferentes contextos, decidimos dividir a Europa em:
9 - Inglaterra
10 - França
""")  

  pais = int(input("Escolha um:"))
  
  
  while continente not in range(1, 11):
    print("Escolha um número de 1 a 10!")
    pais = int(input("Escolha um:"))
  
  print("------------------------------------------------------------")

  return pais
    
def localizacao_media(pais):
  
  match pais:
    #Brasil ---- região
    case 1: 
        print("""Certo, agora selecione a região a qual você pertence
1 - Norte
2 - Nordeste
3 - Centro-Oeste
4 - Sudeste
5 - Sul""")
    #Cuba
    case 2:
        print("""Certo, agora selecione a região a qual você pertence
6 - Centro
7 - Leste 
8 - Oeste""")
    #Estados Unidos
    case 3:
        print("""Certo, agora selecione a região a qual você pertence
9 - Oeste
10 - Centro-oeste
11 - Nordeste
12 - Sul""")
    #Australia
    case 4:
        print("""Certo, agora selecione a região a qual você pertence
13 - Ocidental
14 - Norte 
15 - Meridional 
16 - Oriental""")
    #Egito
    case 5:
        print("""Certo, agora selecione a região a qual você pertence
17 - Norte
18 - Sul
19 - Leste
20 - Oeste""")
    #Republica Democrática do Congo
    case 6:
        print("""Certo, agora selecione a região a qual você pertence
21 - Norte
22 - Sul
23 - Leste
24 - Oeste""")
    #Africa do Sul
    case 7:
        print("""Certo, agora selecione a região a qual você pertence
25 - Norte
26 - Sul
27 - Leste
28 - Oeste""")
    #China
    case 8:
        print("""Certo, agora selecione a região a qual você pertence
29 - Noroeste
30 - Nordeste 
31 - Oriental  
32 - Centro-Sul
33 - Sudoeste 
34 - Norte """)
    #Inglaterra
    case 9:
        print("""Certo, agora selecione a região a qual você pertence
35 - Norte
36 - Sul
37 - Leste
38 - Oeste""")
    #França
    case 10:
        print("""Certo, agora selecione a região a qual você pertence
39 - Norte
40 - Sul
41 - Leste
42 - Oeste""")
      
  regiao = int(input("Escolha uma:"))
  
  print("------------------------------------------------------------")

  return regiao
      
def selecao_bioma(regiao):
  
  match regiao:
    case 1:
        print("""Escolha o bioma que você reside:
1 - Floresta Amazônica
2 - Cerrado(1)""")
    
    case 2:
        print("""Escolha o bioma que você reside:
3 - Caatinga
4 - Mata Atlântica(1)""")

    case 3:
        print("""Escolha o bioma que você reside:
5 - Cerrado(2)
6 - Pantanal""")

    case 4:
        print("""Escolha o bioma que você reside:
7 - mata atlantica(2)
8 - Cerrado(3)""")

    case 5:
        print("""Escolha o bioma que você reside:
9 - Mata Atlântica(3)
10 - Pampas""")
    
    case 6:
        print("""Escolha o bioma que você reside:
11 - Montanhas e Serras""")

    case 7:
        print("""Escolha o bioma que você reside:
12 - Floresta Tropical(1)""")

    case 8:
        print("""Escolha o bioma que você reside:
13 - Planícies e Pântanos""")

    case 9:
        print("""Escolha o bioma que você reside:
13- Floresta Temperada(1)
14 - Desertos(1)""")

    case 10:
        print("""Escolha o bioma que você reside:
15 - Pradarias
16 - Floresta Temperada(2)""")

    case 11:
        print("""Escolha o bioma que você reside:
17 - Floresta temperada(3)
18 - Bosques e Áreas Úmidas""")

    case 12:
        print("""Escolha o bioma que você reside:
19 - Florestas Temperadas e subtropicais
20 - Pântanos e Áreas Úmidas""")

    case 13:
        print("""Escolha o bioma que você reside:
21 - Desertos(2)""")

    case 14:
        print("""Escolha o bioma que você reside:
22 - Savanas(1)""")

    case 15:
        print("""Escolha o bioma que você reside:
23 - Floresta Temperada(4)
24 - Matagal e arbustos""")

    case 16:
        print("""Escolha o bioma que você reside:
25 - Floresta Tropical Úmida""")

    case 17:
        print("""Escolha o bioma que você reside:
26 - Deserto do Saara(1)""")

    case 18:
        print("""Escolha o bioma que você reside:
27 - Deserto do Saara(2)
28 - Vale do Nilo""")

    case 19:
        print("""Escolha o bioma que você reside:
29 - Delta do Nilo""")

    case 20:
        print("""Escolha o bioma que você reside:
30 - Deserto do Saara(3)""")

    case 21:
        print("""Escolha o bioma que você reside:
31 - Floresta Tropical(2)""")

    case 22:
        print("""Escolha o bioma que você reside:
32 - Savanas(2)
33 - Floresta tropical(3)""")

    case 23:
        print("""Escolha o bioma que você reside:
34 - Floresta Tropical(4)
35 - Montanhas e Vulcões""")

    case 24:
        print("""Escolha o bioma que você reside:
36 - Floresta tropical(5)
37 - Manguezais""")

    case 25:
        print("""Escolha o bioma que você reside:
38 - Savanas(3)
39 - Desertos(3)""")

    case 26:
        print("""Escolha o bioma que você reside:
40 - Fynbos
41 - Litoral""")

    case 27:
        print("""Escolha o bioma que você reside:
42 - Savannah arborizada
43 - Florestas Úmidas""")

    case 28:
        print("""Escolha o bioma que você reside:
44 - Karoo
45 - Desertos(4)""")

    case 29:
        print("""Escolha o bioma que você reside:
46 - Desertos(5)""")

    case 30:
        print("""Escolha o bioma que você reside:
47 - Floresta Temperada(5)""")

    case 31:
        print("""Escolha o bioma que você reside:
48 - Estepes(1)""")

    case 32:
        print("""Escolha o bioma que você reside:
49 - Floresta Sub-Tropical
50 - Montanhas e Planaltos(1)""")

    case 33:
        print("""Escolha o bioma que você reside:
51 - Floresta tropical(6)
52 - Montanhas e vales""")

    case 34:
        print("""Escolha o bioma que você reside:
53 - Floresta Temperada(6)
54 - Estepes(2)
55 - Desertos(6)
56 - Montanhas e planaltos(2)""")

    case 35:
        print("""Escolha o bioma que você reside:
57 - Montanhas e Colinas
58 - Moorlands""")

    case 36:
        print("""Escolha o bioma que você reside:
59 - Floresta Temperada(7)
60 - Pastagens e Campos agrícolas""")

    case 37:
        print("""Escolha o bioma que você reside:
61 - Planíces férteis
62 - Zonas úmidas costeiras""")

    case 38:
        print("""Escolha o bioma que você reside:
63 - Paisagem costeira
64 - Cotswolds""")

    case 39:
        print("""Escolha o bioma que você reside:
65 - Floresta Temperada(8)
66 - Campos e pastagens""")

    case 40:
        print("""Escolha o bioma que você reside:
67 - Mediterrâneo
68 - Alpino
69 - Litoral/Costeiro""")

    case 41:
        print("""Escolha o bioma que você reside:
70 - Florestas Mistas e temperadas
71 - Área de montanha""")

    case 42:
        print("""Escolha o bioma que você reside:
72 - Paisagem agrícola
73 - Zonas úmidas""")

  bioma = int(input("Escolha um:"))
  
  print("------------------------------------------------------------")
  
  return bioma

def informacoes_biomas(bioma):
  
  match bioma:
    case 1:
        with open('floresta_amazonica.md', "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        print(conteudo)
    
    case 2:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 3:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 4:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 5:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 6:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 7:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 8:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 9:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 10:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 11:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 12:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 13:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 14:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 15:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 16:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 17:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 18:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 19:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 20:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 21:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 22:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
   
    case 23:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 24:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 25:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 26:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 27:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 28:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 29:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 30:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 31:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 32:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 33:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 34:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 35:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 36:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 37:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 38:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 39:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 40:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 41:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 42:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 43:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 44:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 45:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 46:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 47:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 48:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 49:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 50:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 51:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 52:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 53:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 54:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 55:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 56:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 57:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
   
    case 58:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 59:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 60:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 61:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 62:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 63:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 64:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 65:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 66:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 67:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 68:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 69:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 70:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 71:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 72:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
    case 73:
        with open('.md', "r", encoding="utf-8") as file:
            content = file.read()
        print(content)
    
def main():
  Confirmacao = dados()
  pais = localizao_macro(Confirmacao)
  regiao = localizacao_media(pais)
  bioma = selecao_bioma(regiao)
  informacoes_biomas(bioma)

main()