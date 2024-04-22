from typing import Union

from fastapi import FastAPI

from fastapi.responses import RedirectResponse, HTMLResponse

from cpf import cpf_validate

app = FastAPI()


@app.get("/")
def read_root():
    #return {"DOCS": "https://validate-api.onrender.com/docs"}
    return RedirectResponse("https://validate-api.onrender.com/docs", status_code=303)


@app.get("/cpf/{cpf}")
def read_item(cpf: Union[str, None] = None):

    validate = cpf_validate( cpf )

    return {"validate": validate, "doc": cpf}
