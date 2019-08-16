#-*- coding: utf-8 -*-
# @ fuction MXNet 测试
# @ author alexchung
# @ date 15/8/2019 PM 15:45

from mxnet import nd
import numpy as np

if __name__ == "__main__":
    x = nd.arange(12).reshape(3, 4)
    print(x)
    # 行索引
    x0 = x[1:3]
    # 列索引
    x1 = x[:, 1:3]
    print(x1)

    x[1:2] = 12
    print(x)


