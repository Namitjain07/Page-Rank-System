# Page Rank System
 This is a simplified implementation of a page rank system. The program reads a text file containing pages and their respective links, and calculates the overall importance of each page based on the initial importance and link distribution. The program then ranks the pages and outputs the top N pages.

## Input File Format
    The input file (pages.txt) should have lines of the following format:

```python
    URLnn, init_importance: text containing some URLnn
```

-`URLnn`: The URL of the page.
-`init_importance`: A number between 0 and 1.0 representing the initial importance of the page.
-`text containing some URLnn`: The text of the page, which may contain references (URLs) to other pages.

## Usage
    To run the program, ensure you have a file named `pages.txt` in the same directory as the script. Modify the script to specify the value of `N` (the number of top pages to display) if needed. Then, execute the script using a Python interpreter.

    python "Page Rank System.py"

## Example
    Given the input file `pages.txt`:
```python
URL00, 0.5: This is page zero, and has references to URL01, URL09, and also to URL08. It may have repeated references - so there are two references to URL09.
URL02, 0.6: This is another page (page is represented as a line in this). This has reference to URL05, URL04, and URL00
```

The program will calculate the overall importance of each page and display the top N pages based on their ranking.

...
## Implementation
    The implementation of this page rank system is available in the associated script file. Please refer to the code for detailed implementation details.

    Please make sure to have the pages.txt file in the same directory as the script before running it.