
print("+----------------------------------------------------------+")
print("|                      숫자 야구 게임                      |")
print("+----------------------------------------------------------+")
print("| 수비수가 고른 세자릿수를 맞춰보세요.                     |")
print("| 0에서 9까지 서로 다른 숫자이다. (같은 숫자 사용 금지)    |")
print("| 스트라이크 : 공격수가 제시한 숫자와 위치가 모두 맞을 경우|")
print("| 볼 : 공격수가 제시한 숫자는 맞고 위치가 틀릴 경우        |")
print("| 아웃 : 공격수가 제시한 숫자가 모두 틀릴 경우             |")
print("+----------------------------------------------------------+")

print("> 수비수가 고른 숫자")
number1 = 3
number2 = 2
number3 = 0
print(number1)
print(number2)
print(number3)

print("> 첫 번째 숫자를 입력하세요.")
guess_number1 = int(input("prompt>"))
print("> 두 번째 숫자를 입력하세요.")
guess_number2 = int(input("prompt>"))
print("> 세 번째 숫자를 입력하세요.")
guess_number3 = int(input("prompt>"))

print("> 공격수가 고른 숫자")
print(guess_number1)
print(guess_number2)
print(guess_number3)

if guess_number1 == guess_number2 or guess_number1 == guess_number3 or guess_number2 == guess_number3:
    print("같은 숫자를 입력하면 안 됩니다.")
else:
    strike_count = 0
    ball_count = 0

    if guess_number1 == number1:
        strike_count = strike_count + 1
    elif guess_number1 == number2 or guess_number1 == number3:
        ball_count = ball_count + 1

    if guess_number2 == number2:
        strike_count = strike_count + 1
    elif guess_number2 == number1 or guess_number2 == number3:
        ball_count = ball_count + 1

    if guess_number3 == number3:
        strike_count = strike_count + 1
    elif guess_number3 == number1 or guess_number3 == number2:
        ball_count = ball_count + 1

    print("스트라이크 :", strike_count)
    print("볼 :", ball_count)
    print("아웃 :", 3 - strike_count - ball_count)
