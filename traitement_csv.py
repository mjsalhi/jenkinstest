import csv
import copy
from vm import *
from fonctions_put_vm import *

class lab:
    def __init__(self):
        # Définition de la classe
        self.labname = ""
        self.nblab = 1
        self.incvmid = 1
        self.vminfo = []

def csvastuple(fichiercsv):
    contenu = csv.reader(fichiercsv, delimiter=';', quotechar='|')
    tuple=[]
    for ligne in fichiercsv:
        tuple.append(ligne)
    return tuple

def getlabconf(config,lab):
    # Récupération, à partir d'un fichier config = mise en liste du fichier csv, les informations globales du lab
    #
    # name = nom du lab qui sera utilisé lors du nommage des VM
    # nblab = nombre d'itération de création de VM à analyser
    # incvmid = incrément entre chaque lab sur les vmid
    lab.name=(config[1].split(";"))[1]
    lab.nblab=(config[2].split(";"))[1]
    lab.incvmid=(config[3].split(";"))[1]

def getvminfounitaire(config,i):
    # Fonction de récupération des informations sur les VM, à mettre sous forme dans une liste
    #
    # Cette fonction renvoie un tuple vm si valide, entraitant la ligne i du fichier de configuration
    vminfobrute=config[i].split(";")
    return vminfobrute

def getvmconf(config):
    i=9 # démarrage de l'analyse à la 9ème ligne
    list=[]
    bool=1
    while bool>0:
        a=getvminfounitaire(config,i)
        if a[0]=="":
            bool=0
        else:
            a[-1]=(a[-1])[:-2] # Suppression des caractères superflus sur le dernier enregistrement = \r\n
            list.append(a)
            i=i+1
    return list

def printlabinfo(lab):
    print("configuration globale du lab")
    print("============================")
    print("Nom : ",lab.name)
    print("NB : ",lab.nblab)
    print("Inc VMID : ",lab.incvmid)
    print ("\n")
    print("configuration des VM")
    print("====================")
    i=0
    for element in lab.vminfo:
        print("VM"+str(i+1)+": ",lab.vminfo[i])
        i=i+1
        #print("VM"+i+" : ", str(element))

def labclonevm(vminfo):
    vmclone=VM()
    vmclone.vmid=vminfo[0]
    vmclone.clone(vminfo[1])

def labconfvm(vminfo,labname,i):
    vmid=vminfo[0]
    putvmname(vmid,labname+str(i)+"-"+vminfo[3])
    putvmmemory(vmid,int(vminfo[8]))
    putvmsocket(vmid,int(vminfo[9]))
    putvmcore(vmid,int(vminfo[10]))
    ip=str2ip(vminfo[5]+"."+vmid)
    msr=int(vminfo[6])
    gw=str2ip(vminfo[7])
    putvmconfip(vmid,ip,msr,gw)
    putvmvmbr(vmid,int(vminfo[4]))
    putvmhddsize(vmid,int(vminfo[11]))


def labdeploy(lab):
    for i in range (0, int(lab.nblab)):
        for element in lab.vminfo:
            cible = copy.deepcopy(element)
            a=int(cible[0])+i*int(lab.incvmid)
            cible[0]=str(a)
            labclonevm(cible)
            labconfvm(cible,lab.name,(i+1))

def labdestroy(lab):
    for i in range (0, int(lab.nblab)):
        for element in lab.vminfo:
            cible = copy.deepcopy(element)
            a=int(cible[0])+i*int(lab.incvmid)
            cible[0]=str(a)
            vmcible=VM()
            vmcible.vmid=a
            vmcible.destroy()
