COLOR = {
    "y": "\033[93m",
    "g": "\033[92m",
    "end": "\033[0m",
}

MSG = {
    "complt": f"{COLOR['g']}completed {COLOR['end']}"
}


print(f"{COLOR['y']}running {__file__}: import pkg1{COLOR['end']}")
import pkg1
print(MSG["complt"])

print(f"{COLOR['y']}\nrunning {__file__}: import pkg1.subpkg1{COLOR['end']}")
import pkg1.subpkg1
print(MSG["complt"])

print(f"{COLOR['y']}\nrunning {__file__}: import pkg1.subpkg1.modA{COLOR['end']}")
import pkg1.subpkg1.modA
print(MSG["complt"])

print(f"{COLOR['y']}\nrunning {__file__}: import main_3{COLOR['end']}")
import main_3
print(MSG["complt"])