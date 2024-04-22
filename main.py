from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
from validate_docbr import CPF, CNH, CNPJ, CNS
import re

# Config FastApi
tags_metadata = [
    {
        "name": "Validate number",
        "description": "Logical validation of document numbers",
    },
    {
        "name": "Validate card",
        "description": "Validate card informations",
        # "externalDocs": {
        #     "description": "Items external docs",
        #     "url": "https://fastapi.tiangolo.com/",
        # },
    },
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

@app.get("/card-brand/{number}", tags=["Validate card"] )
def card_brand(number: Union[str, None] = None):
    # Brands regex
    brands = {
        'visa': r'^4\d{12}(\d{3})?$',
        'mastercard': r'^(5[1-5]\d{4}|677189)\d{10}$',
        'diners': r'^3(0[0-5]|[68]\d)\d{11}$',
        'discover': r'^6(?:011|5[0-9]{2})[0-9]{12}$',
        'elo': r'^((((636368)|(438935)|(504175)|(451416)|(636297))\d{0,10})|((5067)|(4576)|(4011))\d{0,12})$',
        'amex': r'^3[47]\d{13}$',
        'jcb': r'^(?:2131|1800|35\d{3})\d{11}$',
        'aura': r'^((?!504175))^((?!5067))(^50[0-9])/', # '/^(5078\d{2})(\d{2})(\d{11})$/',
        'hipercard': r'^(606282\d{10}(\d{3})?)|(3841\d{15})$',
        'maestro': r'^(?:5[0678]\d\d|6304|6390|67\d\d)\d{8,15}$',
    }

    # Run test
    card_number = number
    validate = False
    brand = None
    for _brand, regex in brands.items():
        if re.match(regex, card_number):
            brand = _brand
            validate = True
            break

    return {"validate": validate, "brand": brand}
