from fastapi import FastAPI, Path
from fastapi.responses import FileResponse
from pydantic import BaseModel
from mixtaper import mix, status

app = FastAPI()


class Links(BaseModel):
    links: list[str]


@app.get("/")
def test():
    return {"Hello": "World"}


@app.post("/youtube")
def get_mixtape(songs: Links):
    mix(songs.links)
    return {"Files": "Uploaded"}


@app.get("/youtube")
def mixtape():
    return FileResponse("mixtape.mp3", media_type="audio/mp4")


@app.get("/status")
def getStatus():
    return { "status" : status }
