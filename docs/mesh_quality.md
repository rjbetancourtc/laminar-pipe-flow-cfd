# Mesh Quality and Mesh Evolution

## Final mesh composition

The final mesh contains a tetrahedral core and prism cells adjacent to the wall.

| Quantity | Value |
|---|---:|
| Points | 11,233 |
| Faces | 76,701 |
| Internal faces | 70,059 |
| Cells | 33,917 |
| Tetrahedra | 22,825 |
| Prisms | 11,092 |
| Regions | 1 |
| Boundary patches | 3 |

The three patches are `inlet`, `outlet`, and `walls`.

## Final quality metrics

| Metric | Value |
|---|---:|
| Max aspect ratio | 5.4232 |
| Max non-orthogonality | 58.557° |
| Mean non-orthogonality | 14.981° |
| Max skewness | 0.54186 |
| Minimum determinant | 0.050361 |
| Average determinant | 2.0863 |
| Cells with determinant < 0.001 | 0 |
| Min cell volume | 3.55938e-9 m³ |
| Max cell volume | 1.23828e-6 m³ |
| Total mesh volume | 3.91265785e-3 m³ |

The final `checkMesh -allTopology -allGeometry` result is `Mesh OK`.

## Mesh evolution

The mesh was improved through multiple states. The important observation is that simply increasing element count did not automatically improve the determinant criterion.

| Mesh state | Cells | Tetrahedra | Prisms | Cells with determinant < 0.001 | Max skewness | Result |
|---|---:|---:|---:|---:|---:|---|
| Initial | 4,882 | 4,882 | 0 | 39 | 0.5873 | failed one check |
| Iteration 1 | 21,920 | 21,920 | 0 | 148 | 0.6674 | failed one check |
| Final | 33,917 | 22,825 | 11,092 | 0 | 0.5419 | Mesh OK |

The final mesh also improved geometric volume representation:

```text
exact cylindrical volume = 3.926990817e-3 m³
final mesh volume         = 3.912657850e-3 m³
relative difference       ≈ 0.3650 %
```

The detailed mesh history is provided in [`../data/mesh_iteration_history.csv`](../data/mesh_iteration_history.csv).
