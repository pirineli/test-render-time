from fastapi import FastAPI
from datetime import datetime, timedelta, timezone

app = FastAPI()

fuso_sp = timezone(timedelta(hours=-3))

@app.get("/")
def read_root():
    return {"message": "Server is running!"}

@app.get("/now")
async def agora():
    agora_sp = datetime.now(fuso_sp)
    return {"now": agora_sp.strftime('%Y-%m-%d %H:%M:%S %z')}
