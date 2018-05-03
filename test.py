# -- This is just a generic test file, mostly used to test how pystruct can be used to train CRFs and perform
#    Inference with the trained models -- #
import cvxopt

import numpy as np
from pystruct.models import GridCRF
import pystruct.learners as ssvm



from apply_crf import *
from data_gen import *
from noise_gen import *
from evaluation import *


crf = GridCRF(n_states=2, inference_method="ad3", neighborhood=8)  # create a new grid-crf with an 8-Neighborhood

original_map = create_neighborhood_map(15, 15, 0.05, 2, 1)
noisy_map = salt_and_pepper(original_map, hits=40)

print("Counting the abs number of differences between the two maps")
print(diff_count(original_map, noisy_map))

