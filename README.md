# Python Coding Assessment

The goal of the assessment is to allow you to demonstrate basic coding knowledge using modern Python 3. The version of Python used to perform and test the assertion checks was 3.11.5. Your system installation of Python should be at least version 3.10.

You are free to use the code editor of your choice to implement your solution to the coding exercises. PyCharm is popular and is slightly easier to use than other IDEs. VS Code is also another popular option. Please attempt the assessment on your own without using human or AI assistance. Internet search engines are fine otherwise.

The assessment is divided into two sections:

1. Functions
2. Data Exploration

There are two folders, <code>functions</code> and <code>data_exploration</code> in the project root folder corresponding to the two sections described earlier.

## Functions

There are four Python files in the <code>functions</code> folder, two module files <code>count_vowels.py</code> and <code>reverse_string.py</code> and their corresponding unit test files, <code>test_count_vowels.py</code> and <code>test_reverse_string.py</code>.

### Count Vowels

The file <code>count_vowels.py</code> contains a function stub shown below:

```py
def count_vowels(string: str) -> dict[str, int]:
    # Replace the next line with your implemention
    raise NotImplementedError()
```

Implement the function using the sample input/output hint.

| **Input**        | **Output**                                 |
| ---------------- | ------------------------------------------ |
| `"education"`    | `{"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}` |
| `"able does it"` | `{"a": 1, "e": 2, "i": 1, "o": 1, "u": 0}` |
| `""`             | `{"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}` |

Test your solution by running the unit test <code>test_count_vowels.py</code> from your IDE or the command line.

### Reverse String

The file <code>reverse_string.py</code> contains a function stub shown below:

```py
def reverse_string(string: str) -> str:
    # Replace the next line with your implemention
    raise NotImplementedError()
```

Implement the function using the sample input/output hint.

**Sample Input and Output**

| **Input**   | **Output**  |
| ----------- | ----------- |
| `"madam"`   | `"madam"`   |
| `""`        | `""`        |
| `"123.456"` | `"654.321"` |

Test your solution by running the unit test <code>test_reverse_string.py</code> from your IDE or the command line.

## Data Exploration

There are three files in the <code>data_exploration</code> folder, <code>students.py</code> with its corresponding unit test file <code>test_students.py</code> and a CSV file <code>students.csv</code>.

There is a function stub shown below for you to implement.

```py
def get_students_by_female_with_score_greater_than_90(
    students: pd.DataFrame,
) -> pd.DataFrame:
    # Replace the next line with your implemention
    raise NotImplementedError()
```

Run the <code>test_students.py</code> from your IDE or the command line.
