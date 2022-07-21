from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 01. Добавить одну книгу.
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        assert len(collector.get_books_rating()) == 1, 'Книга не добавлена!'

    # 02. Добавить эту же книгу повторно.
    def test_add_new_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        collector.add_new_book('Зеленая миля')
        assert len(collector.get_books_rating()) == 1, 'Одна книга добавлена 2 раза!'

    # 03. Добавить рейтинг к несуществующей книге.
    def test_add_rating_to_not_in_list_book(self):
        collector = BooksCollector()
        collector.set_book_rating('Зеленая миля', 9)
        assert len(collector.get_books_rating()) == 0, 'Рейтинг добавлен!'

    # 04. Добавить рейтинг меньше 1.
    def test_add_rating_below_1(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        collector.set_book_rating('Зеленая миля', -1)
        assert collector.get_book_rating('Зеленая миля') == 1, 'Рейтинг меньше 1!'

    # 05. Изменить рейтинг на 5.
    def test_add_rating_equal_5(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        collector.set_book_rating('Зеленая миля', 5)
        assert collector.get_book_rating('Зеленая миля') == 5, 'Рейтинг не обновился!'

    # 06. Добавить рейтинг больше 10.
    def test_add_rating_above_10(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        collector.set_book_rating('Зеленая миля', 11)
        assert collector.get_book_rating('Зеленая миля') == 1, 'Рейтинг больше 10!'

    # 07. Добавить книгу в избранное.
    def test_add_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        collector.add_new_book('Долгая прогулка')
        collector.add_book_in_favorites('Долгая прогулка')
        assert collector.get_list_of_favorites_books() == ['Долгая прогулка'], 'Книга не добавлена в избранное!'
        assert len(collector.get_list_of_favorites_books()) == 1, 'Список избранного пустой!'

    # 08. Удалить книгу из избранного.
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        collector.add_new_book('Долгая прогулка')
        collector.add_book_in_favorites('Долгая прогулка')
        collector.delete_book_from_favorites('Долгая прогулка')
        assert len(collector.get_list_of_favorites_books()) == 0, 'Список избранного не пустой!'

    # 09. Добавить несуществующую книгу в избранное.
    def test_add_not_in_list_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Долгая прогулка')
        assert len(collector.get_list_of_favorites_books()) == 0, 'Несуществующая книга добавлена в избранное!'

    # 10. Вывести список избранного.
    def test_get_favorites_books_list(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        collector.add_new_book('Долгая прогулка')
        collector.add_book_in_favorites('Долгая прогулка')
        collector.add_book_in_favorites('Зеленая миля')
        assert len(collector.get_list_of_favorites_books()) != 0, 'Список избранного пустой!'

    # 11. Вывести весь список.
    def test_get_books_list(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        collector.add_new_book('Долгая прогулка')
        assert len(collector.get_books_rating()) != 0, 'Список книг пустой!'

    # 12. Вывести список с определенным рейтингом.
    def test_get_books_list_with_specified_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        collector.add_new_book('Долгая прогулка')
        collector.add_new_book('Бегущий человек')
        collector.set_book_rating('Долгая прогулка', 3)
        collector.set_book_rating('Бегущий человек', 8)
        assert collector.get_books_with_specific_rating(3) == ['Долгая прогулка'], 'Нет книги с таким рейтингом!'
        assert collector.get_books_with_specific_rating(8) == ['Бегущий человек'], 'Нет книги с таким рейтингом!'


    # 13. Вывести рейтинг по названию.
    def test_get_rating_by_the_title(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        collector.add_new_book('Долгая прогулка')
        collector.add_new_book('Бегущий человек')
        collector.set_book_rating('Долгая прогулка', 9)
        collector.set_book_rating('Бегущий человек', 2)
        assert collector.get_book_rating('Долгая прогулка') == 9, 'Рейтинг не совпадает!'
        assert collector.get_book_rating('Бегущий человек') == 2, 'Рейтинг не совпадает!'
        assert collector.get_book_rating('Зеленая миля') == 1, 'Рейтинг не совпадает!'

    # 14. Вывести рейтинг несуществующей книги.
    def test_get_rating_by_not_in_list_book(self):
        collector = BooksCollector()
        collector.add_new_book('Зеленая миля')
        assert collector.get_book_rating('Долгая прогулка') == None, 'Книга есть в списке!'
