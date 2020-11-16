# Copyright (C) 2020, All rights reserved.
# Author: Roby

# python3.7
# 机器学习概率分布基础
# 二项分布 与 Beta 分


import os
import numpy
import matplotlib as plt
import random



# 产生N个样本
N = 10
mu = 0.42
samples = []

for i in range(N):
    if random.uniform(0,1)<0.42:
        samples.append(1)
    else:
        samples.append(0)
print(samples)

#   dev_cocos_sample_0923
#   dev_roby_common_v1.0.2
#   dev_roby_common_v1.0.3
#   dev_roby_crazy_store_v1.1.2
#   dev_roby_crazy_store_v1.1.3
#   dev_roby_magic_cube_v1.0.0
#   dev_roby_magicline_v1.0.4
#   dev_roby_slice_factor_v1.0.6


