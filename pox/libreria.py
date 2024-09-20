from pox.core import core


def apply_rule(rule,block,log):
    block.dl_type = 0x800
    bloques = [block]
    log.info("Se sube el siguiente match flow al switch:")

    if "ip_src" in rule:
        log.info("-IP_SRC: [%s]",rule["ip_src"])
        block.nw_src = str(rule["ip_src"])
    if "ip_dst" in rule:
        log.info("-IP_DST: [%s]",rule["ip_dst"])
        block.nw_dst = str(rule["ip_dst"])
    if "dst_port" in rule:
        log.info("-DST_PORT: [%s]",rule["dst_port"])
        block.tp_dst = rule["dst_port"]
    if "src_port" in rule:
        log.info("-SRC_PORT: [%s]",rule["src_port"])
        block.tp_src = rule["src_port"]
    if "protocol" in rule:
        block.nw_proto = 6 if rule["protocol"] == "TCP" else 17
    if blocking_single_port(rule):
        block.nw_proto = 6
        second_block = block.clone()
        second_block.nw_proto = 17
        bloques.append(second_block)
    
    return bloques

def blocking_single_port(rule):
    if ("dst_port" in rule or "src_port" in rule) and len(rule) == 1:
        return True

    return False
