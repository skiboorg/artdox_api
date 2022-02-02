from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from Cart.models import Cart


class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
    username = None
    firstname = None
    lastname = None
    avatar = models.ImageField('Аватар', upload_to='user', blank=True, null=True, default='profile.svg')
    fio = models.CharField('ФИО', max_length=50, blank=True, null=True, default='Иван')
    phone = models.CharField('Телефон', max_length=50, blank=True, null=True)
    email = models.EmailField('Эл. почта', blank=True, null=True, unique=True)
    birthday = models.CharField('Дата рождения', max_length=50, blank=True, null=True)

    is_email_verified = models.BooleanField('EMail подтвержден?', default=False , editable=False)

    total_summ = models.DecimalField('Сумма куртин',decimal_places=2,max_digits=8,default=0)
    total_in_localstore = models.IntegerField('На хранении', default=0)
    total_in_store = models.IntegerField('Заложено картин', default=0)
    pay_summ = models.DecimalField('К выплате',decimal_places=2,max_digits=8,default=0)
    total_amount = models.IntegerField('Всего картин',default=0)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    def __str__(self):
        return f'{self.fio} {self.phone} '


class Transaction(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='transactions')
    amount = models.IntegerField('Сумма', default=0)
    is_buy = models.BooleanField('Покупка? False - возврат', default=True)
    type = models.CharField('Тип',max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

def user_post_save(sender, instance, created, **kwargs):
    """Создание всех значений по-умолчанию для нового пользовыателя"""
    if created:
        Cart.objects.create(user=instance)

post_save.connect(user_post_save, sender=User)


class PaymentType(models.Model):
    label = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='icons', blank=True, null=True)

    def __str__(self):
        return f'{self.label} '

    class Meta:
        verbose_name = "Платежная система"
        verbose_name_plural = "Платежные системы"

class WithdrawalRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='withdrawal_requests')
    payment_type = models.ForeignKey(PaymentType,on_delete=models.CASCADE, null=True)
    message = models.TextField(blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=8, default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_done = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.amount = self.user.pay_summ
        if self.is_done:
            self.user.pay_summ = 0
            self.user.save()

            orders = self.user.order_set.all()
            for order in orders:
                items = order.order_items.all()
                for item in items:
                    item.your_profit = 0
                    item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'№{self.id} | Запрос на вывод от {self.user.email} | {self.created_at}'

    class Meta:
        verbose_name = "Запрос на вывод"
        verbose_name_plural = "Запросы на вывод"


class ContactForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='contact_requests')
    subject = models.CharField('Название', max_length=100, blank=True, null=True)
    email = models.CharField('email', max_length=100, blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    file = models.ImageField('Баннер', upload_to='form', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'Форма обратной связи от {self.email} | {self.created_at}'

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"


class ReturnForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='return_requests')
    item = models.ForeignKey('Order.OrderItem', on_delete=models.CASCADE,blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'№{self.id} | Запрос на возврат от {self.item.order.user.email} | {self.created_at}'

    class Meta:
        verbose_name = "Запрос на возврат"
        verbose_name_plural = "Запросы на возврат"


class StoreForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='store_requests')
    item = models.ForeignKey('Order.OrderItem', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_in_store = models.BooleanField(default=False)
    is_return_store = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_in_store:
            self.item.order.user.total_in_store += self.item.amount
            self.item.is_in_store = True
            self.item.order.user.save()
            self.item.save()
        if self.is_return_store:
            self.item.order.user.total_in_store -= self.item.amount
            self.item.is_in_store = False
            self.item.order.user.save()
            self.item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'№{self.id} | Запрос на заклад от {self.item.order.user.email} | {self.created_at}'

    class Meta:
        verbose_name = "Запрос на заклад"
        verbose_name_plural = "Запросы на заклад"