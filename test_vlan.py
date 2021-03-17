from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F

nr = InitNornir(config_file="config.yaml")
group = nr.filter(F(role="access_switch"))

def get_vlans(task):
    vlan_list = []
    result = task.run(task=send_command, command="show vlan")
    task.host["facts"] = result.scrapli_response.genie_parse_output()
    vlans = task.host['facts']['vlans']
    for vlan in vlans:
        if vlan in ["1", "1002", "1003", "1004", "1005"]:
            continue
        vlan_id = int(vlan)
        name = vlans[vlan]['name']
        vlan_dict = {"id": vlan_id, "name": name}
        vlan_list.append(vlan_dict)
        print(vlan_list)

group.run(task=get_vlans)