def test_substring(full_string, substring):
    assert str(substring) in str(full_string), f"expected '{substring}' to be substring of '{full_string}'"


x1 = 'fulltext'
x2 = 'some_value'
test_substring(x1, x2)

# некий текст является подстрокой другого текста
s = 'My Name is Julia'
# с помощью ключевого слова in
if 'Name' in s:
    print('Substring found')

#  с помощью функции find
index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

# для проверки того,
# что в текущем url содержится строка login:
# assert "login" in browser.current_url, # сообщение об ошибке
