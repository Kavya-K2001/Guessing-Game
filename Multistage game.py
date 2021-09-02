import random
stage = 3
levels = 0
while levels <3:
    levels +=1
    if levels <= stage:
      print('Enter the value of x which shows the range:')
      x =0
      x=int(input())
      number = random.randint(1, x)
      print('Hi , start guessing the number from 1-'+ str(x) +'range')

      number_of_guesses = 0
      while number_of_guesses < 5:
         guess = int(input())
         number_of_guesses += 1
         if guess < number:
           print('Your guess is too low')
         if guess > number:
           print('Your guess is too high')
         if guess == number:
           break
      if guess == number:
        print('You win the game in ' + str(number_of_guesses) + ' tries! ')
      else:
        print('You did not guess the number, you lose')
    
    
