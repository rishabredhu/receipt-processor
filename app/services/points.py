from app.api.schemas import Receipt
import math

def calculate_points(receipt: Receipt) -> int:
    points = 0
    
    # Rule 1: Points for retailer name
    points += sum(c.isalnum() for c in receipt.retailer)
    
    # Rule 2: Round dollar amount (no cents)
    total_float = float(receipt.total)
    if total_float.is_integer():
        points += 50
    
    # Rule 3: Multiple of 0.25
    if total_float * 4 % 1 == 0:
        points += 25
    
    # Rule 4: Every two items
    points += (len(receipt.items) // 2) * 5
    
    # Rule 5: Item description length multiple of 3
    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            points += math.ceil(float(item.price) * 0.2)
    
    # Rule 6: Odd day
    if receipt.purchaseDate.day % 2 == 1:
        points += 6
    
    # Rule 7: Time between 2:00 PM and 4:00 PM
    purchase_hour = receipt.purchaseTime.hour
    purchase_minute = receipt.purchaseTime.minute
    if (14 <= purchase_hour < 16) or (purchase_hour == 16 and purchase_minute == 0) :
        points += 10
        
    return points