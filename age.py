driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit
    
age = input('請問你的年齡是?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('恭喜你,通過測驗嘞')
    else:
        print('為什麼?你會開過車?')
elif driving == "沒有":
    if age >= 18:
        print('你可以考駕照囉~~快去考')
    else:
        print('很好，18歲才能考駕照喔')
else:
    print('請輸入 有/沒有')