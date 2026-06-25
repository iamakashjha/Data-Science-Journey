# Reflection Questions

### 1. What is matrix addition?

Matrix addition is the process of adding two matrices by adding their corresponding elements.


Matrix addition combines information from two matrices of the same size.

### 2. Why do dimensions matter?

Dimensions determine whether mathematical operations on matrices are possible.

For matrix addition, both matrices must have the same dimensions.
 - Example: 2×3+2×3 ✓
 - Example: 2×3+3×2 ✗

For matrix multiplication, the number of columns in the first matrix must equal the number of rows in the second matrix.
- Example: 2×3×3×4 ✓
- Example: 2×3×2×4 ✗

Dimensions ensure that rows and columns align correctly during calculations.

### 3. What does matrix multiplication do?

Matrix multiplication combines the information from two matrices to produce a new matrix.

Each element in the result is calculated by taking the **dot product of a row and a column.**

### 4. Why is matrix multiplication important in AI?

Matrix multiplication is one of the fundamental operations in AI and machine learning because it allows models to transform input data into useful outputs.

It is used in:

- Linear Regression to compute predictions.
- Neural Networks to calculate neuron activations.
- Computer Vision to process images.
- Natural Language Processing to transform word embeddings.
- Transformers and Large Language Models for attention calculations.

Most AI frameworks such as NumPy, TensorFlow, and PyTorch perform millions or billions of matrix multiplications during training and inference.

### 5. What does XW mean in machine learning?

In machine learning:

XW

represents the multiplication of the input matrix X with the weight matrix W.

- X = input features (data)
- W = learned weights (parameters)
- XW = transformed output or predictions

In neural networks, the basic computation is:
```
Z=XW+b
```
where:

X = input data  
W = weights learned during training  
b = bias  
Z = output before applying an activation function

This operation is the foundation of almost every machine learning model.