#我是林珈生


def BinarySearch(data, left, right, tar):
    global count
    count = count +1
    if left > right:
        print(f"There are no data '{tar}', find {count} times. ")
        return
    middle = int((right + left) / 2)
    if data[middle] > tar:
        return BinarySearch(data, left, middle-1, tar)

    if data[middle] < tar:
        return BinarySearch(data, middle+1, right, tar)

    else:
        print(f"Find data '{tar}' in index {middle}, find {count} times.")
        return

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lon = len(data)
count = 0
tar = int(input("Enter target> "))
BinarySearch(data, 0, lon-1, tar)

    
