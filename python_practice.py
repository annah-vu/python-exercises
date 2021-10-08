def fibonacci(x):
    n = x
    n1 = 0
    n2 = 1

    count = 0

    if n > 1:
        while count < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth

            count +=1
    elif n == 1:
        print(n1)
    else:
        print('Please enter a positive integer')


def palindrome(sentence):
    sentence = sentence.replace(' ','')
    forward = list(sentence)
    backward = list(sentence)
    backward.reverse()
    if str(forward) == str(backward):
        return True
    else:
        return False


def check_palindrome(sentence):
    if len(sentence) %2 ==0:
        for i in range(int(len(sentence)/2)):
            if sentence[i] != sentence[-i-1]:
                return False
        return True
    
    else: 
        for i in range(int((len(sentence)-1)/2)):
            if sentence[i] != sentence[-i-1]:
                return False
        return True
