from fastapi import FastAPI
from service import FizzBuzzService, MegaSumator

from starlette.testclient import TestClient
app = FastAPI()


@app.get("/fizzbuzz/")
async def read_main(first: int = 0, last: int = 0):
    fizzbuzz = FizzBuzzService(MegaSumator)
    response = fizzbuzz.get(first, last)
    return {'result': response}


