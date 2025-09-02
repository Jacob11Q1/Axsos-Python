# Insertion (Optional):

def insertion_sort(arr):
    for i in range(1 , len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
            
            arr[j + 1] = current
    return arr

numbers = [50,98,14,22,11]
sorted_numbers = insertion_sort(numbers)
print(sorted_numbers)