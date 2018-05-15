from django.db import models
from django.contrib.auth.models import User
from django.db.models.manager import Manager
# Create your models here.


class UserInfo(models.Model):
    """
    # 普通用户
    """
    category_choice = [('ad', '管理员'), ('cu', '用户'), ('cs', '客服')]
    category = models.CharField(choices=category_choice, max_length=2)
    user = models.OneToOneField(User)
    nick_name = models.CharField(max_length=64, help_text='昵称')
    age = models.IntegerField(help_text='年龄')
    gender_choices = [
        ('male', '男'),
        ('female', '女')
    ]
    gender = models.CharField(
        max_length=8, choices=gender_choices, help_text="性别")
    photo = models.OneToOneField('Image', help_text='头像')
    phone = models.CharField(max_length=11, help_text='手机号码')
    email = models.EmailField(help_text='邮箱')
    description = models.TextField(help_text='介绍')
    born_date = models.DateField(help_text='出身日期')
    job = models.CharField(max_length=16, help_text='职业')
    addresses = models.ManyToManyField('Address', help_text='收货地址')

    @property
    def is_cs(self):
        return self.category == 'cs'

    @property
    def is_ad(self):
        return self.category == 'ad'

    @property
    def is_cu(self):
        return self.category == 'cu'
    


class Image(models.Model):
    path = models.CharField(max_length=256)
    size = models.IntegerField()
    filename = models.CharField(max_length=256)
    saved_name = models.CharField(max_length=256)
    category_choices = [
        ('oss', '阿里云 oss'),
        ('qiniu', '七牛云存储')
    ]
    category = models.CharField(choices=category_choices, max_length=8)

    def file(self):
        """
        # 获取文件
        return File:保存的文件
        """
        pass

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Image, self).save(force_insert,
                                force_update, using, update_fields)


class Province(models.Model):
    name = models.CharField(max_length=32, help_text="省份名称")
    zip_code = models.CharField(max_length=16)


class City(models.Model):
    name = models.CharField(max_length=32, help_text="市/区名称")
    zip_code = models.CharField(max_length=16)
    province = models.ForeignKey('Province')


class County(models.Model):
    name = models.CharField(max_length=32, help_text="县名称")
    zip_code = models.CharField(max_length=16)
    city = models.ForeignKey('City')


class Address(models.Model):
    province = models.OneToOneField('Province', help_text="所在省份")
    city = models.OneToOneField('City', help_text='所在城市')
    county = models.OneToOneField('County', help_text="所在县")
    street = models.CharField(max_length=256, help_text="街道")
    label = models.CharField(max_length=32, help_text='地址别名')
