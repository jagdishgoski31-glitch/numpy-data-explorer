# Reproducible dataset generation
np.random.seed(42)
data = np.random.randint(50, 100, size=(5, 4))

# Indexing and slicing operations
print("First Row:", data[0])
print("First Column:", data[:, 0])
print("Sub-matrix:", data[:3, :2])

# Statistical analysis
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))

# Axis-wise computations
print("Column-wise Mean:", np.mean(data, axis=0))
print("Row-wise Sum:", np.sum(data, axis=1))

# Reshaping and normalization
reshaped_data = data.reshape(2, 10)
normalized_data = data / np.max(data)
