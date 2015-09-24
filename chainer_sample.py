import numpy as np
from chainer import cuda, Function, FunctionSet, gradient_check, Variable, optimizers, utils
import chainer.functions as F

x_data = np.array([5], dtype=np.float32)
x = Variable(x_data)
y = x**2 - 2 * x + 1

print(y.backward())