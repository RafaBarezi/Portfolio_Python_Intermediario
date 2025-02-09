# Tratando de uma API

usuario = {
    "nome":"joao",
    "redes":[{
        "nome": "Facebook",
        "imagem_profile": "",
        "imagem_capa": "imagem_01"
    },{
        "nome": "Twitter",
        "imagem_profile": "imagem_02",
        "imagem_capa": ""
    }]
}

# retorna a imagem do profile
def get_imagem_profile(usuario):
    for rede in usuario["redes"]:
        if rede[imagem_profile]: # type: ignore
            return rede["imagem_profile"]
    return "default"

# retorna a imagem de capa 
def get_imagem_capa(usuario):
    for rede in usuario["redes"]:
        if rede[imagem_capa]:# type: ignore
            return rede["imagem_capa"]
    return "default"

# utilizando o partial 
from functools import partial
def get_imagem(qual_imagem, usuario):
    for rede in usuario["redes"]:
        if rede[qual_imagem]:
            return rede[qual_imagem]
    return "default"

get_imagem_profile = partial(get_imagem, "imagem_profile")
get_imagem_capa = partial(get_imagem, "imagem_capa")

print("\nsaida partial final")
print(get_imagem_profile(usuario))
print(get_imagem_capa(usuario),"\n")