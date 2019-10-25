from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
#nr.inventory.hosts.keys()

Junos_devices = nr.filter(F(platform="junos"))
#print(Junos_devices.inventory.hosts.keys())

result = Junos_devices.run(task=networking.napalm_get, getters=["facts"])

for item in Junos_devices.inventory.hosts:
   dev=nr.inventory.hosts[item]
   print("********device " + item + " ********")
   print("expected version is " + dev['version']) 
   print("actual version is " + result[item][0].result["facts"]["os_version"])
   if dev['version'] == result[item][0].result["facts"]["os_version"]: 
     print ("the expected version is equal to the actual version")
   else: 
     print ("the expected version is not equal to the actual version")


