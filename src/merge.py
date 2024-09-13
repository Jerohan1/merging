"""Code for merging two sorted lists."""


def merge(x: list[int], y: list[int]) -> list[int]:
    """
    Merge two sorted lists.

    Returns a list that contains all the elements in x and y
    in sorted order.

    >>> merge([1, 2, 4, 6], [1, 3, 4, 5])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    i, j = 0, 0
    z = []
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
            
        if i == len(x):
            z.extend(y[j:])
            return z
        elif j == len(y): 
            z.extend(x[i:])
            return z
    if i == 0:
        return x
    elif j == 0:
        return y

print(merge([1, 2, 4, 6], []))