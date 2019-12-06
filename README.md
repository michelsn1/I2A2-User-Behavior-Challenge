Mouse Challenge
==============================

Competição do I2A2 para o desafio do mouse:
https://www.kaggle.com/c/i2a2-user-mouse-challenge

## Para configurar o projeto digite no terminal os seguintes comandos:

1) $ make create_environment

Irá criar um ambiente virtual;

2) $ source venv/bin/activate

Irá ativar o ambiente virtual;

3) $ make requirements

Irá instalar as bibliotecas necessárias para a execução do código;

4) $ make create_data_folder

Irá criar o dataset

**Atenção: Os dados na pasta recém criada Data devem obedecer a seguinte estrutura**
------------

    ├── data
    │   ├── processed             <- O dado final salvo pronto para o input dos modelos
    │   └── raw            
    │        ├──test_files        <- Pasta de Dados de teste para submissão direto do Kaggle
    │        ├──training_files    <- Pasta de Dados de treino para submissão direto do Kaggle
    │        ├──sample_submission <- Arquivo com a sample submission dos resultados
    │        ├──test_data.csv     <- Arquivo com o dataset compilado de submissão após o uso do comando 5
    │        └──train_data.csv    <- Arquivo com o dataset compilado de treino após o uso do comando 5
    │
    └── submissions            <- Pasta de arquivos de saída com as predições

--------

5) $ make create_raw_data

Irá criar os datasets compilando todos as diferentes pessoas de treino e validação num único arquivo

6) $ make predictions

Irá realizar a predição dos dados salvos em /data/raw/test_data.csv.
Salvando os resultados na pasta Submissions
OBS1: para alterar o arquivo de predição, basta mudar o path do arquivo em ./main.py

OBS2: Para treinar o modelo novamente basta rodar o notebook "Creating Processed Data and Trainning"
da pasta Notebooks.

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
