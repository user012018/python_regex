
# -*- coding: UTF-8 -*-
# //coding: utf-8
# coding=utf-8
# vim: set fileencoding=utf-8 :
# print "Content-Type: text/html\r\n"
    # re.match()
    # re.search()
    # re.findall()
    # re.split()
    # re.sub()
    # re.compile()
# https://python-scripts.com/no-lambda
# d:\dev\ppt\numpy-python-and-regex-tutorial.ipynb-------------------!!!!!!!!!!!!1

import pandas as pd
import numpy as np
import re
from numpy import array



r = re.compile('[Ab]')
vmatch = np.vectorize(lambda x:bool(r.match(x)))

A = np.array(list('abc abc abc'))
sel = vmatch(A)

for i in range(len(A)):
    pass
    # print(A[i],sel[i])
# print(A)
# print(sel)

# boolprint=False
boolprint=True

text = "AV Fnohkoh Hdind AV"

text = "0001-01-01T00:00:00"

regEX = r"\w+"
regEX = r"0001-01-01T00:00:00"
# regEX = r'AV'
pattern = re.compile(regEX)
# pattern = re.compile('AV')

if boolprint: print(dir(pattern))
search = pattern.search(text)

if boolprint: print('>search:')
if boolprint: print(search.group())
if boolprint: print('searchs:',search.groups())
if boolprint: print(type(search.group()))
# indices = [i for i,x in enumerate(pattern.search(text))]
# if boolprint: print(indices)
if boolprint: print()


search = pattern.findall(text)
if boolprint: print('>findall:')
if boolprint: print(search)
if boolprint: print('findall:',search)
if boolprint: print(type(search))
# indices = [i for i,x in enumerate(pattern.search(text))]
# if boolprint: print(indices)
if boolprint: print()

# line = 'asdf fjdk;afed,fjek,asdf,foo'
# result = re.sub(r'[;,\s]',' ', line) # asdf fjdk afed fjek asdf foo
# osub = pattern.sub(text)
osub = re.sub(regEX,' ', text)
if boolprint: print('>sub:')
if boolprint: print('sub (len):',len(osub))
if boolprint: print(type(osub))
# indices = [i for i,x in enumerate(pattern.search(text))]
# if boolprint: print(indices)
if boolprint: print()

omatch = pattern.match(text)
if boolprint: print('>math:')
if boolprint and type(omatch)!=type(None): print(omatch.group())
if boolprint and type(omatch)!=type(None): print(type(omatch.group()))
# indices = [i for i,x in enumerate(pattern.match(text))]
# if boolprint: print(indices)
if boolprint: print()

findall = pattern.findall(text)
if boolprint: print('>findall:')
if boolprint: print(findall)
if boolprint: print(type(findall))
indices = [i for i,x in enumerate(pattern.findall(text))]
if boolprint: print('ind:findall:iter->',indices)
if boolprint: print()

finditer = pattern.finditer(text)
if boolprint: print('>finditer:')
if boolprint: print(finditer)
if boolprint: print(type(finditer))
indices = [i for i,x in enumerate(pattern.finditer(text))]
if boolprint: print('ind:finditer:iter->',indices)
if boolprint: print()

for anObject in finditer:
    pass
    if boolprint: print('---finditer.group()->iter:',anObject.group()) # .group(0) all .group(1) first
    if boolprint: print('---finditer.groups()->iter:',anObject.groups())
    if boolprint: print(type(anObject.group()))
    if boolprint: print()  

print('--------------------------')


a = array(['zzzz', 'zzzd', 'zzdd', 'zddd', 'dddn', 'ddnz', 'dnzn', 'nznz',
       'znzn', 'nznd', 'zndd', 'nddd', 'ddnn', 'dnnn', 'nnnz', 'nnzn',
       'nznn', 'znnn', 'nnnn', 'nnnd', 'nndd', 'dddz', 'ddzn', 'dznn',
       'znnz', 'nnzz', 'nzzz', 'zzzn', 'zznn', 'dddd', 'dnnd'], dtype=object)

'''>>> import re
>>> sequence = 'aaabbbaaacccdddeeefff'
>>> query = 'aaa'
>>> r = re.compile(query)
>>> [[m.start(),m.end()] for m in r.finditer(sequence)]
[[0, 3], [6, 9]]'''
# print('\n'.join([x for x in a]))   # for make reg exp expression  
 

def func(ar,pattern):
    indices = [i for i,x in enumerate(ar) if re.match(pattern,x)]
    # print(indices)                # [2, 3, 10, 11, 20, 29]
    return ar.take(indices)     # ['zzdd' 'zddd' 'zndd' 'nddd' 'nndd' 'dddd']

