from django.db import models


class MyPost(models.Model):
    default_path = 'http://drive.google.com/uc?export=view&id='
    default_img = default_path + '1iw2yepgodB0n5lglh7EThnbwx-JPNJvF'
    postDate = models.DateTimeField('Время')
    numberPhoto = models.IntegerField('Количество фотографий')
    photo_1 = models.URLField('Фото 1', default=default_path)
    photo_2 = models.URLField('Фото 2', default=default_path)
    photo_3 = models.URLField('Фото 3', default=default_path)
    photo_4 = models.URLField('Фото 4', default=default_path)
    photo_5 = models.URLField('Фото 5', default=default_path)
    photo_6 = models.URLField('Фото 6', default=default_path)
    photo_7 = models.URLField('Фото 7', default=default_path)
    photo_8 = models.URLField('Фото 8', default=default_path)
    photo_9 = models.URLField('Фото 9', default=default_path)
    photo_10 = models.URLField('Фото 10', default=default_path)
    someText = models.TextField('Текст')

    def get_absolute_url(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'