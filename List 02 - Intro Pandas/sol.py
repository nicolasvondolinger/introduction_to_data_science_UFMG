import numpy as np
import pandas as pd

"""## NumPy Novamente

Vamos começar examinando alguns dados simples.

Em determinadas épocas do ano a venda de certos produtos sofre um aumento significativo. Um exemplo disso, são as vendas de sorvete que aumentam bastante no verão. Além do sorvete, outros itens como protetor solar e vestuário de banho podem ganhar maior atenção durante essa época do ano enquanto outros produtos podem não ser tão valorizados.

Inicialmente, vamos criar alguns dadoos de vendas de sorvete.
"""

ice_cream = [3000, 2600, 1400, 1500, 1200, 500, 300, 400, 700, 600, 800, 1900]

"""Os dados foram carregados em um TAD **list**. Como falamos no último laboratório, listas não são otimizadas para análise numérica. Para isso, vamos usar o pacote **NumPy** novamente. Então, vamos criar um vetor Numpy dos dados!"""

ice_cream_v = np.array(ice_cream)

"""Caso você ainda esteja se perguntando sobre as diferenças entre uma **list** e uma **array numpy (np.array)**, vamos comparar como esses tipos de dados se comportam quando os usamos em uma expressão que os multiplica por 2."""

print (type(ice_cream),'x 2:', ice_cream * 2)
print('---')
print (type(ice_cream_v),'x 2:', ice_cream_v * 2)

"""Observe que multiplicar uma lista por 2 cria uma nova lista com o dobro do comprimento e a sequência original de elementos da lista repetida. Multiplicar um array NumPy, por outro lado, realiza um cálculo elementar no qual o array se comporta como um *vetor*. Terminamos com um array do mesmo tamanho no qual cada elemento foi multiplicado por 2.

A principal conclusão disso é que os arrays NumPy são projetados especificamente para suportar operações matemáticas em dados numéricos.
"""

np.median(ice_cream_v)

"""### Exercício 01

Altere a função abaixo para retornar a mediana do valor dos sorvetes e o número de elementos no array.
"""

def median_and_size(array):
      return np.median(array), array.size;

"""Novamente, vanos carregar os módulos de testes"""

from numpy.testing import assert_almost_equal
from numpy.testing import assert_equal

from numpy.testing import assert_array_almost_equal
from numpy.testing import assert_array_equal

"""Nosso teste"""

median, size = median_and_size(ice_cream_v)
assert_equal(1000, median)
assert_equal(12, size)

len(ice_cream_v)

"""## Pandas

Embora o NumPy forneça muitas das funcionalidades de que você precisa para trabalhar com números, quando você começa a lidar com tabelas de dados bidimensionais, o pacote Pandas oferece uma estrutura mais conveniente para trabalhar - o DataFrame.

Agora, vamos criar alguns dados de vendas de outros produtos. Além do mais, vamos criar um array de meses.
"""

ice_cream = np.array([3000, 2600, 1400, 1500, 1200, 500, 300, 400, 700, 600, 800, 1900])
sunglasses = np.array([1000, 800, 100, 70, 50, 190, 60, 50, 100, 120, 130, 900])
coats = np.array([10, 20, 80, 120, 100, 500, 900, 780, 360, 100, 120, 20])
labels = np.array(["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"])

"""O código abaixo cria um DataFrame na mão. É mais comum ler dados de arquivos. Porém, neste laboratório inicial, vamos usar um DataFrame com a pequena base de dados acima. A tabela vai ser da seguinte forma:

   icecream   sunglasses   coats

Jan 3000 1000 10
Fev 2600 800 20
... ... ... ...
Dez 1900 900 20

Observe que, além das colunas que você especificou, o DataFrame inclui um índice para identificar cada linha de forma exclusiva.
"""

df = pd.DataFrame({'icecream': ice_cream,      # coluna 0
                   'sunglasses': sunglasses,   # coluna 1
                   'coats': coats},            # coluna 2
                   index=labels)

"""A chamada head mostra as 5 primeiras linhas do DataFrame."""

df.head()

"""### Exercício 02

Lembre-se da sala de aula que pandas contém chamadas `loc` e `iloc` para acessar o índice. Sabendo disto, implemente a função abaixo que retorna a quantidade de vendas em um dado mês na forma de `string`. A sua função deve retornar uma Series do pandas. Por exemplo, segue a saída esperada para 'Jan'.

month_sales(df, 'Jan')

icecream      3000
sunglasses    1000
coats           10
Name: Jan, dtype: int64

"""

