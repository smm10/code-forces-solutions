n = input()
i_hate = "I hate"

i_love = "I love"
that = " that "

it = " it"

answer = ""


for i in range(1,int(n)+1):
    if(i%2==0):
        if (answer!=""):
            answer = answer+that+ i_love
        else:
            answer = answer + i_love

    else:
        if (answer!=""):
            answer = answer+that+ i_hate
        else:
            answer = answer + i_hate

answer  = answer + it
    
print(answer)
    