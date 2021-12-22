from budget_program.get_data_from_db import read_amounts
from budget_program.get_user_input import amount_input
from budget_program.update_data_in_db import append_new_amount
from budget_program.count_balance import count_budget_overview
def main():
    filename = "Mini biudžetas.txt"
    old_amounts = read_amounts(filename)
    new_amounts = amount_input()
    for amount in new_amounts:
        old_amounts.append(amount)
    append_new_amount(old_amounts, filename)

    budget_overview = count_budget_overview(old_amounts)

    print(budget_overview)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
