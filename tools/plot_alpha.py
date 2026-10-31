#!/usr/bin/env python3
"""Plot the phase-fraction field (alpha) from a solver snapshot as a 2D contour map.

Usage:  python3 tools/plot_alpha.py results/fields/300_alpha.txt [output.png]
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    sys.exit(__doc__)

infile = sys.argv[1]
outfile = sys.argv[2] if len(sys.argv) > 2 else infile.replace(".txt", ".png")

# File layout: one row per cell, columns  x  y  alpha, written row by row (x fastest).
data = np.loadtxt(infile)
x, y, alpha = data[:, 0], data[:, 1], data[:, 2]
nx, ny = len(np.unique(x)), len(np.unique(y))
X = x.reshape(ny, nx)
Y = y.reshape(ny, nx)
A = alpha.reshape(ny, nx)

fig, ax = plt.subplots(figsize=(6, 5.4))
levels = np.linspace(0.0, 1.0, 21)
cf = ax.contourf(X, Y, A, levels=levels, cmap="Blues", extend="both")
ax.contour(X, Y, A, levels=[0.5], colors="#1a1a1a", linewidths=1.2)   # interface
cb = fig.colorbar(cf, ax=ax, ticks=[0, 0.25, 0.5, 0.75, 1.0], pad=0.02)
cb.set_label("phase fraction α  (1 = water)")

ax.set_aspect("equal")
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
step = infile.split("/")[-1].split("_")[0]
ax.set_title(f"α at step {step}   min {A.min():.3f}  max {A.max():.3f}", fontsize=10)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(outfile, dpi=150)
print("wrote", outfile)
