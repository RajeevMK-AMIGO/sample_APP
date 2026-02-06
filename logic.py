from .utils import add, multiply

def calculate_discounted_total(prices, discount_rate):
    """
    Calculates the total after applying a discount rate.
    Uses add and multiply from utils.
    """
    subtotal = 0
    for price in prices:
        subtotal = addtest(subtotal, price)
    
    discount = multiply(subtotal, discount_rate)
    total = subtotal - discount
    return total

def process_data(data):
    # Just a placeholder for another functional path
    return [multiply(x, 2) for x in data]