def month_sales(df, month: str):
    return df.loc[month]

series = month_sales(df, 'Jan')
assert_equal(3000, series.loc['icecream'])
assert_equal(1000, series.loc['sunglasses'])
assert_equal(10, series.loc['coats'])

"""### Exercício 03

Agora, implemente uma função que retorna uma linha do DataFrame a partir do número da linha (um número inteiro).
"""

def row_sales(df, row: int):
    return df.iloc[row]

series = row_sales(df, 0)
assert_equal(3000, series.loc['icecream'])
assert_equal(1000, series.loc['sunglasses'])
assert_equal(10, series.loc['coats'])

"""### Exercício 04 (Sem correção Automática)

Agora, faça um gráfico estilo o abaixo para entender a venda de produtos ao longo dos meses. Esta tarefa não tem correção automática, use o gráfico abaixo para saber se acertou ou não.

Lembre-se que em Pandas os data frames contém um método plot. Leia a documentação do mesmo caso necessário.


"""

"""### Exercício 05

Agora, altere a função abaixo para retornar 'Norte' caso você acha ache que o país das vendas acima é do hemisfério norte. Retorne 'Sul' caso contrário.
"""

def north_or_south():
    return 'Norte'

"""### Exercício 06

Por fim, crie um método que retorne as estatísticas agregadas. Seu método deve retornar um novo DataFrame no seguinte formato.

          icecream   sunglasses       coats
count    12.000000    12.000000   12.000000
mean   1241.666667   297.500000  259.166667
std     879.522942   367.896354  308.676304
min     300.000000    50.000000   10.000000
25%     575.000000    67.500000   65.000000
50%    1000.000000   110.000000  110.000000
75%    1600.000000   342.500000  395.000000
max    3000.000000  1000.000000  900.000000

Uma única chamada Pandas resolve este problema!
"""

def questao6(df):
    statistics = {
    'count': df.count(),
    'mean': df.mean(),
    'std': df.std(),
    'min': df.min(),
    '25%': df.quantile(0.25),
    '50%': df.quantile(0.50),
    '75%': df.quantile(0.75),
    'max': df.max()
    }
    
    return pd.DataFrame(statistics)

"""## Arquivos

É bem mais comum fazer uso de DataFrames que já existem em arquivos. Note que o trabalho do cientista de dados nem sempre vai ter tais arquivos prontos. Em várias ocasiões, você vai ter que coletar e organizar os mesmos. Limpeza e coleta de dados é uma parte fundamental do seu trabalho. Durante a matéria, boa parte dos notebooks já vão ter dados prontos.

Neste último exercício, vamos fazer uso dos dados de John Snow. Os dados já foram limpos para a tarefa.
"""

df = pd.read_csv('https://raw.githubusercontent.com/icd-ufmg/icd-ufmg.github.io/master/listas/l2/snow.csv')
df.head()

"""A coluna Count indica o número de mortes em uma casa. A NearestPumpID indica qual bomba d'água é a mais próxima da casa. Os dados não vão bater com os da aula, pois não tínhamos a informação precisa onde cada casa pegava água. Apenas assumi ser no local mais próximo!
Groupby

Vamos responder uma pergunta com a função groupby. Lembrando a ideia é separar os dados com base em valores comuns, ou seja, agrupar por nomes e realizar alguma operação. O comando abaixo agrupa todos os recem-náscidos por nome. Imagine a mesma fazendo uma operação equivalente ao laço abaixo:

buckets = {}                    # Mapa de dados
names = set(df['Name'])         # Conjunto de nomes únicos
for idx, row in df.iterrows():  # Para cada linha dos dados
    name = row['Name']
    if name not in buckets:
        buckets[name] = []      # Uma lista para cada nome
    buckets[name].append(row)   # Separa a linha para cada nome

O código acima é bastante lento!!! Enquanto isso, o groupby é otimizado, sendo bem mais rápido!
Exercício 07

Implemente uma função que retorna a quantidade de mortes para cada bomba. Use o groupby.
"""

def mortes_por_pump(df):
    return df.groupby(['NearestPumpID']).sum()['Count']