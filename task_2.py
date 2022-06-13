def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Permyakov', name='Andrey', year='1997', city='Tomsk', email='home@mail.ru',
              telephone='8-999-111-22-33'))