from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
from validate_docbr import CPF, CNH, CNPJ, CNS

# Config FastApi
tags_metadata = [
    {
        "name": "Validate number",
        "description": "Logical validation of document numbers",
    },
    # {
    #     "name": "items",
    #     "description": "Manage items. So _fancy_ they have their own docs.",
    #     "externalDocs": {
    #         "description": "Items external docs",
    #         "url": "https://fastapi.tiangolo.com/",
    #     },
    # },
]

# Start FastApi
app = FastAPI(title="Validate API", version="0.2", summary="API to validate brazilian documents", openapi_tags=tags_metadata )

@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse("https://validate-api.onrender.com/docs", status_code=200)


@app.get("/validate-cpf/{number}", tags=["Validate number"])
def validate_cpf(number: Union[str, None] = None):

    cpf = CPF()
    validate = cpf.validate(number)
    if( validate ):
        number = cpf.mask( number )

    return {"validate": validate, "doc": number, 'doc_type' : 'CPF'}


@app.get("/validate-cnh/{number}", tags=["Validate number"])
def validate_cnh(number: Union[str, None] = None):

    cnh = CNH()
    validate = cnh.validate(number)
    if( validate ):
        number = cnh.mask( number )

    return {"validate": validate, "doc": number, 'doc_type' : 'CNH'}


@app.get("/validate-cnpj/{number}", tags=["Validate number"])
def validate_cnpj(number: Union[str, None] = None):

    cnpj = CNPJ()
    validate = cnpj.validate(number)
    if( validate ):
        number = cnpj.mask( number )

    return {"validate": validate, "doc": number, 'doc_type' : 'CNPJ'}


@app.get("/validate-cns/{number}", tags=["Validate number"])
def validate_cns(number: Union[str, None] = None):

    cns = CNS()
    validate = cns.validate(number)
    if( validate ):
        number = cns.mask( number )

    return {"validate": validate, "doc": number, 'doc_type' : 'CNS'}
