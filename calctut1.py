import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ar = np.random.randn(10000)
plt.hist(ar, bins = 100)
plt.show()