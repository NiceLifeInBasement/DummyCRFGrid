# -- This file contains methods for map evaluation -- #

import numpy as np
import math


def diff_count(org_map, new_map):
    """
    Counts the absolute difference in occupied cells between the two input maps.

    :param org_map: The original map as a 2D (numpy) Array of 0s and 1s. Needs to be of the same size as new_map
    :param new_map: The second map (e.g. the noisy or "cleaned up" map) as a 2D (numpy) Array of 0s and 1s.
    :return: The absolute count of differences between the cells of the two input maps
    """
    # The current solution uses a potential deprecated == comparison of numpy arrays
    # TODO: double check that this is working as expected

    x_size = org_map.shape[0]
    y_size = org_map.shape[1]
    error_count = (x_size*y_size)-(org_map == new_map).sum()
    return error_count
