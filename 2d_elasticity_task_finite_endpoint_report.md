# Nonfinite input and included RMS endpoint repair

Archive: `2d_elasticity_task_finite_endpoint_fixed.zip`

Date: 11 October 2026 (Australia/Sydney).

Baseline: `2d_elasticity_task_coverage_fixed.zip` at e8ea50b313ff72a006e25d94aaadd77c7865258b.

SHA-256: `eb00b7d022fc3e34f3b3f596f3e7ad197aca629557359a6e4dcfe5af1046d709`

## Screenshot findings addressed

| Finding | Added zero-based test case | Required behavior |
| --- | --- | --- |
| Step 1 nonfinite inputs untested | Step 1 case 25 | NaN and positive/negative infinity in prescribed strains, free guesses, stiffness, and free component labels must raise ValueError. |
| Step 2 nonfinite fitting data untested | Step 2 case 25 | An otherwise full-rank, well-conditioned physical dataset with a nonfinite energy observation must raise ValueError. |
| Step 2 normal-column included RMS endpoints untested | Step 2 case 26 | Separate designs for columns 0, 1, and 2 at RMS 1e-6 must be accepted and recover known stiffness within the existing accuracy budget. |
| Step 3 nonfinite tensor/direction inputs untested | Step 3 case 17 | Nonfinite coupling or shear stiffness and nonfinite loading angles must raise ValueError. |
| Advisory: unstable branch nonfinite angles untested | Step 4 case 23 | Nonfinite angles remain invalid for a valid finite dataset with a clearly unstable fitted tensor; ValueError required. |

NaN and infinities model missing or diverged calculation records, not extreme physical materials. The main scientific prompt and each step now explicitly require ValueError for these records, including free initial guesses and loading angles before the unstable response branch. This clarifies rejection behavior without changing the valid physical domain or any reference algorithm.

The RMS endpoint designs use constant-magnitude target entries. For normal columns a=sqrt(2e-6) gives a*a/2=1e-6; for the coupling column the strain product 0.004*0.00025=1e-6. The measured target RMS values equal binary64 1e-6 locally. Conditions are approximately 236.493, 236.493, and 36.140, all designs have rank 4, and every other RMS is above the threshold. Tests compare endpoint agreement using the already published dimensionless rounding allowance. Coefficient comparisons retain rtol=1e-8 and atol=1e-5 N/m.

## Scope preserved

Every reference implementation, independent implementation, scaffold, source, packaged scientific mutant, prior test, numerical tolerance, and mechanical stability convention is unchanged. Existing test files remain byte-for-byte prefixes of the updated files. Only five new self-contained cases were appended, and problem.yaml received the finite-input rejection clarification and case-count updates. README.md records the resulting coverage.

The optional Step 2 transcription advisory remains a task-design consideration. This focused repair retains the existing unweighted least-squares objective rather than adding a new inference decision or changing its expected answer. The solver remains free to choose a numerically stable implementation: the supplied implementations already use distinct SVD/lstsq and QR constructions. This revision does not claim to resolve the platform's difficulty or method-freedom assessment.

## Verification

- 105 cases: 26, 27, 18, 24 per step, plus 10 whole-task cases.
- Complete reference and independent implementation: 105/105 each.
- Both implementations through call-only evaluator proxies: 105/105 each.
- All per-step references pass with only their declared dependencies.
- All five existing packaged scientific mutants are rejected.
- None and zero no-op controls fail every case.
- All nine additional targeted author controls are rejected: six omitted-finiteness implementations and three column-specific excluded RMS endpoints.
- Existing broader wrong-physics controls retain their rejection results.
- All 30 final-output perturbation modes pass for each implementation; evaluated applicable cases: {'solution.py': 958, 'second_solution.py': 958}.
- Admissible intermediate-error checks pass for both implementations.
- Complete references and output-perturbation controls pass in three fresh-process configurations: threads/seed 1/0, 1/271, and 2/913.
- The 24-file ZIP was checked for corruption, freshly extracted, byte-compared to the revised folder, and its complete validation rerun successfully.

Public dependency fixtures retain the baseline shared-binding execution pattern; no private evaluator or function introspection was introduced. The environment supports the existing NumPy computation and author checks without any new runtime dependency. Author-only controls, scripts, and result records are kept outside the submission archive.

These are local verification results. The submission platform's new Oracle and content-quality checks must be run on this archive to establish approval.
