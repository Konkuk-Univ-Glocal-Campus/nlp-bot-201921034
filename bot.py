import random

# 이 리스트에는 무작위 응답이 포함되어 있습니다 (원하는 대로 추가하거나, 자신만의 언어로 번역할 수도 있습니다)
random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

# 영어를 한글로 번역하는 함수
def translate_to_korean(text):
    translations = {
        "That is quite interesting, please tell me more.": "그것은 매우 흥미롭군요. 더 자세히 말해주세요.",
        "I see. Do go on.": "알겠어요. 계속해주세요.",
        "Why do you say that?": "왜 그렇게 말하시나요?",
        "Funny weather we've been having, isn't it?": "좀 웃긴 날씨네요, 그렇죠?",
        "Let's change the subject.": "주제를 바꿔볼까요.",
        "Did you catch the game last night?": "어젯밤 경기 보셨나요?"
    }
    return translations.get(text, text)  # 번역이 없는 경우에는 그대로 반환

print("안녕하세요, 저는 간단한 로봇 Marvin입니다.")
print("'안녕'을 입력하여 대화를 종료할 수 있습니다.")
print("각 답변 입력 후 'enter'를 눌러주세요.")
print("오늘 기분은 어떠세요?")

while True:
    # 사용자가 텍스트를 입력할 때까지 기다립니다
    user_input = input("> ")
    if user_input.lower() == "bye":
        # 사용자가 'bye'을 입력하면 (대소문자 구분 없이), 루프를 탈출합니다.
        break
    else:
        response = random.choice(random_responses)
    print(translate_to_korean(response))

print("대화가 재밌었어요. 안녕히 가세요!")
