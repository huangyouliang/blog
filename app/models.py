from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField("名称", max_length=20,)
    city = models.CharField("城市", max_length=20,)
    address = models.CharField("地点", max_length=30,)
    email = models.CharField("邮箱",max_length=20,)

class User(models.Model):
    username= models.CharField("用户名",max_length=20,)
    password = models.CharField("密码",max_length=30,)
    truename = models.CharField("真实姓名",max_length=20,)
    xueke = models.CharField("xueke",max_length=30, )
    typefs = models.CharField("学院",max_length=20,)
    labnumber = models.CharField("实验室名称",max_length=50, )
    zhiwu = models.CharField("职务",max_length=50,)
    zhicheng = models.CharField("职称",max_length=50,)
    tel = models.CharField("联系电话",max_length=50,)
    tel_office = models.CharField("办公电话",max_length=50,)
    eamil = models.CharField("邮箱",max_length=50,)
    class Meta:
        def __str__(self):
            return self.username

class book(models.Model):
    name = models.CharField("名字",max_length=20,)
    password = models.CharField("密码",max_length=30)

class itemsb(models.Model):
    itemname = models.CharField("项目名称",max_length=50)
    applyyear = models.DateTimeField("申报年份",max_length=20)
    itemtypes = models.CharField("经费来源",max_length=30)
    types2 = models.CharField("经费项目",max_length=30)
    types3 = models.CharField("具体项目",max_length=30)
    f_xiao = models.CharField("经费额度",max_length=20)
    fuzeren = models.CharField("负责人",max_length=20)
    zhiwu = models.CharField("职务",max_length=20)
    tel2 = models.CharField("负责人电话",max_length=12)
    email1 = models.CharField("负责人邮箱",max_length=20)
    lxren = models.CharField("联系人",max_length=20)
    tel = models.CharField("联系人电话",max_length=20)

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    email = models.EmailField()
    filhos = models.IntegerField()
    ativo = models.NullBooleanField()

    def __str__(self):
        return self.nome



