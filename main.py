import os

from fastapi import FastAPI, Path, BackgroundTasks
from fastapi.responses import FileResponse
from pydantic import BaseModel
from mixtaper import mix
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)

class Links(BaseModel):
    links: list[str]


@app.get("/")
def test():
    return {"Hello": "API works"}


@app.post("/youtube")
async def get_mixtape(songs: Links,background_tasks: BackgroundTasks):
    try:
        os.remove("mixtape.mp3")
    except:
        print("Mixtape not found")
    background_tasks.add_task(mix, songs.links)
    return {"Files": "Added to background"}


@app.get("/youtube")
def mixtape():
    if os.path.isfile("mixtape.mp3"):
        return FileResponse("mixtape.mp3", media_type="audio/mp4")
    else:
        return {"File": "Not Found"}
