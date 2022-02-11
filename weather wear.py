weather = input('what is the weather?: ')

if weather ==  'rain' or weather == 'rainy':
    wear = 'a rain jacket'
elif weather == 'snow':
    wear = 'a warm jacket'
elif weather == 'hot':
  wear = 'some shorts'
else:
    wear = 'sandals'

print('todays weather is ' + weather + ', you should wear ' + wear)