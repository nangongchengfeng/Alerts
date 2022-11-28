from django.db import models


# Create your models here.
class alerts(models.Model):
    startsAt = models.DateTimeField(verbose_name='告警产生时间')
    endsAt = models.DateTimeField(verbose_name='告警恢复时间')
    instance = models.CharField(max_length=50, verbose_name='实例', blank=True)
    alertname = models.CharField(max_length=100, verbose_name='告警名称')
    status = models.CharField(max_length=20, verbose_name='状态', blank=True)
    severity = models.CharField(max_length=20, verbose_name='告警级别', blank=True)
    message = models.CharField(max_length=1000, verbose_name='告警信息', blank=True)
    known = models.BooleanField(default=False, verbose_name='知悉')
    memo = models.CharField(max_length=50, verbose_name='知悉备注', blank=True)

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'alerts'
        verbose_name = '告警日志'
        verbose_name_plural = verbose_name
        # ordering = ['-startsAt']  # 按故障时间倒排


class production(models.Model):
    startsAt = models.DateTimeField(verbose_name='告警产生时间')
    endsAt = models.DateTimeField(verbose_name='告警恢复时间')
    instance = models.CharField(max_length=50, verbose_name='实例', blank=True)
    alertname = models.CharField(max_length=100, verbose_name='告警名称')
    status = models.CharField(max_length=20, verbose_name='状态', blank=True)
    severity = models.CharField(max_length=20, verbose_name='告警级别', blank=True)
    message = models.CharField(max_length=1000, verbose_name='告警信息', blank=True)
    known = models.BooleanField(default=False, verbose_name='知悉')

    # memo = models.CharField(max_length=50, verbose_name='知悉备注', blank=True)

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'production'
        verbose_name = '告警统计'
        verbose_name_plural = verbose_name


class alarmuser(models.Model):
    username = models.CharField(max_length=20, verbose_name='告警人', blank=True)
    useremail = models.EmailField(max_length=20, verbose_name='告警邮件', blank=True)
    group = models.CharField(max_length=20, verbose_name='分组', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'alarmuser'
        verbose_name = '告警人配置'
        verbose_name_plural = verbose_name
