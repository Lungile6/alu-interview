Here’s a simple `README.md` file for your Pascal's triangle implementation:

```markdown
# Pascal's Triangle

This Python program generates Pascal's triangle up to a specified number of rows.

## Function

### `pascal_triangle(n)`

- **Description:** Returns a list of lists representing Pascal's triangle with `n` rows.
- **Parameters:**
  - `n` (int): The number of rows in the triangle. Must be a non-negative integer.
- **Returns:**
  - A list of lists containing integers representing Pascal's triangle.
  - Returns an empty list if `n <= 0`.

## Example

To generate Pascal's triangle with 5 rows, you can use the following code:

```python
from your_module import pascal_triangle

triangle = pascal_triangle(5)
for row in triangle:
    print(row)
```

### Output

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## Usage

1. Clone the repository or download the code file.
2. Import the `pascal_triangle` function in your Python script.
3. Call the function with the desired number of rows.

## License

This project is licensed under the MIT License.
```

### Instructions:
- Replace `your_module` with the actual name of the Python file where the `pascal_triangle` function is defined.
- Feel free to modify the content as needed!