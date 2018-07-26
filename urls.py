from handlers import Index
from handlers import AssetsGroupApi
from handlers import Hosts
from handlers import Projects
from handlers import HostsApi


urls = [
    (r"/", Index),
    (r"/index$|index.html$", Index),
    (r"/assets/projects$|projects.html$", Projects),
    (r"/assets/hosts$|hosts.html$", Hosts),
    (r"/api/assets/(.*)", AssetsGroupApi),
]

