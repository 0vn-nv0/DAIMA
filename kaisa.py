print("1.加密\n2.解密\n请选择模式:",end="")
while True:
    Num = input()
    if Num == "1" or Num == "2":
        num = int(Num)
        break
    else:
        print("请输入'1'或'2'选择模式！")
if num == 1:
    mi = ""
    ming = input("请输入明文：")
    key = 3
    while True:
        k = input("请输入秘钥（默认为3）：")
        if k.isdigit():
            break
        else:
            print("请输入数字！")
    key = int(k)        
    for i in ming:
        if "a" <= i <= "z":
            mi = mi + chr(ord("a")+(ord(i)-ord("a")+key) % 26)
        elif "A" <= i <= "Z":
            mi = mi + chr(ord("A")+(ord(i)-ord("A")+key) % 26)
        else:
            mi = mi + i
if num == 2:
    ming = ""
    mi = input("请输入密文：")
    key = 3
    while True:
        k = input("请输入秘钥（默认为3）：")
        if k.isdigit():
            break
        else:
            print("请输入数字！")
    key = int(k)        
    for i in mi:
        if "a" <= i <= "z":
            ming = ming + chr(ord("z")-(ord("z")-ord(i) + key) % 26)
        elif "A" <= i <= "Z":
            ming = ming + chr(ord("Z")-(ord("Z")-ord(i) + key) % 26)
        else:
            ming = ming +i
if num == 1:
    print("加密后为："+mi)
if num == 2:
    print("解密后为："+ming)
 
    
