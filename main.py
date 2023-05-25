# Import des classes VM et Ipaddress, utilisée par VM
from vm import *
from fonctions_get_vm import *
from traitement_csv import *
# Import du module pour exécuterdes commandes bash

with open('descriptif.csv', newline='', errors='ignore') as csvfile:
    config=csvastuple(csvfile)
    labo=lab()
    getlabconf(config,labo)
    labo.vminfo=getvmconf(config)
    printlabinfo(labo)
    labdeploy(labo)
    print("fin déploiement. Attention : suppression")
    print(labo)
    labdestroy(labo)




