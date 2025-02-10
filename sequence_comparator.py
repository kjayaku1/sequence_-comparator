# Author: KALAI ARASI

class SequenceComparator:
    def __init__(self, str1, str2):
        """
        Initialize the StringComparator class with two input strings.
        """
        self.string1 = str1
        self.string2 = str2

    def get_normalized_edit_distance(self):
    
        """
        Calculate the normalized edit distance between the two input strings.
        
        Returns:
            float: Normalized edit distance between the two input strings.
        """
        # Determine the lengths of the input strings
        len1, len2 = len(self.string1), len(self.string2)
        
        # Swap the strings if the first string is shorter to reduce space usage
        if len1 < len2:
            self.string1, self.string2 = self.string2, self.string1
            len1, len2 = len2, len1

        # Initialize the previous and current rows of the dynamic programming matrix
        prev_row = list(range(len2 + 1))
        current_row = [0] * (len2 + 1)

        # Iterate over each character of the first string
        for i in range(1, len1 + 1):
            # Initialize the current row with the appropriate index
            current_row[0] = i
            
            # Iterate over each character of the second string
            for j in range(1, len2 + 1):
                # If the characters at the current positions are equal
                if self.string1[i - 1] == self.string2[j - 1]:
                    # Set the current cell to the diagonal cell value
                    current_row[j] = prev_row[j - 1]
                else:
                    # Set the current cell to the minimum of adjacent cell values plus 1
                    current_row[j] = min(prev_row[j], current_row[j - 1]) + 1
            
            # Update the previous and current rows for the next iteration
            prev_row, current_row = current_row, prev_row

        # Calculate the normalized edit distance
        normalized_distance = (len1 + len2 - prev_row[len2]) / (len1 + len2) if (len1 + len2) != 0 else 0
        return normalized_distance


    def get_longest_common_subsequence(self):
        """
        Find the longest common subsequence between the two input strings.

        Returns:
            str: The longest common subsequence.
        """
        len1, len2 = len(self.string1), len(self.string2)
        
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        # Populate the dynamic programming matrix
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if self.string1[i - 1] == self.string2[j - 1]:
                    # If characters match, increment LCS length
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Otherwise, take the maximum of LCS lengths without the current characters
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Reconstruct the LCS from the dynamic programming matrix
        lcs = []
        x, y = len1, len2
        while x > 0 and y > 0:
            if self.string1[x - 1] == self.string2[y - 1]:
                # If characters match, append to LCS
                lcs.append(self.string1[x - 1])
                x -= 1
                y -= 1
            elif dp[x - 1][y] > dp[x][y - 1]:
                # Move to the cell with the larger LCS length
                x -= 1
            else:
                y -= 1
        
        # Reverse the LCS to get the correct order
        lcs.reverse()

        # Return the LCS as a string
        return ''.join(lcs)


    def lcs_using_linear_memory(self):
        """
        Find the longest common subsequence using linear memory.

        Returns:
            str: The longest common subsequence.
        """
        # Determine the lengths of the input strings
        len1, len2 = len(self.string1), len(self.string2)
        
        # Initialize previous and current arrays to store lengths of LCSs
        prev = [0] * (len2 + 1)
        current = [0] * (len2 + 1)
        
        # Initialize an empty list to store the LCS characters
        lcs = []

        # Iterate over the characters of the first string
        for i in range(1, len1 + 1):
            # Iterate over the characters of the second string
            for j in range(1, len2 + 1):
                if self.string1[i - 1] == self.string2[j - 1]:
                    # If characters match, increment LCS length
                    current[j] = prev[j - 1] + 1
                else:
                    # Otherwise, take the maximum of the previous LCS lengths
                    current[j] = max(prev[j], current[j - 1])

            # Check if it's the end of the first string or the character is different from the previous one
            if i == len1 or self.string1[i] != self.string1[i - 1]:
                # Find the maximum LCS length in the current row
                max_length = max(current)
                # Find the index of the maximum LCS length
                idx = current.index(max_length)
                if max_length > len(lcs):
                    # Append the corresponding character from the second string to the LCS list
                    lcs.append(self.string2[idx - 1])

            # Update previous and current arrays for the next iteration
            prev, current = current, [0] * (len2 + 1)

        # Join the characters of the LCS list to form a string
        return ''.join(lcs)

    def calculate_metrics_and_lcs(self):
        """
        Calculate normalized edit distance and longest common subsequence.
        """
        lcs_string = self.get_longest_common_subsequence()
        normalized_distance = self.get_normalized_edit_distance()
        lcs_length_linear_memory = self.lcs_using_linear_memory()
        return normalized_distance, lcs_string, lcs_length_linear_memory

    def run_comparison(self):
        """
        Run comparison and print results.
        """
        normalized_distance = self.get_normalized_edit_distance()
        lcs_string = self.get_longest_common_subsequence()
        lcs_string_linear_memory = self.lcs_using_linear_memory()

        print(f"The Normalized Edit Distance is: {normalized_distance:.4f}")
        print(f"Longest common subsequence: {lcs_string}")
        print(f"LCS using linear memory: {lcs_string_linear_memory}")


def main():
    """
    Main function to input strings and run comparisons.
    """
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    comparator = SequenceComparator(str1, str2)
    comparator.run_comparison()


if __name__ == "__main__":
    main()
