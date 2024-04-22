from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
from validate_docbr import CPF, CNH

app = FastAPI(title="Validate API", version="0.1" )


@app.get("/")
def read_root():
    #return {"DOCS": "https://validate-api.onrender.com/docs"}
    return RedirectResponse("https://validate-api.onrender.com/docs", status_code=303)


@app.get("/validate-cpf/{number}")
def validate_cpf(number: Union[str, None] = None):

    cpf = CPF()
    validate = cpf.validate(number)
    if( validate ):
        number = cpf.mask( number )

    return {"validate": validate, "doc": number, 'doc_type' : 'CPF'}


@app.get("/validate-cnh/{number}")
def validate_cpf(number: Union[str, None] = None):

    cnh = CNH()
    validate = cnh.validate(number)
    if( validate ):
        number = cnh.mask( number )

    return {"validate": validate, "doc": number, 'doc_type' : 'CNH'}
