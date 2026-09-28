"""1-Dimensional Weisfeiler-Lehman (1-WL) Graph Kernel Engine.
100% Python Standard Library.
"""

import hashlib
import collections

class WeisfeilerLehmanKernel:
    """1-WL (Weisfeiler-Lehman) graph coloring isomorphism test."""
    @staticmethod
    def get_color_histogram(adj_dict, iterations=2):
        nodes = sorted(adj_dict.keys())
        colors = {u: str(len(adj_dict[u])) for u in nodes}
        histograms = []

        for _ in range(iterations):
            new_colors = {}
            for u in nodes:
                nbr_colors = sorted(colors[v] for v in adj_dict[u])
                sig = colors[u] + "_" + ",".join(nbr_colors)
                h = hashlib.md5(sig.encode("utf-8")).hexdigest()[:8]
                new_colors[u] = h
            colors = new_colors
            counts = collections.Counter(colors.values())
            histograms.append(dict(sorted(counts.items())))

        return histograms

    @classmethod
    def are_isomorphic(cls, g1, g2, iterations=3):
        h1 = cls.get_color_histogram(g1, iterations=iterations)
        h2 = cls.get_color_histogram(g2, iterations=iterations)
        return h1 == h2
