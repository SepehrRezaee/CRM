from django.db import models


class FollowUp(models.Model):
    """
    This model saves the last situation of an organization's purchase
    """
    registrar = models.ForeignKey('auth.User', verbose_name='کاربر ثبت کننده', on_delete=models.CASCADE)
    register_on = models.DateTimeField(verbose_name='ناریخ ثبت', auto_now_add=True)
    content = models.CharField(verbose_name='توضیحات', max_length=250)
    organization = models.ForeignKey('organizations.Organizations', verbose_name='سازمان', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'پیگیری'
        verbose_name_plural = 'پیگیری ها'

    def __str__(self):
        return f'{self.organization.brand}'
