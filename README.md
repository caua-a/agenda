# 📝 To-Do List em Python

Aplicativo de linha de comando simples para gerenciar tarefas (adicionar, remover, listar e marcar como concluída). Os dados são persistidos em arquivos `.txt`.

---

## 📌 Funcionalidades

* Adicionar tarefas (salva em `tarefas.txt`)
* Remover tarefas (atualiza `tarefas.txt`)
* Listar tarefas pendentes (lê `tarefas.txt`)
* Marcar tarefa como concluída (mantém em memória em `lista_concluido`)
* Listar tarefas concluídas
* Sair do programa

---

## 📂 Estrutura do projeto

```text
to-do_python/
├── main.py          # Menu e loop principal
├── func.py          # Funções (Adicionar, Remover, Listar, Concluir, etc.)
├── tarefas.txt      # Armazena tarefas pendentes (texto, uma por linha)
└── concluidas.txt   # (opcional) onde tarefas concluídas podem ser salvas
```

---

## 🚀 Como executar

1. Certifique-se de ter Python 3 instalado.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python main.py
```

---

## 🧭 Uso (menu)

Ao executar, você verá um menu com opções:

```
1. Adicionar Tarefa
2. Remover Tarefa
3. Listar Tarefas
4. Concluir
5. Listar Concluídos
6. Sair
```

Digite o número da opção e pressione Enter.

---

## 💾 Como os dados são armazenados

* **tarefas.txt** — tarefas pendentes; o programa adiciona novas entradas usando modo append (`a`) e a função `carregar_tarefas` lê esse arquivo para popular a lista em memória.
* **concluidas.txt** — As tarefas marcadas como concluídas são adicionadas à lista em memória (`lista_concluido`) durante a execução, mas não são persistidas em disco a menos que você implemente essa gravação.

---

## 🛠 Arquivos principais

* **main.py** — contém o loop principal e o menu; importa funções de `func.py`.
* **func.py** — contém as funções:

  * `Adicionar_tarefa()` — pede input e adiciona (salva em `tarefas.txt`)
  * `Remover_tarefa()` — remove da lista e chama `salvar_tarefas`
  * `carregar_tarefas(nome_arquivo)` — lê e popula `lista_tarefas`
  * `salvar_tarefas(nome_arquivo, lista)` — grava lista no arquivo
  * `concluida()` — marca tarefa como concluída (apaga da pendente e adiciona à lista de concluídos em memória)
  * `listar_concluidos()` — imprime a lista de concluídos em memória
  * `Sair()` — encerra o programa

---

## 📝 Exemplo de fluxo

1. Executar `python main.py`
2. Escolher `1` → digitar a tarefa → tarefa salva em `tarefas.txt`
3. Escolher `3` → listar tarefas carregadas de `tarefas.txt`
4. Escolher `4` → marcar uma tarefa como concluída
5. Escolher `5` → ver tarefas concluídas na sessão atual

---

## 🤝 Contribuição

1. Commit e pull request com a descrição da melhoria

---
