# TP2 - Software-Defined Networks


# How to run

En un terminal correr la topologia de mininet. Podemos elegir la cantidad de switches que queremos cambiando el ```switches=5``` y podemos tambien elegir el puerto al cual pondremos nuestro controlador pox

```sudo mn --custom firewall_topo.py --topo customTopo,switches=5 --mac --arp --switch ovsk --controller=remote,port=6655 ```

En otra terminal correremos nuestro firewall/SDN en el cual podemos elegir el switch que utilizaremos como firewall con ```--switch_id = n``` y debemos utilizar el mismo puerto que utilizamos para mininet
```python2.7 pox/pox.py log.level --INFO samples.pretty_log --openflow=INFO openflow.of_01 --port=6655 forwarding.l2_learning firewall --switch_id=1 ```

En caso de error al ejecutar pox debido a un puerto ya utilizado, se debera cambiar a otro puerto en ambos mininet y pox (utilizar el mismo).

Overleaf: https://www.overleaf.com/7233763945sqvfxrvgxpzv#1072cf
