from typing import List


def stringSequence(self, target: str) -> List[str]:
    result = {}
    current = ""

    # Process each character in target
    for i in range(len(target)):
        # Press key 1 first to append ">"
        current += ">"
        # Keep pressing key 2 until we get the desired character
        while current[-1] != target[i]:
            # Replace last character with next alphabet
            if current[-1] == ">":
                current = current[:-1] + "a"
            else:
                current = current[:-1] + chr(ord(current[-1]) + 1)
            result[current] = 0

        result[current] = 0

    return list(result.keys())