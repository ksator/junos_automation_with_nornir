# generate config and load config (dry_run) on a single device  

from nornir import InitNornir
from nornir.plugins.tasks import networking, text
from nornir.plugins.functions.text import print_title, print_result

def configuration(task):
    r = task.run(task=text.template_file, name="Generate configuration", template="config.j2", path=f"templates/{task.host.platform}")
    task.host["config"] = r.result
    task.run(task=networking.napalm_configure, name="Loading configuration on the device", replace=False, configuration=task.host["config"])

nr = InitNornir(config_file="config.yaml", dry_run=True)
dev = nr.filter(name="vMX1")
# dev.inventory.hosts

# from nornir.core.filter import F
# Junos_devices = nr.filter(F(platform="junos"))

print_title("Playbook to configure the network")
result = dev.run(task=configuration)
print_result(result)

# result["vMX1"]
# result["vMX1"][0]
# result["vMX1"][1]
# result["vMX1"][2]

# result["vMX1"].failed
# result["vMX1"].changed
# result["vMX1"].diff

# result["vMX1"][2].changed

