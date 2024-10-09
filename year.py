id = "ilovepython"
password = "123456"

d = input("아이디를 입력하시오:")
if id == d:
    for i in range(3):
        p = input("패스워드를 입력하시오:")
        if password == p: #입력받은 p의 값이 password의 값과 일치하는지 확인하는 조건문이다.
            print("로그인 성공") 
            break
        else:
            print("비밀번호를",(i+1),"회 틀렸습니다.") #비밀번호가 틀릴 때마다 
    else:
        print("비밀번호를 3회 틀렸습니다. 나중에 로그인해주세요.")
else:
    print("아이디가 틀렸습니다.")

        
