from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

from mininet.topo import Topo

class Topo (Topo):
    def build(self,switches= 5):
        info(switches)
    
        info( '*** Adding hosts\n' )

        h1 = self.addHost( 'h1', ip='10.0.0.1', mac='00:00:00:00:00:01' )
        h2 = self.addHost( 'h2', ip='10.0.0.2', mac='00:00:00:00:00:02' )
        

        h7 = self.addHost( 'h7', ip='10.0.0.7', mac='00:00:00:00:00:07' )
        h8 = self.addHost( 'h8', ip='10.0.0.8', mac='00:00:00:00:00:08' )

        info( '*** Adding switches\n' )
        switch_dic = {}
        for i in range(1,switches+1):
            switch = self.addSwitch(f's{i}')
            switch_dic[f's{i}'] = switch

        
        info( '*** Creating links\n' )
        s1 = switch_dic['s1']

        self.addLink( h1, s1 )
        self.addLink( h2, s1 )

        for i in range(2,switches+1):
            s2 = switch_dic[f's{i}']
            self.addLink( s1, s2 )
            s1 = s2
        s2 = switch_dic[f's{switches}']
        
        self.addLink(s2,h7)
        self.addLink(s2,h8)

topos = { "customTopo": Topo}
