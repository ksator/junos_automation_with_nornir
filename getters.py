from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking

nr = InitNornir(config_file="config.yaml")
dev = nr.filter(name="vMX1")
# dev.inventory.hosts
result = dev.run(task=networking.napalm_get, getters=["interfaces", "facts"])
print_result(result)
# result['vMX1'][0].result["interfaces"]["ge-0/0/0"]['is_up']
# result['vMX1'][0].result["facts"]["os_version"]

