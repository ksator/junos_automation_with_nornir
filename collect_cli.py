# collect show commands on Junos devices 

'''
$ tree cli
cli
├── vMX1
│   ├── show bgp summary
│   └── show interfaces terse
├── vMX2
│   ├── show bgp summary
│   └── show interfaces terse
├── vMX3
│   ├── show bgp summary
│   └── show interfaces terse
├── vMX4
│   ├── show bgp summary
│   └── show interfaces terse
├── vMX5
│   ├── show bgp summary
│   └── show interfaces terse
├── vMX6
│   ├── show bgp summary
│   └── show interfaces terse
└── vMX7
    ├── show bgp summary
    └── show interfaces terse

7 directories, 14 files

'''


from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking
from nornir.core.filter import F
import os

nr = InitNornir(config_file="config.yaml")
#dev = nr.filter(name="vMX1")
Junos_devices = nr.filter(F(platform="junos"))
#print(Junos_devices.inventory.hosts.keys())

cwd = os.getcwd()
cli_directory = os.path.dirname(cwd + "/cli/")
if not os.path.exists(cli_directory):
     os.makedirs(cli_directory)

for dev in Junos_devices.inventory.hosts: 
  device_cli_directory = cli_directory + "/" + dev 
  if not os.path.exists(device_cli_directory):
    os.makedirs(device_cli_directory)

commands_to_collect=["show bgp summary", "show interfaces terse"]

result = Junos_devices.run(task=networking.napalm_cli, commands=commands_to_collect)  
# print_result(result)
# print(result['vMX1'][0].result['show bgp summary'])
# print(result['vMX7'][0].result['show interfaces terse'])
# print(result['vMX1'][0].result[commands_to_collect[0]])
# print(result['vMX7'][0].result[commands_to_collect[1]])

for dev in Junos_devices.inventory.hosts:
  for command in commands_to_collect: 
    cli = open(cli_directory + '/' + dev  + '/' + command, 'w') 
    cli.write(result[dev][0].result[command])
    cli.close()


 
