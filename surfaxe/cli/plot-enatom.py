# Misc 
from argparse import ArgumentParser
import yaml
import os
import warnings 
import pandas as pd

# Surfaxe 
from surfaxe.io import plot_enatom

def _get_parser(): 
    parser = ArgumentParser(
        description="""Plots the surface energy for all terminations."""
    )
    parser.add_argument('-d', '--data', 
    help='Path to the csv file from parsefols with data')
    parser.add_argument('--no-time-taken', default=True, action='store_false',
    dest='time_taken', help=('Do not show time taken for calculations to '
    'complete (default: True)')) 
    parser.add_argument('--plt-fname', default='energy_per_atom.png', type=str,
    dest='plt_fname', help='Filename of the plot (default: energy_per_atom.png)')
    parser.add_argument('--dpi', default=300, type=int, 
    help='Dots per inch (default: 300)')
    parser.add_argument('-c', '--colors', default=None, nargs='+', type=str, 
    help=('Colours for different vacuum thicknesses plots in any format '
    'supported by mpl e.g. r g "#eeefff" where hex colours starting with # need '
    'to be surrounded with quotation marks' ))
    parser.add_argument('--width', default=6, type=float, 
    help='Width of the figure in inches (default: 6)')
    parser.add_argument('--height', default=5, type=float, 
    help='Height of the figure in inches (default: 5)')
    parser.add_argument('--heatmap', default=False, action='store_true', 
    help='If True, plots a heatmap of surface energies (default: False)')
    parser.add_argument('--cmap', default='Wistia', type=str, 
    help='Matplotlib colourmap for heatmap (default: Wistia)')
    parser.add_argument('--yaml', default=False, action='store_true', 
    help='Read optional args from surfaxe_config.yaml file.')

    return parser

def main(): 
    args = _get_parser().parse_args()

    df = pd.read_csv(args.data)

    if args.yaml==True: 
        with open('surfaxe_config.yaml', 'r') as y: 
            yaml_args = yaml.load(y)
        args.update(
            (k, yaml_args[k]) for k in args.keys() and yaml_args.keys()
        )

    plot_enatom(df, time_taken=args.time_taken, colors=args.colors, dpi=args.dpi, 
    width=args.width, height=args.height, heatmap=args.heatmap, cmap=args.cmap, 
    plt_fname=args.plt_fname)

if __name__ == "__main__":
    main()