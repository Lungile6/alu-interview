# Minimum Operations

This project calculates the minimum number of operations needed to produce exactly `n` characters 'H' in a text file using only two operations: **Copy All** and **Paste**.

## Problem Description

Given a single character 'H' in a text file, you can perform the following operations:

1. **Copy All**: Copies all currently displayed characters to the clipboard.
2. **Paste**: Pastes the contents of the clipboard to the file.

Your task is to implement a function that computes the fewest number of operations needed to achieve exactly `n` 'H' characters.

## Function Prototype

```python
def minOperations(n: int) -> int:
```

### Parameters

- **n** (int): The target number of 'H' characters you want to achieve.

### Returns

- (int): The minimum number of operations needed to reach exactly `n` characters. If it's impossible to achieve, return `0`.

## Example

For `n = 9`:

```
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
```

**Number of operations: 6**

## Implementation

Here is an example implementation of the `minOperations` function:

```python
def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
```

## Test Cases

You can test the function with the following script:

```python
if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

### Expected Output

```
Min # of operations to reach 4 characters: 4
Min # of operations to reach 12 characters: 7
```

## Usage

To use this function, simply call `minOperations(n)` with your desired number of characters `n`. It will return the minimum number of operations required.

## Notes

- The function efficiently computes the result using a greedy approach by continuously dividing `n` by its smallest factors.
- For any `n` that cannot be achieved through the defined operations, the function will return `0`.
