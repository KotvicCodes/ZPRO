#! /usr/bin/env python3

"""
!!! Do not delete or edit this file! It is used for automated tests of the assignment.
"""

import builtins
from builtins import print as builtin_print
from builtins import input as builtin_input
from contextlib import contextmanager

stdout = ""

def print(*values, sep=" ", end="\n", **kwargs):
    global stdout
    stdout += sep.join([str(value) for value in values]) + end
    builtin_print(*values, sep=sep, end=end, **kwargs)

builtins.print = print

stdin = []

def input(prompt="", /):
    if len(stdin) > 0:
        return str(stdin.pop(0))
    else:
        raise ValueError("The input function was used too many times in this assignment.")

def set_input(*, inputs):
    if isinstance(inputs, list):
        global stdin
        stdin += inputs
    else:
        raise TypeError("inputs must be supplied as a list of values")
    builtins.input = input
    return builtins.input

@contextmanager
def mock_input(*, inputs):
    global stdout
    stdout = ""
    resource = set_input(inputs=inputs)
    try:
        yield resource
    finally:
        builtins.input = builtin_input
        if stdin:
            raise ValueError("The input function was not used enough times in this assignment.")
        # ignore the output of the %rerun magic from stdout
        lines = stdout.splitlines(keepends=True)
        try:
            begin = lines.index("=== Executing: ===\n")
            end = lines.index("=== Output: ===\n")
            del lines[begin:end + 1]
            stdout = "".join(lines)
        except ValueError:
            # marks not found, keep stdout as is
            pass


from IPython.core.magic import Magics, magics_class, line_magic

@magics_class
class ZproMagics(Magics):
    @line_magic
    def rerun_quiet(self, parameter_s=''):
        """Re-run previous input

        Same as the built-in [%rerun magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-rerun)
        but does not print the code that is being rerun.

        By default, you can specify ranges of input history to be repeated
        (as with %history). With no arguments, it will repeat the last line.

        Options:

          -l <n> : Repeat the last n lines of input, not including the
          current command.

          -g foo : Repeat the most recent line which contains foo
        """
        opts, args = self.parse_options(parameter_s, 'l:g:', mode='string')
        if "l" in opts:         # Last n lines
            try:
                n = int(opts["l"])
            except ValueError:
                print("Number of lines must be an integer")
                return

            if n == 0:
                print("Requested 0 last lines - nothing to run")
                return
            elif n < 0:
                print("Number of lines to rerun cannot be negative")
                return

            hist = self.shell.history_manager.get_tail(n)
        elif "g" in opts:       # Search
            p = "*"+opts['g']+"*"
            hist = list(self.shell.history_manager.search(p))
            for l in reversed(hist):
                if "rerun" not in l[2]:
                    hist = [l]     # The last match which isn't a %rerun
                    break
            else:
                hist = []          # No matches except %rerun
        elif args:              # Specify history ranges
            hist = self.shell.history_manager.get_range_by_str(args)
        else:                   # Last line
            hist = self.shell.history_manager.get_tail(1)
        hist = [x[2] for x in hist]
        if not hist:
            print("No lines in history match specification")
            return
        #histlines = "\n".join(hist)
        #print("=== Executing: ===")
        #print(histlines)
        #print("=== Output: ===")
        self.shell.run_cell("\n".join(hist), store_history=False)

# register the magics if running in IPython
try:
    ipython = get_ipython()
except NameError:
    pass
else:
    ipython.register_magics(ZproMagics)


if __name__ == "__main__":
    print("foo", 42, 3.14, sep="\t", end="\n\n")
    assert stdout == "foo\t42\t3.14\n\n"

    stdin = ["foo", 42]
    a = input()
    b = input()
    assert a == "foo", a
    assert b == "42", b
    try:
        input()
        assert False, "input did not raise an exception"
    except ValueError:
        pass