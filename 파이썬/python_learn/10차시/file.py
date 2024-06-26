infile = open('c:\\Users\\Jin\\Desktop\\proverbs.txt','r')

for line in infile:
    word_list = line.split()
    for word in word_list:
        print(word)

infile.close()

key = 'abcdefghijklmnopqrstuvwxyz'

# 평문을 받아서 암호화하고 암호문을 반환한다.
def encrypt(n, plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            if l == ' ':  # 공백인 경우 그대로 추가
                result += ' '
            else:
                i = (key.index(l) + n) % 26
                result += key[i]
        except ValueError:
            result += l
    return result.lower()

# 암호문을 받아서 복호화하고 평문을 반환한다.
def decrypt(n, ciphertext):
    result = ''
    for l in ciphertext:
        try:
            if l == ' ':  # 공백인 경우 그대로 추가
                result += ' '
            else:
                i = (key.index(l) - n) % 26
                result += key[i]
        except ValueError:
            result += l
    return result

n = 3
text = 'The language of truth is simple.'
encrypted = encrypt(n, text)
decrypted = decrypt(n, encrypted)

print('평문: ', text)
print('암호문: ', encrypted)
print('복호문: ', decrypted)
