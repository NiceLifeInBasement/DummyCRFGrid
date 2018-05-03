# -- This file is generating simulated grid maps in a given file format -- #
# For this, noise_gen is used to apply noise to the "ground-truth"-maps which are generated beforehand (in this file)

# TODO:
#   Try out numpy.random.rand to create an array filled with random numbers
#   ---
#   Using the following code:
#       xim[i-d:i+d+1, j-d:j+d+1].flatten()
#       This selects the 8 neighborhood of element (i,j) in array x with a range of d (how "far away" nb may be)
#           Usually range d=1 for the direct neighborhood

# Imports
import numpy as np
from random import randint
# End of imports


def create_neighborhood_map(x_size, y_size, nb_prob=0, avg_hits=3, keep_borders=1):
    """
    Create a new map of size x_size * y_size. The map will have occupied borders ('1') and randomly spread,
    neighborhood-depending cells occupations. For this, cells will be randomly selected and then randomly set to 0/1,
    depending on their neighbors.

    :param x_size: The x size of the map
    :param y_size: The y size of the map
    :param nb_prob: nb_prob is added to the relative count of neighboring cells that are occupied ('1')
            Negative np_prob values lead to a tendency to 0s, positive values lead to a tendency to 1s
            np_prob should be between -1 and 1, even though 1/-1 make no sense (guarantee outcome)
    :param avg_hits: avg_hits determines how often every cell is hit on average during the random selection of cells to change.
                    for np_prob!=0, higher avg_hits values lead to convergence of the entire map towards one value.
                    For example: with a reasonably small np_prob > 0 and avg_hits=100, every cell will converge towards 1.
                    Even if np_prob < 0, the borders influence will cause a convergence towards '1', if they are skipped during selec.
    :param keep_borders: Can be 0 or 1: If a value of 0 is selected, the borders can be hit during the random selection.
                         With a value of 1 , the borders will not be selected
    :return: A 2D (numpy) Array of 0s and 1s indicating occupation of the map
    """
    occ_map = np.zeros((x_size, y_size))  # create a new 0filled array of the relevant size
    # All borders are switched to 1
    occ_map = create_borders(occ_map)
    # Now perform a random walk on the map, switching cells depending on their 8-nbhood
    map_size = x_size * y_size
    for i in range(0, avg_hits*map_size):  # Every cell is hit on avg avg_hits times
        # Pick a random position on the map
        x_pick = randint(keep_borders, x_size - 1 - keep_borders)  # Do not select border positions if keep_borders=1
        y_pick = randint(keep_borders, y_size - 1 - keep_borders)
        # EXPLANATION FOR THE FOLLOWING: SEE ABOVE (in TODO section)
        nb_count = np.sum(occ_map[x_pick-1:x_pick+1+1, y_pick-1:y_pick+1+1].flatten())
        nb_count /= 8  # Divide by neighborhood size
        nb_count += nb_prob
        if nb_count > np.random.random():
            occ_map[x_pick, y_pick] = 1
        else:
            occ_map[x_pick, y_pick] = 0
    return occ_map


# Given the map input (which is an array containing 0's and 1's)
# Set all borders of the map to 1
def create_borders(occ_map):
    """
    Given the map input (which is an array containing 0's and 1's)
    Set all borders of the map to 1

    :param occ_map: The map that should have its borders manipulated as a 2D (numpy) array
    :return: A 2D (numpy) Array that is equiv to the input, but has all the outer borders set to 1
    """
    occ_map[0, :] = 1
    occ_map[occ_map.shape[0]-1, :] = 1
    occ_map[:, 0] = 1
    occ_map[:, occ_map.shape[1]-1] = 1
    return occ_map


