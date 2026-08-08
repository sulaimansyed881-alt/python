actualprice=int(input("Enter your actualprice"))
sellingprice=int(input("Enter your sellingprice"))
if sellingprice>actualprice:
    print("There is a total profit of",sellingprice-actualprice)
else:
    print("There is no profit")