import random
money = 100000
chonvat = [] #Lưu tất cả lựa chọn của người chơi
vatchoiceinstr = [] #Dịch các lựa chọn sang cả số lẫn chữ
chontien = []
vatchoice = []
tiencuoc = 0
chonthem = ' '
tienlai = 0

def game():
    global money
    chonvat.clear()
    vatchoiceinstr.clear()
    chontien.clear()
    vatchoice.clear()
    tiencuoc = 0
    chonthem = ' '
    tienlai = 0
    print('Game bầu cua python được tạo bởi nâL')
    print('----------------------------------------')
    print('Bạn đang có',money,'đồng')
    print('Bầu - 1 | Cua - 2 | Tôm - 3 | Cá - 4 | Gà - 5 | Nai - 6')
    randomvat()
    datcuoc()
    for i in range (1, 4):
        switcher = {
            '1': '1 - Bầu',
            '2': '2 - Cua',
            '3': '3 - Tôm',
            '4': '4 - Cá',
            '5': '5 - Gà',
            '6': '6 - Nai'
            }
        vatchoiceinstr.append(switcher.get(str(vatchoice[i-1])))
        string = ' | '
    print('Kết quả bầu cua:',string.join(vatchoiceinstr))
    for i in range(1, len(chonvat)+1):
        if vatchoice.count(chonvat[i-1]) == 0:
            money -= chontien[i-1]
            tienlai -= chontien[i-1]
        elif vatchoice.count(chonvat[i-1]) == 1:
            money += chontien[i-1]
            tienlai += chontien[i-1]
        elif vatchoice.count(chonvat[i-1]) == 2:
            money += chontien[i-1] * 2
            tienlai += chontien[i-1] * 2
        elif vatchoice.count(chonvat[i-1]) == 3:
            money += chontien[i-1] * 3
            tienlai += chontien[i-1] * 3
    print('Số tiền bạn nhận/được sau đợt (chắc thế):',tienlai)
    print('Số tiền bạn đang có:',money)

def randomvat():
    for i in range (1, 4):
        vatchoice.append(random.randint(1, 6))

def datcuoc():
    chon = int(input('Vui lòng chọn vật mà bạn muốn cược: '))
    while chon < 1 or chon > 6:
        chon = int(input('Vui lòng chọn vật mà bạn muốn cược: '))
    tiencuoc = int(input('Vui lòng chọn số tiền mà bạn muốn cược (tiền cược không quá tiền bạn đang có và phải chia hết cho 1000 đồng)'))
    while tiencuoc < 1000 or tiencuoc > money or tiencuoc % 1000 != 0:
        tiencuoc = int(input('Vui lòng chọn số tiền mà bạn muốn cược (tiền cược không quá tiền bạn đang có và phải chia hết cho 1000 đồng)'))
    chonvat.append(chon)
    chontien.append(tiencuoc)
    if len(chonvat) < 3 and tiencuoc != money:
        datthem()

def datthem():
    chonthem = input('Bạn có muốn đặt cược thêm? y/n ')
    while chonthem != 'y' and chonthem != 'n':
        chonthem = input('Bạn có muốn đặt cược thêm? y/n ')
    if chonthem == 'y':
        datcuoc()
for i in range(1, 4):
    print(i)

while True:
    game()
    if money == 0:
        print('Bạn đã hết tiền :(')
        break
