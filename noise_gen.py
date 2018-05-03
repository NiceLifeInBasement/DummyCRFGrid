# -- This file provides different methods of adding noise to a map -- #
# All methods in this file should take a grid map, apply noise in a certain way to it and return that

import numpy as np
from random import randint


def salt_and_pepper(occ_map, hits=25):
    """
    Adds salt and pepper (impulse) noise to a given map.
    For this, a certain number of cells is flipped from 0 to 1 and vice versa
    :param occ_map: The map which should be used as a ground-truth. This needs to be a 2D (numpy) Array of 0s and 1s
    :param hits: The number of cells selected for flipping
    :return: A 2D (numpy) Array that is similar to the input, but has salt and pepper noise sprayed on it
    """
    noisy_map = np.copy(occ_map)
    for i in range(1, hits):
        x_size = occ_map.shape[0]
        y_size = occ_map.shape[1]
        x_pick = randint(0, x_size - 1)
        y_pick = randint(0, y_size - 1)
        if noisy_map[x_pick, y_pick] == 1:
            noisy_map[x_pick, y_pick] = 0
        else:
            noisy_map[x_pick, y_pick] = 1
    return noisy_map

