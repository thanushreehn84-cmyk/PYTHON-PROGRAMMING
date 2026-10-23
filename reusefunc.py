
def emoji_convertor(messege):
    words=messege.split(" ")
    emojis={
    ":)":"😄",
    ":(":"😭"
    }
    output=" "
    for word in words:
        output+=emojis.get(word,word) +" "
    return output


messege=input()
print(emoji_convertor(messege))
