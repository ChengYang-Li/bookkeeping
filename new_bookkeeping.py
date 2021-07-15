import os

bucklists = []

if os.path.isfile('new_result.csv'): # 檢查檔案是否存在
# 讀取檔案
	with open('new_result.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			product, price = line.strip().split(',')
			bucklists.append([product, price])
# 使用者輸入
while True:
	product = input('輸入商品，按q離開: ')
	if product == 'q':
		break
	price = input('請輸入價錢: ')
	bucklists.append([product, price])

# 印出明細
for b in bucklists:
	print('商品: ', b[0], '價格: ', b[1])

# 寫入檔案
with open('new_result.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for b in bucklists:
		f.write(b[0] + ',' + b[1] + '\n')
