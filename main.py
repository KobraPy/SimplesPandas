import pandas as pd
import numpy as np

# Basic visualization
dataset = pd.read_csv("C:\\Users\\outho\\13.Prática em Python\\dados\\trees.csv")
print(dataset)
print(dataset.head(n=3)) # See the number n of lines

# Acssar ponto específico do dataFrame passando "ID" e o nome da Coluna
# Se não houver a linha ou a coluna especifiado a função retorna erro(dã)
print(dataset.at[0, "Height"]) #70

                           #MÉTODO .iat[]

# Fazer acesso usando inteiros tanto para linhas quanto colunas (iniciando no zero)
print(dataset.iat[1,1]) #65


                            #MÉToDO .loc[]

# Fazer acesso à um conjunto de dados usando lista de ["Colunas"] ou de ["linhas" e "colunas"]
# Passando um simples indice
# Retorna um objeto "Series" do Pandas
print(dataset.loc[1])
""""Girth      8.6
    Height    65.0
    Volume    10.3
    Name: 1, dtype: float64"""
print("="*20)

# Passando uma lista de "ID"  retorna um DataFrame com as linhas especificadas | Lembrar de usar [[]]
# Também é possível utiizar uma lista de valores boolean de mesma quantidade
                                  # de "IDs" para recebermos somente as "True"
print(dataset.loc[[1,5]])
""""   Girth    Height   Volume
    1    8.6      65    10.3
    5   10.8      83    19.7  """
print("="*20)

# Assim como o metódo "iat[]" também é possível passar "ID" e "Coluna" para receber um valor único
print(dataset.loc[1,"Girth"])
"""Retorna 8.6"""
print("="*20)

# É posssivel passar um slice somente de "IDs"  ou em relação a uma "Coluna"
# Lembrar que a função inclui o valor inicial e final no slice diferente de outras funções ignoram o último
print(dataset.loc[3:5])
""""    Girth  Height  Volume
        3   10.5      72    16.4
        4   10.7      81    18.8
        5   10.8      83    19.7"""
print("="*20)
print(dataset.loc[3:5, "Volume"])
""" 3    16.4
    4    18.8
    5    19.7
    Name: Volume, dtype: float64"""
print("="*20)
print("="*20)
# É possível passar somente uma condição ou relaciona-la
# Dessa forma ele faz a checagem e devolve os valorem em "False" e " True"
print(dataset.loc[1:5,"Height"] > 80)
""" 1    False
    2    False
    3    False
    4     True
    5     True
    Name: Height, dtype: bool
"""
print("="*20)
# Mesmo exemplo mas visualizando toda a coluna, então não usamos o .loc e também é possivel transformar o objeto em uma lista
teste2 = list(dataset["Height"] > 80)
print(teste2)
"""[False, False, False, False, True, True, False, False, False, False, False, False, False, False, 
    False, False, True, True, False, False, False, False, False, False, False, True, True, False, False,
    False, True]"""
print("="*20)
# Utilizando [[]] podemos fazer acesso aos valores
# Dessa forma ele nos mostra o DataFrame completo em que os itens atendem a condição
print(dataset.loc[dataset["Height"] > 80])
# Também podemos limitar a exibição a apenas uma coluna
print(dataset.loc[dataset["Height"] > 80,["Volume"]])
""" Volume
4     18.8
5     19.7
16    33.8
17    27.4
25    55.4
26    55.7
30    77.0"""
print("="*20)
# É possivel também inciar o comando com um slice e fazer a checagem dentro dele
# A checagem feita dessa forma devolve um objeto "DataFrame"
print(dataset[5:20].loc[dataset["Height"] > 80,["Volume"]])
"""    Volume
5     19.7
16    33.8
17    27.4"""
print("="*20)
# Também podemos fazer a checagem com uma função lambda mas ela nos devolve um objeto do tipo "Series"
# Dessa forma não podemos ter mais uma dimenção nos dados
print(dataset[5:20].loc[lambda x: x["Height"] > 80, "Volume"])
"""    Volume
5     19.7
16    33.8
17    27.4"""
# Series é um objeto de dados de  apenas uma dimenção(ele aceita apenas uma coluna), ele pode ser criado
#a partir de um dicionario, a partir de uma lista(se você não informar os IDs por default ele sera 1,2,3...
# O DataFrame é um objeto bidimensinoal, ele aceita diversas linhas e colunas