import random as r

def generate_password(l, c):
    ps = ""
    for _ in range(l):
        ps += r.choice(c)
    return ps

digits = '0123456789'
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = ''

cntP = int(input('Укажите количество паролей для генерации: '))
lenP = int(input('Укажите длину одного пароля: '))

dig = input('Включать ли цифры 0123456789? (y/n) ')
ABC = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ')
abc = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ')
pun = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ')
exc = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ')

if dig == "y":
    chars += digits
if ABC == "y":
    chars += uppercase_letters
if abc == "y":
    chars += lowercase_letters
if pun == "y":
    chars += punctuation
if exc == "y":
    chars = [i for i in chars if i not in "il1Lo0O"]

print("Доступные символы")
print(*chars, sep="")
print("Пароль(-и):")
for _ in range(cntP):
    print(generate_password(lenP, chars))