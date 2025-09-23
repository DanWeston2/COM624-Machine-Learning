import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dirty = pd.read_csv("titanic.csv")
cleaned = pd.read_csv("cleanedTitanic.csv")

#Age

dirtyAge = np.array(dirty.get("Age")[0:50])

cleanAge = np.array(cleaned.get("Age")[0:50])

plt.plot(dirtyAge, c="chocolate", linewidth="10")
plt.plot(cleanAge, c="aqua")
plt.show()