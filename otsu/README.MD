# Atividade 4

## Implementar o algoritmo de limiarização global ótimo de Otsu.

1. Para obter apenas uma banda pego a imagem e utilizo a banda vermelha para os cálculos.

2. Obtive o histograma e o normalizei.

3. Então fiz o cálculo de variância para T de 1 até L-1. Ao invés de armazenar todos as variâncias num vetor, salvei apenas o t e o valor da maior variância.

4. Com o valor de T, fiz a limiarização deixando como 255 todos os pixels com intesidade maior que T e como 0 os com intensidade menor que T.

*O resultado da imagem se encontra em thresholded-image.jpg*

> ℹ️ Como rodar?
> 
> Entre na pasta do projeto e rode o comando python3 main.py nome-da-imagem.jpg.
>
> A imagem test.jpg pode ser usada para teste.