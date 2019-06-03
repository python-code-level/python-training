# PEP 8 guide has several options for indentation
# Selected examples shown below

# spaces not tabs
# respect max line length limitation


# Add 4 spaces (an extra level of indentation) to distinguish arguments
# from the rest.

def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)


my_list = [
    1, 2, 3,
    4, 5, 6,
    ]


# operators on new lines

# Yes: easy to match operators with operands

income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
