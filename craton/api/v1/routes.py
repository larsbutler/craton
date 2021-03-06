from craton.api.v1.resources import users
from craton.api.v1.resources import projects

from craton.api.v1.resources.inventory import ansible_inventory
from craton.api.v1.resources.inventory import cells
from craton.api.v1.resources.inventory import hosts
from craton.api.v1.resources.inventory import regions
from craton.api.v1.resources.inventory import networks


routes = [
    dict(resource=ansible_inventory.AnsibleInventory,
         urls=['/ansible_inventory'],
         endpoint='ansible_inventory'),
    dict(resource=hosts.HostsData,
         urls=['/hosts/<id>/data'],
         endpoint='hosts_data'),
    dict(resource=hosts.HostsLabels,
         urls=['/hosts/<id>/labels'],
         endpoint='hosts_labels'),
    dict(resource=hosts.HostById,
         urls=['/hosts/<id>'],
         endpoint='hosts_id'),
    dict(resource=hosts.Hosts,
         urls=['/hosts'],
         endpoint='hosts'),
    dict(resource=regions.Regions,
         urls=['/regions'],
         endpoint='regions'),
    dict(resource=regions.RegionsById,
         urls=['/regions/<id>'],
         endpoint='regions_id'),
    dict(resource=regions.RegionsData,
         urls=['/regions/<id>/data'],
         endpoint='regions_data'),
    dict(resource=cells.CellById,
         urls=['/cells/<id>'],
         endpoint='cells_id'),
    dict(resource=cells.Cells,
         urls=['/cells'],
         endpoint='cells'),
    dict(resource=cells.CellsData,
         urls=['/cells/<id>/data'],
         endpoint='cells_data'),
    dict(resource=projects.Projects,
         urls=['/projects'],
         endpoint='projects'),
    dict(resource=projects.ProjectById,
         urls=['/projects/<id>'],
         endpoint='projects_id'),
    dict(resource=users.Users,
         urls=['/users'],
         endpoint='users'),
    dict(resource=users.UserById,
         urls=['/users/<id>'],
         endpoint='users_id'),
    dict(resource=networks.Networks,
         urls=['/networks'],
         endpoint='networks'),
    dict(resource=networks.NetworkById,
         urls=['/networks/<id>'],
         endpoint='networks_id'),
    dict(resource=networks.NetInterfaces,
         urls=['/net_interfaces'],
         endpoint='net_interfaces'),
    dict(resource=networks.NetInterfaceById,
         urls=['/net_interfaces/<id>'],
         endpoint='net_interfaces_id'),
    dict(resource=networks.NetDevices,
         urls=['/netdevices'],
         endpoint='netdevices'),
    dict(resource=networks.NetDeviceById,
         urls=['/netdevices/<id>'],
         endpoint='netdevices_id'),
    dict(resource=networks.NetDeviceLabels,
         urls=['/netdevices/<id>/labels'],
         endpoint='netdevices_labels'),
]
