from fastapi import FastAPI, Path
from fastapi.responses import FileResponse
from pydantic import BaseModel
from mixtaper import mix

app = FastAPI()


class Links(BaseModel):
    links: list[str]


@app.get("/")
def test():
    return {"Hello": "World"}


@app.post("/youtube")
def get_mixtape(songs: Links):
    mix(songs.links)
    return FileResponse("mixtape.mp3", media_type="audio/mp4")