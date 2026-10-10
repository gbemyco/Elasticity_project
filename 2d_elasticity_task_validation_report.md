# Content-only revision with reference implementations preserved

11 October 2026. The user reports that the preceding archive passes the platform
reference check. This revision is limited to the latest content feedback.
No reference implementation, independent implementation, scaffold, mutant,
function signature, dependency declaration or numerical tolerance changes.
All six reference/independent implementation files are byte-identical to the
previous archive. The source and scientific background also remain unchanged.

The latest content report lists four input-policy findings, two missing complex
input cases and a conditional isotropy assertion. The input-policy statements
already existed in the previous parsed YAML, but the report described them as
absent. This revision puts them beside the input definitions, repeats their
scientific rationale in the main prompt, and emits agent-visible prose as literal
YAML blocks. NaN and infinities are failed-computation markers that must raise
ValueError; machine epsilon is explicitly an internal precision constant rather
than a physical input. Existing rejection tests and numeric limits are retained.

| Latest finding | Content repair |
|---|---|
| Step 1 nonfinite input policy not recognized | Main and Step 1 input paragraphs name np.nan, np.inf, -np.inf and ValueError, including ignored free guesses and invalid component labels. |
| Step 2 nonfinite inputs and machine epsilon | Its input paragraph names failed DFT-data markers and their rejection. Its precision paragraph defines binary64 epsilon and its existing endpoint role. The test comment distinguishes an internal comparison constant from supplied data. |
| Step 3 nonfinite input policy not recognized | Its input paragraph explicitly rejects missing/diverged stiffness data and undefined nonfinite loading directions. |
| Step 4 nonfinite inputs and machine epsilon | Its input paragraph requires rejection before either stability branch. The precision statement and comparison comments identify epsilon as internal arithmetic data. Valid unstable-output NaNs remain a defined result. |
| No complex strain in a free input column | New Step 1 case 23 supplies .02+1j in free column 1 and requires ValueError. |
| No empty complex-typed strain batch | New Step 1 case 24 supplies np.empty((0,3),dtype=complex) and requires ValueError. |
| Exact-isotropy assertions can be skipped by an asymmetric fit | Step 4 case 20 now computes independent critical-direction work and canonical tie targets unconditionally. All directions and extrema are checked on every run. The same general canonical rule applies to the isotropic limit; no separate bitwise-fit acceptance branch remains. |

Case numbers are zero-based. There are 97 cases: 25,25,16,21 in the four steps,
plus ten whole-task cases. The package still contains four evaluated functions,
five scientific mutants and 24 files under the original task identity.

For the isotropic dataset, the SVD reference reaches an exactly isotropic returned
fit; both implementations give canonical directions (0,0). An incorrect-physics
control changing only exactly isotropic directions to pi/4 is rejected by case 20.
Correct asymmetric fits within the published fitting error budget are also
checked unconditionally against their own independently computed directions.
This preserves the scientific contract rather than demanding that every valid
least-squares implementation reproduce bitwise fitting symmetry.

The screenshot recommends temporarily substituting the public fitting dependency.
No supported override mechanism is supplied for the platform's call-only
interface. The prior attempt to inspect function globals failed Oracle. This
revision therefore uses the unconditional public-result oracle and the general
tie definition; it does not claim a forced dependency-injection test. The general
rule entails zero canonical directions for isotropic work without requiring a
particular implementation branch.

Executed author checks:

- Both complete implementations and both call-only proxy interfaces: 97/97 each.
- Isolated per-step references: 25/25,25/25,16/16,21/21.
- All five packaged scientific mutants are rejected by their relevant suites.
- None and zero controls are rejected on every case.
- Thirty expected-pass final-output perturbation modes per implementation:
  876/876 evaluations each, including relative +/-1e-12 nudges and allowed
  extremum-angle errors.
- Existing admissible intermediate-error checks: 1334/1334 per implementation.
- Admissible Step 1 output-error checks: 300/300.
- Existing conditioning, stability, tie, clipping, complex-input and isotropic
  direction controls remain rejected. Two additional author controls that
  discard only complex free guesses or accept only empty complex batches are
  rejected specifically by the new cases in both implementations.
- Core and output-noise checks pass in three clean processes with thread/hash
  configurations (1,0), (1,271), (2,913).
- Direct file comparison verifies reference-code preservation, unchanged
  metadata field sets, signatures, dependencies and numerical criteria.

Changed submission files are README.md, problem.yaml, Step 1 test coverage,
Step 4's unconditional canonical oracle, and comments in Step 2 tests. The
computational Step 2 tests, Step 3 tests and general tests are unchanged.
Author runners and detailed execution records stay outside the submission ZIP.
The final archive is unpacked separately and checked again. These are local
verification results; a new platform content-check result is not asserted.

Archive: 24 files, 54734 bytes.

SHA256: `0382205b2ce4d908ec8e77853937d2523e3d62c87226d42c4cc8b217d57f8aec`.
