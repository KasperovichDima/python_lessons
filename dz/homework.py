# 1 Открыв файл anthem_1 в режиме чтения - прочитайте
# и выведите на экран все содержимое файла.
with open('anthem_1', 'r') as f:
    print(f.read())

print('\n')
# 2. Открыв файл anthem_2 в режиме чтения - прочитайте
# и выведите на экран первые 2 строки файла.
with open('anthem_2', 'r') as f:
    print(f.readline())
    print(f.readline())

# 3. Открыв файл в режиме чтения - прочитайте
# и выведите на экран список всех строк файла anthem_2.
with open('anthem_2', 'r') as f:
    print(f.readlines())

# 4. Сложное задание!
# Откройте файл anthem_1 в режиме чтения.
# Откройте файл anthem_2 в режиме чтения.
# Откройте файл anthem_full в режиме записи. Будет создан автоматически.
# Запишите в файл сперва все содержимое файла anthem_1
# Запишите в файл сперва все содержимое файла anthem_2
# Не забывайте про перенос строк ('\n')
with open('anthem_1', 'r') as source1:
    with open('anthem_2', 'r') as source2:
        with open('anthem_full', 'w') as target:
            target.write(source1.read())
            target.write('\n\n')
            target.write(source2.read())

# 5. Нагуглите автора Американского гимна
# и добавьте его в конец файла anthem_full
# через пустую строку.
with open('anthem_full', 'a') as f:
    f.write('\n\nFrancis Scott Key')

# 6. Проверьте что все получилось как надо.
