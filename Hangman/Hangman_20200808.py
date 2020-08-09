import random
import os
import time

##---------------------------- Importing word from word bank
filename='Word library.txt'

numLines = 0
with open(filename,'r') as fin:
    for line in fin:
        numLines = numLines+1
    print("Number of lines is %i" % numLines)  


word_index=random.randint(1,numLines)
print("Number of index selected is %i" % word_index)

with open(filename,'r') as fin:
    for i in range(word_index):
        word=fin.readline()
print(word)
##---------------------------- Functions for partitioning and combining strings and arrays


def parse(val):
    var=list(val)
    return var


def combine(val):
    var=''
    for i in range(0, len(val)):
        var+= val[i]
    return var

def cls(): os.system("cls")#print( "\n" * 100)
    
class man:
    stage=0
    pics={0:'',
          1:'0',
          2:'0-',
          3:'0/-',
          4:'0>-',
          5:'0>-/',
          6:'0>-<',
    }
    def pic(self):
        return self.pics[self.stage]

##----------------------------- Create blank word space

word=parse(word)
uncovered=''
if word_index==numLines:
    uncovered += '-'
    
for x in range(len(word)-1):
    uncovered += '-'
print(uncovered)

uncovered=combine(uncovered)

##----------------------------- this is where the game runs
playing=1;
cls() #clear shell
list_guesses=[]
rob=man()
word=parse(word)

num_wrong=0
num_right=0

while playing:
    n=len(word)-1
    print(("\n Number of letters: %i"% n)+"\n Word:"+uncovered+"\n Hanging Man: "+rob.pic()+"\n Previous guesses:")
    print(list_guesses)
    c_guess=input("Guess a letter:")

    cls() #clear shell

    skip=0
    guess_correct=0
    listcorrect=[]

    if c_guess == '':
        skip=1
        
        
    
    for x in range(len(word)):
        if word[x]==c_guess:
            guess_correct=1
            listcorrect.append(x)


    for i in range(len(list_guesses)):
        if c_guess==list_guesses[i]:
            print("\n Letter already guessed! \n")
            skip=1
            
    if skip==0:
        if guess_correct: #what happens if guess is correct
            
            if len(listcorrect)==1:
                verb="is "
                appos=""
            else:
                verb="are "
                appos="'s"
                
            print("\n"+"there "+ verb+ "%i %s" % (len(listcorrect), c_guess) + appos)
            uncovered=parse(uncovered)
            for i in listcorrect:
                uncovered.insert(i,c_guess)
                del uncovered[i+1]
                num_right+=1
            uncovered=combine(uncovered)
            list_guesses.append(c_guess)
        
        else: #what happens if guess is incorrect
            num_wrong+=1
            rob.stage+=1
            print(("\n"+"there are no %s's" %  c_guess) +"\n")
            list_guesses.append(c_guess)
            
    if num_wrong == 6: #if wrong guesses are too many
        word=combine(word)
        print('\n the word was %s' % word)
        print('\n'+ rob.pic())
        print('\n \n GAME OVER...')
        break
    
    if num_right == n: #if the word is guessed correctly
        print("\n the word is %s" % uncovered)
        print('\n \n \n YOU WIN')
        break
    
time.sleep(5)
