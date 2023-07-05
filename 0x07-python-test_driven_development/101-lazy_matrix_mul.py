#!/usr/bin/python3
"""The Matrix that defines a multiplication function"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """return the mmltiplies of 2 matrices"""

    return (np.matmul(m_a, m_b))
