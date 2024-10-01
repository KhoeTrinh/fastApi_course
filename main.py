from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

class GenreURLChoices(Enum):
    KHOA1 = 'khoaone'
    KHOA2 = 'khoatwo'
    KHOA3 = 'khoathree'
    KHOA4 = 'khoafour'

BANDS = [
    {'id': 1, 'name': 'Khoa1', 'genre': 'Khoaone'},
    {'id': 2, 'name': 'Khoa2', 'genre': 'Khoatwo'},
    {'id': 3, 'name': 'Khoa3', 'genre': 'Khoathree'},
    {'id': 4, 'name': 'Khoa4', 'genre': 'Khoafour'},
]

@app.get('/bands')
def band() -> list[dict]:
    return BANDS

@app.get('/bands/{id}', status_code=201)
def bandById(id: int) -> dict:
    band = next((b for b in BANDS if b['id'] == id), None)
    if band is None:
        raise HTTPException(status_code=404, detail='Band not found');
    return band

@app.get('/bands/genres/{genre}', status_code=202)
def bandGenreById(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]
