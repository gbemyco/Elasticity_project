# Four remaining coverage repairs

Archive: `2d_elasticity_task_coverage_fixed.zip`

Baseline: `2d_elasticity_task_isotropy_candidate.zip` at b1e1fa21c67208f699eae02ea3f5eb72c422faba.

SHA-256: `6103ac882e75f33b928e6431d82a50f0b780ad5ff862ca653b93fa25961ea910`

The scientific task remains the existing four-step, NumPy-only 2D energy–strain computation. The historical discussion reinforces the use of energy per unstrained area and stiffness in N/m; it does not introduce stress–strain fitting, VASP, piezoelectric metrics, or a new scientific method into this revision.

## Changes confined to the four reported coverage gaps

| Finding | Added isolated case | Verification |
| --- | --- | --- |
| Step 1: out-of-range free initial guess untested | Step 1, zero-based case 24 | Component 1 is 0.031 with free_components=[1]; ValueError required before relaxation. |
| Step 2: normal-column RMS thresholds untested | Step 2, zero-based case 24 | Each of columns 0, 1, 2 separately has RMS 0.99e-6; all other columns exceed 1e-6. Every design has rank 4 and condition number below 1000; ValueError required. |
| Step 3: strictly positive soft tensors below calibration untested | Step 3, zero-based case 16 | Tiny positive C11, C22, C66 (1e-12), and a dyadic normal block with determinant ratio approximately 9.09e-13 must be accepted and produce finite, correctly shaped principal-axis arrays. |
| Step 4: independently classified returned soft fits untested | Step 4, zero-based case 22 | Public fitting dependency supplies each of the same four exact tensors; invocation is confirmed, born_stable must be True, and response arrays and scalar summaries must be finite. |

Step 2 designs have condition numbers approximately 110.16, 110.17, and 90.35. Their rejection is attributable to the targeted column RMS, not rank, conditioning, shape, or strain range. The below-calibration mechanical cases check strict admissibility and finite responses rather than imposing unsupported calibrated accuracy guarantees.

Only six files differ: the four step test files, the four case-count fields in problem.yaml, and README.md describing this coverage. Existing test files remain byte-for-byte prefixes of their updated files. Every scientific contract, reference implementation, independent implementation, scaffold, source, mutant, numerical tolerance, and prior test is unchanged. No cases were removed or relaxed.

## Local verification

- 100 cases: 25, 25, 17, 23 per step; 10 whole-task cases.
- Both complete implementations: 100/100 each.
- Both implementations through call-only proxies: 100/100 each.
- Declared-dependency per-step references: 25/25, 25/25, 17/17, 23/23.
- All five existing packaged scientific mutants rejected.
- None and zero no-op controls fail all 100 cases each.
- Ten additional author-only wrong implementations rejected specifically by the new cases: skipped free-guess range validation, shear-only RMS validation, and four positive-cutoff variants in each of Steps 3 and 4.
- Existing broader wrong-physics controls pass their rejection checks.
- All 30 final-output perturbation modes pass for both implementations (926 evaluated applicable cases per implementation), including relative 1e-12 output changes.
- Intermediate-error budget checks pass for both implementations using the shared public dependency binding.
- Complete reference and final-output perturbation checks pass in three fresh-process configurations: one thread/hash seed 0, one thread/seed 271, and two threads/seed 913.
- The 24-file ZIP was checked for corruption, extracted, byte-compared against the revised folder, and its complete validation repeated successfully.

The Step 4 fixture reuses the public-fit rebinding pattern already present in baseline case 21 and specifically requested in the supplied feedback. No test accesses __globals__, unwraps a proxy, reads source, or uses private evaluator state. Shared public dependency bindings are required for these fixtures. A separate-namespace diagnostic runner does not apply these overrides and fails the invocation assertion for both the unchanged baseline fixture and the added fixture; this is distinguished from the passing supported-context checks above.

Author-only validation scripts and records remain outside the submission archive. These results establish local regression and coverage checks; the submission platform's new Oracle and content-quality results have not been run here.
