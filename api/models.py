from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password,check_password


# 建立自定义用户表
class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    
    # 用户类型
    # 1：超管 | 1000： 普通管理员 | 2000：学生 | 3000：老师
    usertype = models.PositiveIntegerField()
    
    # 真实姓名
    realname = models.PositiveIntegerField()
    
    # 学号
    studento = models.CharField(
        max_length=10,
        db_index=True,
        null=True,
        blank=True
    )
    
    # 备注描述
    desc = models.CharField(max_length=500,null=True,blank=True)
    
    REQUIRED_FIELDS=['usertype','realname']
    
    class Meta:
        db_table = '用户表'