# 記帳程式

products = []
while True:
	name = input('請輸入商品名稱, 按q離開: ')
	if name == 'q':
		print('目前清單如下: ', products, '共計有', len(products), '項商品')
		break
	products.append(name.strip())


