# Algoritmo DDA
<img align="right" src="https://deno.land/logo.svg" height="150px" alt="the deno mascot dinosaur standing in the rain">

### Funcionalidades

O algoritmo recebe dois pontos do plano 2D e faz o cálculo de todos os pontos de uma reta aproximada entre eles.

Como retorno é impresso no terminal os pontos um por linha no formato: (x, y).

### Tecnologias

O código foi feito usando **TypeScript** e compilado através do [Deno](https://deno.land/std/).

### Como rodar?

Clone o repositório.

```shell
git clone https://github.com/rricoldi/computer-graphics.git
```

Entre no diretório.

```shell
cd computer-graphics
```

E então, basta rodar o programa dda passando como argumentos os pontos de início e fim.

```shell
# ./dda x1 y1 x2 y2
./dda 6 9 11 12

# caso esteja rodando no windows use dda-windows.exe
./dda-windows 6 9 11 12

# exemplo de retorno
# (6, 9)
# (7, 10)
# (8, 10)
# (9, 11)
# (10, 11)
# (11, 12)
```



