import math

a = -1
b = 1
p = 751

nb = 54
cipher = [
    [[188, 93], [295, 219]],
    [[618, 206], [646, 706]],
    [[440, 539], [573, 583]],
    [[16, 416], [694, 581]],
    [[179, 275], [585, 540]],
    [[377, 456], [701, 570]],
    [[618, 206], [67, 667]],
    [[286, 136], [36, 664]],
    [[72, 254], [727, 65]],
    [[568, 355], [438, 40]]
]


def euler_function(n: int) -> int:
    if n == 1:
        return 1
    result = 0
    for i in range(n):
        if math.gcd(i, n) == 1:
            result += 1
    return result


def inverse_mod(x: int, mod: int) -> int:
    if math.gcd(x, mod) != 1:
        raise ValueError("Negative modular value doesn't exists")
    phi = euler_function(mod) - 1
    result = pow(x, phi, mod)
    return result


def div_mod(x: int, y: int, mod: int) -> int:
    x %= mod
    y %= mod
    if x % y == 0:
        return (x // y) % mod
    y = inverse_mod(y, mod)
    result = (x * y) % mod
    return result


def add_mod(x1: int, y1: int, x2: int, y2: int, mod: int) -> list[int]:
    l: int
    if x1 == x2:
        l = div_mod(3 * x1 * x1 + a, 2 * y1, mod)
    else:
        l = div_mod(y2 - y1, x2 - x1, mod)
    x3: int = (l * l - x1 - x2) % mod
    y3: int = (l * (x1 - x3) - y1) % mod
    return [x3, y3]


def times_mod(x: int, y: int, scalar: int, mod: int) -> list[int]:
    if scalar < 0:
        y = -y
        scalar = -scalar
    result = [x, y]
    for i in range(scalar - 1):
        result = add_mod(x, y, *result, mod)
    return result


if __name__ == '__main__':
    for idx in range(len(cipher)):
        tmp = times_mod(*cipher[idx][0], -nb, p)
        text = add_mod(*cipher[idx][1], *tmp, p)
        print(text)
