# Analytical Reference

## Kinematic viscosity

The kinematic viscosity is

```text
nu = mu / rho
   = 0.100 / 900
   = 1.111111e-4 m²/s
```

## Cross-sectional area and flow rate

For a circular section,

```text
A = pi D² / 4
  = 7.853981634e-3 m²
```

The flow rate corresponding to the prescribed mean velocity is

```text
Q = Um A
  = 7.853981634e-5 m³/s
```

## Reynolds number

```text
Re = rho Um D / mu
   = Um D / nu
   = 9
```

This is a strongly laminar internal-flow condition.

## Entrance length

A common estimate for laminar hydrodynamic entrance length is

```text
Le / D ≈ 0.05 Re
```

which gives

```text
Le ≈ 0.045 m
Le / L ≈ 0.09
```

Therefore, roughly the first 9 % of the pipe length is expected to be strongly influenced by inlet-profile development.

## Fully developed velocity profile

For steady, fully developed laminar flow in a circular pipe,

```text
u_x(r) = 2 Um [1 - (r/R)²]
```

The centerline maximum is

```text
Umax = 2 Um = 0.020 m/s
```

## Fully developed pressure gradient

The Hagen–Poiseuille relation gives

```text
|dp/dx| = 32 mu Um / D²
        = 3.2 Pa/m
```

Over the complete pipe length,

```text
Delta p_HP = |dp/dx| L
           = 1.6 Pa
```

This `1.6 Pa` value assumes fully developed flow over the entire 0.5 m. The CFD problem starts from a uniform velocity profile, so the total CFD pressure drop is expected to include an additional entrance-region contribution.
