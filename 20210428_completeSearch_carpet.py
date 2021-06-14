def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for width in range(3, int(total // 3) + 1):
        if total % width == 0:
            if (total // width + width) * 2 - 4 == brown:
                if total // width >= width:
                      return [total // width, width]