#!/usr/bin/env python3
"""Generate validation plots from the repository CSV files."""

from pathlib import Path
import csv
import math
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)


def read_csv(name):
    with (DATA / name).open(newline="") as f:
        return list(csv.DictReader(f))


# Solver residuals
conv = read_csv("convergence_history.csv")
it = [int(r["iteration"]) for r in conv]
plt.figure(figsize=(8, 5))
for key, label in [
    ("Ux_initial", "Ux"),
    ("Uy_initial", "Uy"),
    ("Uz_initial", "Uz"),
    ("p_initial", "p"),
]:
    plt.semilogy(it, [float(r[key]) for r in conv], label=label)
plt.xlabel("SIMPLE iteration")
plt.ylabel("Initial residual")
plt.title("OpenFOAM steady-solver convergence")
plt.grid(True, which="both", alpha=0.25)
plt.legend()
plt.tight_layout()
plt.savefig(FIG / "convergence_residuals.png", dpi=180)
plt.close()

# Continuity history
plt.figure(figsize=(8, 5))
plt.semilogy(it, [abs(float(r["continuity_local"])) for r in conv], label="local")
plt.semilogy(it, [abs(float(r["continuity_global"])) for r in conv], label="global")
plt.xlabel("SIMPLE iteration")
plt.ylabel("Absolute continuity error")
plt.title("Continuity-error history")
plt.grid(True, which="both", alpha=0.25)
plt.legend()
plt.tight_layout()
plt.savefig(FIG / "continuity_history.png", dpi=180)
plt.close()

# Mesh evolution
mesh = read_csv("mesh_iteration_history.csv")
labels = ["Initial", "Iteration 1", "Final"]
cells = [int(r["cells"]) for r in mesh]
bad = [int(r["cells_determinant_lt_0_001"]) for r in mesh]
fig, ax1 = plt.subplots(figsize=(8, 5))
x = range(len(labels))
ax1.bar(x, cells, alpha=0.7)
ax1.set_ylabel("Cells")
ax1.set_xticks(list(x), labels)
ax1.set_title("Mesh evolution")
ax2 = ax1.twinx()
ax2.plot(list(x), bad, marker="o", linewidth=2)
ax2.set_ylabel("Cells with determinant < 0.001")
fig.tight_layout()
fig.savefig(FIG / "mesh_evolution.png", dpi=180)
plt.close(fig)

# Mesh quality evolution
plt.figure(figsize=(8, 5))
plt.plot(labels, [float(r["max_non_orthogonality_deg"]) for r in mesh], marker="o", label="max non-orthogonality [deg]")
plt.plot(labels, [float(r["max_skewness"]) for r in mesh], marker="o", label="max skewness")
plt.plot(labels, [float(r["max_aspect_ratio"]) for r in mesh], marker="o", label="max aspect ratio")
plt.ylabel("Metric value")
plt.title("Mesh-quality evolution")
plt.grid(True, alpha=0.25)
plt.legend()
plt.tight_layout()
plt.savefig(FIG / "mesh_quality_evolution.png", dpi=180)
plt.close()

# Radial profile against analytical solution
rad = read_csv("radial_velocity_x045.csv")
rvals = [float(r["r_m"]) for r in rad]
uvals = [float(r["Ux_m_s"]) for r in rad]
R = 0.05
Um = 0.01
analytical = [2 * Um * (1 - (rv / R) ** 2) for rv in rvals]
plt.figure(figsize=(8, 5))
plt.plot(rvals, uvals, label="CFD at x = 0.45 m")
plt.plot(rvals, analytical, "--", label="Hagen–Poiseuille")
plt.xlabel("Radius r [m]")
plt.ylabel("Axial velocity Ux [m/s]")
plt.title("Downstream radial velocity profile")
plt.grid(True, alpha=0.25)
plt.legend()
plt.tight_layout()
plt.savefig(FIG / "radial_velocity_validation.png", dpi=180)
plt.close()

# Axial pressure with analytical-gradient reference anchored at outlet
ap = read_csv("axial_pressure.csv")
xm = [float(r["x_m"]) for r in ap]
p_pa = [float(r["p_physical_Pa"]) for r in ap]
ref = [3.2 * (0.5 - x) for x in xm]
plt.figure(figsize=(8, 5))
plt.plot(xm, p_pa, label="CFD")
plt.plot(xm, ref, "--", label="3.2 Pa/m fully developed reference")
plt.xlabel("x [m]")
plt.ylabel("Pressure [Pa]")
plt.title("Axial pressure distribution")
plt.grid(True, alpha=0.25)
plt.legend()
plt.tight_layout()
plt.savefig(FIG / "axial_pressure_validation.png", dpi=180)
plt.close()

print(f"Generated plots in {FIG}")
