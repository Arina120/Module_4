from django.db import models

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если возможен торг')
    connection = models.BooleanField('Связь', help_text='Отметьте, если возможна связь с продавцом', default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'advertisements'

    def __str__ (self):
        return 'Advertisement(id={0}, title={1}, price={2})'.format (self.id, self.title, self.price)