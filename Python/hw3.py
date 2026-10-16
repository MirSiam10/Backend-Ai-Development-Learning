recharge_amount = int(input("Enter your recharge amount: "))

if 101 <= recharge_amount <= 150:

    option_1 = "4 GB 7 Days - 95 Taka"
    option_2 = "10 Minutes 7 Days - 98 Taka"
    option_3 = "200 Minutes 7 Days - 139 Taka"

    print(f"""
Available Offers:
1. {option_1}
2. {option_2}
3. {option_3}
""")

elif 150 <= recharge_amount <= 300:

    option_1 = "12 GB + 120 Minutes 30 Days - 198 Taka"
    option_2 = "20 GB + 200 Minutes 30 Days - 298 Taka"
    option_3 = "15 GB 30 Days - 299 Taka"
    option_4 = "12 GB 7 Days - 169 Taka"

    print(f"""
Available Offers:
1. {option_1}
2. {option_2}
3. {option_3}
4. {option_4}
""")

elif recharge_amount > 300:

    option_1 = "25 GB + 300 Minutes 30 Days - 398 Taka"
    option_2 = "15 GB + 150 Minutes 30 Days - 318 Taka"
    option_3 = "35 GB + 450 Minutes 30 Days - 498 Taka"
    option_4 = "45 GB + 450 Minutes 90 Days - 998 Taka"
    option_5 = "For more dial - *111#"

    print(f"""
Available Offers:
1. {option_1}
2. {option_2}
3. {option_3}
4. {option_4}
5. {option_5}
""")

else:
    print("Sorry! No offers are available for this recharge amount.")