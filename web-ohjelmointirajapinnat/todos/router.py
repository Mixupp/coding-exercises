from datetime import datetime
from fastapi import APIRouter, Response
import sqlite3
from models import TodoItem, NewTodoItem

todos_router = APIRouter(tags=['Todos'])

con_todo = sqlite3.connect("todo_app.sqlite", check_same_thread=False)

sql_create_todo_table = "CREATE TABLE IF NOT EXISTS todo(id INTEGER PRIMARY KEY, title VARCHAR, description VARCHAR, done INTEGER, created_at INTEGER)"

with con_todo:
    con_todo.execute(sql_create_todo_table)

@todos_router.on_event("shutdown")
def database_disconnect():
    con_todo.close()

@todos_router.get('/todos')
def get_todos(response: Response, done: bool | None = None):
    try:
        with con_todo:
            if done is not None:
                cur = con_todo.execute("SELECT id, title, description, done, created_at FROM todo WHERE done = ?", (int(done),))
            else:
                cur = con_todo.execute("SELECT id, title, description, done, created_at FROM todo")

            values: list[TodoItem] = []

            for item in cur.fetchall():
                id, title, description, done, created_at = item
                todo = TodoItem(id=id, title=title, description=description, done=bool(done), created_at=created_at)
                values.append(todo)
            
            return values
    except Exception as e:
        response.status_code = 500
        return {"err": str(e)}

@todos_router.get('/todos/{id}')
def get_todo_by_id(id: int, response: Response):
    try:
        with con_todo:
            cur = con_todo.execute("SELECT id, title, description, done, created_at FROM todo WHERE id = ?", (id,))

            result = cur.fetchone()

            if result is None:
                response.status_code = 404
                return {"err": f"Todo item with id {id} does not exist."}

            id, title, description, done, created_at = result

            return TodoItem(
                id=id,
                title=title,
                description=description,
                done=bool(done),
                created_at=created_at
            )
    except Exception as e:
        response.status_code = 500
        return {"err": str(e)}
    
@todos_router.post('/todos')
def create_todo(todo_item: NewTodoItem, response: Response):
    try:
        with con_todo:
            dt = datetime.now()
            ts = int(datetime.timestamp(dt))
            cur = con_todo.execute("INSERT INTO todo (title, description, done, created_at) VALUES(?, ?, ?, ?)", (todo_item.title, todo_item.description, int(False), ts,))
            response.status_code = 201
            return TodoItem(id=cur.lastrowid, title=todo_item.title, done=False, description=todo_item.description, created_at=ts)
            
    except Exception as e:
        response.status_code = 500
        return {"err": str(e)}


@todos_router.put('/todos/{id}')
def update_todo(id: int, todo_item: TodoItem, response: Response):
    try:
        with con_todo:
            cur = con_todo.execute(
                "UPDATE todo SET title = ?, description = ?, done = ? WHERE id = ? RETURNING *",
                (todo_item.title, todo_item.description, todo_item.done, id,)
            )
            
            result = cur.fetchone()

            if result is None:
                response.status_code = 404
                return {"err": f"Todo item with id {id} does not exist."}

            id, title, description, done, created_at = result

            return TodoItem(
                id=id,
                title=title,
                description=description,
                done=bool(done),
                created_at=created_at
            )

    except Exception as e:
        response.status_code = 500
        return {"err": str(e)}

@todos_router.patch('/todos/{id}/{done}')
def update_todo_status(id: int, done: bool, response: Response):
    try:
        with con_todo:
            cur = con_todo.execute("UPDATE todo SET done = ? WHERE id = ? RETURNING done", (int(done), id,))
            result = cur.fetchone()

            if result is None:
                response.status_code = 404
                return {"err": f"Todo item with id {id} does not exist."}
            
            return {"done": bool(result[0])}

    except Exception as e:
        response.status_code = 500
        return {"err": str(e)}

@todos_router.delete('/todos/{id}')
def delete_todo(id: int, response: Response):
    try:
        with con_todo:
            cur = con_todo.execute("DELETE FROM todo WHERE id = ?", (id,))
            
            if cur.rowcount < 1:
                response.status_code = 404
                return {"err": f"Can't delete todo item, id {id} does not exist."}

            return "ok"

    except Exception as e:
        response.status_code = 500
        return {"err": str(e)}

    
