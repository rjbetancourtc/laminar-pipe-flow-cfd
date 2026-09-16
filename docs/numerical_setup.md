# Numerical Setup

## Solver formulation

The included OpenFOAM 12 case solves steady incompressible laminar flow using the `incompressibleFluid` module.

The transport model is constant-viscosity laminar flow. No turbulence variables are present.

## Pressure variable

The OpenFOAM pressure field has kinematic-pressure dimensions:

```text
[0 2 -2 0 0 0 0]
```

Therefore physical pressure is obtained from

```text
p_physical = rho * p_kinematic
```

with `rho = 900 kg/m³`.

## Pressure–velocity coupling

The case uses consistent SIMPLE with

```text
momentumPredictor       yes
nNonOrthogonalCorrectors 2
consistent              yes
```

The residual controls are

```text
p : 1e-8
U : 1e-8
```

## Linear solvers

### Pressure

```text
solver    GAMG
tolerance 1e-10
relTol    0.01
```

The final pressure solve uses `relTol = 0`.

### Velocity

```text
solver    smoothSolver
smoother  symGaussSeidel
tolerance 1e-10
relTol    0.01
```

## Relaxation

```text
p = 0.3
U = 0.7
```

## Spatial discretization

The principal schemes are:

```text
gradients:        Gauss linear
velocity advection: bounded Gauss linearUpwind grad(U)
laplacian:        Gauss linear corrected
interpolation:    linear
surface-normal gradient: corrected
```

## Iteration control

The case sets a large maximum `endTime = 5000` for the steady iteration counter, but convergence control terminates the solution earlier. The converged solution is reached at iteration 341.

A periodic state is written at iteration 250 because `writeInterval = 250`.
