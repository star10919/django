class Member(object):
    id = ''
    pw = ''
    name = ''
    email = ''

    @staticmethod
    def main():
        member = Member()
        while 1:
            menu = int(input('0.exit 1.회원가입 2.로그인 3.MYPAGE 4.회원정보수정 5.회원탈퇴'))
            if menu == 0:
                break
            elif menu == 1:
                member.id = input('id')
                member.pw = input('pw')
                member.name = input('name')
                member.email = input('email')
            elif menu == 2:
                member.name = input('name')
                member.pw = input('pw')
            elif menu == 3:
                member.id = input('id')
                member.pw = input('pw')
            elif menu == 4:
                member.pw = input('pw')
            elif menu == 5:
                member.id = input('id')
                member.pw = input('pw')
            else:
                print('wrong number')
                continue

Member.main()