#!/usr/bin/python
#Author:HaclerNoDo
import webbrowser
from colorama import init, Fore,Back,Style
print(Fore.GREEN+
''' #####    #####    ######  ##   ##   # #####
### ###  ##   ##     ##    ###  ##  ## ## ##
##   ##  ##          ##    #### ##     ##
##   ##   #####      ##    #######     ##
##   ##       ##     ##    ## ####     ##
### ###  ##   ##     ##    ##  ###     ##
 #####    #####    ######  ##   ##    ####

''')
print(Fore.RED+
'''88b 88  dP"Yb  8888b.   dP"Yb
88Yb88 dP   Yb  8I  Yb dP   Yb
88 Y88 Yb   dP  8I  dY Yb   dP
88  Y8  YbodP  8888Y"   YbodP
''')
print(Fore.YELLOW+"NOTA: ESTE SCRIP PERMITE BUSCAR DIRECCIONES E INFO DE UNA PERSONA CON EL NOMBRE O RUT DE ELLA, ADEMAS TIENE OTRAS HERRAMIENTAS LAS CUALES LE PUEDEN AYUDAR A VARIS COSAS MAS..... DISFRUTENLA\n\n AUTHOR:Hacker NoDo\n\n Canal oficial : https://youtube.com/@hackerNoDo\n\n")
print("SOLO CHILE......:)\n\n")
opc=str(input("OSINT \n [1] [BUSCAR DORECCION POR NOMBRE] \n [2] [LOCALIZAR UNA IP, GEOLOCALIZAR SOLO INGRESELA]\n [3] [BUSQUEDA AVANZADA SIN SABER GOOGLE DORKINGS]\n [4] [APRENDER BUSQUEDA AVANZADA GOOGLE DORKS]\n [5] [APRENDER TODO SOBRE NMAP SCANEO DE REDES]\n [6] [APRENDER TODO DE HACKING, SOTWARE Y PROGRAMACION]\n salir\n  \n\n seleccione opcion:  "))

if opc == "1":
	webbrowser.open("https://www.nombrerutyfirma.com")
elif opc == "2":
	webbrowser.open("https://dnschecker.org/ip-location.php")
elif opc == "3":
	webbrowser.open("https://www.google.com/advanced_search")
elif opc == "4":
	webbrowser.open("https://www.ma-no.org/en/security/google-hacking-secrets-the-hidden-codes-of-google")
elif opc == "5":
	webbrowser.open("https://www.ma-no.org/es/search/?q=nmap")
elif opc == "6":
	webbrowser.open("https://www.elhacker.net/")
elif opc == "salir":
	print("Gracias por ocupar mi scrip")
else:
	print("La opcion ingresada no es valida, intenta nuevamente\n\n")
print("SI TE GUSTO ENTRA A MI CANAL Y DALE LIKE O SUBCRIBETE ✓")

