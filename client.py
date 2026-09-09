class WeisfeilerLehmanKernel:
    """1-WL color refinement graph isomorphism tester."""
    def compute_signature(self, adj_list: dict[int, list[int]], initial_colors: dict[int, str], iterations: int = 2) -> dict:
        colors = dict(initial_colors)
        for _ in range(iterations):
            new_colors = {}
            for node, nbrs in adj_list.items():
                multiset = sorted([colors[nbr] for nbr in nbrs])
                combined = f"{colors[node]}_" + "-".join(multiset)
                new_colors[node] = combined
            colors = new_colors

        # Histogram of color frequencies
        hist = {}
        for c in colors.values():
            hist[c] = hist.get(c, 0) + 1

        return {
            "iterations": iterations,
            "refined_colors": colors,
            "graph_feature_vector": hist
        }
