def apply_discount(price, discount_percent=10):
    discounted_price = price - (price * discount_percent / 100)
    return round(discounted_price, 2)