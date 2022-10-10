# Algoritmos genéticos

<p>
Algoritmo feito em python para descrever o funcionamento de um algoritmo genético passo-a-passo. Implementação baseada no <a href="https://www.geeksforgeeks.org/genetic-algorithms/">exemplo sobre algoritmos genéticos</a> do GeeksForGeeks.
</p>

<br>

## O que é um algoritmo genético?

<p align="justify">
Algoritmos genéticos são modelos matemáticos baseados em conceitos de biologia evolutiva, frequentemente utilizados na otimização de problemas ao gerar um conjunto de soluções que se adaptam evolutivamente até obter o que seria a solução ideal mais próxima para determinado problema.
</p>

## Como o algoritmo funciona?

<p align="justify">
Da forma como fora implementado, o algoritmo pedirá a solução final do problema para que, sabendo disso, ele consiga implementar uma série de heurísticas a partir de um determinado ponto, até chegar na solução que lhe foi proposta. Nesse caso em específico o algoritmo deve encontrar a string "testando o algoritmo".
</p>

<img src="assets/testing.png" />

<p align="justify">
Após isso o algoritmo trabalhará através de várias funções que simulam comportamentos biológicos, como a criação de gerações, cruzamento e mutações entre as possíveis soluções. Como neste caso o objetivo é encontrar uma determinada sequência de caracteres, o algoritmo testará várias e várias sequências de combinações para encontrar o resultado correto, usando das heurísticas propostas para tal.
</p>

<img src="assets/generations.png">

<p align="justify">
Passando gerações de possíveis resultados, nota-se que a solução vai chegando cada vez mais perto do ideal, onde todas essas possíveis soluções estão sendo encontradas através de cruzamentos entre os mesmos, onde o caractere que faz parte da solução é preservado na geração seguinte e assim suscetivamente até que se encontre o resultado esperado.
</p>

<img src="assets/final.png">

<br>