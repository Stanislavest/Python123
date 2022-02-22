def add_title(title):
    pass

class UserInterface:
    def wait_user_answer(self):
        print(" Ввод пользовательских данных ".center(50, "="))
        print("Действия со статьями:")
        print("1 - создание статьи"
              "\n2 - просмотр статей"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        print("=" * 50)
        return user_answer

    def add_user_articles(self):
        dict_article = {
            "название": None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }
        print(" Создание статьи: ".center(50, "="))
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} статьи: ')
        print("=" * 50)
        return dict_article

    @add_title('Список статей:')
    def show_all_articles(self, articles):
        # print(" Создание статей: ".center(50, "="))
        for ind, article in enumerate(articles, 1):
            print(f'{ind}. {article}')
        # print("=" * 50)
