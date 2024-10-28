def bubble_sort(arr):
    """
    Сортира масив използвайки bubble sort алгоритъм
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Сравняваме съседни елементи
            if arr[j] > arr[j + 1]:
                # Разменяме елементите ако са в грешен ред
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    """
    Сортира масив използвайки quick sort алгоритъм
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Примери за използване
def main():
    # Тестов масив
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    # Използване на bubble sort
    bubble_sorted = bubble_sort(numbers.copy())
    print("Bubble sort резултат:", bubble_sorted)
    
    # Използване на quick sort
    quick_sorted = quick_sort(numbers.copy())
    print("Quick sort резултат:", quick_sorted)
    
    # Тестване с различни типове данни
    # Числа с плаваща запетая
    float_numbers = [3.14, 1.41, 2.71, 0.58]
    print("Сортирани дробни числа:", quick_sort(float_numbers))
    
    # Думи
    words = ["ябълка", "банан", "круша", "ананас"]
    print("Сортирани думи:", quick_sort(words))

if __name__ == "__main__":
    main()