from datetime import datetime
from fastapi import APIRouter, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

from models import NoteItem, NewNoteItem

notes_router = APIRouter(tags=['Notes'])

con_note = sqlite3.connect("todo_app.sqlite", check_same_thread=False)
sql_create_note_table = "CREATE TABLE IF NOT EXISTS note(id INTEGER PRIMARY KEY, title VARCHAR, description VARCHAR, created_at INTEGER)"

with con_note:
    con_note.execute(sql_create_note_table)

@notes_router.on_event("shutdown")
def database_disconnect():
    con_note.close()

@notes_router.get('/notes')
def get_notes(response: Response):
    try:
        with con_note:
            cur = con_note.execute("SELECT id, title, description, created_at FROM note")
            values: list[NoteItem] = []

            for item in cur.fetchall():
                id, title, description, created_at = item
                note = NoteItem(id=id, title=title, description=description, created_at=created_at)
                values.append(note)
            
            return values
        
    except Exception as e:
        response.status_code = 500
        return {"err": str(e)}

@notes_router.get('/notes/{id}')
def get_note_by_id(id: int, response: Response):
    try:
        with con_note:
            cur = con_note.execute(
                "SELECT id, title, description, created_at FROM note WHERE id = ?", (id,))

            result = cur.fetchone()

            if result is None:
                response.status_code = 404
                return {"err": f"Note item with id {id} does not exist."}

            id, title, description, created_at = result

            return NoteItem(
                id=id,
                title=title,
                description=description,
                created_at=created_at
            )
    except Exception as e:
        response.status_code = 500
        return {"err": str(e)}

@notes_router.post('/notes')
def create_note(note_item: NewNoteItem, response: Response):
    try:
        with con_note:
            dt = datetime.now()
            ts = int(datetime.timestamp(dt))
            cur = con_note.execute("INSERT INTO note (title, description, created_at) VALUES (?, ?, ?)", (note_item.title, note_item.description, ts,))
            response.status_code = 201
            return NoteItem(id=cur.lastrowid, title=note_item.title, description=note_item.description, created_at=ts)
            
    except Exception as e:
         response.status_code = 500
         return {"err": str(e)}

@notes_router.put('/notes/{id}')
def update_note(id: int, note_item: NoteItem, response: Response):
    try:
        with con_note:
            cur = con_note.execute(
                "UPDATE note SET title = ?, description = ? WHERE id = ? RETURNING *", (note_item.title, note_item.description, id,))
            
            result = cur.fetchone()

            if result is None:
                response.status_code = 404
                return {"err": f"Note item with id {id} does not exist."}

            id, title, description, created_at = result

            return NoteItem(
                id=id,
                title=title,
                description=description,
                created_at=created_at
            )

    except Exception as e:
        response.status_code = 500
        return {"err": str(e)}

    
@notes_router.delete('/notes/{id}')
def delete_note(id: int, response: Response):
    try:
        with con_note:
            cur = con_note.execute("DELETE FROM note WHERE id = ?", (id,))

            if cur.rowcount < 1:
                response.status_code = 404
                return {"err": f"Can't delete note item, id {id} does not exist."}

            return "ok"

    except Exception as e:
        response.status_code = 500
        return {"err": str(e)}
    

@notes_router.on_event("shutdown")
def database_disconnect():
    con_note.close()