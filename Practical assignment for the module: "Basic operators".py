from main import find_password


def dinf_password(n):
    result = ""

    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += f"{i}{j}"

    return result

n = 3
password = find_password(n)
print(f"Это ваш пароль {n} - {password}")
