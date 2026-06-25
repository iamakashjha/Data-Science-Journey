## Reflection Questions
### 1. What is a dot product?
The dot product is a mathematical operation that multiplies two vectors and produces a single number (scalar).

### 2. What does a large value mean?
A large positive dot product means the two vectors point in similar directions.

Large positive value → very similar directions.

Zero → vectors are perpendicular (unrelated).

Negative value → vectors point in opposite directions.

For example:

(1, 1) · (2, 2) = 4 → highly similar.

(1, 0) · (0, 1) = 0 → unrelated.

(1, 1) · (−1, −1) = −2 → opposite directions.

### 3. Why does the dot product measure similarity?
The geometric formula of the dot product is:

```
A⋅B = ∣A∣*∣B∣*cos(θ)
```

where:

∣A∣ = magnitude of A  
∣B∣ = magnitude of B  
θ = angle between the vectors

The value depends on the angle between the vectors:

θ = 0° → cos(0°) = 1 → maximum similarity.  
θ = 90° → cos(90°) = 0 → no similarity.  
θ = 180° → cos(180°) = −1 → opposite.

This is why vectors pointing in the same direction have a larger dot product.

### 4. Where is it used in AI?
The dot product is one of the most important operations in AI and Machine Learning.

**a) Similarity Search**

Embeddings from text or images are compared using dot products.

Example:

- "cat" embedding
- "kitten" embedding

Their vectors have a high dot product, meaning they are semantically similar.

**b) Recommendation Systems**

Netflix, YouTube, and Amazon compare user vectors and item vectors.

Higher dot product → higher recommendation score.

**c) Neural Networks**

Each neuron computes:
```
z = W⋅X+b
```
where:

W = weights  
X = inputs

The dot product combines inputs and weights.

**d) Transformers and LLMs**

Models like GPT use:

- Query vectors
- Key vectors

Their dot products determine attention scores.


### 5. How is it different from vector addition?

**Vector Addition** ----------------------

Adds two vectors
Produces another vector
Changes position or direction	
Example: (1,2)+(3,4)=(4,6)	

**Dot Product**
- Multiplies corresponding values
- Produces a scalar (number)
- Measures alignment/similarity
- Example: (1,2)·(3,4)=11

Example:
```
Let:

A = (1, 2)
B = (3, 4)
```
**Vector Addition:**
```
A+B=(4,6)
```
**Dot Product:**
```
A⋅B=(1×3)+(2×4)=11
```
So:

- Vector addition gives a new vector.  
- Dot product gives a measure of similarity or alignment.