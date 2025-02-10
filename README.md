#KALAI ARASI JAYAKUMAR
# Sequence Comparator

## Program Design

The Sequence Comparator is a Python script designed to compare two input sequences (strings) using various metrics, including normalized edit distance and longest common subsequence (LCS). The program is structured into a single Python class, `SequenceComparator`, which encapsulates the functionalities for calculating metrics and comparing sequences. Additionally, there is a `main` function for user interaction and running comparisons.

## Files

- `sequence_comparator.py`: The main Python script containing the `SequenceComparator` class and the `main` function for user interaction.
- `README.md`: This file, providing information about the program, its usage, and other details.

## Compiler Used

The program is written in Python and can be executed using any Python interpreter, such as CPython or Anaconda Python.

## Program Evaluation

### Works Well
- **Efficiency**: The program utilizes dynamic programming techniques to efficiently calculate metrics such as normalized edit distance and longest common subsequence.
- **User Interaction**: The `main` function provides a user-friendly interface for inputting sequences and viewing comparison results.
- **Modularity**: The program is well-structured into functions and a class, facilitating readability, maintainability, and potential future enhancements.

### Areas for Improvement
- **Error Handling**: Currently, the program does not include robust error handling mechanisms to handle invalid inputs or edge cases.
- **Optimization**: While the program is efficient for small to moderate-sized inputs, further optimization could be explored for very large sequences.
- **Documentation**: While the code includes inline comments, additional documentation, such as docstrings and more detailed explanations, could improve clarity and understanding.

## Data Structure Design

The program employs dynamic programming matrices to store intermediate results for calculating metrics. Specifically, it utilizes a 2D array to represent the dynamic programming table for computing the longest common subsequence (LCS) and the normalized edit distance between two sequences. Additionally, it utilizes arrays to store previous and current rows for optimal memory usage in the LCS algorithm.

"# sequence_-comparator" 
