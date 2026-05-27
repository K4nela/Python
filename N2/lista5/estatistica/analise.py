def estatisticas(dados, campo):
    valores = [item[campo] for item in dados]

    return {
        'media': sum(valores) / len(valores),
        'minimo': min(valores),
        'maximo': max(valores),
        'total': sum(valores)
    }
        