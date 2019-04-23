# Arquitetura II - Projeto I

## Descrição da atividade

- Escolha um programa de código aberto na internet
  - Analise seu código em busca de partes que não exploram corretamente o uso de memória cache
  - Apresente as modificações e apresenta uma comparação no tempo de execução
- Elabore um relatório técnico onde você apresenta
  - Qual código utilizado (com URL, mas sem o código-fonte) 
  - Quais pontos de melhoria foram encontrados
  - Que mudanças você propôs
  - Quais as melhorias em desempenho? (apresentar gráficos ou tabelas)
- Se você não encontrar um código-fonte adequado, você deve implementar um código seu e apresentar uma comparação entre sua versão com - e sem otimização de memória.
- Enviar o relatório por e-mail e apresentar a execução ao professor em sala de aula na data estabelecida

# Sobre o projeto

É um projeto simples que pega uma imagem de qualquer tamanho e deixa em uma escala monocromatica. Podendo ser cinza, vermelha, azul ou verde

## Dependencias

### Numpy
```sh
sudo apt-get install python-pip  
sudo pip install numpy
```

### OPenCV
```sh
sudo apt-get install python-opencv
```

* Qualquer problema com alguma bilbioteca, tente instalar para o python3

## Como executar

```sh
python3 main_v<versao>.py -i <caminho_da_imagem> -c <cor> -o <caminho_para_salvar_a_imagem>
```

Parametros

    -i | --image   :   caminho_da_imagem original                       : opcional (usa uma imagem padrão na raiz do repositorio)
    -c | --scale   :   cor. Pode ser ["gray", "red", "blue", "green"]   : opcional (default é cinza)
    -o | --output  :   caminho_para_salvar_a_imagem                     : obrigatorio


# Arquitetura II - Projeto II

- A segunda parte do projeto consiste em criar mais uma versão do código, mas utilizando o paralelismo

## Observações

1. Foi feito 3 maneiras de paralelizar o processo: usando threads, usando processos, usando procesos com memória compartilhada.

1.1. **Usando threads**: quando se divide o programa em threads, elas se distribuem pelos processadores (no meu caso são 4), mas por algum motivo elas não executado com 100$ da capacidade (compartilham o mesmo interpretador) (custo piora, pois além de compartilhar o mesmo interpretador, tem o custo de ficar trocando de thread)


1.2 **Usando processos**: O melhor dos casos. Aqui, cada processo é executado com 100% da capacidade e o tempo de execução é visibvelmente melhor. O problema é que como cada processo é criado a partir de um fork, o retorno do processamento de cada work não é feito (em c/c++ poderíamos compartilhar a memória através de ponteiros)


1.3 **Usando processos com memória compartilhada**: Pesquisando um pouco, existe uma maneira de compartilhar memória entre os processos python. Porém essa abordagem gera um join muito demorado. E a causa ainda é desconhecida


## Como executar
```sh
python main_v6.py -i <imagem_original> -o <imagem de saída> -t <número de processos>
```

Para trocar o tipo de abordagem, em `main_v5.py` altere o import para o desejado, por exemplo:
```py
# from handythread import foreach # Thread
from handythread2 import foreach # Processo
# from handythread3 import foreach # Processo compartilhando memoria
```

## Relatorio
[link](Relatorio_Arq_2.pdf)



# Grupo
- Aline Moura Araújo
- Luiz Henrique Freire Barros