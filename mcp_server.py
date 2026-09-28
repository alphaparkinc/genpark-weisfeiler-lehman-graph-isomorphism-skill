import sys
import json
from client import WeisfeilerLehmanKernel

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-weisfeiler-lehman-graph-isomorphism-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "check_graph_isomorphism",
                        "description": "Test structural isomorphism between two graphs using 1-WL coloring kernel",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "graph_a": {"type": "object"},
                                "graph_b": {"type": "object"},
                                "iterations": {"type": "integer", "default": 3}
                            },
                            "required": ["graph_a", "graph_b"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "check_graph_isomorphism":
            ga = args.get("graph_a", {})
            gb = args.get("graph_b", {})
            it = args.get("iterations", 3)
            iso = WeisfeilerLehmanKernel.are_isomorphic(ga, gb, iterations=it)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps({"isomorphic": iso})}]
                }
            }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
