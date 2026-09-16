# OpenFOAM Case Structure

The directory [`../openfoam_case`](../openfoam_case) contains the technical OpenFOAM 12 case used for the benchmark.

## Initial fields: `0/`

### `0/U`

The inlet is prescribed as a uniform axial velocity:

```text
inlet  : fixedValue (0.01 0 0)
outlet : zeroGradient
walls  : noSlip
```

### `0/p`

The pressure field is kinematic pressure:

```text
inlet  : zeroGradient
outlet : fixedValue 0
walls  : zeroGradient
```

## Physical model: `constant/`

`physicalProperties` defines constant kinematic viscosity

```text
nu = 1.111111111111e-4 m²/s
```

`momentumTransport` sets

```text
simulationType laminar
```

`constant/polyMesh/` contains the final verified mesh.

## Numerical controls: `system/`

- `controlDict` selects `foamRun` with `incompressibleFluid`.
- `fvSchemes` contains the steady spatial discretization.
- `fvSolution` defines linear solvers, SIMPLE controls, residual criteria, and relaxation.

## Solution directories

### `250/`

Periodic output written at iteration 250.

### `341/`

Converged final solution written when SIMPLE residual control is satisfied at iteration 341.

The public case includes the primary solution fields `U`, `p`, and `phi`.

## Post-processing

`postProcessing/` contains numerical patch integrals and averages for iteration 341:

- inlet flow rate;
- outlet flow rate;
- inlet average `p` and `U`;
- outlet average `p` and `U`.

`results_basic.csv` consolidates the principal validation quantities in a compact machine-readable form.

## Mesh hash reference

`polyMesh.sha256.beforeBasicLaminar` contains the reference SHA-256 recorded for the mesh before the basic laminar solve.

## Rerunning the case

To preserve the included converged output, work from a copy of the case. For a clean run from the initial condition, remove `250/` and `341/` in the working copy and execute:

```bash
checkMesh -allTopology -allGeometry
foamRun
```
