import sys
from libnmap.parser import NmapParser

def execute_script(file_name):
    nmap_report = NmapParser.parse_fromfile(file_name)
    print(nmap_report.summary)
    for host in nmap_report.hosts:
        print(host.os)
        print(host.get_open_ports())
        print(host.services)
        print(host.scripts_results)


if __name__ == "__main__":
    execute_script(sys.argv[1])
