from django.db import models


class MyInformation(models.Model):
    default_path = 'http://drive.google.com/uc?export=view&id='
    default_img = default_path + '1iw2yepgodB0n5lglh7EThnbwx-JPNJvF'
    myName = models.CharField('Мое имя', max_length=100)
    myNumber = models.CharField('Мой номер', max_length=12)
    myPhoto = models.URLField('Мое фото', default=default_path)
    myDescription = models.TextField('Мое описание')
    myGmail = models.EmailField('Гугл почта')
    myYandexMail = models.EmailField('Яндекс почта')
    myVK = models.URLField('VK')
    myInstagram = models.URLField('Instagram')
    MyGitHub = models.URLField('Мой ГитХаб')
    myBirthDay = models.DateField('Мой день рождения')
    myEducation = models.CharField('Мое Образование', max_length=100)

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Мой профиль'
        verbose_name_plural = 'Мои профили'
