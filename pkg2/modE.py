COLOR = {
    "y": "\033[93m",
    "g": "\033[92m",
    "end": "\033[0m",
}
X = ["runnning", "completed"]
msg = "import pkg_same_name"

print(f"{COLOR['y']}{X[0]} {__file__}: {msg}{COLOR['end']}")
import pkg_same_name
print(f"{COLOR['g']}{X[1]} {__file__}: {msg}{COLOR['end']}")
print(("-> if pkg_same_name (a package) and `pkg_same_name.py`exists in root, "
       "pkg will be imported instead of the module\n"
       "-> if the pkg does not exists, the module will be imported\n"
       "-> you can try deleting `pkg_same_name` package and see the difference\n"
       "-> besure to restore it after the test"))