# print('re.match in array:',func(a,"..dd$")) # ['zzdd' 'zddd' 'zndd' 'nddd' 'nndd' 'dddd']
# print(func(a,"n{2}")) #['nnnz' 'nnzn' 'nnnn' 'nnnd' 'nndd' 'nnzz']
print('re.match in array:',func(a,"d{3}")) 



s = pd.Series(['zzzz', 'zzzd', 'zzdd', 'zddd', 'dddn', 'ddnz', 'dnzn', 'nznz',
'znzn', 'nznd', 'zndd', 'nddd', 'ddnn', 'dnnn', 'nnnz', 'nnzn',
 'nznn', 'znnn', 'nnnn', 'nnnd', 'nndd', 'dddz', 'ddzn', 'dznn',
 'znnz', 'nnzz', 'nzzz', 'zzzn', 'zznn', 'dddd', 'dnnd'])
# print(s[s.str.endswith("dd")])
'''
2     zzdd
3     zddd
10    zndd
11    nddd
20    nndd
29    dddd
dtype: object
'''
# s[s.str.endswith("dd")].values
'''array(['zzdd', 'zddd', 'zndd', 'nddd', 'nndd', 'dddd'], dtype=object)'''
# print(s[s.str.match(".*dd$")])
'''
2     zzdd
3     zddd
10    zndd
11    nddd
20    nndd
29    dddd
dtype: object
'''
rra = pd.Series(['zzzz', 'zzzd', 'zzdd', 'zddd', 'dddn', 'ddnz', 'dnzn', 'nznz',
'znzn', 'nznd', 'zndd', 'nddd', 'ddnn', 'dnnn', 'nnnz', 'nnzn',
 'nznn', 'znnn', 'nnnn', 'nnnd', 'nndd', 'dddz', 'ddzn', 'dznn',
 'znnz', 'nnzz', 'nzzz', 'zzzn', 'zznn', 'dddd', 'dnnd'])
arr=array([['zzzz', 'zzzd', 'zzdd'],
       ['zzzz', 'zzzf', 'zzdd'],
       ['zzzz', 'zzzd', 'zzdd']])
# arr1=array(['zzzz', 'zzzd', 'zzdd'])       
# print(func(arr1,"z")) 
# print(arr.ndim)
# arr=arr.reshape(1,9)
# arr=arr.flatten()
arr=arr.flatten().reshape(arr.shape)
print(arr)
# exit()
# '''
print('arr.shape', 'Array dimensions',arr.shape)
print('len(arr)', 'Length of array',len(arr))
print('arr.ndim' ,'Number of array dimensions',arr.ndim)
print('arr.size' ,'Number of array elements',arr.size)
print('arr.dtype' ,'Data type of array elements',arr.dtype)
print('arr.dtype.name',arr.dtype.name)
# print(arr)

arr = np.array(["AB", "AC", "XAB", "XAC", "AD"])                #  to add "X" in the  based on a regex match of "^A".
print(np.array(list(map(lambda v: re.sub(r'^A','XA', v) ,arr))))  # ['XAB' 'XAC' 'XAB' 'XAC' 'XAD']

f = open('test.dat', 'w')
f.write("1312 foo\n1534  bar\n444   qux")
f.close()
regexp = r"(\d+)\s+(...)"  # match [digits, whitespace, anything]
output = np.fromregex('test.dat', regexp,
                      [('num', np.int64), ('key', 'S3')])
'''
>>> output
array([(1312L, 'foo'), (1534L, 'bar'), (444L, 'qux')],
      dtype=[('num', '<i8'), ('key', '|S3')])
>>> output['num']
array([1312, 1534,  444], dtype=int64)
'''
# '''

# --------------------------convert array /Dataframe/ (only one column) to list /Series/ and search by patter
pattern8 = re.compile(r'.*',re.I)
# print(np.where(arr =='zzzz', 3, 2))
# print(np.where(rra.contains(pattern8), 3, 2))
tmp_list_type = map(lambda x: x[1], arr) # get one column  # tmp_list_type = arr.tolist()
s1 = pd.Series(tmp_list_type)
# print(s1.str.contains('d', regex=False))
'''
0     True
1    False
2     True
dtype: bool
'''
# ==========================================================================

