# Programa To Do List

## Descrição Geral

Este programa é uma aplicação de lista de tarefas (To Do List) desenvolvida em Python utilizando a biblioteca Tkinter para a interface gráfica. Ele permite adicionar, atualizar e deletar itens da lista de tarefas, além de exibir mensagens de erro quando necessário.

## Estrutura da Classe  `Application`

### Inicialização (`__init__`)

O método  `__init__`  é responsável por inicializar a interface gráfica e os componentes da aplicação.

-   **Parâmetros:**
    
    -   `master`: O widget pai para a aplicação Tkinter.
-   **Atributos:**
    
    -   `selected_index`: Índice do item selecionado na lista.
    -   `project_font`: Fonte padrão utilizada na aplicação.
    -   `title_container`,  `text_container`,  `list_container`,  `error_container`: Containers para organizar os widgets na interface.
    -   `titulo`: Label que exibe o título da aplicação.
    -   `item_title`: Campo de entrada para o título do item.
    -   `add_item`,  `delete_item`,  `update_item`: Botões para adicionar, deletar e atualizar itens, respectivamente.
    -   `scrollbar`: Barra de rolagem para a lista de tarefas.
    -   `listbox_tasks`: Listbox que exibe as tarefas.
    -   `task_list`: Lista que armazena as tarefas.
    -   `error_handling`: Label que exibe mensagens de erro.

### Métodos

#### `add_item_clicked(self)`

Adiciona um novo item à lista de tarefas.

-   **Comportamento:**
    -   Verifica se o campo de entrada está vazio ou contém apenas espaços em branco.
    -   Exibe uma mensagem de erro se o campo estiver vazio.
    -   Adiciona o item à lista de tarefas e limpa a mensagem de erro.
    -   Insere o novo item no  `Listbox`.
    -   Limpa o campo de entrada.

#### `delete_item_clicked(self)`

Deleta o item selecionado da lista de tarefas.

-   **Comportamento:**
    -   Remove o item da lista de tarefas com base no índice selecionado.
    -   Exibe uma mensagem de erro se nenhum item estiver selecionado.
    -   Limpa o campo de entrada.

#### `update_item_clicked(self)`

Atualiza o item selecionado na lista de tarefas.

-   **Comportamento:**
    -   Atualiza o item na lista de tarefas com base no índice selecionado.
    -   Exibe uma mensagem de erro se nenhum item estiver selecionado.
    -   Insere o item atualizado no  `Listbox`.

#### `items_selected(self, event)`

Atualiza o campo de entrada com o item selecionado na lista de tarefas.

-   **Parâmetros:**
    
    -   `event`: Evento de seleção do Listbox.
-   **Comportamento:**
    
    -   Atualiza o índice selecionado e preenche o campo de entrada com o item correspondente.

#### `clear_error_message(self)`

Limpa a mensagem de erro exibida.

### Funções Auxiliares

#### `clear_error_message(self)`

Limpa a mensagem de erro exibida.

### Função Principal

#### `main()`

Função principal para iniciar a aplicação.

  
<div align="center">  
  
## <b> Entre em Contato..!</b><img src="https://github.com/0xAbdulKhalid/0xAbdulKhalid/raw/main/assets/mdImages/handshake.gif" width ="80">
<div>
<a href = "mailto:emilly.fernandesads@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
<a href="https://www.linkedin.com/in/emilly-fernandes" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>  
<a href="https://leetcode.com/emilyfas/" target="_blank"><img src="https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black" target="_blank"></a> 
</div>
</div>
