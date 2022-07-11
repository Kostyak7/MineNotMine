from django.db import models


class MyPost(models.Model):
    postDate = models.DateTimeField('Время')
    numberPhoto = models.IntegerField('Количество фотографий')
    photo_1 = models.ImageField('Фото 1',  upload_to='uploads/posts/', default='static/userList/Platypus.png')
    photo_2 = models.ImageField('Фото 2', upload_to='uploads/posts/', default='static/userList/Platypus.png')
    photo_3 = models.ImageField('Фото 3', upload_to='uploads/posts/', default='static/userList/Platypus.png')
    photo_4 = models.ImageField('Фото 4', upload_to='uploads/posts/', default='static/userList/Platypus.png')
    photo_5 = models.ImageField('Фото 5', upload_to='uploads/posts/', default='static/userList/Platypus.png')
    photo_6 = models.ImageField('Фото 6', upload_to='uploads/posts/', default='static/userList/Platypus.png')
    photo_7 = models.ImageField('Фото 7', upload_to='uploads/posts/', default='static/userList/Platypus.png')
    photo_8 = models.ImageField('Фото 8', upload_to='uploads/posts/', default='static/userList/Platypus.png')
    photo_9 = models.ImageField('Фото 9', upload_to='uploads/posts/', default='static/userList/Platypus.png')
    photo_10 = models.ImageField('Фото 10', upload_to='uploads/posts/', default='static/userList/Platypus.png')
    someText = models.TextField('Текст')

    def get_absolute_url(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'