'''   replace count find found !!!!!

import re
s = "15301 Query	SELECT COUNT(*) FROM designers WHERE id > 0 AND id_order IN ()"
replaced = re.sub('[0-9]+\s?Query\s?', '--', s)

print(replaced) 
print(re.sub(r'(;)([a-zA-Z<]+)', r'\g<1>123\g<2>', 'on;use Bi'))

re.sub(r'(foo)', r'\g<1>123', 'foobar')
# foobar with foo123bar

matches = re.findall("\w{6,}", f.read())

matches = re.findall("SELECT", 'SELECT (SELECT DISTINCT name FR')
print((matches))    #   ['SELECT', 'SELECT']

fault
            'long.file.name.jpg' -> 'long.file.name_suff.jpg'
            'long.file.name_a.jpg' -> 'long.file.name_suff.jpg'
             re.sub(r'(?:_a)?\.([^.]*)$', r'_suff.\1', "long.file.name.jpg")

            replacedString = re.sub(pattern, replacement_pattern, input_str, count, flags=0)

            v = "running eating reading"
            v = re.sub(r"r.*?ing", "ring", v)
                            ring eating ring

            print re.sub(r'r.*?выпущен', u' \1', r"ппе древесные шипровые. выпущен в 2009 году. Парфюмер: .").decode('utf-8').encode('cp1251')
            regexp = re.compile(r'[а-я]')
            #~ Проверьте, теперь команда
            print re.sub(regexp, '', r'КрасОТИЩЕ')
            exit()
'''

CARRIS_REGEX=r'<th>(\d+)</th><th>([\s\w\.\-]+)</th><th>(\d+:\d+)</th><th>(\d+m)</th>'
pattern = re.compile(CARRIS_REGEX, re.UNICODE)
# mailbody = open("test.txt").read()
mailbody=''''''
for match in pattern.finditer(mailbody):
    print(match)
print()
for match in pattern.findall(mailbody):
    print(match)
'''
<_sre.SRE_Match object at 0x00A63758>
<_sre.SRE_Match object at 0x00A63F98>

('790', 'PR. REAL', '21:06', '04m')
('758', 'PORTAS BENFICA', '21:10', '09m')
'''
for match in pattern.finditer(mailbody):
    print(tuple(match.groups()))
    
    
    
    
    
    
    
text = "He was carefully disguised but captured quickly by police."

regEX = r"\w+ly"
pattern = re.compile(regEX)

search = pattern.search(text)
# print(search)
# print(type(search))
# print()

findall = pattern.findall(text)
# print(findall)
# print(type(findall))
# print()

finditer = pattern.finditer(text)
# print(finditer)
# print(type(finditer))
# print()
for anObject in finditer:
    pass
    # print(anObject)
    # print(type(anObject))
    # print()    
    
    
    
n='3 4 4 5 5 5 2 2'
n='44 555 22'
    
x=[x for x,y in re.findall(r'((\d)\2+)', '33344555')]   # ('333', '44', '555')   
    
x=[x for x,y in re.findall(r'((\d)(?: \2)+)', '3 3 3 4 4 5 5 5')]   #  ['3 3 3', '4 4', '5 5 5']

x=re.findall(r'(\d)(\1+)', n) # [('4', '4'), ('5', '55'), ('2', '2')]

x=[''.join(i) for i in re.findall(r'(\d)(\1+)', n)] # ['44', '555', '22']

x = re.findall(r"((\d)\2+)", "34455522") # -> [('44', '4'), ('555', '5')]

x = [elem[0] for elem in x] # -> ['44', '555']

# ---------------------------------re.match(pattern, string):
import re
result = re.match(r'AV', 'AV Fnohkoh Hdind AV')
# print result
# result = re.match(r'AV', 'AV Fnohkoh Hdind AV')
# print result.group(0)
result = re.match(r'AV', 'AV Fnohkoh Hdind AV')
# print result.start()
# print result.end()
# Также есть методы start() и end() для того, чтобы узнать начальную и конечную позицию найденной строки.

li = ['9999999999', '999999-999', '99999x9999']

for val in li:
    if re.match(r'[8-9]{1}[0-9]{9}', val) and len(val) == 10:
        pass
        # print 'yes'
    else:
        # print 'no'
        pass




#-------------------------------- re.search(pattern, string):

# Этот метод похож на match(), но он ищет не только в начале строки. В отличие от предыдущего, search() вернет объект, если мы попытаемся найти «Fnohkoh».

result = re.search(r'Fnohkoh', 'AV Fnohkoh Hdind AV')
# print result.group(0)


# ------------------- re.findall(pattern, string):

# Этот метод возвращает список всех найденных совпадений. У метода findall() нет ограничений на поиск в начале или конце строки. Если мы будем искать «AV» в нашей строке, он вернет все вхождения «AV». Для поиска рекомендуется использовать именно findall(), так как он может работать и как re.search(), и как re.match().

