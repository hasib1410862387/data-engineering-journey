
# ==========================================
# You can run this full code to check the result of level 1 and level 2 are same or not
# ==========================================



import os

PATH = os.path.join("module-02", "data", "raw_sales.txt")


# ==========================================
# লেভেল ১ — payment
# ==========================================

with open(PATH, encoding="utf-8") as fh:
    lines = fh.read().strip().split("\n")


bkash_total = 0.0
bkash_count = 0
nagad_total = 0.0
nagad_count = 0
card_total = 0.0
card_count = 0
rocket_total = 0.0
rocket_count = 0
cod_total = 0.0
cod_count = 0

for raw in lines:
    parts   = raw.split(";")
    amount  = float(parts[5].strip().replace("৳", "").replace(",", ""))
    payment = parts[6].strip().lower()
    status  = parts[7].strip().lower()

    
    if status == "cancelled":
           continue

    
    if payment == "bkash":
           bkash_total = bkash_total + amount
           bkash_count = bkash_count + 1

    if payment == "nagad":
          nagad_total = nagad_total + amount
          nagad_count = nagad_count + 1

    if payment == "card":
          card_total = card_total + amount
          card_count = card_count + 1

    if payment == "rocket":
          rocket_total = rocket_total + amount
          rocket_count = rocket_count + 1

    if payment == "cash on delivery":
          cod_total = cod_total + amount
          cod_count = cod_count + 1

    pass        

total_money = bkash_total + nagad_total +card_total + rocket_total + cod_total

print("========== ORIGINAL OUTPUT ==========")
print("payment ধরে হিসাব (বাতিল বাদে)")
print()
print(f"bkash  {bkash_count}টা  ৳{bkash_total:.2f}")
print(f"nagad  {nagad_count}টা  ৳{nagad_total:.2f}")
print(f"card  {card_count}টা  ৳{card_total:.2f}")
print(f"rocket  {rocket_count}টা  ৳{rocket_total:.2f}")
print(f"cash on delivery  {cod_count}টা  ৳{cod_total:.2f}")
print()
print(f"সব মিলিয়ে:  ৳{total_money:.2f}")


# ==========================================
# লেভেল ২ — function
# ==========================================

def clean_amount(text):
    """৳ আর কমা সরিয়ে সংখ্যায় ফেরত দিন।"""
    return float(text.replace("৳", "").replace(",", "").strip())


def taka(amount):
    """1240.5 → "৳1240.50" """
    return f"৳{amount:.2f}"


def read_lines(path):
    """ফাইল পড়ে লাইনগুলোর list ফেরত দিন।"""
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def count_sales(lines):
    bkash_total = 0.0
    bkash_count = 0
    nagad_total = 0.0
    nagad_count = 0
    card_total = 0.0
    card_count = 0
    rocket_total = 0.0
    rocket_count = 0
    cod_total = 0.0
    cod_count = 0

    for raw in lines:
        parts = raw.strip().split(";")

        amount = clean_amount(parts[5])
        payment = parts[6].strip().lower()
        status = parts[7].strip().lower()

        if status == "cancelled":
            continue

        if payment == "bkash":
            bkash_total += amount
            bkash_count += 1

        if payment == "nagad":
            nagad_total += amount
            nagad_count += 1

        if payment == "card":
            card_total += amount
            card_count += 1

        if payment == "rocket":
            rocket_total += amount
            rocket_count += 1

        if payment == "cash on delivery":
            cod_total += amount
            cod_count += 1

    total_money = (
        bkash_total + nagad_total + card_total
        + rocket_total + cod_total
    )

    return (
        bkash_count, bkash_total,
        nagad_count, nagad_total,
        card_count, card_total,
        rocket_count, rocket_total,
        cod_count, cod_total,
        total_money
    )


def main():
    lines = read_lines(PATH)
    results = count_sales(lines)

    bkash_count, bkash_total = results[0:2]
    nagad_count, nagad_total = results[2:4]
    card_count, card_total = results[4:6]
    rocket_count, rocket_total = results[6:8]
    cod_count, cod_total = results[8:10]
    total_money = results[10]

    print("========== REFACTORED OUTPUT ==========")
    print("payment ধরে হিসাব (বাতিল বাদে)")
    print()
    print(f"bkash  {bkash_count}টা  {taka(bkash_total)}")
    print(f"nagad  {nagad_count}টা  {taka(nagad_total)}")
    print(f"card  {card_count}টা  {taka(card_total)}")
    print(f"rocket  {rocket_count}টা  {taka(rocket_total)}")
    print(f"cash on delivery  {cod_count}টা  {taka(cod_total)}")
    print()
    print(f"সব মিলিয়ে:  {taka(total_money)}")


if __name__ == "__main__":
    main()



