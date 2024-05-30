# project 함수 선언 / 이유 : 조금 더 보기편하게 하기위해
def project():
    pat = input("Patrons? (answer None/Some/Full)  ")
    # patrons가 none,some,full인지 구별하여 full일 경우 추가 조건.
    if pat == "None" or pat == "none": 
        print("y"+number, "= No")
        print("Finish~~~~!!")
    elif pat == "Some" or pat == "some":
        print("y"+number, "= Yes")
        print("Finish~~~~!!")
    elif pat == "Full" or pat == "full":
        hun = input("Hungry? (answer Yes/No)  ")
        # hungry가 no,yes인지 구별하여 yes일 경우 추가 조건.
        if hun == "No" or hun == "no":
            print("y"+number, "= No")
            print("Finish~~~~!!")
        elif hun == "Yes" or hun == "yes":
            fri = input("Fri/Sat? (answer Yes/No)  ")
            # fri/sat가 no,yes인지 구별하여 yes일 경우 추가 조건.
            if fri == "No" or fri == "no":
                print("y"+number, "= No")
                print("Finish~~~~!!")
            elif fri == "Yes" or fri == "yes":
                res = input("Reservation? (answer Yes/No)  ")
                # reservation이 no,yes인지 구별하여 yes면 willwait no / no면 willwait yes
                if res == "Yes" or res == "yes":
                    print("y"+number, "= No")
                    print("Finish~~~~!!")
                elif res == "No" or res == "no":
                    print("y"+number, "= Yes")
                    print("Finish~~~~!!")
                else:
                    # 괄호안에 제시된것이 아니면 다시 시도하길 유도. 자비롭게 대소문자 구분 안해도 되게 추가하였음.
                    print("Wrong answer!! plz check () and try again!!")
            else:
                print("Wrong answer!! plz check () and try again!!")
        else:
            print("Wrong answer!! plz check () and try again!!")
    else:
        print("Wrong answer!! plz check () and try again!!")


print("It's ANJUBBRO's 12wk Homework Project. LET GO!!!!")
number = input("Please enter the example x number. (it does not affect the results)  ")

# number변수 안에 주어진 숫자만 입력받을 수 있게 조건문 추가
if number in "1""2""3""4""5""6""7""8""9""10""11""12":
    # 주어진 12개의 숫자면 project함수 실행.
    project()
else:
    # 주어진 숫자외의 것이 입력되면 다시 시도하기 유도.
    print("Wrong number!! plz check number and try again!!")