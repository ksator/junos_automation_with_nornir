# This Nornir script executes several tasks against the ubuntu hosts

from nornir import InitNornir
from nornir.plugins.tasks import commands
from nornir.plugins.functions.text import print_result

def check_ubuntu(task):
    task.run(task=commands.remote_command, name="Ubuntu release", command="lsb_release -a")
    task.run(task=commands.remote_command, name="Available disk", command="df -h")
    task.run(task=commands.remote_command, name="Available memory", command="free -m")
    task.run(task=commands.remote_command, name="Ping google public ipv4 dns", command="ping 8.8.8.8 -c 3")

nr = InitNornir(config_file="config.yaml")
paris_servers = nr.filter(site="paris", type="server")
result = paris_servers.run(task=check_ubuntu)
print_result(result, vars=["stdout"])

