ulang = "y"
while ulang == "y":
    text = input(str("masukkan text: "))
    text = text.casefold()
    balik_text = reversed(text)

    if list(text) == list(balik_text):
        print(text, " is a Palindrome")
    else:
        print(text, " is not a Palindrome")
    ulang = input("coba lagi?(y/n)")