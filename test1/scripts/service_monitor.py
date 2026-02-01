
import subprocess, json, socket
from datetime import datetime

services = ["httpd", "rabbitmq-server", "postgresql"]
host = socket.gethostname()

def check(service):
    try:
        subprocess.check_output(["systemctl","is-active","--quiet",service])
        return "UP"
    except:
        return "DOWN"

for s in services:
    payload = {
        "service_name": s,
        "service_status": check(s),
        "host_name": host,
        "timestamp": datetime.utcnow().isoformat()
    }
    fname = f"{s}-status-{int(datetime.utcnow().timestamp())}.json"
    with open(fname,"w") as f:
        json.dump(payload,f,indent=2)
