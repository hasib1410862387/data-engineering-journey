def clean_amount(text):
    
    return float(text.replace("৳", "").replace(",", "").strip())


def taka(amount):
    
    return f"৳{amount:.2f}"


if __name__ == "__main__":
    print(clean_amount(" ৳ 1,240.50 "))    # 1240.5
    print(taka(1240.5))                     # ৳1240.50
