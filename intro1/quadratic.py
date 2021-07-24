def quadratic(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return None
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        return x1, x2


print(quadratic(2, 6, 4))
