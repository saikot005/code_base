"""
Array Rotation Program
Different approaches to rotate an array
"""

from collections import deque


# Approach 1: Using Python Slicing (Simple and Pythonic)
def rotate_left_slicing(arr, k):
    """
    Rotate array left by k positions using slicing
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    k = k % len(arr)  # Handle k > len(arr)
    return arr[k:] + arr[:k]


def rotate_right_slicing(arr, k):
    """
    Rotate array right by k positions using slicing
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    k = k % len(arr)  # Handle k > len(arr)
    return arr[-k:] + arr[:-k] if k != 0 else arr


# Approach 2: Using Reversal (Space efficient)
def rotate_left_reversal(arr, k):
    """
    Rotate array left by k positions using reversal
    Time Complexity: O(n)
    Space Complexity: O(1) - in-place
    """
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    k = k % len(arr)
    reverse(arr, 0, k - 1)
    reverse(arr, k, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)
    return arr


# Approach 3: Using collections.deque
def rotate_using_deque(arr, k):
    """
    Rotate array using collections.deque
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    d = deque(arr)
    d.rotate(k)  # Positive k = right rotation, negative k = left rotation
    return list(d)


# Approach 4: Manual in-place rotation
def rotate_right_manual(arr, k):
    """
    Rotate array right by k positions (in-place)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)
    k = k % n
    
    for _ in range(k):
        last = arr[-1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last
    
    return arr


# Main Program with Examples
if __name__ == "__main__":
    print("=" * 60)
    print("ARRAY ROTATION PROGRAM")
    print("=" * 60)
    
    # Test array
    original_array = [1, 2, 3, 4, 5]
    k = 2
    
    print(f"\nOriginal Array: {original_array}")
    print(f"Rotation Count (k): {k}\n")
    
    # Example 1: Left rotation using slicing
    print("1. Left Rotation using Slicing:")
    result1 = rotate_left_slicing(original_array.copy(), k)
    print(f"   Result: {result1}")
    print(f"   Explanation: Moved {k} elements from start to end\n")
    
    # Example 2: Right rotation using slicing
    print("2. Right Rotation using Slicing:")
    result2 = rotate_right_slicing(original_array.copy(), k)
    print(f"   Result: {result2}")
    print(f"   Explanation: Moved {k} elements from end to start\n")
    
    # Example 3: Left rotation using reversal
    print("3. Left Rotation using Reversal (In-place):")
    arr_copy = original_array.copy()
    result3 = rotate_left_reversal(arr_copy, k)
    print(f"   Result: {result3}")
    print(f"   Explanation: Reversed sublists strategically\n")
    
    # Example 4: Rotation using deque
    print("4. Right Rotation using deque:")
    result4 = rotate_using_deque(original_array.copy(), k)
    print(f"   Result: {result4}")
    print(f"   Explanation: Used rotate() method from deque\n")
    
    # Example 5: Manual in-place rotation
    print("5. Right Rotation Manual (In-place):")
    arr_copy = original_array.copy()
    result5 = rotate_right_manual(arr_copy, k)
    print(f"   Result: {result5}")
    print(f"   Explanation: Shifted elements one by one\n")
    
    # Test with different values
    print("=" * 60)
    print("ADDITIONAL TESTS")
    print("=" * 60)
    
    test_cases = [
        ([1, 2, 3, 4, 5], 1),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 5),  # Full rotation
        ([1, 2, 3, 4, 5], 7),  # k > length
        ([10, 20, 30], 2),
    ]
    
    for arr, rotation in test_cases:
        left_result = rotate_left_slicing(arr, rotation)
        right_result = rotate_right_slicing(arr, rotation)
        print(f"\nArray: {arr}, k={rotation}")
        print(f"  Left Rotation:  {left_result}")
        print(f"  Right Rotation: {right_result}")
    
    print("\n" + "=" * 60)
    print("Program completed successfully!")
    print("=" * 60)
    