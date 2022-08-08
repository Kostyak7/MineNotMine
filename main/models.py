from django.db import models


class MyPost(models.Model):
    default_img = 'https://psv4.userapi.com/c536236/u240514110/docs/d7/e6002448a5a1/Platypus.png?extra=3kj7j47V1IJwlfpurBOiY03oCvrGiGEs3numdSZvXHje4m03UDgzQfGyJ3Xox6Ma_YenUS-DdKdovaXyaTMGPvMHROgXQs1jEHhXLT81VG-WYKtvy_yyXC2SyJlLqL7eX9UaODc0oI1Nmxp2me0z3L_C0A'
    postDate = models.DateTimeField('Время')
    numberPhoto = models.IntegerField('Количество фотографий')
    photo_1 = models.URLField('Фото 1', default=default_img)
    photo_2 = models.URLField('Фото 2', default=default_img)
    photo_3 = models.URLField('Фото 3', default=default_img)
    photo_4 = models.URLField('Фото 4', default=default_img)
    photo_5 = models.URLField('Фото 5', default=default_img)
    photo_6 = models.URLField('Фото 6', default=default_img)
    photo_7 = models.URLField('Фото 7', default=default_img)
    photo_8 = models.URLField('Фото 8', default=default_img)
    photo_9 = models.URLField('Фото 9', default=default_img)
    photo_10 = models.URLField('Фото 10', default=default_img)
    someText = models.TextField('Текст')

    def get_absolute_url(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'