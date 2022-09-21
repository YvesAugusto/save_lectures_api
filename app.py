from fastapi import FastAPI, Path, Response, Body, Request, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from cruds import save
import schemas
import logging

logger = logging.getLogger('lectures')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('lectures.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler(stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

FILEPATH = '/home/pi/data/data.json'

app = FastAPI()

@app.post('/api/v1/lectures/save', tags=['api/lectures'])
async def save_lectures_on_json(
    results: schemas.Results = Body(embed=True)
):
    results_to_json = jsonable_encoder(results)
    valid, message, status_code = save.save_results_to_json(results_to_json, FILEPATH)
    return JSONResponse(content={"message": message, "data": results_to_json}, status_code=status_code)