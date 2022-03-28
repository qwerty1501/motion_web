from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Order(models.Model):
    image = models.ImageField(verbose_name='Фотография', upload_to ='image/poduct')
    name = models.CharField(verbose_name='Название', max_length=20)
    url_project = models.URLField(verbose_name='Укажите url путь', max_length = 200, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
    
    
class CreateStaff(models.Model):
    image = models.ImageField(verbose_name='Фотография', upload_to ='image/person')
    name = models.CharField(verbose_name='Имя', max_length=20)
    position = models.CharField(verbose_name='Должность', max_length=50)
    url_instagram = models.URLField(verbose_name='Укажите сылку на ваш instagram (*Не обязательно)', max_length = 200, blank=True, null=True)
    url_facebook = models.URLField(verbose_name='Укажите сылку на ваш facebook (*Не обязательно)', max_length = 200, blank=True, null=True)
    url_mail = models.URLField(verbose_name='Укажите сылку на ваш mail (*Не обязательно)', max_length = 200, blank=True, null=True)
    url_linkedin = models.URLField(verbose_name='Укажите сылку на ваш linkedin (*Не обязательно)', max_length = 200, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    
class Jobs(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    description = RichTextUploadingField('Введите описание')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Вакансию"
        verbose_name_plural = "Вакансии"
        
        
class Feedback(models.Model):
    name = models.CharField(verbose_name='Название', max_length=20)
    url_project = models.URLField(verbose_name='Укажите url путь youtube (*Не обязательно)', max_length = 200, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
