import numpy as np
import pandas as pd

if __name__ == "__main__":
    readings = np.loadtxt(fname="u2p1export.csv", delimiter=",")
    stdDeviations = np.std(readings, axis=0)
    stdDeviations = [stdDeviations]
    dataFrame = pd.DataFrame(stdDeviations, columns=["Promedio", "ValorMenor", "ValorMayor", "Mediana"])
    print(dataFrame)