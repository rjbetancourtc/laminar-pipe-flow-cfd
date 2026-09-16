# CFD Validation

## Solver convergence

The steady SIMPLE solution converged in 341 iterations.

At the final iteration, the initial equation residuals were approximately

```text
Ux : 5.9781e-10
Uy : 3.3525e-9
Uz : 9.9876e-9
p  : 2.8957e-9
```

The final continuity errors were

```text
local      = 1.9481e-11
global     = -9.5332e-14
cumulative = 4.7847e-6
```

The full iteration history is available in [`../data/convergence_history.csv`](../data/convergence_history.csv).

## Conservation

The boundary fluxes are

```text
Qin  = -7.840500810899e-5 m³/s
Qout = +7.840500810860e-5 m³/s
```

The opposite signs follow the outward-normal convention on the two boundary patches. Comparing magnitudes gives a mass-conservation error of approximately

```text
5.10e-10 %
```

The corresponding mass flow rate is approximately

```text
mdot = 0.0705645 kg/s
```

## Flow rate versus exact circular area

The exact geometric flow rate from the prescribed mean velocity is

```text
Q_exact = 7.853981634e-5 m³/s
```

The CFD flux is about `0.1716 %` lower. This small difference is consistent with the faceted representation of the circular boundary in the volume mesh.

## Velocity validation

The downstream maximum cell-centered velocity is

```text
Umax_CFD = 0.0199034 m/s
```

The fully developed analytical value is

```text
Umax_HP = 0.0200000 m/s
```

so the CFD result differs by approximately `-0.48 %` and

```text
Umax_CFD / Um = 1.9903
```

which is very close to the theoretical value of 2.

The radial profile at `x = 0.45 m` is included in [`../data/radial_velocity_x045.csv`](../data/radial_velocity_x045.csv).

## Pressure validation

The total inlet-to-outlet pressure drop is

```text
Delta p_CFD,total = 1.89817 Pa
```

The fully developed Hagen–Poiseuille value over 0.5 m is

```text
Delta p_HP = 1.60000 Pa
```

The CFD total is about `18.64 %` higher because the numerical problem includes a hydrodynamic entrance region created by the uniform inlet profile.

A downstream linear fit gives

```text
|dp/dx|_CFD = 3.3977 Pa/m
```

compared with

```text
|dp/dx|_HP = 3.2000 Pa/m
```

for a difference of about `+6.18 %` in the developed region.

## Overall interpretation

The benchmark exhibits the expected low-Reynolds-number behavior:

- excellent inlet/outlet flow balance;
- a developing profile downstream of the uniform inlet;
- downstream velocity approaching the parabolic Hagen–Poiseuille profile;
- centerline velocity approaching `2 Um`;
- approximately linear pressure decay downstream;
- developed pressure gradient close to the analytical reference.
