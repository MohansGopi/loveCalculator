print('''
__,,,__
                ,-""-,-"       "-,-""-,
               /,-' , .-'-.7.-'-. , '-,\
               \(    /  _     _  \    )/
                '-,  { (0)   (0) }  ,-'
                 /    >  .---.  <    \
                |/ .-'   \___/   '-. \|
                {, /  ,_       _,  \ ,}
                \ {,    \     /    ,} /
                 ',\.    '---'    ./,'
             _.-""""""-._     _.-""""""-._
           .'            `._.`            '.
         _/_               _                \
      .'`   `\            | |                \
     /        |           | |                 ;
     |        /           |_|                 |
     \  ;'---'    _    ___  _  _  ___         ;
      '. ;       | |  /   \| || ||  _|     _ ;
        `-\      | |_ | | || |/ /|  _|   .' `,
           `\    |___|\___/ \__/ |___|  |     \
             \            _ _           \     |
         jgs  `\         | | |         /`   _/
    ,-""-.    .'`\       | | |       /`-,-'` .-""-,
   /      `\.'    `\     \___/     /`    './`      \
  ;  .--.   \       '\           /'       /   .--.  ;
  | (    \   |,       '\       /'        |   /    ) |
   \ ;    }             ;\   /;         `   {    ; /
    `;\   \         _.-'  \ /  `-._         /   /;`
      \ \__.'   _.-'       Y       `-._    '.__//
       '.___,.-'                       `-.,___.

''')


your_name = input("enter your name : ")
your_partner = input("enter your partner name : ")

your_name_lowercase = your_name.lower()
your_partner_lowercase = your_partner.lower()

r = your_name_lowercase.count("r") + your_partner_lowercase.count("r")
e = your_name_lowercase.count('e') + your_partner_lowercase.count('e')
a = your_name_lowercase.count('a') + your_partner_lowercase.count('a')
l = your_name_lowercase.count('l') + your_partner_lowercase.count('l')
real = r + e + a + l

l = your_name_lowercase.count('l') + your_partner_lowercase.count('l')
o = your_name_lowercase.count('o') + your_partner_lowercase.count('o')
v = your_name_lowercase.count('v') + your_partner_lowercase.count('v')
e = your_name_lowercase.count('e') + your_partner_lowercase.count('e')
love = l + o + v + e

real_love = int(f"{real}{love}")

if real_love <= 20:
  print(f"Your score is {real}{love}%, you are like coke and mentos")
elif (real_love>20) or (real_love<70):
  print(f"Your score is {real_love}%, you are alright together")
elif real_love>=70:
  print(f"Your score is {real_love}%, the fairy tales comes true")







