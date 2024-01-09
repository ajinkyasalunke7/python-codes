def usd_to_inr(usd_amount):
    exchange_rate = 83.11 
    inr_amount = usd_amount * exchange_rate
    return inr_amount


usd_amount = float(input("Enter the amount in U.S. dollars: "))
converted_amount = usd_to_inr(usd_amount)
print(f"{usd_amount} U.S. dollars is equal to {converted_amount} Indian Rupees.")
