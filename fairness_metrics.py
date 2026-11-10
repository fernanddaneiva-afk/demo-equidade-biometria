"""Demo de métricas de equidade demográfica para verificação facial.

Usa SCORES SINTÉTICOS (nenhum dado real). Mostra como medir FMR/FNMR por grupo
e as diferenças entre grupos com um único limiar global.
"""
import numpy as np

rng = np.random.default_rng(42)


def simulate(n_pairs=20000, groups=("A", "B", "C"), shift=(0.0, -0.04, -0.08)):
    """Gera scores de similaridade. O grupo com shift negativo tem genuínos piores."""
    g = rng.choice(groups, n_pairs)
    genuine = rng.random(n_pairs) < 0.5
    base = np.where(genuine, 0.70, 0.30)
    sh = np.array([shift[groups.index(x)] for x in g])
    scores = base + np.where(genuine, sh, 0.0) + rng.normal(0, 0.10, n_pairs)
    return g, genuine, scores


def rates(genuine, scores, thr):
    fmr = np.mean(scores[~genuine] >= thr)   # falsa aceitação (impostores)
    fnmr = np.mean(scores[genuine] < thr)    # falsa rejeição (genuínos)
    return fmr, fnmr


def threshold_for_fmr(genuine, scores, target=1e-2):
    imp = np.sort(scores[~genuine])
    return imp[int(np.ceil((1 - target) * len(imp))) - 1]


def report():
    g, genuine, scores = simulate()
    thr = threshold_for_fmr(genuine, scores)
    print(f"Limiar global (FMR global = 1%): {thr:.3f}\n")
    print("grupo   FMR     FNMR")
    fnmrs = []
    for grp in sorted(set(g)):
        m = g == grp
        fmr, fnmr = rates(genuine[m], scores[m], thr)
        fnmrs.append(fnmr)
        print(f"{grp:<6} {fmr:6.3%} {fnmr:7.3%}")
    print(f"\nRazão FNMR max/min: {max(fnmrs) / min(fnmrs):.2f}")
    print("Diferença FNMR max-min:", f"{max(fnmrs) - min(fnmrs):.3%}")


if __name__ == "__main__":
    report()
