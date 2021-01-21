class User:
    count = 0

    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {}입니다.".format(cls.count))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        User.count += 1

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def check_name(self, name):
        return self.name == name

    def login(self, my_email, my_password):
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")


user1 = User("김대위", "captain@codeit.kr", "12345")
user2 = User("강영훈", "younghoon@codeit.kr", "98765")
user3 = User("최지웅", "jiwoon@codeit.kr", "78945")

User.number_of_users()