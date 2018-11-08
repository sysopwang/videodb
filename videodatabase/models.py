from django.db import models

# Create your models here.


class CVE_Case(models.Model):
    case_id=models.IntegerField(auto_created=True,primary_key=True, serialize=False)
    name=models.CharField(max_length=100) #varchar

    jumpArg=models.IntegerField() #组接参数1，跳剪，是、否  0.1
    speedArg=models.IntegerField() #组接参数2，主体运动状态，运动/平稳 0.1
    positionArg=models.IntegerField() #组接参数3，主体位置，一致/不一致 0.1
    cramArg=models.IntegerField() #组接参数4，镜头运动状态，运动/平稳 0.1
    colorArg=models.IntegerField() #组接参数5，色调，一致/对比 0.1



class CVE_Shot(models.Model):
    shot_id = models.IntegerField(auto_created=True,primary_key=True, serialize=False)
    case_id = models.IntegerField()
    start=models.IntegerField() #镜头起始帧 int
    end=models.IntegerField() #镜头结束帧 int
    during=models.IntegerField() #镜头属性0，时长 int

    speed=models.IntegerField() #镜头属性1，主体运动状态 0.1.2.3
    position=models.IntegerField() #镜头属性2，主体位置 0.1.2.3
    craMotion=models.IntegerField() #镜头属性3，镜头运动状态 0.1.2.3
    color=models.IntegerField() #镜头属性4，色调 0.1.2.3
    shotSize=models.IntegerField() #镜头属性5，景别 0.1.2.3

class CVE_Case_Tags(models.Model):
    case_id = models.IntegerField(auto_created=True, primary_key=True, serialize=False)
    product_type=models.IntegerField() #产品类型 0.1.2
    busi_orientation=models.IntegerField() #业务导向 0.1.2
    product_style=models.IntegerField() #产品风格 0.1.2
    media=models.IntegerField() #传播载体 0.1.2
    year=models.IntegerField() #年份 0.1.2.3.4.5.6.7.8.9.10
    consumer=models.IntegerField() #消费者 0.1.2