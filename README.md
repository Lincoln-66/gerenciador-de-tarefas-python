# Gerenciador de Tarefas em Python

Um projeto de linha de comando desenvolvido em Python para praticar lógica de programação e manipulação de dados. O programa permite cadastrar, listar, concluir e excluir tarefas por meio de um menu interativo.

## Funcionalidades

- **Cadastrar tarefas:** adicionar uma ou várias tarefas.
- **Listar tarefas:** visualizar todas as tarefas cadastradas e seus respectivos estados.
- **Concluir tarefas:** marcar tarefas como concluídas.
- **Excluir tarefas:** remover tarefas da lista.
- **Menu interativo:** navegar pelas funcionalidades até escolher a opção de sair.

## Tecnologias utilizadas

- Python 3.10 ou superior
- Listas e dicionários
- Estruturas de controle: `while`, `for`, `if/else` e `match/case`

## Como executar o projeto

**1. Clone o repositório**

```bash
git clone https://github.com/Lincoln-66/gerenciador-de-tarefas-python
```

**2. Entre na pasta do projeto**

```bash
cd nome-do-repositorio
```

**3. Execute o programa**

```bash
python main.py
```

Caso seu arquivo tenha outro nome, substitua `main.py` pelo nome correto.

## Exemplo de utilização

Ao executar o programa, será exibido um menu semelhante a este:

```text
1. Cadastrar tarefa
2. Listar tarefas
3. Concluir tarefa
4. Excluir
0. Sair
```

As tarefas são armazenadas em uma lista de dicionários, contendo o nome da tarefa e seu estado de conclusão.

Exemplo de uma tarefa:

```python
{
    "nome": "Estudar Python",
    "concluida": False
}
```

## Objetivo do projeto

Este projeto faz parte do meu processo de aprendizado em Python, com foco em desenvolver habilidades práticas de programação e construir projetos progressivamente mais completos.

Conceitos praticados:

- Listas e dicionários
- Laços de repetição
- Condicionais e controle de fluxo
- Manipulação de dados
- Organização de um programa interativo
- Operações básicas de cadastro, consulta, atualização e exclusão (CRUD)

## Melhorias futuras

- [ ] Separar as funcionalidades em funções.
- [ ] Validar as entradas do usuário.
- [ ] Tratar erros com `try/except`.
- [ ] Salvar as tarefas em um arquivo JSON para mantê-las após encerrar o programa.
- [ ] Adicionar testes automatizados.
- [ ] Melhorar a organização do código.

## Autor

Desenvolvido como projeto de estudo para aprimorar minhas habilidades em Python.

Feedbacks e sugestões são bem-vindos!