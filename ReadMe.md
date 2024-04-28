This repo contains a number of dummy packages, subpackages and modules and a .vscode debug config file. The debug config contains 2 settings:
- "Python Debugger: Current File": use this to run files that are not modules
- "Python: module": use this to run modules

Follow the following steps to understand Python's import mechanism. Ensure your directory is in this repo before proceeding.

1. Wtih debug mode (setting: Current File), run `main.py` in root dir.
    - nothing gets printed out for the first 2 imports
        - `import pkg1`, `import pkg1.subpkg1`
    - msgs are printed out with `import pkg1.subpkg1.modA`
        - see comments in `pkg1.subpkg1.modA`, they illustrates how to import 
            - from current subpkg of same pkg
            - from another subpkg of same pkg
            - from immediate parent pkg of current subpkg
            - module from root even if current subpkg has a module of same name
    - msgs are printed out with `import main_3`
        - shows how to import from root, similar to last point in `import pkg1.subpkg1.modA`
2. with debug mode (module), run `pkg1\modF.py`, it shows how to import
    - modules of same name from the current pakage and root, compliments the point made in 1.
3. with debug mode (module), run `pkg2\modE.py`
    - it shows what happens when in the root directory, a package and a module shares the same name.
        - if both package and module shares the same name, the package will be imported. otherwise the module will be imported.
        - try this out by running first without deleting the package. you should see a msg from `<root>\pkg_same_name\__.init__`
        - now delete the package and rerun the code. you should see a message from `<root>\pkg_same_name.py`
        - restore the package from recycle b
4. with debug mode (module), run `pkg2\modE_2.py`
    - shows how to import from a module from a pkg in root dir, similar to example 2. above.
    - however, notice that 2 messages are printed.
5. with debug mode (module), run `pkg2\modE_3.py`
    - shows how to import from current package, even if current package has a subpackage of the same name
6. with debug mode (module), run `pkg2\modE_4.py`
    - shows how to import from subpkg of currrent pkg, even if the subpackage has same name as current package