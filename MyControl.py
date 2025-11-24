import MathFunction as math

while True:
    try:
        Person = int(input("please input PersonNumber[1~10]: "))
    except ValueError:
        print("❌ 請輸入整數！")

    if 1 <= Person <= 10:
        for I in range(Person):
            print(f"This is a {I+1}:")

            # ===== Input SetX =====
            while True:
                try:
                    SetX = int(input("please input X: "))
                except ValueError:
                    print("❌ X 必須是整數！")
                    continue

                if SetX > 0:
                    break
                else:
                    print("❌ X 必須 > 0，請重新輸入")

            # ===== Input SetY =====
            while True:
                try:
                    SetY = int(input("please input Y: "))
                except ValueError:
                    print("❌ Y 必須是整數！")
                    continue

                if SetY > 0:
                    break
                else:
                    print("❌ Y 必須 > 0，請重新輸入")

            print("Welcome to MathSystem !!")

            # ===== Choose Prepare =====
            while True:
                try:
                    Prepare = int(input("1.Add\t2.Sub\t3.Miv\t4.Division\nplease prepare[1~4]: "))
                except ValueError:
                    print("❌ 請輸入整數選項！")
                    continue

                if 1 <= Prepare <= 4:
                    math.MathPrepare(Prepare, SetX, SetY)
                    break
                else:
                    print("❌ 選項需為 1~4，請重新輸入")

        break

    else:
        print("❌ 人數需為 1~10，請重新輸入")
