import os

# 讀取檔案
def read_file(filename):
    bucklists = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            product, price = line.strip().split(',')
            bucklists.append([product, price])
    return bucklists

# 使用者輸入
def user_input(bucklists):
    while True:
        product = input('輸入商品，按q離開: ')
        if product == 'q':
            break
        price = input('請輸入價錢: ')
        bucklists.append([product, price])
    return bucklists

# 印出明細
def printlist(bucklists):
    for b in bucklists:
        print('商品: ', b[0], '價格: ', b[1])

# 寫入檔案
def write_file(filename, bucklists):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for b in bucklists:
            f.write(b[0] + ',' + b[1] + '\n')
    print('執行完成，獲得清單')

def main():
	filename = 'new_result.csv'
	if os.path.isfile(filename):
		bucklists = read_file(filename)
	else:
		print('檔案不存在，開新檔案紀錄')
		bucklists = []
	bucklists = user_input(bucklists)
	printlist(bucklists)
	write_file(filename, bucklists)

if __name__ == '__main__':
	main()
