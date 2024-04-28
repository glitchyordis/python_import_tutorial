COLOR = {
    "y": "\033[93m",
    "g": "\033[92m",
    "end": "\033[0m",
}
X = ["runnning", "completed"]

msg = "import pkg2.pkg2.modE"
print(f"{COLOR['y']}\n{X[0]} {__file__}: {msg}{COLOR['end']}")
import pkg2.pkg2.modE
print(f"{COLOR['g']}{X[1]} {__file__}: {msg}{COLOR['end']}")