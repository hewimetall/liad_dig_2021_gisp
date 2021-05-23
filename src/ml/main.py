import re

import translators as ts
from gensim import corpora, models


class DataProcess:
    num_topics = 2
    num_words = 3
    prefix_pach = 'ml.data_files'

    def get_model(self):

        # обучение модель
        ldamodel = models.ldamodel.LdaModel(self.data, id2word=self.dictionary, num_topics=self.num_topics, passes=20,
                                            alpha=1.25,
                                            eta=1.25)
        # Сохранение модели
        ldamodel.save("ldamodel_xkcd")
        return ldamodel

    def __call__(self, *args, **kwargs):
        # Импортируем данные в формте UCI Bag of Words
        self.data = corpora.UciCorpus(f"{self.prefix_pach}/docword.xkcd.uci", f"{self.prefix_pach}/vocab.xkcd.uci")
        self.dictionary = self.data.create_dictionary()

        if None:
            # Загрузка модели
            self.ldamodel = models.ldamodel.LdaModel.load("ldamodel_xkcd")
        else:
            self.ldamodel = self.get_model()

    def valid_row(self, text_info):
        data_list = text_info.split()
        data_list_lower = []
        for word in data_list:
            lw = word.lower().replace('\n', '')
            data_list_lower.append(lw)
        return list(set(data_list_lower))

    def trans_seach(self, text):
        return ts.alibaba(text, professional_field='general')

    def get_word_of_theme(self):
        # Получение топовых слов по теме
        # Индекс списка соответствует тематике
        count_of_themes = 6
        words_of_theme = []
        for j in range(self.num_topics):
            df = [re.split('[^a-z]', sentence.lower().replace('\n', '')) for sentence in \
                  self.ldamodel.print_topics(num_topics=self.num_topics, num_words=self.num_words)[j][1].split('+')]
            words_of_theme.append(list(set([word for sen in df for word in sen if len(word) > 2])))
        return words_of_theme

    def get_doc(self):
        # Получение распределения тем для конкретного документа
        # Индекс + 1 списка data соответствует id меры поддержки (нумерация мер с 1 до последней меры)
        doc = list(self.data)[0]
        self.ldamodel.get_document_topics(doc)

    def get_list_themes(self, text_info):
        list_of_themes = []
        words_user = self.valid_row(text_info)
        words_of_theme = self.get_word_of_theme()
        doc = self.get_doc()

        for i in range(len(words_user)):
            for j in range(len(words_of_theme)):
                for y in range(self.num_words):
                    if words_user[i] == words_of_theme[j][y]:
                        if self.ldamodel.get_document_topics(doc)[0][1] > self.ldamodel.get_document_topics(doc)[1][1]:
                            list_of_themes.append(self.ldamodel.get_document_topics(doc)[0])
                        else:
                            list_of_themes.append(self.ldamodel.get_document_topics(doc)[1])
        return list_of_themes

    def get_qureset(self, text_info):
        self.get_list_themes(text_info)
        return ['123123', '12334', '3461']
