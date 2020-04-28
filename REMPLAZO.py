# Hermes Raymundo Campos De la Fuente - Overclockes Mexico SA de CV
# Import de libs necesarias
import pymsteams
import requests  # para hacer peticiones HTTP
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # Para ignorar certificados


### Obtener Token para auth en API Calls
def sacarToken():
    url = REMPLAZO_DNA_URL

    # parametros a pedir
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': REMPLAZO_BASE64 
    }

    # Mandar peticion, en motodo POST, con la url, los headers que hicimos, payload en este caso no fue necesario y sin v>
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    tokenJSON = response.json()
    tokenValor = tokenJSON['Token']
    return tokenValor

# Fin sacarToken


# Ejemplo de API call, solo copia y pega de POSTMAN en code, Python- requests
def obtenerDevices(token):
    url = REMPLAZO_DNA_DEVICES

    payload = {}
    headers = {
        'x-auth-token': token,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    # print(response.json())
    return response.json()


# Fin verUpdate

def messageBuilder(jsonParseo,i):
    REMPLAZO_TEAMS_HOOK
    myMessageSection = pymsteams.cardsection()
    myMessageSection.title("Resumen")
    myMessageSection.text("This is my section text")
    # Pasring del JSON de algunas keys interesantes
    reach = jsonParseo["reachabilityStatus"]

    # Imprimir, la lib de pymsteams solo puede enviar un renglon en cada mensaje se hizo un work-around ya que teams soporta formato de texto se creacion secciones por cada mensaje, para que al final se unan todas las secciones y se envie tood como un solo mensaje
    myMessageSection = pymsteams.cardsection()
    myMessageSection.title("Resumen")
    if reach == "Unreachable":
        nombreDevice = jsonParseo['hostname']
        versionSO = jsonParseo["softwareVersion"]
        softwareType = jsonParseo["softwareType"]
        macAddress = jsonParseo["macAddress"]
        mgmt = jsonParseo["managementIpAddress"]
        pid = jsonParseo["platformId"]
        ses = jsonParseo["series"]
        ces = jsonParseo["collectionStatus"]

#ver foreach
        if nombreDevice:
            section1 = pymsteams.cardsection()
            section1.text("Dispositivo: " + nombreDevice)
        else:
            section1 = pymsteams.cardsection
            section1.text("Dispositivo: NULL")

        if versionSO:
            section2 = pymsteams.cardsection()
            section2.text("Version de SO: " + versionSO)
        else:
            section2 = pymsteams.cardsection()
            section2.text("Version de SO: NULL")

        if softwareType:
            section3 = pymsteams.cardsection()
            section3.text("Tipo de SO: " + softwareType)
        else:
            section3 = pymsteams.cardsection()
            section3.text("Tipo de SO: NULL")

        if macAddress:
            section4 = pymsteams.cardsection()
            section4.text("MAC: " + macAddress)
        else:
            section4 = pymsteams.cardsection()
            section4.text("MAC: NULL")

        if mgmt:
            section5 = pymsteams.cardsection()
            section5.text("MGMT IP: " + mgmt)
        else:
            section5 = pymsteams.cardsection()
            section5.text("MGMT IP: NULL")

        if pid:
            section6 = pymsteams.cardsection()
            section6.text("Platform ID: " + pid)
        else:
            section6 = pymsteams.cardsection()
            section6.text("Platform ID: NULL")

        if ses:
            section7 = pymsteams.cardsection()
            section7.text("Series: " + ses)
        else:
            section7 = pymsteams.cardsection()
            section7.text("Series: NULL")

        if ces:
            section8 = pymsteams.cardsection()
            section8.text("Collection Status: " + ces)
        else:
            section8 = pymsteams.cardsection()
            section8.text("Collection: NULL")

        section9 = pymsteams.cardsection()
        section9.text("El equipo no esta disponible")
    # Unir secciones
        myTeamsMessage.addSection(section1)
        myTeamsMessage.addSection(section2)
        myTeamsMessage.addSection(section3)
        myTeamsMessage.addSection(section4)
        myTeamsMessage.addSection(section5)
        myTeamsMessage.addSection(section6)
        myTeamsMessage.addSection(section7)
        myTeamsMessage.addSection(section8)
        myTeamsMessage.addSection(section9)
        myTeamsMessage.summary("Test Message")  # Aun que no se vea en el mensaje se ocupa tener, si no marca error
        myTeamsMessage.send()  # Enviar todo el mensaje unido
        
        
###Main programa
def main():
    print('Iniciando Programa')
    print('Generando token')
    print('Obteniendo resultados, entre mas dispositivos mas tardado')

    jsonAParsear = obtenerDevices(sacarToken())

    for memorySize in jsonAParsear["response"]:
        messageBuilder(memorySize)


### Ejecutar programa
if __name__ == '__main__':
    main()
