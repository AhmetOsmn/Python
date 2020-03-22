
import math #math modülünü eklemiş olduk
#help(math) #math modulundeki fonksiyonların kullanımlarını veiryor.
#print(math.factorial(5))
#import math as matematik #math modülünü matemmatik ismi ile kullanmak isitoyrum demek.

from math import * #farklı bir kullanım olarak:
                   #(*)math modülündeki bütün fonksiyonları import et demek.

print(factorial(5)) #from math import * şeklinde kullanım yaparsak,
                    #math.factorial() yerine direkt factorial() olarak kullanabiliyoruz.


from math import floor,ceil
factorial(5) # tanınmmaz.

#eger math modulundekiyle aynı isimde fonksiyon tanımlarsak,
#en son hangisi tanımlanmışsa o fonksiyonu kullanır.
