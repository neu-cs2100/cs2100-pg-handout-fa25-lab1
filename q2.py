"""
Please implement these stub functions to match the documentation.
"""

# Relevant information:
# Federal income tax rates:  https://www.irs.gov/filing/federal-income-tax-rates-and-brackets
# California income tax rates: https://www.hrblock.com/tax-center/filing/states/california-tax-rates
# Massachusetts income tax rate: 5% for everyone
# New York state income tax rates: https://www.nerdwallet.com/article/taxes/new-york-state-tax

def income_tax_fed(income: int) -> float:
    """Calculates the amount of federal income tax paid by somebody in the United States
    
    Parameters
    ----------
    income : int
        A person's annual income (before tax)
    
    Returns
    -------
    float
        The amount of federal income tax they pay
    """
    pass

def income_tax_CA(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in California
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of CA state tax they pay if they live in California
    """
    pass

def income_tax_MA(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in Massachusetts
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of MA state tax they pay if they live in Masachusetts
    """
    pass

def income_tax_NY(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in New York state
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of MA state tax they pay if they live in New York state
    """
    pass

def main() -> None:
    """
    1. Ask the user to input their state (CA for California, MA for Massachusetts, NY for New York)
    2. Ask the user to input an annual income
    3. Print a sentence formatted like this: "Your income is XX before tax and XX after tax. You pay XX income tax."
    4. Handle invalid unit inputs gracefully
    """
    pass

if __name__ == '__main__':
    main()
