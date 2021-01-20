#!/bin/bash/

echo '###Iniciando instalación..'
echo '###Actualizando Repos..'
sudo apt update -y
echo '###Instalando dependencias..'
sudo apt install python3 curl wget nano htop python3-pip -y
echo '###Dependencias instaladas..'
echo '###Instalando librerias..'
sudo pip3 install requests
sudo pip3 install pymsteams
echo '###Librerias instaladas..'

echo '###Configurando script'
echo '###Ingrese username de DNA'
read userDNA
echo '###Ingrese password de DNA'
read varname
#Generando base64
encode="'Basic "
encode+=$(echo $userDNA:$varname | base64)
encode+="'"
echo '###Ingrese FQDN o IP del DNA (https://dnaejemplo.com, https://10.10.10.1)'
read dna_url
#Api call de Token Auth
dna1='"'
dna1+="$dna_url"
dna1+='/dna/system/api/v1/auth/token"'
#Api Call de Get Devices
dna2='"'
dna2+="$dna_url"
dna2+='/dna/intent/api/v1/network-device"'
#URL del WebHook de MS Teams
echo '###Pega la URL del WebHook de MS Temas'
read teamsURL
teams1='myTeamsMessage = pymsteams.connectorcard("'
teams1+="$teamsURL"
teams1+='")'
#Remplazo de variables en el script
sed -i "s/REMPLAZO_BASE64/$encode/g" REMPLAZO.py
sed -i "s@REMPLAZO_DNA_URL@$dna1@g" REMPLAZO.py
sed -i "s@REMPLAZO_DNA_DEVICES@$dna2@g" REMPLAZO.py
sed -i "s!REMPLAZO_TEAMS_HOOK!$teams1!g" REMPLAZO.py
#Renombrar el script
mv REMPLAZO.py unreach_Message.py
