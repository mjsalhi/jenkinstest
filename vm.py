from ipaddress import *
import subprocess
class VM:
    def __init__(self):
        # Définition de la classe
        self.vmid = 0
        self.name = "noname"
        self.memory = 1024
        self.socket = 1
        self.core = 1
        self.hdd0size = 8
        self.hdd0file = "noname"
        self.hdd0volume = "data"
        self.net0modele = "virtio"
        self.net0mac = "01:02:03:04:05:06"
        self.net0vmbr = 0
        self.net0ip = Ipaddress(192, 168, 50, 10)
        self.net0msr = 24
        self.net0gw = Ipaddress(192, 168, 50, 1)
        self.user = "mehdi"
        self.pwd = "Epsi2022!"

    def listparam(self):
        # Affiche la configuration de la VM de façon compréhensible
        lignea = 'vmid =     ' + str(self.vmid) + '\n'
        ligneb = 'name =     ' + self.name + '\n'
        lignec = 'memory =   ' + str(self.memory) + ' Mo' + '\n'
        ligned = 'socket =   ' + str(self.socket) + '\n'
        lignee = 'cores =    ' + str(self.core) + '\n'
        lignef = 'HDD Size = ' + str(self.hdd0size) + ' Go' + '\n'
        ligneg = 'HDD fil =  ' + self.hdd0volume + ":" + self.hdd0file + '\n'
        ligneh = 'NIC =      ' + self.net0modele + ":" + self.net0mac + '\n'
        lignei = 'V.Bridge = vmbr' + str(self.net0vmbr) + '\n'
        lignej = 'IP v4 =    ' + self.net0ip.printIP() + '/' + str(self.net0msr) + '\n'
        lignek = 'Gateway =  ' + self.net0gw.printIP() + '\n'
        lignel = 'User =     ' + self.user + '\n'
        lignem = 'Password = ' + self.pwd + '\n'

        return lignea + ligneb + lignec + ligned + lignee + lignef + ligneg + ligneh + lignei + lignej + lignek + lignel + lignem

    def start(self):
        return subprocess.run(['qm','start',str(self.vmid)]).returncode

    def stop(self):
        return subprocess.run(['qm','stop',str(self.vmid)]).returncode

    def destroy(self):
        return subprocess.run(['qm', 'destroy', str(self.vmid)]).returncode

    def clone(self, vmidsource):
        return subprocess.run(['qm', 'clone', str(vmidsource),str(self.vmid)]).returncode


    def exists(self):
        return 'booleén : true si la VM existe, false si elle n\'existe pas'

