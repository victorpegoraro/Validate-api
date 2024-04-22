from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
from validate_docbr import CPF, CNH, CNPJ, CNS

app = FastAPI(title="Validate API", version="0.1", summary="API to validate brazilian documents" )


@app.get("/")
def read_root():
    #return {"DOCS": "https://validate-api.onrender.com/docs"}
    return RedirectResponse("https://validate-api.onrender.com/docs", status_code=200)


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


@app.get("/validate-cns/{number}")
def validate_cnpj(number: Union[str, None] = None):

    cnpj = CNPJ()
    validate = cnpj.validate(number)
    if( validate ):
        number = cnpj.mask( number )

    return {"validate": validate, "doc": number, 'doc_type' : 'CNPJ'}


@app.get("/validate-cns/{number}")
def validate_cnpj(number: Union[str, None] = None):

    cns = CNS()
    validate = cns.validate(number)
    if( validate ):
        number = cns.mask( number )

    return {"validate": validate, "doc": number, 'doc_type' : 'CNS'}
