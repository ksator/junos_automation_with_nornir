
# validate the state of bgp sessions (should be Established) 

'''
$ python ./validate_bgp_sessions_state.py
****** vMX1 *******
BGP session with 192.168.1.1 is Established
BGP session with 192.168.1.3 is Established
BGP session with 192.168.1.5 is Established
BGP session with 192.168.1.7 is Established
****** vMX2 *******
BGP session with 192.168.2.1 is Established
BGP session with 192.168.2.3 is Established
BGP session with 192.168.2.5 is Established
BGP session with 192.168.2.7 is Established
****** vMX3 *******
BGP session with 192.168.3.1 is Established
BGP session with 192.168.3.3 is Established
BGP session with 192.168.3.5 is Established
BGP session with 192.168.3.7 is Established
****** vMX4 *******
BGP session with 192.168.1.0 is Established
BGP session with 192.168.2.0 is Established
BGP session with 192.168.3.0 is Established
****** vMX5 *******
BGP session with 192.168.1.2 is Established
BGP session with 192.168.2.2 is Established
BGP session with 192.168.3.2 is Established
****** vMX6 *******
BGP session with 192.168.1.4 is Established
BGP session with 192.168.2.4 is Established
BGP session with 192.168.3.4 is Established
****** vMX7 *******
BGP session with 192.168.1.6 is Established
BGP session with 192.168.2.6 is Established
BGP session with 192.168.3.6 is Established
'''

from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
Junos_devices = nr.filter(F(platform="junos"))
# print(Junos_devices.inventory.hosts.keys())

result = Junos_devices.run(task=networking.napalm_get, getters=["bgp_neighbors"])
# print_result(result)
# result['vMX1'][0].result["bgp_neighbors"]["global"]["peers"]["192.168.1.1"]["is_up"]

for dev in Junos_devices.inventory.hosts:
  print ("****** " + dev + " *******")  
  for item in result[dev][0].result["bgp_neighbors"]["global"]["peers"]:
    if result[dev][0].result["bgp_neighbors"]["global"]["peers"][item]["is_up"] == True: 
        print ("BGP session with " + item + " is Established")  
    else: 
        print ("BGP session with " + item + " is not Established")



