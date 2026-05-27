_registro = {}

def registrar(resultado, callback):
    _registro.setdefault(resultado, []).append(callback)

def disparar(resultado):
    callbacks = _registro.get(resultado, [])
    if callbacks:
        for cb in callbacks:
            cb(resultado)
    else:
        print(f"  Resultado {resultado}: nenhum evento especial.")
    