import numpy as np

# This author-side fixture requires a shared, writable PUBLIC dependency
# binding. It deliberately avoids function internals and private attributes.
# It is not a graded case until the platform supports this dependency fixture.
strains = np.array([[.01,0.,0.], [0.,.012,0.], [.01,.01,0.],
                    [.01,-.01,0.], [0.,0.,.02]])
stiffness = np.array([96.,96.,48.,24.])
x, y, shear = strains.T
design = np.column_stack((x*x/2, y*y/2, x*y, shear*shear/2))
area = 150.
energy = area*(design@stiffness)/16.02176634
angles = np.array([.13,.69,1.27])
original_fit = fit_stiffness_2d
fit_calls = []

def fit_stiffness_2d(strains, delta_energy_ev, area_ang2):
    fit_calls.append(True)
    return stiffness.copy()

try:
    result = analyze_elastic_2d(strains, energy, area, angles)
finally:
    fit_stiffness_2d = original_fit

# This assertion detects an unsupported override instead of silently treating
# a nearly isotropic energy fit as an exact-isotropy fixture.
assert fit_calls, 'The evaluator did not apply the public dependency fixture'
assert result['born_stable'] is True
assert np.allclose(result['stiffness_npm'], stiffness, rtol=1e-8, atol=1e-5)
assert np.allclose(result['young_npm'], 72., rtol=1e-9, atol=1e-8)
assert np.allclose(result['poisson'], .5, rtol=1e-9, atol=1e-10)
assert np.allclose([result['young_min_npm'], result['young_max_npm']],
                   [72.,72.], rtol=1e-9, atol=1e-8)
assert np.isclose(result['anisotropy_ratio'], 1., rtol=1e-8, atol=1e-8)
# Zero is the canonical label for a directionless isotropic response.
assert result['theta_young_min_rad'] == 0.0
assert result['theta_young_max_rad'] == 0.0
