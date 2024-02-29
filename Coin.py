import random
while True:
    b=int(input('How many times you want to flip -'))
    c=input("Type start to Flip")
    if c=='start':
        cnt1=0
        cnt2=0
        List=['Heads','Tails']
        for i in range(b):
            a=random.choice(List)
            if a=='Heads':
                cnt1=cnt1+1
            else:
                cnt2=cnt2+1
            print(a)
        print('Heads Count =',cnt1)
        print('Tails Count =',cnt2)
        print('Want to try again - y/n')
        k=input('')
        if k=='n':
            print('Thanks for plying')
            break
        
    else:
        print('Just Type the Fucking ''start'' text')



    