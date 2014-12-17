import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(0, 2 * np.pi, 100)

plt.plot(x, np.sin(x))
plt.savefig('sin')
p=pd.DataFrame({'a':[1,2]})
print p
