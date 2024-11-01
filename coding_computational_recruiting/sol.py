import numpy as np

# Replace 'filename.txt' with your actual file path
data = np.genfromtxt('data.txt', delimiter=None, names=True, dtype=None, encoding='utf-8')

# Access as a dictionary-like structure (map)
data_map = {name: data[name] for name in data.dtype.names}

# Example of accessing one column by its title
print(data_map)  # R