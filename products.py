products = [] #大清單
while True:
    name = input('請輸入商品名稱：')
    if name == 'q': #quit
        break
    price = input('請輸入商品價格：')
    price = int(price)
    products.append([name, price]) #小清單裝進大清單
print(products)

for p in products:
    print(p[0], '的價格是', p[1] )

with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
        #價格要從整數再轉成字串str()

