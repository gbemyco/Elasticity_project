# Isolated exact-isotropy coverage revision

11 October 2026. Edit label: grading_fix.

This candidate addresses only the remaining exact-isotropy coverage finding.
The five soft-limit advisories are not changed in this archive, following the
user's latest instruction to leave other task content alone.

The uploaded standard guide was read. Its relevant requirements are independent
special-case expectations, numerical comparisons using visible tolerances,
verification with a genuinely different implementation, and explicit reporting
of infrastructure limitations rather than changing the science to conceal them.

## Narrow change

Added Step 4 case 21 (zero-based), a self-contained isolated public-dependency
fixture. It temporarily replaces the supplied `fit_stiffness_2d` binding with a
stub returning exactly `[96,96,48,24]`, records whether the stub was invoked,
calls `analyze_elastic_2d`, and restores the original dependency in `finally`.
No function internals, private attributes, evaluator files or processes are
accessed by the graded test.

For this isotropic constitutive matrix, independent analytic expectations are
`E=C11-C12**2/C22=72 N/m`, `nu=C12/C22=0.5`, unit anisotropy, and both canonical
directions zero. Targets are not derived from the submission's numerical fit.
The angle targets are mathematically zero; the test compares numerically with
the existing `rtol=1e-7, atol=1e-7` angle budget, following the attached guide's
instruction not to pin floating-point outputs with exact equality. The test
also checks the specified stable response and scalar/array output contracts.

No existing test was edited. Every reference implementation, the independent
implementation, Steps 1–3 tests, general tests, scaffolds, source text,
background, mutants, scientific prompt, signatures, dependencies and numerical
tolerances are byte-identical to the preceding input-policy repair.

Changed files are limited to:

- `tests/step_4.py`: append one isolated case.
- `problem.yaml`: only Step 4 `n_test_cases` changes from 21 to 22.
- `README.md`: update case counts and describe the added fixture's context.

There are 96 cases: 24,24,16,22 per step and 10 whole-task cases. The archive
retains 24 files, four evaluated steps and five declared scientific mutants.

## Executed checks and compatibility limitation

With shared writable public dependency bindings:

- Both complete implementations pass 96/96 cases.
- Both call-only proxy interfaces pass 96/96 cases.
- Isolated per-step references pass 24/24,24/24,16/16,22/22 cases.
- All five packaged scientific mutants are rejected by their targeted suites.
- All-function None and zero controls are rejected on every case.
- A targeted control returning pi/4 only for a bitwise-exact isotropic tensor is
  rejected by the new case with both independent implementations.
- Thirty final-output perturbation modes pass 896/896 evaluations per
  implementation, including relative +/-1e-12 nudges and the existing permitted
  numerical angle errors.
- Core and perturbation checks pass in clean processes with thread/hash
  settings (1,0), (1,271), and (2,913).
- File comparison confirms unchanged reference/scientific content and the
  unchanged prefix containing all 21 pre-existing Step 4 cases.

The fixture mechanism is not portable to a grader that executes the reference
in a separate namespace and merely copies public callable aliases into the
test namespace. I ran that diagnostic: both implementations fail only the new
case because the stub receives zero calls. The test reports this explicitly as
`Public dependency fixture was not applied`; it does not silently substitute an
almost-isotropic numerical fit.

No supported platform dependency-override interface has been supplied, and the
uploaded standard guide does not document one. This is therefore a **review
candidate**, not a confirmed platform-ready submission. Its scientific coverage
gap is fixed when the grader supports this public binding replacement; grader
compatibility must be established before claiming Oracle or content-check
approval. The previous `.__globals__` approach is not reintroduced.

Archive: `2d_elasticity_task_isotropy_candidate.zip`, 24 files, 55110 bytes.

SHA256: `60e5816157a54ee389222ea6df675a65a21f74d11a6006eb088f1a5c87d1a72f`.
