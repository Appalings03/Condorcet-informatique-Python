import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as scint

T=np.array([290,300,310,320,330])
E=np.array([1.15053,1.14950,1.14488,1.14403,1.14325])
plt.plot(T,E,"b",label="interp linéaire")   # Interpolation faite par défaut graphiquement
plt.plot(T,E,"ro")
f=scint.interp1d(T,E,"cubic")    # f est la fonction d'interpolation par splines cubiques passant les points de coordonnées (T,E)
Tinterp=np.linspace(290,330,100)  
#print(Tinterp)
plt.plot(Tinterp,f(Tinterp),"g",label="interp spline cubique")
plt.xlabel("T(K)")
plt.ylabel("E(V)")
plt.grid()
plt.legend()
plt.show()