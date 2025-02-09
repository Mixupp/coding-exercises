
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")



# Tuodaan routerit omista kansioistaan
from todos.router import todos_router
from ai_images.router import ai_image_router
from notes.router import notes_router



app = FastAPI()

# CORS tarvitaan kun tehdään client sovellusta, 
# muutoin requestit React clientilta eivät ole 
# mahdollisia kehitysvaiheessa koska React kehityspalvelimen 
# origin tulee olemaan eri kuin API:n.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lisätään tuodut routerit app instanssiin.
app.include_router(todos_router)
app.include_router(ai_image_router)
app.include_router(notes_router)

