# ZPRO

My coursework archive from **18ZPRO**, the introductory Python programming course at the Faculty of Nuclear Sciences and Physical Engineering (FJFI), Czech Technical University in Prague (ČVUT), 2025 run.

It contains the course's lesson notebooks with exercises I filled in, my submitted weekly assignments with their graded feedback, and a few small scripts I wrote while working through the material.

The course materials come from the [KSI group at FJFI ČVUT](https://gitlab.fjfi.cvut.cz/ksi) and are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). See [Credits and license](#credits-and-license).

## Contents

```text
ZPRO/
├── README.md
├── ZPRO-readme.md        # original course README (Czech): links and list of authors
├── LICENSE               # CC BY-SA 4.0
├── drunkenSailor.py      # random-walk simulation drawn with turtle
├── primeFinder.ipynb     # early trial-division prime finder
├── lessons/              # course lesson notebooks (Czech), 00–21
│   └── images/           # figures used by the notebooks
└── assignments/          # 11 graded assignments (English)
```

### Lessons

The lesson notebooks are in Czech. Topics in order:

| # | Topic |
|---|-------|
| 00 | Introductory lecture from the preparatory week (`00_PT.pdf`) |
| 01–04 | Basic concepts and the Python environment, number input, data types and nbgrader, the `complex` type |
| 05–06 | Conditions and loops |
| 07–09 | Functions and recursion |
| 10 | IDEs (VSCode / VSCodium), plus `10 Turtle.py` |
| 11–12 | Containers: sequences, sets and dictionaries |
| 13–14 | Strings: creation, `str` methods and formatting, plus `14 probabilistic_caesar_decipher.py` |
| 15–16 | Iterators and generators |
| 17–18 | Error handling and debugging, plus `erasthothenes-debug.py` |
| 19–20 | Files and directories |
| 21 | Basics of object-oriented programming |

Notebooks 20 and 21 were added unfinished.

### Assignments

Each assignment has an nbgrader notebook (`NN assignment.ipynb`) with the task and my solution, and an HTML export of the graded feedback (`NN assignment.html`).

| # | Task |
|---|------|
| 01 | Introduction to the assignment workflow |
| 02 | Time to sail around the Earth along the Tropic of Cancer |
| 03 | Collatz sequence |
| 04 | `sum_primes` with an optional parameter |
| 05 | Koch snowflake perimeter (recursion) |
| 06 | Weather data analysis on lists of tuples |
| 07 | Flight ticket analysis on lists of dictionaries |
| 08 | Czech licence plate (SPZ) validation |
| 09 | Parrot speech analysis |
| 10 | Input validation for geographic distance functions |
| 11 | Sorting Klementinum 2023 temperature records from files |

The `klementinum2023*.txt` and `kl_err*.txt` files are data for assignment 11, and `L0VEZPR0.png` is the image used in assignment 8.

## Setup

You need Python 3 and a Jupyter environment such as JupyterLab or Jupyter Notebook. Most code uses only the standard library. The exceptions:

- **`ipytest`** (which uses `pytest`) runs the test cells in assignments 04, 05, 06, 08 and 10.
- **`tkinter`** is needed by the turtle scripts (`drunkenSailor.py`, `lessons/10 Turtle.py`). Some Python builds don't include it.

```bash
git clone https://github.com/KotvicCodes/ZPRO.git
cd ZPRO
python3 -m venv .venv
source .venv/bin/activate
pip install jupyterlab ipytest
```

The notebooks were written for the course's JupyterHub with nbgrader. Some cells depend on course resources that are not included here:

- Assignments 01–03 import a `zprotests` module, and assignment 05 imports `test_recursion`. Neither module is in this repository, so their validation cells fail with `ModuleNotFoundError`.
- Lesson 19 reads and writes files in a `data/` directory that isn't included.

## Usage

Open the notebooks:

```bash
jupyter lab
```

Run the standalone scripts from the folder they're in, because the lesson filenames contain spaces:

```bash
# Caesar cipher breaker using letter frequencies; decodes the built-in sample texts
cd lessons
python3 "14 probabilistic_caesar_decipher.py"

# Prime sieve exercise from the debugging lesson; asks for a natural number
python3 erasthothenes-debug.py

# Turtle drawings (open a window and need tkinter)
python3 "10 Turtle.py"
cd ..
python3 drunkenSailor.py
```

The Caesar script guesses the shift by comparing each text's letter frequencies with English letter frequencies, so very short or unusual texts can come out wrong.

## Credits and license

Most lesson material, assignment texts and course data come from the [upstream course repository](https://gitlab.fjfi.cvut.cz/ksi/zpro-2025-public), created by the ZPRO teaching team at FJFI ČVUT: Jakub Klinkovský, Zuzana Petříčková, Vladimír Jarý, Maksym Dreval, Petr Pauš, Jan Tomsa and František Voldřich. The original course README is kept in [`ZPRO-readme.md`](ZPRO-readme.md). Course links:

- [KSI on FJFI GitLab](https://gitlab.fjfi.cvut.cz/ksi)
- [Solved exercises from the course](https://gitlab.fjfi.cvut.cz/ksi/zpro-2025-resene-priklady)
- [Course page in the ČVUT Bílá kniha](https://bilakniha.cvut.cz/cs/predmet11274505.html)

My exercise solutions, modifications and original scripts are credited to **Kotvič**.

The entire repository, including my exercise solutions and other additions, is licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](LICENSE), the same license as the upstream course materials.
