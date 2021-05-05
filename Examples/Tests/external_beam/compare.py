#! /usr/bin/env python

import numpy as np
from openpmd_viewer import OpenPMDTimeSeries

ts1 = OpenPMDTimeSeries('./ORIGINAL_diags/diag1/')
ts2 = OpenPMDTimeSeries('./diags/diag1/')

species = 'driver'
iteration = 2

x1_2, z1_2 = ts1.get_particle(species=species, iteration=iteration, var_list = ['x', 'z'])
x2_2, z2_2 = ts2.get_particle(species=species, iteration=iteration, var_list = ['x', 'z'])

are_equal = np.all(np.isclose(np.sort(x1_2), np.sort(x2_2), rtol=1.e-10))
print("np.all(np.isclose(np.sort(x1_2), np.sort(x2_2), rtol=1.e-10)) ? " + str(are_equal))
assert( are_equal )
