import random
 
def partition(vector, left, right, pivotIndex):
    pivotvalue=vector[pivotIndex]
    vector[right],vector[pivotIndex]=vector[pivotIndex],vector[right]
    storedindex=left
    for i in range(left,right):
        if vector[i]<pivotvalue:
            vector[i],vector[storedindex]=vector[storedindex],vector[i]
            storedindex+=1
    vector[right],vector[storedindex]=vector[storedindex],vector[right]
    return storedindex
 
def _select(vector, left, right, k):
    "Returns the k-th smallest, (k >= 0), element of vector within vector[left:right+1] inclusive."
    while True:
        pivotIndex = random.randint(left, right)     # select pivotIndex between left and right
        pivotNewIndex = partition(vector, left, right, pivotIndex)
        pivotDist = pivotNewIndex - left
        if pivotDist == k:
            return vector[pivotNewIndex]
        elif k < pivotDist:
            right = pivotNewIndex - 1
        else:
            k -= pivotDist + 1
            left = pivotNewIndex + 1
 
def select(vector, k, left=None, right=None):
    """
    Returns the k-th smallest, (k >= 0), element of vector within vector[left:right+1].
    left, right default to (0, len(vector) - 1) if omitted
    """
    if left is None:
        left = 0
    lv1 = len(vector) - 1
    if right is None:
        right = lv1
    
    return _select(vector, left, right, k)
 
if __name__ == '__main__':
    v = [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
    print([select(v, i) for i in range(10)])