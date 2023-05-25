# Les fonctions permettent de modifier certaines caractéristiques des VM
# Vérification en entrée des paramètres
# en sortie, une valeur nulle correspond à une erreur dans le traitement
from vm import *
from fonctions_get_vm import *

def putvmname(vmid,name):
    # Fixe le nom de la VM
    subprocess.run(['qm', 'set', str(vmid), '-name', name])

def putvmmemory(vmid,memory):
    subprocess.run(['qm', 'set', str(vmid), '-memory', str(memory)])

def putvmsocket(vmid,socket):
    subprocess.run(['qm', 'set', str(vmid), '-sockets', str(socket)])

def putvmcore(vmid,core):
    subprocess.run(['qm', 'set', str(vmid), '-cores', str(core)])

def putvmuser(vmid,user):
    subprocess.run(['qm', 'set', str(vmid), '-ciuser', user])

def putvmpwd(vmid,password):
    subprocess.run(['qm', 'set', str(vmid), '-cipassword', password])

def putvmvmbr(vmid,vmbr):
    if getvmvmbr(vmid) != vmbr:
        infosrc=getvmnetinfo(vmid)
        debut = (infosrc.find("vmbr"))+4
        infodest = infosrc[:debut]+str(vmbr) + infosrc[debut+1:]
        subprocess.run(['qm', 'set', str(vmid), '-net0', infodest])

def putvmconfip(vmid,ip,msr,gw):
    subprocess.run(['qm', 'set', str(vmid), '-ipconfig0', "gw="+gw.printIP()+","+"ip="+ip.printIP()+"/"+str(msr)])

def putvmhddsize(vmid,size):
    sizeinit=getvmhddsize(vmid)
    if sizeinit < size :
        subprocess.run(['qm', 'disk', 'resize', str(vmid), 'scsi0', str(size)+"G"])
    else:
        print("La taille initiale du disque dur est de ",sizeinit,". La taille demandée est ",". Opération annulée.")

