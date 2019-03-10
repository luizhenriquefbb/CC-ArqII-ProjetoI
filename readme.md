# Arquitetura II - Projeto I

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


# Grupo
- Aline Moura Araújo
- Luiz Henrique Freire Barros