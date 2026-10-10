# 2D elasticity revision and local verification

The revised submission is `2d_elasticity_task_quality_hardened.zip`. It retains
four evaluated scientific steps and the existing numerical tolerance budgets.
It closes additional contract-coverage gaps and corrects a reference arithmetic
failure near a strictly positive stability boundary. The archive contains only
the submission files; this report and author validation tools are separate.

The comparison baseline is commit
`405421d5d8c3f651b16dcabc8209dcce88b7c8f9`, containing
`2d_elasticity_task_finite_endpoint_fixed.zip`. The baseline has 105 cases;
the revision has 117. All original test files are preserved as byte-for-byte
prefixes of the revised files. The archive's 24-file inventory is unchanged.

## Scientific calculation

The model describes small-strain harmonic elasticity of an unstressed
orthotropic monolayer. Engineering shear is `gamma_xy = 2 epsilon_xy`.
Stiffness and conjugate stress are areal quantities in N/m; stored energy
density is in eV/Angstrom^2. Energy observations are in eV and the unstrained
area is in Angstrom^2. The conversion remains
`1 eV/Angstrom^2 = 16.02176634 N/m`. No slab thickness is introduced.

| Step | Scientific contribution | Evaluated cases |
| --- | --- | ---: |
| 1 | Minimize elastic energy under mixed prescribed-strain and zero-stress conditions, returning equilibrium strain, stress, and energy. | 28 |
| 2 | Identify four stiffness coefficients from harmonic energy observations and assess the raw physical design's signal, rank, and conditioning. | 30 |
| 3 | Apply uniaxial loading through the engineering compliance tensor to obtain directional Young moduli and Poisson ratios. | 21 |
| 4 | Classify the returned fitted tensor and solve for continuous global Young-modulus extrema, anisotropy, and canonical directions. | 28 |
| Whole task | Check the integrated scientific calculation. | 10 |

The prompt now explicitly distinguishes macroscopic strain relaxation in
Step 1 from atomic-coordinate relaxation in the energy dataset. All energy
records must use a consistent atomic relaxation convention. Step 2 retains the
same unique, unweighted least-squares physical objective but allows the solver
to choose a stable inversion method; a particular factorization or NumPy
solver is not prescribed. Steps 1 and 2 share the same harmonic work law;
the public Step 2 and Step 3 functions contribute to Step 4.

## Additional contract coverage

Case numbers below are zero-based markers in the test files. These are
parameterized cases, so a case can exercise several physical inputs.

| Step and added cases | Promises now checked |
| --- | --- |
| Step 1, 26–27 | A positive free-normal determinant ratio around 1e-12 is accepted. All-free normal components reach zero equilibrium. Ambiguous positive minors and a binary64-singular factorization with zero forcing are accepted. Empty real batches still reject nonfinite stiffness and complex-typed labels or stiffness. |
| Step 2, 27–29 | Nonfinite strains and area, and complex-typed fitting records, raise `ValueError`. All four raw design columns are checked just inside and outside the published RMS roundoff allowance, using independently verified full-rank designs with condition number below 1000. Coefficients through magnitude 1e4 N/m are recovered without clipping, including unstable curvature. Valid lists are accepted. |
| Step 3, 18–20 | Nonfinite normal diagonals and complex-typed records are rejected. The required tuple and floating array shapes are checked. High-modulus directional responses match analytic values. A strictly positive minor erased by ordinary extended-precision subtraction is accepted and gives finite principal-axis results. |
| Step 4, 24–27 | Stable and unstable branches reject nonfinite or complex fitting inputs and angles. High-modulus extrema are verified independently at the returned fit. A deterministic public-fit fixture exercises an ambiguous positive minor. The required public directional function is invoked for the stable branch and bypassed for the unstable branch. |

Existing tests for the exact-isotropic returned fit, canonical ties, free-column
range validation, per-column included RMS endpoints, the included conditioning
endpoint, tiny positive normal diagonals and shear, and unstable NaN outputs
remain present. Existing prompt explanations distinguish invalid NaN/infinity
input records from the specified NaN outputs for finite unstable tensors.

## Narrow reference precision correction

The represented tensor
`[1.69443407281501, 1.3988569383717917, 1.5395684003547392, 0.5]`
has an exactly positive normal principal minor of approximately
`2.5641825831402423852e-20`. Direct extended-precision product subtraction
rounds this minor to zero on the validation host. This violated the existing
strict-positivity contract; extending tests alone would have broken the oracle.

The primary and independent references now recompute an arithmetically
ambiguous minor using the exact integer ratios of the represented coefficients.
The roundoff bound selects adequate arithmetic precision; it does not impose
a positive eigenvalue, shear, or determinant cutoff. The primary constrained
solver also returns the validated zero-forcing equilibrium directly, avoiding
a spurious singular-factorization error. Standalone Steps 1, 3, and 4 contain
the corresponding correction. Step 2's reference remains byte-for-byte
unchanged. Existing well-resolved mechanics and tolerance budgets are retained.

The calibrated guarantees still apply over the existing stated coefficient,
shear, and determinant-ratio ranges. Softer admissible tensors are tested for
acceptance and finite responses at safe principal-axis directions; those cases
do not introduce an unstated high-accuracy guarantee outside the calibration.

## Local verification results

Validation used Python 3.12.14 and NumPy 2.3.5. Submission computation and
graded tests use NumPy and Python built-ins only. PyYAML and exact-rational
cross-checks are author-side tools, not submission dependencies.

- Both complete implementations pass **117/117** cases. Both also pass through
  call-only proxies with shared public dependency bindings. Each standalone
  step reference passes all of its declared cases.
- A fresh extraction of the final ZIP passes the same complete check. ZIP
  integrity and all extracted file contents were checked.
- All five packaged scientific mutants are rejected. `None` and zero-output
  no-op controls fail every step. Eleven existing targeted scientific controls
  are rejected.
- Thirty additional incorrect implementations that each passed all 105
  baseline cases are rejected by the added coverage, for both references.
  Seven legacy precision/zero-forcing controls and the public-dependency
  bypass control are also rejected.
- Both implementations pass all 30 required relative output-noise modes,
  including +/-1e-12 perturbations of Step 4 outputs: **1,070 applicable case
  evaluations per implementation**, with no failures.
- Admissible intermediate fitting and directional errors are accepted.
  Step 1 passes 12 output-budget probes across all 28 cases. The high-modulus
  Step 4 case accepts all 16 sign corners at 80% of the allowed fitting error
  budget for each implementation. Its targets are independently computed at
  the returned fit, avoiding tighter demands than the fitting contract.
- Fresh subprocess runs with thread/seed configurations `(1, 0)`, `(1, 271)`,
  and `(2, 913)` each pass all 117 cases and the full output-noise checks.
- Exact rational checks cover ten determinant fixtures, including positive,
  negative, zero, soft, and wide-exponent cases. The precision guard leaves
  256 well-resolved calibrated determinant evaluations unchanged. These checks
  establish the exercised host behavior; they are not a portability proof for
  every possible floating-point implementation.

Public dependency fixtures use shared public names and verify invocation.
Graded tests do not access `__globals__`, unwrap evaluator proxies, inspect
source, or use process, filesystem, or network operations.

The supplied `source.md`, scaffolds, whole-task tests, five packaged mutants,
interfaces, dependency declarations, and numerical tolerance budgets are
preserved. These results are local validation, not a platform Oracle or
content-quality approval. The final ZIP must be resubmitted to obtain that
platform result.

Archive SHA-256:
`125e5cd533428f746e816d6721e26cebfeaacc33c90299ae033c32e48644fc6f`.
