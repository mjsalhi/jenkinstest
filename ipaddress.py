class Ipaddress :
    def __init__(self, a, b, c, d) :
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def printIP (self):
      return str(self.a) + '.' + str(self.b) + '.' + str(self.c) + '.' + str(self.d)
    #def concat(*args, sep="/"):
    #    return sep.join(args)

def str2ip (stringip):
    ipfromstr=Ipaddress(0,0,0,0)
    pos=int(0)
    nextdot=stringip.find(".", pos)
    ipfromstr.a=int(stringip[:nextdot])

    pos=nextdot+1
    nextdot = stringip.find(".", pos)
    ipfromstr.b = int(stringip[pos:nextdot])

    pos = nextdot+1
    nextdot = stringip.find(".", pos)
    ipfromstr.c = int(stringip[pos:nextdot])

    pos = nextdot+1
    ipfromstr.d = int(stringip[pos:])
    return(ipfromstr)
