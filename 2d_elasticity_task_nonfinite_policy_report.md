# Nonfinite-input prompt repair

Submission: `2d_elasticity_task_nonfinite_policy_fixed.zip`.

This revision addresses the four reported **Edge-case inputs** findings.
Only the four `sub_steps[*].step_description_prompt` fields in `problem.yaml`
change. The scientific calculation, reference code, tests, numerical tolerances,
source, README, scaffolds, metadata, and other YAML fields remain unchanged.

The baseline already contained a nonfinite-input rejection rule. This repair
makes that rule the opening scientific paragraph in every step, immediately
after its function signature. It explicitly names **NaN (`np.nan`), positive
infinity (`np.inf`), and negative infinity (`-np.inf`)**, the affected public
inputs, the reason they cannot define the physical calculation, and the required
`ValueError`. It is a clarification of existing behavior.

| Step | Input policy stated directly in the step prompt |
| --- | --- |
| 1 | Reject nonfinite `strains`, `stiffness_npm`, and `free_components` before relaxation or an empty-batch return. Missing calculation records cannot define an equilibrium; an undefined component label cannot specify a boundary condition. Validate free initial guesses as well as prescribed strains. |
| 2 | Reject nonfinite `strains`, `delta_energy_ev`, and `area_ang2` before regression. Incomplete or diverged atomistic calculations supply no physical fitting observation or reference area, even when the other observations remain identifiable. |
| 3 | Reject nonfinite `stiffness_npm` and `angles_rad` before compliance inversion or response evaluation. An undefined tensor coefficient or loading direction cannot define a uniaxial loading experiment. |
| 4 | Reject nonfinite `strains`, `delta_energy_ev`, `area_ang2`, and `angles_rad` before fitting or stability branching. This applies to stable and unstable fits. The specified NaN outputs for a finite unstable tensor do not allow nonfinite input records. |

Each policy requires rejection rather than dropping, replacing, or propagating
invalid records. Existing complex-type, shape, range, positivity, conditioning,
and canonical-direction rules are preserved.

## Verification

- The ZIP has the same 24 members. Byte comparison against the baseline proves
  that `problem.yaml` is the only changed member.
- Parsed YAML comparison proves that the four step-description strings are the
  only changed fields; every numerical and structural field is identical.
- ZIP integrity and freshly extracted file contents were checked.
- Both full implementations pass **117/117** cases, including through call-only
  proxies with shared public dependency bindings. All standalone references
  pass their respective 28, 30, 21, and 28 cases; 10 whole-task cases also pass.
- All five packaged scientific mutants are rejected. `None` and zero-output
  no-op controls fail every step.
- An independent read-only prompt audit confirmed the local scientific reason,
  literal tested values, named inputs, rejection behavior, free-guess/empty-batch
  handling, and stable/unstable distinction in the four step prompts.

These are local results. The submission platform's content-quality check must
be rerun on this ZIP; its approval cannot be inferred from local validation.

Baseline commit: `236ee13396301e8f536e44008f0145546165e648`.
Baseline ZIP SHA-256:
`125e5cd533428f746e816d6721e26cebfeaacc33c90299ae033c32e48644fc6f`.
Revised ZIP SHA-256:
`b9a6b5e822c24c9c9c322ffa602d6cb7aaabb54c237b22f2784e1c63053f352a`.
