from typing import Union

from fastapi import FastAPI

from src.integrations.evolutionApi.router import evolutionApi
from src.integrations.n8n_integration.router import n8n_router

app = FastAPI()

########################################################
################     Routes     #######################
########################################################

app.include_router(router=evolutionApi, prefix="/evolution-api", tags=["Evolution API"])

app.include_router(router=n8n_router, prefix="/n8n", tags=["n8n"])


########################################################
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
