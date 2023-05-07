from random import randint
player_name = input("플레이어의 이름을 입력하시오 : ")
difficulty = int(input("난이도에는 '보통'과 '어려움'이 있습니다.(보통 = '1', 어려움 = '2') \n 무엇을 선택하시겠습니까? : "))

def generate_numbers_easy():
    numbers = []
    i = 0
    new_number = 0
    while i < 3:
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)
            i += 1
    print("안녕하십니까?", str(player_name) + "님, 미니 야구게임 진행을 맡은 김연세입니다.\n\n") 
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess_easy():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    i = 0
    new_guess = []
    while i < 3:
        gue_number = int(input("{}번째 숫자를 입력하세요: ".format(i + 1)))
        if gue_number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if gue_number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요. ")
        else:
            new_guess.append(gue_number)
            i += 1

    return new_guess


def generate_numbers_hard():
    numbers = []
    i = 0
    new_number = 0
    while i < 5:
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)
            i += 1
    print("안녕하십니까?", str(player_name) + "님, 미니 야구게임 진행을 맡은 김연세입니다.\n\n") 
    print("0과 9 사이의 서로 다른 숫자 5개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess_hard():
    print("숫자 5개를 하나씩 차례대로 입력하세요.")
    i = 0
    new_guess = []
    while i < 5:
        gue_number = int(input("{}번째 숫자를 입력하세요: ".format(i + 1)))
        if gue_number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if gue_number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요. ")
        else:
            new_guess.append(gue_number)
            i += 1

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0
    i = 0

    while i < len(guess):
        if guess[i] == solution[i]:
            strike_count += 1
            i += 1
        elif guess[i] in solution:
            ball_count += 1
            i += 1
        else:
            i += 1

    return strike_count, ball_count


if difficulty == 1:
    ANSWER = generate_numbers_easy()
    tries = 0
    n = 1
    stand = 0
    point = 0
    while 1:
        
        print(str(n) + "회~!!")
        
        GUESS = take_guess_easy()
        strike, ball = get_score(GUESS, ANSWER)
        print("{}S  {}B".format(strike, ball))
        
        if strike == 3:
            tries += 1
            break
        else:
            tries += 1

        if tries % 9 == 0:
            n += 1

        if strike == 0 and ball == 0:
            print(" 안타!!!...타자가 1루 전진합니다.")
            stand += 1

        if stand == 4:
            point += 1
            stand -= 1
            print(" 상대팀에서 1점 득점합니다! 현재 스코어 0 대", point ,"입니다.")

        if point >= 15:
            print("몰수패 하셨습니다...다음에 도전하세요")
            break

        if n == 6:
            print("경기가 종료되었습니다!, 최종 스코어는 0 대", point ,"입니다.") 
            break

    if strike == 3:
        print("축하합니다!", str(player_name) + "님! {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))


if difficulty == 2:
    ANSWER = generate_numbers_hard()
    tries = 0
    n = 1
    stand = 0
    point = 0
    while 1:
        
        print(str(n) + "회~!!")
        
        GUESS = take_guess_hard()
        strike, ball = get_score(GUESS, ANSWER)
        print("{}S  {}B".format(strike, ball))
        
        if strike == 5:
            tries += 1
            break
        else:
            tries += 1

        if tries % 9 == 0:
            n += 1

        if strike == 0 and ball == 0:
            print(" 안타!!!...타자가 1루 전진합니다.")
            stand += 1

        if stand == 4:
            point += 1
            stand -= 1
            print(" 상대팀에서 1점 득점합니다! 현재 스코어 0 대", point ,"입니다.")

        if point >= 10:
            print("몰수패 하셨습니다...다음에 도전하세요")
            break

        if n == 6:
            print("경기가 종료되었습니다!, 최종 스코어는 0 대", point ,"입니다.") 
            break

    if strike == 5:
        print("축하합니다!", str(player_name) + "님! {}번 만에 숫자 5개의 값과 위치를 모두 맞추셨습니다.".format(tries))

