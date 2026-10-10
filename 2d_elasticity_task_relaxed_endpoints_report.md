# Relaxation-based quadrant endpoints

Submission: `2d_elasticity_task_relaxed_endpoints.zip`.

This redesign uses the newly uploaded `2d_elasticity_task.zip` as its baseline.
Step 4 now obtains the principal-axis Young moduli from the **returned stored
energies of Step 1's transverse-relaxed loading experiments**. These endpoint
values contribute to the continuous global extrema and anisotropy calculation.
Step 4 declares dependencies `[1, 2, 3]`; its nine-key public result and all four
function signatures remain unchanged.

## Scientific calculation

For the returned Born-stable fitted tensor, Step 4 performs two symmetric
experiments with prescribed strain magnitude `h = 0.03`:

| Quadrant endpoint | Input engineering strains to Step 1 | Free normal component |
| --- | --- | --- |
| x axis, theta = 0 | `[h, 0, 0]`, `[-h, 0, 0]` | 1: transverse yy strain |
| y axis, theta = pi/2 | `[0, h, 0]`, `[0, -h, 0]` | 0: transverse xx strain |

Zero prescribed shear also gives zero shear stress for this orthotropic model.
The free normal component reaches its minimum energy at zero transverse stress.
With `K = 16.02176634 N/m per eV/Angstrom^2`, each endpoint curvature is

`E_axis = K * (U(+h) + U(-h)) / h**2`,

where both `U` values come from the public Step 1 function's
`energy_density_ev_ang2` output. These are relaxed Young moduli, rather than
the clamped stiffness coefficients C11 and C22.

Step 2 supplies the fitted tensor. Step 3 supplies the sampled Young moduli and
Poisson ratios. Step 4 combines the two energy-derived endpoints with any
continuous interior stationary candidate; it does not infer global extrema
from the requested angle grid. Canonical directions and ties remain decisions
at the represented fitted constitutive model, independently of helper errors.
An unstable fitted tensor skips both relaxation and directional evaluation and
retains the existing NaN response contract.

## Numerical contract

Step 1's existing energy tolerance contributes an endpoint uncertainty of
`3.56039252e-8 + 1e-10 * E_axis` N/m. The prompt and strict tests now propagate
this uncertainty candidate by candidate into the minimum, maximum, and ratio;
sampled-response and canonical-direction tolerances are preserved. Existing
fitted-coefficient reporting uncertainty is also retained.

When this energy uncertainty covers a positive endpoint, Step 4 still calls
Step 1 but refines the unresolved curvature at the protected represented tensor.
This prevents an allowed zero energy report from creating zero stiffness or
infinite anisotropy. It is a precision decision, not a stability cutoff. The
candidatewise intervals also remain finite when tiny positive shear produces
an interior minimum.

Both Step 1 references now evaluate single-free-normal stress and stored work
through the protected Schur curvature. Previously, summing cancelling work
terms could produce zero or negative energy for a strictly stable soft normal
mode. The correction preserves Step 1's interface, admissibility rules, and
accuracy budget. It also retains negative held curvature when a valid
constrained minimum exists in an otherwise unstable tensor.

## Verification

The task now has **131 self-contained cases**: 30, 32, 23, and 36 per step,
plus 10 whole-task cases. Five new Step 4 cases check:

1. The two principal-axis loading experiments and their relaxed mechanics.
2. Actual energy dataflow: changing only the public helper's returned energies
   changes global endpoint extrema and anisotropy. This is an explicitly
   counterfactual wiring fixture, separate from physical accuracy checks.
3. No relaxation call for unstable tensors.
4. Continuous oblique minima and maxima alongside the relaxed endpoints.
5. A lawful zero-energy report for an unresolved tiny positive endpoint,
   requiring positive finite refined responses.

Local validation results:

- Both full implementations pass **131/131** cases, including through call-only
  evaluator proxies with shared public dependency bindings. Every standalone
  reference passes its declared cases, including Step 4 supplied only its
  three declared earlier dependencies.
- The freshly extracted final ZIP passes the same full validation. ZIP integrity
  and member contents match the working submission.
- All five packaged scientific mutants are rejected. `None` and zero-output
  no-op controls fail every step.
- Five new incorrect variants are rejected for each reference: decorative
  relaxation calls, extraction from stress, wrong transverse constraints,
  relaxation of unstable fits, and omission of unresolved-energy refinement.
  Decorative calls and stress extraction fail only the new energy-wiring case;
  omitted refinement fails only the new lawful-zero-energy case.
- Both implementations pass all 30 required output-noise configurations,
  including relative +/-1e-12 Step 4 perturbations: **1,274 applicable case
  evaluations per implementation**, with no failures.
- Relaxation fairness passes **2,300/2,300** Step 4/whole-task evaluations across
  baseline, eight lawful Step 1 energy-error patterns, and sixteen combined
  fitting/relaxation/directional-error configurations.
- **112/112** independent candidatewise interval probes pass, including
  isotropic, ordinary principal, oblique, high-modulus, tiny-shear, and
  cancellation-sensitive positive-determinant materials. Canonical directions
  remain unchanged under lawful relaxation errors.
- Six exact-rational Schur-work probes pass, including negative constrained
  curvature and the extremely small positive represented determinant.
- Existing fitting and directional intermediate-error checks pass. Fresh
  subprocess runs at thread/seed configurations `(1, 0)`, `(1, 271)`, and
  `(2, 913)` each pass all 131 cases and the full output-noise checks.

Runtime computation and graded tests use NumPy and Python built-ins only.
Public dependency fixtures use public-name rebinding, without `__globals__`,
proxy unwrapping, source inspection, or external operations. Author validation
tools and this report remain outside the submission archive.

The archive retains its 24-file inventory. Exactly eight members changed:
README, problem YAML, both complete references, standalone Steps 1 and 4,
Step 4 tests, and whole-task tests. The supplied `source.md`, scaffolds,
Step 1–3 tests, Step 2/3 reference functions, and packaged mutant files are
preserved. These local results do not establish the submission platform's
Oracle or content-quality approval; resubmission is required for that result.

Uploaded baseline SHA-256:
`2afabed7079a0725101104538e183189ff7ebd2a656bfcb68883966930734258`.
Revised archive SHA-256:
`3109feac09224ef893920b454d0786fbed3b791cd2b7398b469824026ed23b60`.
