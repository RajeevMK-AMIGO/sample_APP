from .logic import calculate_discounted_total, process_data

def main():
    items = [100, 50, 25, 10]
    rate = 0.1 # 10% discount
    
    print(f"Items: {items}")
    final_price = calculate_discounted_total(items, rate)
    print(f"Final Price (10% off): {final_price}")
    
    transformed = process_data([1, 2, 3])
    print(f"Transformed Data: {transformed}")

if __name__ == "__main__":
    main()
