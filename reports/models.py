from django.db import models
from django.utils import timezone
from froala_editor.fields import FroalaField
# Create your models here.

class Report(models.Model):
    # industry = (
    #     ('CnM', 'Chemical and Materials'),
    #     ('MnE', 'Machinery and Equipment'),
    #     ('RnCG', 'Retails and Consumer Goods'),
    #     ('HnM', 'Health and Medical'),
    #     ('FnB', 'Food and Beverages')
    # )

    industry = (
        ('Chemicals and Materials', 'Chemicals and Materials'),
        ('Machinery and Equipment', 'Machinery and Equipment'),
        ('Retail and Consumer Goods', 'Retail and Consumer Goods'),
        ('Healthcare and Medical', 'Healthcare and Medical'),
        ('Food and Beverages', 'Food and Beverages')
    )

    # industry = (
    #     ('Chemical and Materials', 'CnM'),
    #     ('Machinery and Equipment', 'MnE'),
    #     ('Retails and Consumer Goods', 'RnCG'),
    #     ('Health and Medical', 'HnM'),
    #     ('Food and Beverages', 'FnB')
    # )
    
    published_date = models.DateField(default = timezone.now)
    report_title = models.CharField(max_length=256)
    main_category = models.CharField(max_length=32, choices=industry)
    pages = models.IntegerField(null=True, blank=True)
    summary = FroalaField(default="summary")
    table_of_contents = FroalaField(default="table of contents")
    list_of_table = FroalaField(default="list of tables")
    list_of_figures = FroalaField(default="list of figures")
    companies_mentioned = models.CharField(max_length=128, null=True, blank=True)
    single_user_licence = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    multi_user_licence = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    corporate_user_licence = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # def __str__(self):
    #     return self.report_title
