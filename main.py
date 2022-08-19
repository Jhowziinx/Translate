from translate import Translator
import translate
from time import sleep

x = input('''Como voce deseja traduzir?
[1] Português -> Inglês
[2] Inglês -> Português
\>''')

if x == '1':
    tra = Translator(from_lang='pt-br', to_lang='english')
    pt = input('Digite oq deverá ser traduzido:')
    en = tra.translate(pt)
    print(f'"{pt}" em inglês ficará "{en}".')
elif x == '2':
    tra = Translator(from_lang='english', to_lang='pt-br')
    en = input(str('Digite oq deverá ser traduzido:'))
    pt = tra.translate(en)
    print(f'"{en}" em portugues ficará "{pt}".')
else:
    print('Error! Digite um valor válido')
    sleep(1.5)
    

    