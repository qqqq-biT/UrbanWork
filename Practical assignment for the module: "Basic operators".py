def generate_password(n):
    result = ""

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += str(i) + str(j)

    return result

n = 9
password = generate_password(n)
print(f"Пароль для {n}: {password}")
