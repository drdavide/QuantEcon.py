import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
import pandas as pd

a = np.linspace(-np.pi, np.pi, 100)
b = np.cos(a)
c = np.sin(a)

output = b @ c

print(output)

ϕ = norm()
value, error = quad(ϕ.pdf, -2, 2)  # Integrate using Gaussian quadrature

print(value)

np.random.seed(1234)

data = np.random.randn(5, 2)  # 5x2 matrix of N(0, 1) random draws
dates = pd.date_range('28/12/2010', periods=5)

df = pd.DataFrame(data, columns=('price', 'weight'), index=dates)
print(df)
