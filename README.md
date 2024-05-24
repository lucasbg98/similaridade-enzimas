# similaridade-enzimas
Repositório referente a um modelo que testa a similardade de enzimas entre diferentes organismos

Os três arquivos anexados representam as sequências DNA de enzima topoisomerase 1 de três
organismos: rato (rat.fasta), hamster chinês (hamster.fasta) e cavalo (horse.fasta). Usando
sequências armazenadas nestes arquivos, foi implementado um algoritmo em Python que realiza:
- uma comparação de proximidade usando verificação simples entre dois organismos;
- a contagem de ocorrência de cada aminoácido nas sequências construindo um vetor
numérico de ocorrências e o calculo das distâncias Manhattan, euclidiana, supremum, e a
similaridade de cosseno entre dois organismos.
