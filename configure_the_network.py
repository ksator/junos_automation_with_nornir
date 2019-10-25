
# generate config files and load config files on network devices 

from nornir import InitNornir
from nornir.plugins.tasks import networking, text
from nornir.plugins.functions.text import print_title, print_result
from nornir.core.filter import F

def configuration(task):
    r = task.run(task=text.template_file, name="Generate configuration", template="config.j2", path=f"templates/{task.host.platform}")
    task.host["config"] = r.result
    task.run(task=networking.napalm_configure, name="Loading configuration on the device", replace=False, configuration=task.host["config"])

nr = InitNornir(config_file="config.yaml", dry_run=False)
Junos_devices = nr.filter(F(platform="junos"))

print_title("Playbook to configure the network")
result = Junos_devices.run(task=configuration)
print_result(result)


'''
# to check if a task failed:
result.failed
'''

'''
# to check if the device vMX1 configuration changed
result["vMX1"].changed
result["vMX1"][2]
result["vMX1"][2].changed
result["vMX1"][2].diff
'''

'''
# the check which devices had a configuration changed 
for item in Junos_devices.inventory.hosts:
   dev=nr.inventory.hosts[item]
   print ('**** ' + item + ' ****')
   result[item][2].changed 
'''

