import sys

print("parsing resolution... ", end="")
# parse resolution from command line
if ( len(sys.argv) > 1 ):
    resolution = sys.argv[1]
else:
    resolution = "960*960"

resolution = [int(s) for s in resolution.split("*")]

ratio = resolution[0] / resolution[1]
if ( ratio == 16 / 9 ):  # use relative pixel
    size_unit = resolution[0] / (16 * 8)
elif ( ratio == 1 ):  # use absolute pixel
    size_unit = 1
else:
    raise ValueError("resolution should be 16:9 or 1:1")
print(f"resolution: {resolution}, size_unit: {size_unit}")

class px:
    pass

