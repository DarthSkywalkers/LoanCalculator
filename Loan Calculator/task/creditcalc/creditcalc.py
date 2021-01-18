import argparse
from math import log, ceil, floor

parser = argparse.ArgumentParser(description="This program is a loan calculator "
                                             "able to work with different types "
                                             "of payment. It can calculate various "
                                             "financial parameters of your loan.")

parser.add_argument("--type", choices=["annuity", "diff"],
                    help='It indicates the type of payment: '
                         '"annuity" or "diff" (differentiated).')
parser.add_argument("--payment", type=int,
                    help="It is the monthly payment amount.")
parser.add_argument("--principal", type=int,
                    help="It is used for calculations of both types "
                         "of payment. You can get its value if you know "
                         "the interest, annuity payment, and number of months.")
parser.add_argument("--periods", type=int,
                    help="denotes the number of months needed to repay the loan. "
                         "It's calculated based on the interest, annuity payment, "
                         "and principal.")
parser.add_argument("--interest", type=float,
                    help="interest rate should be specified without a percent sign. "
                         "Note that it can accept a floating-point value. This loan "
                         "calculator can't calculate the interest, "
                         "so it must always be provided.")

args = parser.parse_args()

calc_type = args.type
monthly_payment = args.payment
loan_principal = args.principal
periods = args.periods
interest = args.interest

zero_count = 0
if args.payment is None:
    monthly_payment = 0
    zero_count += 1
if args.principal is None:
    loan_principal = 0
    zero_count += 1
if args.periods is None:
    periods = 0
    zero_count += 1
if args.interest is None:
    interest = 0
    zero_count += 1


def calc_number_of_payments():
    result = log(monthly_payment / (monthly_payment - (interest * loan_principal)),
                 1 + interest)

    months = months_1 = ceil(result)

    years = 0
    if months >= 12:
        years = months // 12
        months -= years * 12

    if years > 0:
        years = f"{years} year{insert_s(years)}"
    else:
        years = ""
    if months > 0:
        months = f"{months} month{insert_s(months)}"
    else:
        months = ""
    if years and months:
        and_ = " and "
    else:
        and_ = ""

    message = f"It will take {years}{and_}{months} to repay this loan!" \
              f"\n{overpayment(months_1 * monthly_payment, loan_principal)}"

    return message


def calc_monthly_payment():
    result = loan_principal * ((interest * pow(1 + interest, periods))
                               / (pow(1 + interest, periods) - 1))

    return f"Your monthly payment = {ceil(result)}!\n"


def calc_loan_principal():
    loan_principal = floor(monthly_payment / ((interest * pow(1 + interest, periods))
                                              / (pow(1 + interest, periods) - 1)))

    return f"Your loan principal = {loan_principal}!\n{overpayment(monthly_payment * periods, loan_principal)}"


def diff():
    month = 1
    payment_sum = 0
    while month <= periods:
        payment_m = ceil(monthly_diff_payment(month))
        payment_sum += payment_m
        print(f"Month {month}: payment is {payment_m:.0f}")
        month += 1
    print()
    print(overpayment(payment_sum, loan_principal))


def monthly_diff_payment(month):
    return loan_principal / periods + interest * (loan_principal - ((loan_principal * (month - 1)) / periods))


def overpayment(paid_amount, loan_principal):
    overpayment_1 = round(paid_amount - loan_principal)
    return f"Overpayment = {overpayment_1}"


def insert_s(number):
    if number > 1:
        return "s"


def error():
    print("Incorrect parameters")


if interest > 0 and zero_count == 1:
    interest /= (12 * 100)
    if calc_type == "diff" and periods > 0 and loan_principal > 0 and interest > 0:
        diff()
    elif calc_type == "annuity":
        if monthly_payment > 0 and loan_principal > 0 and interest > 0:
            print(calc_number_of_payments())
        elif loan_principal > 0 and periods > 0 and interest > 0:
            print(calc_monthly_payment())
        elif monthly_payment > 0 and periods > 0 and interest > 0:
            print(calc_loan_principal())
        else:
            error()
    else:
        error()
else:
    error()
