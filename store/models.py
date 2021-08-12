from django.db import models
from goods.models import Product


class Quote(models.Model):
    """
    Creates an order for each organization
    """
    creator = models.ForeignKey('auth.User', verbose_name='کارشناس ثبت کنند', on_delete=models.CASCADE)
    owner = models.ForeignKey('organizations.Organizations', verbose_name='سازمان', on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='تاریخ ثبت', auto_now_add=True)
    slug = models.CharField(verbose_name='برچسب', max_length=100, unique=True, default='پیش فاکتور')

    class Meta:
        verbose_name = 'پیش فاکتور'
        verbose_name_plural = 'پیش فاکتور ها'

    def get_grand_total(self):
        """
        Returns grand total of Quote
        """
        total_price = 0
        for item in self.quoteitem_set.all():
            total_price += item.final_price()
        return total_price

    def __str__(self):
        return f'{self.owner.brand}'


class QuoteItem(models.Model):
    """
    Add some products to the quote
    """
    product = models.ForeignKey('goods.Product', verbose_name='محصول', on_delete=models.PROTECT)
    pre_quote = models.ForeignKey('store.Quote', verbose_name='پیش فاکتور', on_delete=models.CASCADE)
    qty = models.IntegerField(verbose_name='تعداد', default=1)
    discount = models.FloatField(verbose_name='تخفیف', default=0)

    class Meta:
        verbose_name = 'آیتم پیش فاکتور'
        verbose_name_plural = 'آیتم های پیش فاکتور'
        unique_together = ['product', 'pre_quote']

    def total(self):
        """
        Calculates price of an item before applying taxes
        """
        return int(self.product.price * self.qty)

    def final_price(self):
        """
        Calculates final price of an item
        """
        if self.product.includes_taxes:
            return int(self.product.price * self.qty * (1.09 - (self.discount / 100)))
        else:
            return int(self.product.price * self.qty * (1 - (self.discount / 100)))

    def __str__(self):
        return f'{self.pre_quote}'
