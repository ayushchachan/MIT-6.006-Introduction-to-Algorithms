# Document Distance (MIT 6.006)

The **Document Distance Problem** measures how similar two documents are.  
It has applications in:
- Finding duplicate or near-duplicate pages (e.g., Google, Wikipedia mirrors)
- Detecting plagiarism
- Information retrieval and search (query vs. document similarity)

---

## Problem Definition

- A **word** = sequence of alphanumeric characters (ignore punctuation/whitespace).
- A **document** = sequence of words.

We represent each document as a **vector of word frequencies**:


The similarity of two documents D1 and D2 is based on the **cosine similarity**:

\[
\cos(\theta) = \frac{D1 \cdot D2}{|D1| \times |D2|}
\]

- If θ = 0° → the documents are identical.
- If θ = 90° → no words in common.

The **document distance** is the angle θ between the two word-frequency vectors.

---

## Algorithm

1. **Tokenize**: split each document into words.
2. **Count frequencies**: build a dictionary of word → frequency.
3. **Compute dot product** of the two frequency dictionaries.
4. **Normalize** by magnitudes (vector lengths).
5. **Return angle** between vectors as the distance.

---

## Example Usage

```bash
# Run the program
python3 main.py tests/a.txt tests/b.txt
