def bargain(price, money_now):
	print("How much does it cost?\nIt costs {}.".format(price))
	print("Can you leave it to me for {}?".format(money_now))
	print("Go away, you are crazy!\n")
	
bargain(10, 5)
bargain(10+5, 5+2)
p = 20; m = 7
bargain(p, m)
bargain(p + 5, m + 5)