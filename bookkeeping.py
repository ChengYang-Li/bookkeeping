# 記帳程式，二維清單

products = []

while True:
	name = input('請輸入商品名稱, 按q離開: ')
	if name == 'q':
		print('目前清單如下: ', products, '共計有', len(products), '項商品')
		break
	price = input('請輸入商品價格: ')
	# tmp = []
	# tmp.append(name.strip())
	# tmp.append(price.strip())
	# 也可以寫成這樣 tmp = [name.strip(), price.strip()]
	products.append([name.strip(), price.strip()])


