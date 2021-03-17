from nornir_scrapli.tasks import send_command
from nornir.core.filter import F
from pytest_check import check_func

NEIGHBOR_COUNT = {
    "router_ce": 3,
    "router_pe": 3
}

@check_func
def pullospf(task):
    ospf_peer = []
    result = task.run(task=send_command, command="show ip ospf neighbor")
    task.host['facts'] = result.scrapli_response.genie_parse_output()
    interfaces = task.host['facts']['interfaces']
    for interface in interfaces:
        ospf_neighbor = interfaces[interface]['neighbors']
        for key in ospf_neighbor:
            ospf_peer.append(key)
    num_neighbors = len(ospf_peer)
    role = task.host['role']
    expected_neighbors = NEIGHBOR_COUNT[role]
    assert num_neighbors ==  expected_neighbors, f"{task.host} FAILED"


def test_nornir(nr):
    nr.run(task=pullospf)
