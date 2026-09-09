from client import WeisfeilerLehmanKernel

def main():
    print("=== Weisfeiler-Lehman (1-WL) Graph Kernel ===")
    wl = WeisfeilerLehmanKernel()
    adj = {0: [1], 1: [0, 2], 2: [1]}
    colors = {0: "C1", 1: "C2", 2: "C1"}

    res = wl.compute_signature(adj, colors, iterations=2)
    print("WL Signature Result:", res)
    assert len(res["refined_colors"]) == 3

    print("Weisfeiler-Lehman Kernel verified successfully!")

if __name__ == "__main__":
    main()
