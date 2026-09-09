import sys
import json
from client import WeisfeilerLehmanKernel

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "signature":
        wl = WeisfeilerLehmanKernel()
        adj = {int(k): v for k, v in params.get("adj", {}).items()}
        colors = {int(k): v for k, v in params.get("colors", {}).items()}
        return wl.compute_signature(adj, colors, params.get("iters", 2))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
