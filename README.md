# LoanCalculator :abacus:
This program is a loan calculator able to work with different types of payment. It calculates various financial parameters of your loan. 
You can control this calculator form the command line interface (CLI).

## Requirements

You need Python 3.7 or later to run this loan calculator. You can try to use older versions, but it wasn't tested and you do it on your own risk!

## How to use

Type `python creditcalc.py --help` for a description of possible commands.

## Examples

You can try the following commands:

Annuity payments:
`python creditcalc.py --type annuity --payment 104000 --principal 1000000 --interest 7.8`

Differentiated payments:
`python creditcalc.py --type diff --principal 1000000 --periods 10 --interest 10`

## Built With

* [PyCharm Edu](https://www.jetbrains.com/pycharm-edu/) - IDE used

## Acknowledgments

* Project completed as a part of Python Developer track in [Jetbrains Academy](https://www.jetbrains.com/academy/).
