COLOR = {
    "y": "\033[93m",
    "g": "\033[92m",
    "end": "\033[0m",
}
X = ["runnning", "completed"]

msg = "import pkg_same_name.moduleG"
print(f"{COLOR['y']}\n{X[0]} {__file__}: {msg}{COLOR['end']}")
import pkg_same_name.moduleG
print(f"{COLOR['g']}\n{X[1]} {__file__}: {msg}{COLOR['end']}")