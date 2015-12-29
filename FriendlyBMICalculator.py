print('Please enter your name: ')
n = input()
print('Hello ', n, '!\n', sep='')
print('Please enter your weight in kg: ')
w = float(input())
print('Now, enter your height in m: ')
h = float(input())
BMI = w / h / h
if BMI < 15:
  print('You are very severely underweight.\n')
elif 15 <= BMI and BMI < 16:
  print('You are severely underweight.\n')
elif 16 <= BMI and BMI < 18.5:
  print('You are underweight.\n')
elif 18.5 <= BMI and BMI < 25:
  print('Congratulation, you\'re very healthy. Keep going on.\n')
elif 25 <= BMI and BMI < 30:
  print('You are overweight.\n')
elif 30 <= BMI and BMI < 35:
  print('You are moderately obese.\n')
elif 35 <= BMI and BMI < 40:
  print('You are severely obese.\n')
elif 40 < BMI:
  print('You are very severely obese.\n')
print('Data and classification from Wikipedia.\nKeep fit everyday.Goodbye ', n, '!\n', sep='')