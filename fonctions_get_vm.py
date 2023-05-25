# Ce fichier contient au minimum une fonction de récupération d'information pour chaque attribut de la classe VM
from vm import *

def getvminfo(vmid):
    infosbrute=(str(subprocess.run(['qm', 'config', str(vmid)], stdout=subprocess.PIPE).stdout))
    # Suppression des 2 premiers et 3 derniers caractères et placement des infos dans un tableau
    return(infosbrute[2:-3].split(r"\n"))

def getvmname(vmid):
    # Initialisation de la variable à noname si info pas retrouvée
    name="noname"
    for champs in getvminfo(vmid):
        if champs[0:4] == "name":
            name=champs[6:]
    return(name)

def getvmmemory(vmid):
    memory=0
    for champs in getvminfo(vmid):
        if champs[0:6] == "memory":
            memory=champs[8:]
    return(int(memory))

def getvmcore(vmid):
    core=1
    for champs in getvminfo(vmid):
        if champs[0:5] == "cores":
            core=champs[7:]
    return(int(core))

def getvmsocket(vmid):
    socket=1
    for champs in getvminfo(vmid):
        if champs[0:7] == "sockets":
            socket=int(champs[9:])
    return(socket)
def getvmnetinfo(vmid):
    network=""
    for champs in getvminfo(vmid):
        if champs[0:4] == "net0":
            network = champs[6:]
    return(network)

def getvmnic(vmid):
    nic = ""
    nicbrut=getvmnetinfo(vmid)
    fin = (nicbrut.find(r"="))
    nic = nicbrut[:fin]
    return(nic)

def getvmmac(vmid):
    mac = "00:00:00:00:00:00"
    macbrut=getvmnetinfo(vmid)
    debut = (macbrut.find("=")) + 1
    fin = (macbrut.find(r",", debut))
    mac = macbrut[debut:fin]
    return(mac)

def getvmvmbr(vmid):
    vmbr = 0
    vmbrbrut=getvmnetinfo(vmid)
    debut = (vmbrbrut.find("=",10)) + 5
    vmbr = vmbrbrut[debut:]
    return(int(vmbr))

def getvmipinfo(vmid):
    ipinfo=""
    for champs in getvminfo(vmid):
        if champs[0:9] == "ipconfig0":
            ipinfo=champs[11:]
    return(ipinfo)

def getvmip(vmid):
    ipinfo = "0.0.0.0"
    ipbrut=getvmipinfo(vmid)
    debut = (ipbrut.find("ip")) + 3
    fin = (ipbrut.find(r"/", debut))
    ipinfo = ipbrut[debut:fin]
    return(str2ip(ipinfo))

def getvmmsr(vmid):
    msr=32
    msrbrut = getvmipinfo(vmid)
    debut = (msrbrut.find(r"/")) + 1
    fin = (msrbrut.find(r",", debut))
    msr = msrbrut[debut:fin]
    return(int(msr))

def getvmgw(vmid):
    gw="0.0.0.0"
    gwbrut = getvmipinfo(vmid)
    debut = (gwbrut.find("gw")) + 3
    #print("debut = ",debut)
    gw = gwbrut[debut:]
    return(str2ip(gw))

def getvmhddinfo(vmid):
    hddinfo=""
    for champs in getvminfo(vmid):
        if champs[0:5] == "scsi0":
            hddinfo=champs[7:]
    return(hddinfo)

def getvmvolume(vmid):
    volumeinfo=""
    filebrut = getvmhddinfo(vmid)
    fin = (filebrut.find(r":"))
    volumeinfo = filebrut[0:fin]
    return(volumeinfo)

def getvmfile(vmid):
    fileinfo=""
    filebrut = getvmhddinfo(vmid)
    debut = (filebrut.find(":")) + 1
    fin = (filebrut.find(r",", debut))
    fileinfo = filebrut[debut:fin]
    return(fileinfo)

def getvmhddsize(vmid):
    hddsize=""
    sizebrut = getvmhddinfo(vmid)
    debut = (sizebrut.find("=")) + 1
    hddsize = sizebrut[debut:-1]
    return(int(hddsize))

def getvmuser(vmid):
    userinfo=""
    for champs in getvminfo(vmid):
        if champs[0:6] == "ciuser":
            userinfo=champs[8:]
    return(userinfo)

