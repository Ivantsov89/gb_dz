exception= {11 , 12 , 13 , 14}
for procent in range(100):
    procent = procent + 1
    if procent in exception:
        print(procent, "процентов")
    elif procent % 10 == 1:
        print(procent, "процент")
    elif procent % 10 > 1 and procent % 10 <5:
        print(procent, "процента")
    else:
        print(procent, "процентов")