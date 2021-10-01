import os # operating system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 跳到下一迴
                # continue 和 break 一樣只能寫在迴圈
            name, price = line.strip().split(',')
            # strip() 去掉換行符號
            # split 切割
            products.append([name, price])
    return products        

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q': # quit
            break
        price = input('請輸入商品價格：')
        price = int(price)
        products.append([name, price]) # 小清單裝進大清單
    print(products)
    return products

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1] )

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')
            # 價格要從整數再轉成字串 str()

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 檢查檔案在不在
        print('已有檔案')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()

