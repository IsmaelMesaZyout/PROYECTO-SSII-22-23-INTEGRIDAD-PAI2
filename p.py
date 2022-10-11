import secrets

def gen_nonce():
    cod_nonce = secrets.token_urlsafe()
    return cod_nonce


print(gen_nonce())