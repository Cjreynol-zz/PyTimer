# PyTimer

A timer application for macOS, with stopwatch and split tracking functionality.

## Running PyTimer

The easiest way to use the application is to download the latest `.app` from 
the [releases page](https://github.com/Cjreynol/PyTimer/releases).

If you want to run from source, then run the `__main__.py` script using 
either `python -m pytimer` or `python pytimer/__main__.py` to bring up the 
application window.

## Building from source

Creating the application bundle requires `py2app` to be installed and is only 
tested using Python 3.7 and py2app V0.16, though I suspect older versions 
will work fine as long as the proper `py2app` version is used.

I would suggest creating a virtual environment (`python3 -m venv <env name>`) 
and then installing `py2app` with `pip install py2app`.  

To build from the source run `python app_setup.py py2app` from the project's 
root directory.

## Possible Py2App error

**Update:**  The developer has created a fix for this problem that should 
take effect in v0.17

When attempting to run the app setup script using the commands listed above, 
I received an `UnboundLocalError` stating that `tcl_path` was referenced 
before assignment.  There is an 
[issue](https://bitbucket.org/ronaldoussoren/py2app/issues/247/error-in-tkinterpy) 
listed on the source repository with a suggested hotfix form the issue 
creator.  Find the `py2app/recipes/tkinter.py` module(at 
`path/to/virtualenv/lib/python3.7/site-packages/py2app/recipes/tkinter.py` 
if you followed the instructions above) and add the following two lines at 
line 37, just before `prescript = textwrap.dedent("""\`:

    tcl_path = ""
    tk_path = ""


I did not spend much time exploring the code, but this does get past the 
error in a way that does not appear to affect the resulting application 
bundle.
