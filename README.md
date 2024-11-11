
# Matrix Processing Specification Lab

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-blue.svg)](https://github.com/psf/black)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Discord](https://img.shields.io/discord/872320492936257537?logo=discord)](https://discord.gg/kjah8MFYbR)

## Introduction

This project invites you to implement a `matrix` program that processes a
two-dimensional "list of lists" called a matrix. The program will report
how many negative numbers are stored in the matrix. For this project, use
VS Code instead of Sublime Text.

## Learning Objectives

The learning objectives of this assignment are to:

1. Use Git and GitHub to manage source code file changes
2. Use VS Code
3. Check files, read files
4. Index into lists
5. Use data structure of nested lists
6. Write clearly about the programming concepts in this assignment.

## Quick Links

- Due date: Check Discord or the
  [Course Materials Schedule](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials/blob/main/Schedule.md)
- Policy on
  [Tokens](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#tokens)
- [Token Form for Automatic Extension](https://forms.gle/y9Mz55hQKr84wzvXA)
- Policy for
  [Assignment Evaluation](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#assignment-evaluation)
- Policy for [Assignment Submission](https://github.com/allegheny-college-cmpsc-101-fall-2024/course-materials#assignment-submission).
- [#data-structures Discord channel](https://discord.com/channels/877320365825749002/1274744318124359732)
- [Starter repo](https://github.com/allegheny-college-cmpsc-101-fall-2024/matrix-starter)

## Policy Reminders

Students are reminded to uphold the Honor Code. Cloning this assignment
repository is a commitment to the latter.

For this assignment, you may use class materials, the textbook, notes,
and the internet, including AI, for reference and learning. AI may **not** be
used to generate answers that you submit. All code and writing that are turned
in **must be your own work and your own words**. Copying or otherwise
representing ChatGTP or other AI outputs as your own work or your own words is
not permitted.

Please ask questions freely in Lab, on the #data-structures Discord channel,
TL office hours, instructor office hours, or by opening a GitHub Issue with
@emgraber tagged at least 24 hours before the deadline.

Modifications to the gatorgrade.yml file are not permitted without explicit
instruction.

## Project Goals ([Project Overview](#project-overview) Below)

This project invites you to implement a `matrix` program that processes a
two-dimensional "list of lists" called a matrix. The main feature of the program
is that it can count the number of negative numbers inside of a matrix that it
inputs from a file specified on its command-line. In addition to implementing
part of the command-line interface for `matrix` you will add source code that
traverses the input matrix and counts the negative numbers. Instead of using
Sublime Text, you will explore the Integrated Development Environment VS Code.

## Expected Output

As previously mentioned, this project invites you to implement a matrix
processing program program called `matrix`. The program accepts through its
command-line interface a `matrix-file` parameter that designates a file with a
matrix inside of it and the `matrix-dir` that is the directory containing the
specified file. For this project, you should use the `matrix.txt` file inside of
the `input` directory that contains these contents:

```text
100,19,9,9
10,9,8,7
6,4,2,-1
4,2,0,-1
3,0,-1,-2
-1,-1,-2,-5
```

After correctly adding all of the required features, you can use Poetry to run
the program with the command `poetry run matrix --matrix-dir input --matrix-file
matrix.txt` and see that it it produces the following output:

```text
✨ Searching for negative numbers in a matrix stored in input/matrix.txt!

📦 The matrix contains the following integer values:

---  --  --  --
100  19   9   9
 10   9   8   7
  6   4   2  -1
  4   2   0  -1
  3   0  -1  -2
 -1  -1  -2  -5
---  --  --  --

🧮 The matrix contains 8 negative numbers!
```

To learn more about how to run this program, you can type the command `poetry
run matrix --help` to see the following output showing how to use `matrix`:

```text
╭─ Options ─────────────────────────────────────────────────────────────╮
│ --matrix-dir                PATH                 [default: None]      │
│ --matrix-file               PATH                 [default: None]      │
│ --install-completion        [bash|zsh|fish|powe  Install completion   │
│                             rshell|pwsh]         for the specified    │
│                                                  shell.               │
│                                                  [default: None]      │
│ --show-completion           [bash|zsh|fish|powe  Show completion for  │
│                             rshell|pwsh]         the specified shell, │
│                                                  to copy it or        │
│                                                  customize the        │
│                                                  installation.        │
│                                                  [default: None]      │
│ --help                                           Show this message    │
│                                                  and exit.            │
╰───────────────────────────────────────────────────────────────────────╯
```

Please note that the provided source code does not contain all of the
functionality to produce this output. As explained in the next section, you are
invited to add the missing features and ensure that `matrix` produces the
expected output. Once the program is working correctly, it should produce output
similar to that shown in this section.

Don't forget that if you want to run the `matrix` program you must use
your terminal to first go into the GitHub repository containing this project
and then go into the `matrix` directory that houses the project's code.
Finally, remember that before running the program you must run `poetry
install` to add the dependencies.

## Adding Functionality

If you study the file `matrix/matrix/main.py` you will see that it has many
`TODO` markers that designate the parts of the program that you need to
implement before `matrix` will produce correct output. Specifically, you should
implement these functions in `matrix`:

- `def confirm_valid_file(file: Path) -> bool`
- `def count_negatives_in_matrix(matrix: List[List[int]]) -> int`
- `def matrix(matrix_dir: Path = typer.Option(None), matrix_file: Path = typer.Option(None)) -> None`

Once you have correctly resolved all of the `TODO` markers in the `matrix`
program, it should produce the expected output described in the previous
section. The most important function you need to implement for this project is
`count_negatives_in_matrix`, which has a signature indicating that it accepts as
input a `List` of `List`s that contain `int` values (i.e., `List[List[int]]`)
and returns as output an `int` for the number of negative numbers in the file.
You may assume that the `matrix` parameter that is input to the
`confirm_valid_file` function is organized such that each row and column of the
`matrix` is sorted in a non-increasing order.

The following excerpt of output created by a correct implementation of `matrix`,
which was produced through the use of the
[python-tabulate](https://github.com/astanin/python-tabulate) package,
illustrates the organization of the input matrix. For instance, note that the
first column of the matrix contains the values `100, 10, 6, 4, 3, -1` which are
organized in a non-increasing manner from the top to the bottom of the matrix.
It is also worth noting that all of the other column in the matrix are also
organized in the same non-increasing fashion. Moreover, the third-from-the-top
row of the matrix contains the values `6, 4, 2, -1` while the last row contains
`-1, -1, -2, -5` which are also organized in a non-increasing style.

```text
---  --  --  --
100  19   9   9
 10   9   8   7
  6   4   2  -1
  4   2   0  -1
  3   0  -1  -2
 -1  -1  -2  -5
---  --  --  --
```

## Running Checks

### Gatorgrade

After you have added functionality and checked that your code produces the
expected output, the command `gatorgrade --config config/gatorgrade.yml`
will check your work with the automatic grader. If
your work meets the baseline requirements and adheres to the best practices that
proactive programmers adopt you will see that all the checks pass when you run
`gatorgrade`. All checks must pass in order to get 100% on this lab. All other
gatorgrade score are graded as 0%. Note, modifications to the gatorgrade.yml file
are not permitted without explicit instruction.

### Helper Tasks

Helper tasks are run in the terminal with the poetry environment activated.
The format of the commands are always `poetry run task xyz`...where `xyz`
is the helper task name.

If you study the source code in the `pyproject.toml` file you will see that it
includes the following section that specifies different executable "helper
task" names like `ruff`, `fix`, `ruffdetails`, etc.

```toml
[tool.taskipy.tasks]
```

If you are in the `matrix` directory that contains the
`pyproject.toml` file, the helper tasks
make it easy to run commands like `poetry run task ruff` to automatically run
the ruff linter designed to check the Python source code in your program
to confirm that your source code adheres to industry standards for formatting.
You can also use the command `poetry run task fix` to automatically reformat the
source code. `poetry run task ruffdetails` will print out detailed linting errors
that point to exactly what ruff views as a linting error. Make sure to examine
the `pyproject.toml` file for other convenient tasks that you can use to both
check and improve your project!

If your program has
all of the anticipated functionality, you can run the command `poetry run task
test` and see that the test suite produces output like the following.

```shell
collected 3 items

tests/test_matrix.py ....
```

Don't forget that when you commit source code or technical writing to your
GitHub repository for this project, it will trigger the run of a GitHub
Actions workflow. If you are a student at Allegheny College, then running
this workflow consumes build minutes for the course's organization! As
such, you should only commit to your repository once you have made
substantive changes to your project and you are ready to confirm its
correctness. Before you commit to your GitHub repository, you can still run
checks on your own computer by using Poetry and GatorGrader. You can also
add and commit work locally before pushing it by using git commands in the
terminal: `git add .` and `git commit -m "Commit Message"`.

## Project Reflection

Once you have finished all of the previous technical tasks, you can use a text
editor to answer all of the questions in the `writing/reflection.md` file. For
instance, you should provide the output of the Python program in a fenced code
block, explain the meaning of the Python source code segments that you
implemented and tested, compare and contrast the performance of different
implementations of the square root calculation, and answer all of the other
questions about your experiences in completing this project.

## Project Assessment

You may make an unlimited number of reattempts at submitting
source code and technical writing that meet all aspects of the project's
specification. This spec lab is graded pass/fail. Gatorgrade reports of 100%
meeting all the spec receive a grade of 100%. All other gatorgrade reports
result in a grade of 0%.

## Project Overview

After cloning this repository to your computer, please take the following
steps:

- Use the `cd` command to change into the directory for this repository.
- Specifically, you can change into the program directory by typing `cd matrix`.
- Install the dependencies for the project by typing `poetry install`.
- Run the program to perform matrix processing by typing the following command:
  - `poetry run matrix --matrix-dir input --matrix-file matrix.txt`
  - Please note that the program will not work unless you add the required source code
  - Please refer to the `writing/reflection.md` file for all of the ways to run the program
- Please note that the program will not work unless you add the required
  source code at the designated `TODO` markers.
- Confirm that the program is producing the expected output described
  [above](#expected-output)
- Please make sure that you completely delete the `TODO` markers and their
  labels from all of the provided source code.
- Please make sure that you also completely delete the `TODO` markers and their
  labels from every line of the `writing/reflection.md` file.
- Don't forget to provide all of the required responses to the technical writing
  prompts in the `writing/reflection.md` file.
- Run the automated grading checks by typing
  `gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Submit work to GitHub using git in the terminal
  - Open a terminal
  - `cd` to the project directory on your computer
  - type `git status` to see a list of files you have updated
  - type `git add .` to "stage" your files
  - type `git commit -m "PUT YOUR OWN SHORT MESSAGE"`
  - type `git push origin main`
  - type your ssh passphrase if requested
