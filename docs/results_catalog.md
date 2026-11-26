# Results and Data Catalog

## Consolidated data

### `data/benchmark_summary.csv`

Principal geometric, physical, mesh, convergence, conservation, pressure, and velocity metrics.

### `data/convergence_history.csv`

Iteration-by-iteration residual and continuity history reconstructed from the solver log. It contains the initial residuals for `Ux`, `Uy`, `Uz`, and the first pressure correction, plus final velocity residuals, continuity errors, and execution time.

### `data/mesh_iteration_history.csv`

Mesh statistics and quality metrics for the initial mesh, first refinement, and final mesh.

### `data/boundary_patches.csv`

Face counts and starting-face indices for `inlet`, `outlet`, and `walls`.

### `data/flow_balance.csv`

Signed and magnitude-based inlet/outlet volumetric flow rates, conservation error, and mass flow rate.

## Profile data

### `data/axial_pressure.csv`

Columns:

```text
x_m,p_kinematic_m2_s2,p_physical_Pa
```

### `data/axial_velocity.csv`

Columns:

```text
x_m,U_mag_m_s,Ux_m_s,Uy_m_s,Uz_m_s
```

### `data/radial_velocity_x045.csv`

Radial velocity profile at `x = 0.45 m` with columns

```text
r_m,U_mag_m_s,Ux_m_s,Uy_m_s,Uz_m_s
```

## Figures

The `figures/` directory includes:
- velocity vectors;
- streamlines;
- longitudinal velocity and pressure views;
- downstream cross-sectional velocity field;
- radial velocity validation plot;
- axial pressure validation plot;
- axial velocity development;
- solver residual history;
- continuity history;
- mesh evolution;
- mesh quality evolution.
