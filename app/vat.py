def calculate_vat(amount: float, vat:float=25):
    """VAT calculation

    :param amount: float - monetary amount to calculate VAT for
    :param vat: float - VAT percentage to apply
                Default value: 25 (Denmark)
    :return: float - amount incremented by the VAT percentage
    """
    if amount < 0 or vat < 0:
        return 0
    return round(amount + (amount / 100 * vat), 2)