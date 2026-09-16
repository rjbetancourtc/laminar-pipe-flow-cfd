# Problem Definition

## Physical problem

Consider steady flow of a Newtonian fluid through a straight, horizontal circular pipe of constant cross-section. The fluid is treated as incompressible and isothermal, with constant properties. Gravity is neglected.

The internal fluid domain is a cylinder aligned with the global `x` axis. Flow proceeds in the `+x` direction.

## Geometry

| Parameter | Symbol | Value |
|---|---:|---:|
| Diameter | `D` | 0.100 m |
| Radius | `R` | 0.050 m |
| Length | `L` | 0.500 m |
| Inlet center | — | `(0, 0, 0)` m |
| Outlet center | — | `(0.5, 0, 0)` m |

The computational domain represents the fluid volume, not a solid pipe wall.

## Fluid properties

| Property | Symbol | Value |
|---|---:|---:|
| Density | `rho` | 900 kg/m³ |
| Dynamic viscosity | `mu` | 0.100 Pa·s |
| Kinematic viscosity | `nu = mu/rho` | 1.111111e-4 m²/s |
| Constitutive behavior | — | Newtonian |

## Boundary conditions

### Inlet

Uniform axial velocity:

```text
U = (0.01, 0, 0) m/s
```

The pressure uses zero normal gradient at the inlet.

### Outlet

Reference pressure:

```text
p = 0
```

The velocity uses zero normal gradient at the outlet.

### Wall

No-slip velocity condition:

```text
U = 0
```

The pressure uses zero normal gradient at the wall.

## Requested verification quantities

The benchmark is designed to compare the numerical solution with classical laminar-pipe-flow theory. The main quantities are:

1. kinematic viscosity;
2. exact cross-sectional area and imposed flow rate;
3. Reynolds number;
4. hydrodynamic entrance length;
5. fully developed radial velocity profile;
6. centerline maximum velocity;
7. fully developed pressure gradient;
8. full-length Hagen–Poiseuille pressure drop;
9. CFD mass conservation;
10. CFD downstream velocity and pressure behavior.
