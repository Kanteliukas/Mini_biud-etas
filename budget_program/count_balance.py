
# Skaičiuojam pickled data
def count_budget_overview(amounts):
    budget_overview = 0
    for amount in amounts:
        amount = float(amount)
        budget_overview += amount
    return round(budget_overview, 2)