board = [[' ' for _ in range(15)] for _ in range(15)]

for row in board:
    print(" | ".join(row))
    print("-" * 56)
