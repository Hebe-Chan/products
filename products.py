products = [] #大清單
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q': #quit
    	break
    price = input('請輸入商品價格: ')
    products.append([name, price]) #把細清單裝在products清單
print(products)

for p in products:
	print(p[0], '的價格是', p[1])