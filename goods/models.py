from django.db import models


class Product(models.Model):
    """
    Define products of employer
    """
    name_product = models.CharField(verbose_name='نام محصول', max_length=100)
    price = models.IntegerField(verbose_name='قیمت')
    pdf_catalog = models.FileField(verbose_name='فایل کاتالوگ(pdf)', upload_to='catalogs/pdf/')
    img_catalog = models.ImageField(verbose_name='فایل کاتالوگ(img)', upload_to='catalogs/img/')
    technical_features = models.CharField(verbose_name='ویژگی های فنی', max_length=500)
    includes_taxes = models.BooleanField(verbose_name='شامل مالیات است؟', default=False)
    proposed = models.ManyToManyField('goods.OrganizationProduct', verbose_name='محصولات پیشنهادی')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name_product


class OrganizationProduct(models.Model):
    """
    Define products of organization
    """
    name = models.CharField(verbose_name='نام محصول', max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=False)

    class Meta:
        verbose_name = 'محصول سازمان'
        verbose_name_plural = 'محصولات سازمان ها'

    def __str__(self):
        return self.name
