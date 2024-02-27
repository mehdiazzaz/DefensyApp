from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.contrib.auth.decorators import login_required, user_passes_test
import matplotlib.pyplot as plt
import io
import os

def is_admin(user):
    return user.is_staff

@login_required
#@user_passes_test(is_admin)
def generate_report(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == 'best_of_times_123':
            os.system("echo 'create report for "+request.user.username+"' >> ./logs.txt")
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="sales_report.pdf"'

            doc = SimpleDocTemplate(response, pagesize=letter)
            elements = []

            # Add a title
            elements.append(canvas.Canvas(response).drawString(100, 750, 'Sales Report'))

            # Add a table
            data = [
                ['Month', 'Sales'],
                ['January', '1000'],
                ['February', '1200'],
                ['March', '1500'],
                ['April', '1800'],
                ['May', '2000'],
                ['June', '2200'],
                ['July', '2400'],
                ['August', '2600'],
                ['September', '2800'],
                ['October', '3000'],
                ['November', '3200'],
                ['December', '3400'],
            ]
            table = Table(data)
            table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
            elements.append(table)

            doc.build(elements)


            return response
        elif password == '':
            return render(request, 'report/input_page.html', {'error_message': 'No password Entered'})
        else:
            os.system("echo '"+request.user.username+" typed wrong password : "+password+"' >> ./logs.txt")
            return render(request, 'report/input_page.html', {'error_message': 'Invalid password'})
    return render(request, 'report/input_page.html')