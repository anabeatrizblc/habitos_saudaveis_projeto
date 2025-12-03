SISTEMA DE HÁBITOS SAUDÁVEIS

O Sistema de Hábitos Saudáveis é uma aplicação em Python que permite criar usuários, cadastrar hábitos, registrar atividades diárias e gerar relatórios com base nos dados armazenados. O projeto foi desenvolvido com foco em modularização, organização e fácil manutenção.

============================================================

FUNCIONALIDADES

GERENCIAMENTO DE USUÁRIOS

- Criar, listar, editar e remover usuários.
- Os dados são armazenados no arquivo usuarios.json.

GERENCIAMENTO DE HÁBITOS

- Criar hábitos com nome, descrição e periodicidade.
- Associar hábitos aos usuários.
- Listar e remover hábitos.
- Dados armazenados em habitos.json.

REGISTROS DIÁRIOS

- Registrar quando um hábito foi realizado em um dia específico.
- Consultar histórico por hábito ou por usuário.
- Dados armazenados em registros.json.

RELATÓRIOS

- Quantidade total de hábitos concluídos em um período.
- Porcentagem de adesão aos hábitos.
- Histórico completo de realizações.

============================================================

ESTRUTURA DO PROJETO

habitos_saudaveis/
data/
usuarios.json
habitos.json
registros.json

src/
app.py
CRUD_usuarios.py
CRUD_habitos.py
CRUD_registros.py
relatorios.py

README.md

============================================================

COMO EXECUTAR

1. Abra o terminal dentro da pasta do projeto.

2. Execute o comando abaixo:

python3 src/app.py

Depois disso, o menu principal será exibido na tela, permitindo navegar pelas opções de Usuários, Hábitos, Registros Diários e Relatórios.

============================================================

TECNOLOGIAS UTILIZADAS

Python 3.8 ou superior.
Armazenamento em arquivos JSON.
Código dividido em módulos para facilitar manutenção.

============================================================

OBJETIVO DO PROJETO

Este projeto foi criado para praticar conceitos fundamentais de programação, como:

- CRUD (Create, Read, Update, Delete)
- Manipulação de arquivos JSON
- Menus interativos
- Modularização do código
- Organização de pastas e responsabilidades entre arquivos

============================================================

MELHORIAS FUTURAS

Implementar mais funções nos relatórios, como:

- Histórico agrupado por período (semanal, mensal, anual)
- Ranking de hábitos mais realizados
- Identificação de hábitos com baixa adesão
- Relatórios filtrados por usuário ou por categoria

============================================================