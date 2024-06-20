#Unicode database defines all character properties
#importing module for providing access to this module
import unicodedata
#it returns symbol or character by their name
print(unicodedata.lookup('semicolon'))
#it returns name by their character
print(unicodedata.name('!'))
#print(unicodedata.decimal('&'))
print(unicodedata.digit('0'))
#print(unicodedata.numeric('!'))
#it returns general category assigned to character as string
print(unicodedata.category('&'))
print(unicodedata.bidirectional('!'))
print(unicodedata.combining('!'))
print(unicodedata.east_asian_width('!'))
print(unicodedata.mirrored('!'))
print(unicodedata.decomposition('!'))
