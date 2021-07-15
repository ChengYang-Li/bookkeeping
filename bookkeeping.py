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
	# products.append(tmp)
	products.append([name.strip(), price.strip()])

print('目前清單如下: ', products, '共計有', len(products), '項商品')

for i in products:
	# print('第', count + 1, '項商品為:', products[count][0], '價格為: ', products[count][1])
	print('第', count + 1, '項商品為:', i[0], '價格為: ', i[1])
	count += 1

for p in products:
	print(p[0], '的價格是', p[1])

with open('result.txt', 'w') as f:
	for line in products:
		f.write('買了:' + line[0] + ', 花了:' + line[1] + '元' + '\n')

with open('result.csv', 'w', encoding = 'utf-8') as f: # 寫的時候編碼用utf-8
	f.write('商品名稱, 價格\n') #要記得換行\n
	for line in products:
		f.write(line[0] + ', ' + line[1] + '\n')

data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
# 請開始寫"寫入檔案"的程式碼
with open('test.txt', 'w') as f:
    for d in data:
        f.write(str(d) + '\n')