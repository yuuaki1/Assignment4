import numpy as np
score=0
for i in range (10):
    x=np.random.randint(9)
    y=np.random.randint(9)
    ans=x*y
    answ=int(input('Question{}: {}x{}= '.format(i+1,x,y)))
    if answ==ans:
        print('Correct')
        score+=1
    else:
        print('OOPS! wrong answer correct answer is ',ans)
print('Your score is- ',score)
