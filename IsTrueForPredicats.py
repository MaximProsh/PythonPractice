# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

if (not(0 or 0 or 0)) == (not 0 and not 0 and not 0):
    print("Equality '¬(0 ⋁ 0 ⋁ 0) = ¬0 ⋀ ¬0 ⋀ ¬0' is correctly")
else:
    print("Equality '¬(0 ⋁ 0 ⋁ 0) = ¬0 ⋀ ¬0 ⋀ ¬0' is wrong")

if (not(0 or 0 or 1)) == (not 0 and not 0 and not 1):
    print("Equality '¬(0 ⋁ 0 ⋁ 1) = ¬0 ⋀ ¬0 ⋀ ¬1' is correctly")
else:
    print("Equality '¬(0 ⋁ 0 ⋁ 1) = ¬0 ⋀ ¬0 ⋀ ¬1' is wrong")

if (not(0 or 1 or 0)) == (not 0 and not 1 and not 0):
    print("Equality '¬(0 ⋁ 1 ⋁ 0) = ¬0 ⋀ ¬1 ⋀ ¬0' is correctly")
else:
    print("Equality '¬(0 ⋁ 1 ⋁ 0) = ¬0 ⋀ ¬1 ⋀ ¬0' is wrong")

if (not(1 or 0 or 0)) == (not 1 and not 0 and not 0):
    print("Equality '¬(1 ⋁ 0 ⋁ 0) = ¬1 ⋀ ¬0 ⋀ ¬0' is correctly")
else:
    print("Equality '¬(1 ⋁ 0 ⋁ 0) = ¬1 ⋀ ¬0 ⋀ ¬0' is wrong")

if (not(1 or 0 or 1)) == (not 1 and not 0 and not 1):
    print("Equality '¬(1 ⋁ 0 ⋁ 1) = ¬1 ⋀ ¬0 ⋀ ¬1' is correctly")
else:
    print("Equality '¬(1 ⋁ 0 ⋁ 1) = ¬1 ⋀ ¬0 ⋀ ¬1' is wrong")

if (not(1 or 1 or 0)) == (not 1 and not 1 and not 0):
    print("Equality '¬(1 ⋁ 1 ⋁ 0) = ¬1 ⋀ ¬1 ⋀ ¬0' is correctly")
else:
    print("Equality '¬(1 ⋁ 1 ⋁ 0) = ¬1 ⋀ ¬1 ⋀ ¬0' is wrong")

if (not(1 or 1 or 1)) == (not 1 and not 1 and not 1):
    print("Equality '¬(1 ⋁ 1 ⋁ 1) = ¬1 ⋀ ¬1 ⋀ ¬1' is correctly")
else:
    print("Equality '¬(1 ⋁ 1 ⋁ 1) = ¬1 ⋀ ¬1 ⋀ ¬1' is wrong")

if (not(0 or 1 or 1)) == (not 0 and not 1 and not 1):
    print("Equality '¬(0 ⋁ 1 ⋁ 1) = ¬0 ⋀ ¬1 ⋀ ¬1' is correctly")
else:
    print("Equality '¬(0 ⋁ 1 ⋁ 1) = ¬0 ⋀ ¬1 ⋀ ¬1' is wrong")