from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.addresses import EthAddr
from pox.lib.util import dpid_to_str, str_to_dpid
import pox.lib.packet as pkt
import json
from libreria import *


log = core.getLogger ()
switch = ""
rules_file = "rules.json"

class SDNFirewall (EventMixin):
    
    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug( " Enabling Firewall Module " )
        data = open(rules_file)
        self.rules=json.load(data)
        
    def _handle_ConnectionUp (self, event):
        if not event.connection.dpid == str_to_dpid(switch):
            return
        log.info("Para el Switch con ID = %s se le suben las siguientes entradas:",switch)

        for rule in self.rules:
            block = of.ofp_match()
            bloques = apply_rule(rule, block, log)
            for bloque in bloques:

                flow_mod = of.ofp_flow_mod()
                flow_mod.match = bloque
                event.connection.send(flow_mod)
        
def launch (switch_id=1):
    global switch
    switch = switch_id
    core.registerNew(SDNFirewall)