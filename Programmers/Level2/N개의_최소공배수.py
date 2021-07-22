def solution(arr):
    arr.sort()
    for i in range(len(arr)-1):
        x = arr[i+1]
        y = arr[i]

        # 유클리드 호제법
        while x % y != 0:
            x, y = y, x%y
        arr[i+1] = arr[i]*arr[i+1]//y

    return arr[-1]