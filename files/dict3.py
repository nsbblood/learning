import time

fruits={
'blackberry' : 'die Brombeere',
'grapefruit' : 'die Grapefruit',
'mango'  : 'die Mango',
'kiwi' : 'die Kiwi',
'fig' : 'die Feige',
'raspberry' : 'die Himbeere',
'apricot' : 'die Aprikose',
'pineapple' : 'die Ananas',
'lemon' : 'die Zitrone',
'watermelon' : 'die Wassermelone',
'peach' : 'der Pfirsich',
'plum' : 'die Pflaume',
'grape' : 'die Traube',
'cherry' : 'die Kirsche',
'blueberry' : 'die Blaubeere',
'strawberry' : 'die Erdbeere',
'orange' : 'die Orange',
'pear' : 'die Birne',
'banana' : 'die Banane',
'apple' : 'der Apfel'

}

for fruit in fruits:                  #write line by line
  print(fruit, ":", fruits[fruit])
  time.sleep(0.5)


