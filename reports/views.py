from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset
from .models import Report
from .resources import ReportResource
import pandas as pd

# Create your views here.

def sample(request):
    return HttpResponse("Hello World!")

def simple_upload(request):
    if request.method == 'POST':
        report_set = ReportResource()
        dataset = Dataset()
        new_set = request.FILES['myfile']

        imported_data = dataset.load(new_set.read())
        print(imported_data)
        for data in imported_data:
            print(data)
            # value = Report.objects.create(published_date=data[0], report_title=data[1])
            value = Report.objects.create(published_date=data[0], report_title=data[1], main_category=data[2], pages=data[3], summary=data[4], table_of_contents=data[5], list_of_table=data[6], list_of_figures=data[7], companies_mentioned=data[8], single_user_licence=data[9], multi_user_licence=data[10], corporate_user_licence=data[11])
            print(value)
            # value.save()

        # print("Imported Data:")
        # print(imported_data)
        # result = report_set.import_data(dataset, dry_run=True)  # Test the data import

        # print("Resut:")
        # print(result)
        
        # if not result.has_errors():
        #     a = report_set.import_data(dataset, dry_run=False)  # Actually import now
        #     print("Done")
            

    return render(request, 'base.html')