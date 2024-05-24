from difflib import SequenceMatcher
import string
import math
from collections import Counter

def read_fasta(arq):
 seq = ''
 with open(arq) as f:
    f.readline()
    for line in f:
        seq += line.strip()
 return seq

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def ocurrenciesDict(arq):
    vector = {}
    
    for i in list(string.ascii_uppercase):
        vector[i] = 0
    
    for letter in arq:
        for i in vector:
            if letter == i:
                vector[i] +=1
    return vector
    
def ocurrenciesVector(arq):
    vector = []
    
    for i in list(string.ascii_uppercase):
        vector.append(arq.count(i)) 
    return vector

def euclideanDistance(str1, str2):
    # Converte as strings em listas de códigos ASCII
    vec1 = [ord(char) for char in str1]
    vec2 = [ord(char) for char in str2]

    # Calcula a distância euclidiana entre os vetores
    distance = math.sqrt(sum((x - y) ** 2 for x, y in zip(vec1, vec2)))
    return distance

def manhattanDistance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    # Inicializa uma matriz para armazenar os custos de edição
    dp = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

    # Preenche a primeira linha e a primeira coluna
    for i in range(len_str1 + 1):
        dp[i][0] = i
    for j in range(len_str2 + 1):
        dp[0][j] = j

    # Calcula os custos de edição
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,  # Remoção
                           dp[i][j - 1] + 1,  # Inserção
                           dp[i - 1][j - 1] + cost)  # Substituição

    # Retorna a distância de Manhattan
    return dp[len_str1][len_str2]

def supremumDistance(str1, str2):

    # Calcula a distância supremum
    distance = max(abs(ord(char1) - ord(char2)) for char1, char2 in zip(str1, str2))
    return distance

def cosineSimilarity(str1, str2):
    # Converte as strings em contadores de palavras
    counter1 = Counter(str1.split())
    counter2 = Counter(str2.split())

    # Cria um conjunto de todas as palavras únicas
    all_words = set(counter1.keys()) | set(counter2.keys())

    # Calcula os produtos internos e as magnitudes dos vetores
    dot_product = sum(counter1[word] * counter2[word] for word in all_words)
    magnitude1 = math.sqrt(sum(counter1[word] ** 2 for word in counter1.keys()))
    magnitude2 = math.sqrt(sum(counter2[word] ** 2 for word in counter2.keys()))

    # Calcula a similaridade do cosseno
    cosine_sim = dot_product / (magnitude1 * magnitude2) if magnitude1 * magnitude2 != 0 else 0
    return cosine_sim

def main():

    arq_rat = fr"rat.fasta"
    rat = read_fasta(arq_rat)
    
    arq_horse = fr"horse.fasta"
    horse = read_fasta(arq_horse)
    
    arq_hamster = fr"hamster.fasta"
    hamster = read_fasta(arq_hamster)
    
    #Verificação simples
    print("Verificação Simples entre hamster e rat: ")
    print(similar(hamster, rat))
    
    #Vetor e dicionario numérico de ocorrencias
    resultVector = ocurrenciesVector(hamster)
    resultDict = ocurrenciesDict(hamster)
    
    print("\nVetor numérico de Ocorrências de hamster: ")
    print(resultVector)
    
    print("\nDicionário numérico de Ocorrências de hamster: ")
    print(resultDict)
    
    #Distância Euclidiana
    euclidean_distance = euclideanDistance(horse, hamster)
    
    print("\nDistância Euclidiana entre horse e hamster: ")
    print(euclidean_distance)
    
    #Distância Manhattan
    manhattan_distance = manhattanDistance(horse, rat)
    
    print("\nDistância Manhattan entre horse e rat: ")
    print(manhattan_distance)
    
    #Distância Supremum
    supremum_distance = supremumDistance(hamster, rat)
    
    print("\nDistancia Supremum entre hamster e rat: ")
    print(supremum_distance)
    
    #Similaridade do Cosceno
    cosine_similarity = cosineSimilarity(horse, hamster)
    
    print("\nSimilaridade do Cosceno entre horse e hamster: ")
    print(cosine_similarity)
    

if __name__ == "__main__":
    main()