result = re.findall(r'AV', 'AV Fnohkoh Hdind AV')
# print result  # ['AV', 'AV']

result = re.findall(r'@\w+.\w+', 'abc.test@gmail.com, xyz@test.in, test.first@FnohkohHdind.com, first.test@rest.biz') # ['@gmail.com', '@test.in', '@FnohkohHdind.com', '@rest.biz']

result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009') # ['12-05-2007', '11-11-2011', '12-01-2009']

result = re.findall(r'[aeiouAEIOU]\w+', 'AV is largest Fnohkoh community of India') # ['AV', 'is', 'argest', 'Fnohkoh', 'ommunity', 'of', 'India']

test_str='1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily'

result = re.findall(r'\d([A-Z][A-Za-z]+)([A-Z][A-Za-z]+)', test_str) # [('Noah', 'Emma'), ('Liam', 'Olivia'), ('Mason', 'Sophia'), ('Jacob', 'Isabella'), ('William', 'Ava'), ('Ethan', 'Mia'), ('Michael', 'Emily')]



# -------------re.split(pattern, string, [maxsplit=0]):

# Этот метод разделяет строку по заданному шаблону.
result = re.split(r'h', 'Fnohkoh')
# print result # ['Fho', 'koh']

line = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").
result = re.split(r'[;,\s]', line) # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']





# -----------------re.sub(pattern, repl, string):

# Этот метод ищет шаблон в строке и заменяет его на указанную подстроку. Если шаблон не найден, строка остается неизменной.
result = re.sub(r'India', 'the World', 'AV is largest Fnohkoh community of India')
# print result  # 'AV is largest Fnohkoh community of the World'

line = 'asdf fjdk;afed,fjek,asdf,foo'
result = re.sub(r'[;,\s]',' ', line) # asdf fjdk afed fjek asdf foo



# --------------- re.compile(pattern, repl, string):

# Мы можем собрать регулярное выражение в отдельный объект, который может быть использован для поиска. Это также избавляет от переписывания одного и того же выражения.
pattern = re.compile('AV')
result = pattern.findall('AV Fnohkoh Hdind AV') # ['AV', 'AV']
result2 = pattern.findall('AV is largest Fnohkoh community of India') # ['AV']

'''
re.A / re.ASCII

Флаг ASCII указывает Python сопоставлять против ASCII, вместо использования полного Юникода для сопоставления, в сочетании со следующими кодами: w, W, b, B, d, D, s и S. Также существует флаг re.U / re.UNICODE, который используется в целях обратной совместимости. В любом случае, эти флаги являются излишеством, так как Python выполняет сопоставления в Юникоде в автоматическом режиме.
re.DEBUG

Данный флаг показывает информацию о дебаге вашего скомпилированного выражения.
re.I / re.IGNORECASE

Если вам нужно выполнить сравнение без учета регистра, тогда этот флаг – то, что вам нужно. Если ваше выражение было [a-z] и вы скомпилировали его при помощи этого флага, то ваш паттерн сопоставит заглавные буквы в том числе. Это также работает для Юникода и не влияет на текущую локаль.
re.L / re.LOCALE

Данный флаг делает коды: w, W, b, B, d, D, s и S зависимыми от нынешней локали. Однако, в документации говорится, что вы не должны зависеть от данного флага, так как механизм локали сам по себе очень ненадежный. Вместо этого, лучше используйте сопоставление Юникода. Далее в документации говорится, что данный флаг имеет смысл использовать только в битовых паттернах.
Мы собрали ТОП Книг для Python программиста которые помогут быстро изучить язык программирования Python. Список книг: Книги по Python
re.M / re.MULTILINE

Когда вы используете данный флаг, вы говорите Python, чтобы он использовал символ паттерна ^ для начала строки, и начало каждой линии. Он также указывает Python, что $ должен сопоставить конец каждой строки и конец каждой линии, что не сильно отличается от их значений по умолчанию. Вы можете обратиться к документации для дополнительной информации.
re.S / re.DOTALL

Этот забавный флаг указывает метасимволу «.» (период) сопоставить любой символ. Без этого флага, данный метасимвол будет сопоставлять все, что угодно, но не новую строку.
re.X / re.VERBOSE

Если вы считаете, что ваши регулярные выражения не слишком читабельные, тогда данный флаг – это то, что вам нужно. Он позволяет визуально разделять логические секции ваших регулярных выражений, и даже добавлять комментарии! Пустое пространство внутри паттерна будет игнорироваться, кроме того случая, если классу символа или пробелу предшествует обратная косая черта.



'''
