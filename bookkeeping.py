# 記帳程式，二維清單

products = []
count = 0 

while True:
	name = input('請輸入商品名稱, 按q離開: ')
	if name == 'q':
		# print('目前清單如下: ', products, '共計有', len(products), '項商品')
		# for i in products:
		# 	# print('第', count + 1, '項商品為:', products[count][0], '價格為: ', products[count][1])
		# 	print('第', count + 1, '項商品為:', i[0], '價格為: ', i[1])
		# 	count += 1
		break
	price = input('請輸入商品價格: ')
	# tmp = []
	# tmp.append(name.strip())
	# tmp.append(price.strip())
	# 也可以寫成這樣 tmp = [name.strip(), price.strip()]
	products.append([name.strip(), price.strip()])

print('目前清單如下: ', products, '共計有', len(products), '項商品')

for i in products:
	# print('第', count + 1, '項商品為:', products[count][0], '價格為: ', products[count][1])
	print('第', count + 1, '項商品為:', i[0], '價格為: ', i[1])
	count += 1

for p in products:
	print(p[0], '的價格是', p[1])

