import argparse
import numpy as np

import astropy.units as u
import astropy.cosmology.units as cu
from astropy.cosmology import WMAP9

parser = argparse.ArgumentParser(description="Calculate distance modulus, given an apparent and absolute magnitude")

parser.add_argument(
            "app_mag",
            type=float,
            help="Apparent magnitude"
)
parser.add_argument(
            "abs_mag",
            type=float,
            help="Absolute magnitude"
)
args = parser.parse_args()


app_mag = args.app_mag
abs_mag = args.abs_mag


d = 10 ** ((app_mag - abs_mag + 5) / 5)

print(f'With a distance modulus of {app_mag - abs_mag }')
print(f'The object is {d} parsecs away ({d / 10**6} Mpc)')