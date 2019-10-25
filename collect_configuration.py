
# collect running and candidate configuration 

'''
$ tree backup/
backup/
├── vMX1
│   ├── candidate_configuration.txt
│   └── running_configuration.txt
├── vMX2
│   ├── candidate_configuration.txt
│   └── running_configuration.txt
├── vMX3
│   ├── candidate_configuration.txt
│   └── running_configuration.txt
├── vMX4
│   ├── candidate_configuration.txt
│   └── running_configuration.txt
├── vMX5
│   ├── candidate_configuration.txt
│   └── running_configuration.txt
├── vMX6
│   ├── candidate_configuration.txt
│   └── running_configuration.txt
└── vMX7
    ├── candidate_configuration.txt
    └── running_configuration.txt
'''

from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking
from nornir.core.filter import F
import os

nr = InitNornir(config_file="config.yaml")
#nr.inventory.hosts.keys()

Junos_devices = nr.filter(F(platform="junos"))
#print(Junos_devices.inventory.hosts.keys())

cwd = os.getcwd()

backup_directory = os.path.dirname(cwd + "/backup/")
if not os.path.exists(backup_directory):
     os.makedirs(backup_directory)

for dev in Junos_devices.inventory.hosts: 
  device_backup_directory = backup_directory + "/" + dev 
  if not os.path.exists(device_backup_directory):
    os.makedirs(device_backup_directory)

result = Junos_devices.run(task=networking.napalm_get, getters=["config"], retrieve="all")
# print_result(result)
# print(result['vMX1'][0].result['config']['running'])
# print(result['vMX1'][0].result['config']['candidate'])

for dev in Junos_devices.inventory.hosts:
  running_configuration=open(backup_directory + '/' + dev  + '/' + 'running_configuration.txt','w')
  running_configuration.write(result[dev][0].result['config']['running'])
  running_configuration.close()
  candidate_configuration=open(backup_directory + '/' + dev + '/' + 'candidate_configuration.txt','w')
  candidate_configuration.write(result[dev][0].result['config']['candidate'])
  candidate_configuration.close()

