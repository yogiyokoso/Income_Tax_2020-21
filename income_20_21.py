def tax_deduction():
    # Investment under Section 80C (ELSS+EPF)
    print("Do you have investment under 80C (like ELSS, EPF) (Y/N) : ", end="")
    te = input()
    invs_80c = int(input()) if te.upper() == 'Y' else 0
    invs_80c = 150000 if invs_80c >= 150000 else invs_80c
    print("Investement under 80C :- INR", invs_80c)

    # National Pension System
    print("Do you have NPS (Y/N) : ", end="")
    te = input()
    nps = int(input()) if te.upper() == 'Y' else 0
    nps = 50000 if nps >= 50000 else nps
    print("NPS :- INR ", nps)

    return invs_80c, nps


def income_tax(total_income):
    inc_tax = 0

    if total_income > 500000:
        inc_tax += 12500

    if 500000 < total_income >= 1000000:
        inc_tax += 100000

    if total_income > 1000000:
        inc_tax += (total_income-1000000)*.3
    return inc_tax


def Health_and_Education_Cess(inc_tax):
    inc_tax *= .04
    return round(inc_tax)


def print_all():
    print()
    print("Gross Salary :- ", gross_salary)
    print("HRA & LTA :- ", hra_lta)
    if invs_80c != 0:
        print("Investment :- ", invs_80c)
    if nps != 0:
        print("NPS", nps)
    print("Health Insurance Primium :- ", hlt_ins_prm)
    print("Total Taxable Income :- ", total_income)
    print()
    print("Income Tax", inc_tax)
    print()
    print("Health and Education Cess :- ", hlt_edu_cess)
    print("Total Tax Liability :- ", inc_tax+hlt_edu_cess)


# Income Tax 2020-21
gross_salary = 1300000
hra_lta = 200000
std_deducation = 50000
invs_80c, nps = tax_deduction()
# invs_80c = 150000
# nps = 50000
hlt_ins_prm = 15000
# print(tax_deduction(invs_80c, nps))

total_income = gross_salary - hra_lta - \
    std_deducation - invs_80c - nps - hlt_ins_prm
inc_tax = income_tax(total_income)
hlt_edu_cess = Health_and_Education_Cess(inc_tax)

print_all()
