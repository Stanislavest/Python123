import os.path
import pickle


class Article:
    def __init__(self, name, stl, director, year, duration, studio, actors):
        self.name = name
        self.stl = stl
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.name} ({self.ganre})"


class ArticleModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.articles = self.load_data()  # {'title': article}


    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.name] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "название": article.name,
            "жанр": article.stl,
            "режиссер": article.director,
            "год выпуска": article.year,
            "продолжительность": article.duration,
            "студия": article.studio,
            "актёры": article.actors
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.articles, f)
