def gensquares(N):
    for i in range(1, N + 1):
        yield i ** 2

N = int(input())

squares = gensquares(N)

print(f"Squares till to {N}:", end = " ")
for square in squares:
    print(square, end = " ")

