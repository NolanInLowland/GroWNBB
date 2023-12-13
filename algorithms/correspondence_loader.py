import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset
from typing import List, Dict

def corrLoader(correspondence_A, correspondence_B, correspondence_AB):
    src_index = {}
    tar_index = {}

    src_list = []
    tar_list = []

    for node in correspondence_A[0]:
        if node not in src_list:
            src_list.append(node)
    for node in correspondence_A[1]:
        if node not in src_list:
            src_list.append(node)
    for node in correspondence_AB[0]:
        if node not in src_list:
            src_list.append(node)
    for idx in range(len(src_list)):
        src_index[str(src_list[idx])] = idx

    for node in correspondence_B[0]:
        if node not in tar_list:
            tar_list.append(node)
    for node in correspondence_B[1]:
        if node not in tar_list:
            tar_list.append(node)
    for node in correspondence_AB[1]:
        if node not in tar_list:
            tar_list.append(node)
    for idx in range(len(tar_list)):
        tar_index[str(tar_list[idx])] = idx

    src_interactions = []
    tar_interactions = []
    mutual_interactions = []
    mutual_interactions2 = []


    for i in range(len(correspondence_A[0])):
        idx_A1 = src_list.index(correspondence_A[0][i])
        idx_A2 = src_list.index(correspondence_A[1][i])
        src_interactions.append([idx_A1, idx_A2])
        # count = int(10 * correspondence_A[2][i])
        # for j in range(count):
        #     src_interactions.append([idx_A1, idx_A2])

    for i in range(len(correspondence_B[0])):
        idx_B1 = tar_list.index(correspondence_B[0][i])
        idx_B2 = tar_list.index(correspondence_B[1][i])
        tar_interactions.append([idx_B1, idx_B2])
        # count = int(10 * correspondence_B[2][i])
        # for j in range(count):
        #     tar_interactions.append([idx_B1, idx_B2])

    for i in range(len(correspondence_AB[0])):
        idx_A = src_list.index(correspondence_AB[0][i])
        idx_B = tar_list.index(correspondence_AB[1][i])
        count = int(10 * correspondence_AB[2][i])
        mutual_interactions2.append([[idx_A], [idx_B]])
        mutual_interactions.append([[idx_A], [idx_B]])
        # for j in range(count):
        #     mutual_interactions.append([[idx_A], [idx_B]])

    database = {'src_index': src_index,
                'tar_index': tar_index,
                'src_interactions': src_interactions,
                'tar_interactions': tar_interactions,
                'mutual_interactions': mutual_interactions,
                'mutual_interactions2': mutual_interactions2,
                'correspondence': correspondence_AB,
                'src_list': src_list,
                'tar_list': tar_list}
    return database











