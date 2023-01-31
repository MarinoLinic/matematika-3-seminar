from sympy import symbols, sqrt, asin, diff
from sympy.plotting import plot3d

# definiramo simbole x i y da bi ih mogli koristiti u formulama
x, y = symbols('x y')
f = asin(sqrt((x - y) / x))  # definiramo zadanu funkciju

# Parcijalna derivacija po x
dfdx = diff(f, x)
# diff() je metoda sympy za rješavanje derivacija;
# prvi argument je funkcija, drugi argument po čemu se derivira;
# ako nema dvije varijable se ne mora dodavati drugi argument

# Parcijalna derivacija po y
dfdy = diff(f, y)

# Parcijalna derivacija drugog reda po x
d2fdx2 = diff(dfdx, x)
# kako bi izračunali derivaciju drugog reda, deriviramo po derivaciji prvog reda

# Parcijalna derivacija drugog reda po y
d2fdy2 = diff(dfdy, y)

# Parcijalna derivacija drugog reda po xy
d2fdxdy = diff(dfdx, y)

# Parcijalna derivacija po x u točki T(9,5)
dfdx_T = dfdx.subs({x: 9, y: 5})
# subs() je metoda sympy za uvrštavanje vrijednosti u formulu

# Parcijalna derivacija po y u točki T(9,5)
dfdy_T = dfdy.subs({x: 9, y: 5})

# Parcijalna derivacija drugog reda po x u točki T(9,5)
d2fdx2_T = d2fdx2.subs({x: 9, y: 5})

# Parcijalna derivacija drugog reda po y u točki T(9,5)
d2fdy2_T = d2fdy2.subs({x: 9, y: 5})

# Parcijalna derivacija drugog reda po xy u točki T(9,5)
d2fdxdy_T = d2fdxdy.subs({x: 9, y: 5})

print("{} {}".format("f(x,y) =", f))
print("\n")
print("{} {}".format("Parcijalna derivacija prvog reda po x:", dfdx))
print("\n")
print("{} {}".format("Parcijalna derivacija prvog reda po y:", dfdy))
print("\n")
print("{} {}".format("Parcijalna derivacija drugog reda po x:", d2fdx2))
print("\n")
print("{} {}".format("Parcijalna derivacija drugog reda po y:", d2fdy2))
print("\n")
print("{} {}".format("Parcijalna derivacija drugog reda po xy:", d2fdxdy))
print("\n")
print("{} {}".format("Parcijalna derivacija po x u točki T(9,5):", dfdx_T))
print("{} {}".format("Parcijalna derivacija po y u točki T(9,5):", dfdy_T))
print("{} {}".format("Parcijalna derivacija drugog reda po x u točki T(9,5):",
                     d2fdx2_T))
print("{} {}".format("Parcijalna derivacija drugog reda po y u točki T(9,5):",
                     d2fdy2_T))
print("{} {}".format("Parcijalna derivacija drugog reda po xy u točki T(9,5):",
                     d2fdxdy_T))

# prikazivanje funkcije u trodimenzionalnom prostoru
funkcija = "Funkcija: " + str(f) # određivanje naslova kao string
plot3d(f, title=funkcija)

# prikazivanje prve derivacije po x u trodimenzionalnom prostoru
derivacija_x = "Derivacija prvog reda po x:\n" + str(dfdx)
plot3d(dfdx, title=derivacija_x)

# prikazivanje prve derivacije po y u trodimenzionalnom prostoru
derivacija_y = "Derivacija prvog reda po y:\n" + str(dfdy)
plot3d(dfdy, title=derivacija_y)
