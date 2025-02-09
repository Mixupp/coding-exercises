from pydantic import BaseModel

class TodoItem(BaseModel):
    id: int       
    title: str    
    done: bool   
    description: str
    created_at: int
class NewTodoItem(BaseModel):
    title: str
    description: str

    
class ImageBody(BaseModel):
    prompt: str
    n: int
    size: str

class NoteItem(BaseModel):
    id: int       
    title: str     
    description: str
    created_at: int
class NewNoteItem(BaseModel):
    title: str
    description: str
