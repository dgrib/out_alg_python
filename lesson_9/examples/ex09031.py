import hashlib


print(hashlib.sha1(b'Hello World!').hexdigest())

print(hashlib.sha1(b'Hello World.').hexdigest())

# чтобы не подменили письмо надо секретное слово
# об этом слова знает пользователь 1 и 2, но само слово
# не должно быть в письме (о нем не должен знать человек,
# перехватывающий письмо) теперь даже если письмо перехватить,
# то подделать хеш не получится
print(hashlib.sha1(b'esrgbetv' + b'Hello World.').hexdigest())

# но если дописать в конце письма сообщение любое, взять хеш
# в письме и досчитать к этому хешу хеш от нового добавленного куска

# сохраним в s хеш письма
s = hashlib.sha1(b'Hello World.').hexdigest()
# переводим его из байт в формат utf-8
print(s.encode('utf-8'))
# теперь чтобы сделать хеш подпись письма будем использовать
# не сам текст письма а уже полученную хеш-подпись

# в начале идет секретное слово, далее идет хеш полученный
# на основе нашего письма и все это приводится в 16 формат
print(hashlib.sha1(b'esrgseer' + bytes(s.encode('utf-8'))).hexdigest())
# получили хешподпись которую подделать не получится,
# подсчитать хешподпить не полусится
