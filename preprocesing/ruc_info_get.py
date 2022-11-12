import requests


# params= {"ruc": "1792692091001"}
# autorization=''
# headers= {
#     "Content-Type": "application/json",
#     "Authorization":autorization
#     }

def get_ruc_info(ruc_list,authorization):
    URL= "https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/ConsolidadoContribuyente/obtenerPorNumerosRuc?"
    for ruc in ruc_list:
        URL= URL + "ruc=" + ruc + "&"
    headers= {
    "Content-Type": "application/json",
    "Authorization":authorization
    }
    try:
        response = requests.get(URL, headers=headers)
        return response.json()
    except Exception as e:
        return e
