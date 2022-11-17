def solution(area):
    squares = []
    while area > 0:
        max_square = int(area ** 0.5) ** 2
        squares.append(max_square)
        area -= max_square
    return squares


print(solution(15324))