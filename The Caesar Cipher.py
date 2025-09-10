# Алфавиты
alf_eng_lower = [chr(ord('a') + i) for i in range(26)]
alf_eng_upper = [chr(ord('A') + i) for i in range(26)]
alf_ru_lower = [chr(ord('а') + i) for i in range(32)]
alf_ru_upper = [chr(ord('А') + i) for i in range(32)]

direction = int(input('Выберите направление: шифровать (0) или дешифровать (1)?\n'))
language = input('Выберите язык: русский (ру) или английский (eng)?\n')
# step = int(input('Шаг сдвига:\n'))
text = input('Текст для преобразования:\n')

def caesar(direction, language, step, text):

    if language == 'ру':
        cnt = 32
        low_alf = alf_ru_lower
        upp_alf = alf_ru_upper
    if language == 'eng':
        cnt = 26
        low_alf = alf_eng_lower
        upp_alf = alf_eng_upper

    print(f"Вы {["шифруете", "дешифруете"][direction]} текст: '{text}'0 с шагом сдвига {step}.\nРезультат: ", end="")

    for i in range(len(text)):

        if text[i].isalpha():

            # Находим индекс символа text[i]
            if text[i].islower():
                place = low_alf.index(text[i])
            elif text[i].isupper():
                place = upp_alf.index(text[i])

            if direction == 1:
                index = (place - step) % cnt
            elif direction == 0:
                index = (place + step) % cnt

            if text[i].islower():
                print(low_alf[index], end='')
            if text[i].isupper():
                print(upp_alf[index], end='')

        else:
            print(text[i], end='')
    print()

for step in range(25):
    caesar(direction, language, step, text)