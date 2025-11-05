# Código em C — Cadastro e Lançamento de Notas

Esta pasta contém o código desenvolvido em **C** para o projeto **Sistema Acadêmico Colaborativo com IA (Unikrag)**.  
O objetivo do programa é permitir o **cadastro de alunos** e o **lançamento de notas**, simulando as funções administrativas e docentes da instituição.

---

## Funcionalidades

- Cadastrar novos alunos (matrícula, nome, CPF, RG, sexo, data de nascimento);
- Listar todos os alunos cadastrados;
- Lançar notas (NP1, NP2 e PIM) associadas à matrícula;
- Armazenar os dados em arquivos de texto (`alunos.txt` e `notas.txt`).

---

## Estrutura dos Arquivos

📁 codigo-c/
├── cadastro_alunos.c → código principal em C
├── alunos.txt → registros de alunos cadastrados
└── notas.txt → notas lançadas por matrícula


---

## Como Executar

### Compilar:
```bash
gcc cadastro_alunos.c -o cadastro
Executar:
./cadastro


Durante a execução, o menu oferece as seguintes opções:

1 - Cadastrar novo aluno
2 - Listar todos os alunos
3 - Lançar notas
0 - Sair

## Aprendizados

Este módulo reforçou conceitos de programação estruturada, como:

uso de structs;

manipulação de arquivos (fopen, fscanf, fprintf);

controle de fluxo e menus interativos;

integração com outro sistema (Python) via troca de arquivos.

Desenvolvido por Unikrag — ADS, 2º semestre (2025).
