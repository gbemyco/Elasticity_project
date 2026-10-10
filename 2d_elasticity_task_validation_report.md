# Revised elasticity task: tolerance and content repairs

The latest supplied platform screenshot reports environment, Oracle and no-op
passes. Its remaining reference-check failure is N3.tolerance_noise: a relative
1e-12 perturbation of Step 4 outputs fails test 19. The supplied content check
also reports seven blocking findings and three advisories. This revision
addresses those findings; the execution evidence below is local author
verification, not a new platform approval.

The output perturbation was reproduced in both implementations. The almost-soft
normal mode in zero-based Step 4 case 18 magnifies binary rounding of a rescaled
reported stiffness, changing the recomputed Poisson ratio beyond the old fixed
budget. The repair propagates an explicitly stated coefficient-reporting
precision through positive-matrix compliance bounds. It preserves strict Born
classification and the canonical tie rule. Cases 15 and 18 also find continuous
extrema independently and compare angles and values against separate budgets.
A permitted angle error is no longer converted into an unintended modulus error.

| Reported finding | Repair and coverage |
|---|---|
| Nonfinite-input policy unclear in all four steps | Each visible step prompt explicitly names NaN, positive/negative infinity, relevant arguments and ValueError, and explains missing/diverged data or undefined loading directions. Existing rejection tests remain. |
| Binary floating-point spacing in Step 2 unspecified | Its visible prompt defines np.finfo(float).eps and the 64-eps endpoint allowance as a dimensionless design-roundoff convention. It is not a physical input or a stability cutoff. |
| Complex strains missing from Step 2 tests | New case 24 passes otherwise identifiable real data with a genuinely complex strain entry and requires ValueError. |
| Unstable branch lacks complex-angle coverage | New Step 4 case 19 supplies an unstable material and complex angles, requiring ValueError. |
| Exact fitted isotropic convention untested | New Step 4 case 20 reaches exactly isotropic fitted coefficients in the reference and explicitly checks both canonical angles against zero. Normal public calls are used. Other admissible fitted tensors are checked independently at their own fit, so exact fitting symmetry is not imposed on alternatives. |
| Step 1 coefficient-magnitude calibration untested | New case 21 uses a 10000 N/m coefficient and independent stress and harmonic-work targets. |
| Step 1 soft-normal calibration endpoint untested | New case 22 accepts the actual binary coefficient determinant ratio immediately above 1e-8 and checks zero normal-load relaxation. Its ratio is independently checked in extended precision. |
| Approximate Step 1 energies can corrupt Step 2's design | The reference now derives the raw quadratic design algebraically. Its numerical fit no longer depends on a tolerance-limited energy helper. The independent implementation already constructs local constitutive-matrix contractions and solves by QR. Dependencies now match actual calls. |

All case numbers above are zero-based. The platform's test 19 is case 18.
There are still four evaluated functions, five packaged scientific mutants,
24 submission files, and the original tasks/2d_elasticity identity. Five new
cases bring the total to 95: 23,25,16,21 per step and ten whole-task cases.
Accepted top-level and per-step YAML field names and source paths are retained.
The source.md supplied by the user remains an exact byte prefix; the previously
inspected-paper attribution is retained unchanged. Scientific execution uses
NumPy only and is offline.

Only the reference fitting implementation changes. The relaxation, directional
mechanics and integrated reference functions are unchanged. The independent
solution is unchanged. Per-step and complete reference definitions agree.
The missing-conversion and whole-task shear mutants are updated to retain their
original scientific errors with the algebraic design.

Executed checks:

- Both complete implementations: 95/95 each.
- Both implementations through call-only evaluator proxies: 95/95 each.
- Isolated per-step references: 23/23,25/25,16/16,21/21.
- All five packaged scientific mutants are rejected by their relevant suites.
- None and zero controls are rejected on all 95 cases.
- Final-output verification: 30 expected-pass perturbation modes per
  implementation, 872/872 evaluations each. These include uniform relative
  +/-1e-12 perturbations, independent result-field perturbations and permitted
  extremum-angle errors.
- Admissible intermediate coefficient and response error probes: 1334/1334
  evaluations per implementation; independent Step 1 error probes: 276/276.
- Eleven focused incorrect-physics/validation controls are rejected, including
  strict conditioning below 1000, zero shear/determinant acceptance, positive
  determinant cutoffs, wrong tie selection, coefficient clipping, discarded
  complex inputs and an incorrect exact-isotropic direction.
- Core and final-output checks pass in three clean processes with thread/hash
  configurations (1,0), (1,271), (2,913).
- Eighty deterministic material/design pairs pass independent mechanical and
  inference comparisons. Maximum SVD/QR stiffness difference is
  2.1600499167107046e-12 N/m.

An additional diagnostic deliberately changes coefficient entries independently
at an exactly zero stability boundary while keeping the original Boolean. That
can change the strict physical phase and is not an expected-pass control. It is
kept distinct from the benign uniform output-nudge control that the platform
requires. No stability tolerance is introduced to make inconsistent phases pass.

The final ZIP is unpacked into a new directory and its references, proxies,
per-step references, declared paths, case counts, mutants, no-op controls and
final-output perturbations are checked again. Author runners and execution
records are kept outside the submission ZIP. A fresh upload must run the
platform's reference and content checks; their result is not asserted here.

Final archive: 24 files, 53826 bytes.

SHA256: `7cd9bda1aebdbed86c785bcc60c52b9e3c92f7a26272f951a102d3490142a0ac`.
