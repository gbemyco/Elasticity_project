# Four input-policy repairs; exact-isotropy fixture needs platform support

11 October 2026. This is a partial repair of the latest five content-integrity
findings. Four input-policy findings are addressed. The fifth finding, forced
exact-isotropic fitted-tensor coverage in the platform's graded tests, remains
open. This archive is not represented as having passed the platform quality
check.

All reference implementations are byte-identical to the preceding archive
reported by the user to pass its reference check. The independent implementation,
scaffolds, five scientific mutants, general tests, source text, scientific
background, metadata, signatures, dependencies, mechanical conventions, and
numerical accuracy budgets are also unchanged. Only README.md, problem.yaml's
visible input prose and case counts, and the four step-test files change.

## The four completed repairs

The preceding YAML already explicitly required rejection of nonfinite input
markers, despite the checker saying it contained no such instruction. Repeating
that prose did not resolve the findings. This revision instead scopes the
scientific computation to finite observations from completed calculations.
Diagnosing missing or diverged calculations happens before constructing this
dataset. Nonfinite inputs are outside the task's input domain; their rejection
is no longer a grading requirement. The unchanged references still reject them.

| Finding | Scoped change |
|---|---|
| Step 1 nonfinite strain/stiffness/free-label inputs | Remove the all-nonfinite-input case and NaN/infinity component labels. Preserve free-column and empty-batch complex rejection, finite shape/range errors, constrained-minimum checks, and soft-mode physics. |
| Step 2 NaN/infinity data and apparent epsilon input | Remove the nonfinite-energy case and nonfinite strain/energy/area variants. Preserve all finite data, complex-type, shape, area, rank, RMS, and conditioning checks. State the fixed binary64 roundoff allowance explicitly. |
| Step 3 NaN/infinity stiffness and angles | Remove only nonfinite-input variants. Preserve malformed shapes, empty/multidimensional or complex angles, full Born stability, and all directional scientific comparisons. |
| Step 4 nonfinite data/angles and apparent epsilon input | Remove only nonfinite supplied-input variants. Preserve complex-angle rejection on unstable fits, all Born branches, global extrema and tie comparisons, and every required NaN OUTPUT assertion. Preserve reporting-error propagation. |

The internal roundoff allowance is written as
`delta=1.4210854715202004e-14=64*2**(-52)`. This equals the prior
`64*np.finfo(float).eps` exactly in binary64. The reporting bound remains
`eta=1e-12+delta`, also exactly equivalent to its preceding extended-arithmetic
expression. Neither constant is supplied as a physical observation. No
conditioning endpoint, response tolerance, stability threshold, or tie rule
changes.

The archive has 95 independently executed cases: 24,24,16,21 in Steps 1–4,
plus 10 whole-task cases. Case numbers are consecutive and zero-based.

## The fifth finding and prepared fixture

An exactly isotropic SOURCE dataset cannot guarantee an exactly isotropic
RETURNED fit for every correct implementation. Step 2 allows nonzero coefficient
errors larger than Step 4's relative `1e-10` tie threshold. A valid slightly
asymmetric returned tensor can therefore have unique principal-axis extrema.
Demanding zero angles for that tensor would reject a permitted implementation.
The existing isotropic-source case remains unchanged and is not claimed to
resolve forced exact-isotropy coverage.

The requested isolated test is prepared separately in
[2d_elasticity_exact_isotropy_fixture.py](2d_elasticity_exact_isotropy_fixture.py).
It temporarily binds the public fitting dependency to a stub returning exactly
`[96,96,48,24]`, verifies the stub was actually called, checks the independently
known `E=72 N/m`, `nu=0.5` response and unit anisotropy, and asserts both canonical
angles are exactly `0.0`. It restores the dependency in a `finally` block. It
does not inspect function globals, private attributes, evaluator code, or
process state. The scientific expectation is independent of candidate outputs.

That fixture passes both complete implementations, both call-only proxies when
their public dependency binding is shared with the test, and the isolated Step 4
reference with its declared earlier dependencies. It rejects a mutant that
changes only bitwise-exact isotropic directions to pi/4.

However, when reference execution and test execution have separate namespaces,
ordinary test-name rebinding does not replace the reference's fitting dependency:
the stub receives zero calls. The prepared fixture detects this failure rather
than silently substituting an almost-isotropic end-to-end fit. No documented
platform override mechanism has been supplied. Reintroducing `.__globals__`
would repeat the known platform Oracle exception. The prepared fixture is
therefore outside the submission ZIP until a supported public dependency fixture
can be wired into grading. This limitation is not fixed by additional mutants.

## Executed local verification

- Both complete implementations: 95/95 cases each.
- Both call-only proxy interfaces: 95/95 cases each.
- Isolated per-step references: 24/24,24/24,16/16,21/21.
- All five packaged scientific mutants rejected by their targeted suites.
- None and zero controls rejected on every graded case.
- Thirty expected-pass final-output perturbation modes per implementation:
  872/872 evaluations each, including relative +/-1e-12 nudges.
- Admissible intermediate fitting/response errors: 1334/1334 per implementation.
- Admissible Step 1 field errors: 288/288 evaluations.
- Eleven additional scientific and validation controls remain rejected.
- Core and final-output perturbation checks pass in three clean processes with
  thread/hash settings (1,0), (1,271), and (2,913).
- Direct comparison verifies the 18 unchanged submission files, unchanged field
  sets and all numerical/reference conventions. The packaged archive is unpacked
  and checked separately.

These are author-side results, not a new execution of the platform's Oracle or
content checker. The exact-isotropy grading gap is explicitly outstanding.

Archive: `2d_elasticity_task_input_policy_repair.zip`, 24 files, 54206 bytes.

SHA256: `7b8cd5b4e60be2e2d6e11752812ab0a0ce2c4322c194de058b87a86c55d7c731`.
