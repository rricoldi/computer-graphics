# Atividade 3

## Implementar a transformada e a transformada inversa discreta do cosseno

As transformadas foram implementadas com as funções: 
  
  * get_bi_dimensional_dct_by_image: que recebe uma banda de uma imagem e retorna uma matriz no domínio da frequência.
  * get_image_by_bi_dimensional_dct: que recebe uma matriz no domínio da frequência e retorna uma banda de uma imagem.

*O resultado de uma imagem que passou pelos dois processos está em 'image-with-dct-and-inversed-dct.jpg'.*

---

## Implementar os filtros passa-baixas e passa-altas ideais

Implementei uma função que recebe um filtro e aplica ele em todos os pixels de uma matriz.

Criei os dois filtros com as funções fpbi e fpai.

E passando ambos com a distância provida pelo usuário, consigo as matrizes filtradas, que convoluídas com a matriz de frequências geram a matriz filtrada.

*O resultado de uma imagem que passou pelos filtros fpbi e fpai estão consecutivamente em 'image-filtered-with-fpbi.jpg' e 'image-filtered-with-fpai.jpg'.*

---

## Gerar um ruído periódico em uma imagem de sua preferência e testar o funcionamento dos filtros passa-baixa e passa-alta implementados

A imagem com ruído utilizada foi 'noisy-baby.jpg'.

---

## Criar um ruído no espectro da frequência obtido com a transformada discreta do cosseno e verificar o resultado no domínio espacial

Para criar o ruído mudei alguns valores da matriz de frequência para 255 na função generate_frequency_noise.

Para verificar esse resultado utilizei a imagem 'finger-print.jpg'.

*O resultado de uma imagem que recebeu ruído em sua matriz de frequência está em 'imagem-with-noise.jpg'*

---

> ℹ️ Como rodar?
> 
> Entre na pasta do projeto e rode o comando python3 main.py nome-da-imagem.jpg, em seguida escolha as distâncias para os filtros.