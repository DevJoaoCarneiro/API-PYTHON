# Trabalho de Python Orientado a Objeto

## API To Do List

Projeto de uma API simples para gerenciamento de tarefas.

## Integrantes

- Joao Victor Carneiro
- Donato Valentino de Vellis
- Felipe de souza
- Luan Araujo Mello

## Endpoints

- `GET /` - verifica se a API esta funcionando
- `POST /tasks/` - cria uma nova tarefa
- `GET /tasks/` - lista todas as tarefas
- `GET /tasks/{task_id}` - busca uma tarefa pelo id
- `DELETE /tasks/{task_id}` - remove uma tarefa pelo id

## Exemplo de envio no POST /tasks/

```json
{
  "title": "Estudar Python",
  "description": "Fazer o trabalho da faculdade"
}
```

## Comando para rodar o projeto

```powershell
uvicorn app.main:app --reload
```

## Acesso

- API: `http://127.0.0.1:8000`
- Documentacao: `http://127.0.0.1:8000/docs`
