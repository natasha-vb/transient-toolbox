import argparse
import numpy as np

import astropy.units as u
import astropy.cosmology.units as cu
from astropy.cosmology import WMAP9

parser = argparse.ArgumentParser(description="Convert between redshifts and distances, apparent and absolute magnitudes")

parser.add_argument(
            "--red2dist",
            action="store_true",
            help="Convert redshift to distance in Mpc"
)
parser.add_argument(
            "--dist2red",
            action="store_true",
            help="Convert distance in Mpc to redshift"
)
parser.add_argument(
            "--app2abs",
            action="store_true",
            help="Convert apparent to absolute magnitude, for a given redshift"
)
parser.add_argument(
            "--abs2app",
            action="store_true",
            help="Convert absolute to absolute magnitude, for a given redshift"
)
parser.add_argument(
            "--redshift",
            type=float,
            help="redshift value"
)
parser.add_argument(
            "--distance",
            type=float,
            help="distance in Mpc"
)
parser.add_argument(
            "--app_mag",
            type=float,
            help="Apparent magnitude"
)
parser.add_argument(
            "--abs_mag",
            type=float,
            help="Absolute magnitude"
)
args = parser.parse_args()


##################################
####  REDSHIFT <===> DISTANCE ####
##################################

if args.red2dist:
    z = args.redshift * cu.redshift
    d = z.to(u.Mpc, cu.redshift_distance(WMAP9, kind="comoving"))

    print(f'Redshift z = {z} is equivalent to {d}')


if args.dist2red:
    d = args.distance * u.Mpc
    z = d.to(cu.redshift, cu.redshift_distance(WMAP9, kind="comoving", zmax=1200))  

    print(f'Distance {d} is equivalent to a redshift of z = {z}')


##################################
####  APPARENT <===> ABSOLUTE ####
##################################

if args.app2abs:
    if args.redshift:
        z = args.redshift * cu.redshift
        d = z.to(u.Mpc, cu.redshift_distance(WMAP9, kind="comoving"))
    if args.distance:
        d = args.distance * u.Mpc
    
    abs_mag = args.app_mag - (2.5 * np.log10(((d.value*10**6)/10)**2))

    if args.redshift:
        print(f'At z = {z}, the absolute magnitude is {abs_mag}')
    if args.distance:
        print(f'At distance = {d}, the absolute magnitude is {abs_mag}')


if args.abs2app:
    if args.redshift:
        z = args.redshift * cu.redshift
        d = z.to(u.Mpc, cu.redshift_distance(WMAP9, kind="comoving"))
    if args.distance:
        d = args.distance * u.Mpc
    
    app_mag = args.abs_mag + (2.5 * np.log10(((d.value*10**6)/10)**2))

    if args.redshift:
        print(f'At z = {z}, the apparent magnitude is {app_mag}')
    if args.distance:
        print(f'At distance = {d}, the apparent magnitude is {app_mag}')