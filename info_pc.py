import platform
import cpuinfo
import socket
from jinja2 import Environment, FileSystemLoader
import webbrowser

class SystemInfo:
    def __init__(self):
        self.os_name = platform.system()
        self.os_release = platform.release()
        self.cpu_info = cpuinfo.get_cpu_info()['brand_raw']
        self.hostname = socket.gethostname()

    # "liste" des information systemes à récupérer
    def to_dict(self):
        return {
            "os_name": self.os_name,
            "os_release": self.os_release,
            "cpu_info": self.cpu_info,
            "hostname": self.hostname
        }

system_info = SystemInfo()
system_info_dict = system_info.to_dict()

# Création d'un environement jinja2 pour utiliser la template html
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('Template/template.html')
output = template.render(system_info=system_info_dict)

# affichage du résultat dans une template supplémentaire
with open('infos.html', 'w') as f:
    f.write(output)
webbrowser.open('infos.html')
