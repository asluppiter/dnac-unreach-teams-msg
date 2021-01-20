# Import de libs necesarias
import pymsteams
import requests  # para hacer peticiones HTTP
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # Para ignorar certificados


### Si se obtiene el token por web
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

def messageBuilder(jsonParseo):
    REMPLAZO_TEAMS_HOOK
    myMessageSection = pymsteams.cardsection()
    myMessageSection.title("Resumen de devices")
    myMessageSection.text("This is my section text")
    # Pasring del JSON de algunas keys interesantes
    reach = jsonParseo["reachabilityStatus"]
    # Imprimir, la lib de pymsteams solo puede enviar un renglon en cada mensaje se hizo un work-around ya que teams soporta formato de texto se creacion secciones por cada mensaje, para que al final se unan todas las secciones y se envie tood como un solo mensaje

    if reach != "Reachable":
        hostname = jsonParseo['hostname']
        versionSO = jsonParseo["softwareVersion"]
        softwareType = jsonParseo["softwareType"]
        macAddress = jsonParseo["macAddress"]
        mgmtIP = jsonParseo["managementIpAddress"]
        pid = jsonParseo["platformId"]
        ses = jsonParseo["series"]
        ces = jsonParseo["collectionStatus"]

        if not hostname:
            hostname="NULL"

        section1 = pymsteams.cardsection()
        section1.text("Dispositivo: " + hostname)

        if not versionSO:
            versionSO="NULL"

        section2 = pymsteams.cardsection()
        section2.text("Version de SO: " + versionSO)

        if not softwareType:
            softwareType="NULL"

        section3 = pymsteams.cardsection()
        section3.text("Tipo de SO: " + softwareType)

        if not macAddress:
            macAddress="NULL"

        section4 = pymsteams.cardsection()
        section4.text("MAC: " + macAddress)

        if not mgmtIP:
            mgmtIP="NULL"

        section5 = pymsteams.cardsection()
        section5.text("MGMT IP: " + mgmtIP)

        if not pid:
            pid="NULL"

        section6 = pymsteams.cardsection()
        section6.text("Platform ID: " + pid)

        if not ses:
            ses="NULL"

        section7 = pymsteams.cardsection()
        section7.text("Series: " + ses)

        if not ces:
            ces="NULL"

        section8 = pymsteams.cardsection()
        section8.text("Collection Status: " + ces)

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

# Fin verUpdate
###Main programa
def main():
    print('Ejecutando programa')
    print('Generando token')
    print('Obteniendo resultados y enviando mensajes')

    jsonAParsear = obtenerDevices(sacarToken())

    for memorySize in jsonAParsear["response"]:
        estado = memorySize["reachabilityStatus"]
        if estado != "Reachable":
            messageBuilder(memorySize)


### Ejecutar programa
if __name__ == '__main__':
    main()
