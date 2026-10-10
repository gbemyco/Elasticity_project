# Template comparison and revised-task verification

11 October 2026. This is author verification, not a new platform Oracle result.

The newly supplied template has 22 graded cases. Its reference, independent
solution and each per-step reference pass these cases locally. Both complete
implementations also pass when exposed through call-only proxies. The user
reports that this template previously passed the platform reference check.

The template uses the accepted `tasks/2d_elasticity` folder, four consecutive
`sub_steps`, declared relative paths, NumPy-only scientific imports, matching
reference/scaffold signatures and standalone numbered test cases. It calls
public functions normally and never requires their internal Python globals.
Those conventions are retained in the revised submission.

The previous expanded submission's confirmed Oracle failure was caused by
four Step 4 cases reading `__globals__`. Oracle's callable proxy does not expose
that attribute. The correction rewrote those cases as normal calls using real
energy datasets and scientific expectations at the returned fit. The template
comparison confirms that this correction follows its public-interface pattern.

| Item | Supplied template | Revised submission |
|---|---:|---:|
| Evaluated steps | 4 | 4 |
| Packaged scientific mutants | 5 | 5 |
| Submission files | 24 | 24 |
| Total graded cases | 22 | 90 |
| Direct reference cases passed | 22 | 90 |
| Independent-solution cases passed | 22 | 90 |
| Call-only reference cases passed | 22 | 90 |
| Call-only independent cases passed | 22 | 90 |

Top-level and per-step YAML field-name sets are identical. Submission relative
paths match except for the named Step 4 scientific mutant: the revised task
uses `step_4_sampled_extrema.py`, declared consistently in its YAML, to detect
loss of continuous global extrema. All declared paths exist.

The 24-file submission consists of README.md and the task folder. Author-only
runners and reports are kept outside the upload ZIP. The scientific task files
are byte-identical to the previously corrected version: this comparison does
not revert the new relaxation calculation or weaken its tests.

The revised task retains mixed prescribed/free elastic relaxation, continuous
global extrema, exact conditioning-endpoint coverage, strict returned-fit Born
classification, near-degenerate response checks, anisotropic endpoint ties,
propagated numerical error budgets, and the inspected-paper/source attribution.
The template's short energy transcription and sampled-only extrema are not
reintroduced. Its reference pass demonstrates self-consistency of its tested
cases, rather than comprehensive scientific quality.

Revised per-step case counts are 21,24,16,19; whole-task cases are 10. Both
implementations, their call-only proxy interfaces and all per-step references
pass. Five scientific mutants and both all-function no-op controls are rejected.
The six focused conditioning, stability and tie-error controls remain rejected.
Earlier author verification also passed admissible-error perturbations, three
clean thread/hash runs, 80 deterministic material/design pairs and 2,268
high-precision directional comparisons. No scientific implementation changed
in this packaging revision, so those execution records remain applicable.

A fresh unpack of the final upload archive is checked again for signatures,
paths, case counts, correct implementations, proxies, mutants and no-op controls.
The new ZIP has not been executed in the platform's Oracle container. A new
Oracle run and the subsequent quality checks remain necessary. No identity
mapping schema was supplied, so the original folder identity is retained
without a guessed `_id_mapping.json` or placeholder identity.
