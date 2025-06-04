from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberForm
from .models import Member
from django.contrib import messages

import io
import xlsxwriter
from django.http import HttpResponse
from reportlab.pdfgen import canvas


def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Member added successfully.")
            return redirect('view_members')
    else:
        form = MemberForm()
    return render(request, 'members/add_member.html', {'form': form})

def view_members(request):
    members = Member.objects.all()
    return render(request, 'members/view_members.html', {'members': members})

def edit_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    form = MemberForm(request.POST or None, instance=member)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Member updated successfully.")
        return redirect('view_members')
    return render(request, 'members/edit_member.html', {'form': form})

def disable_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    member.is_active = False
    member.save()
    messages.warning(request, f"Member {member.username} disabled.")
    return redirect('view_members')

def export_members_excel(request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()

    headers = ['Full Name', 'Sex', 'Age', 'Date of Birth', 'Address', 'Phone', 'Email', 'Next of Kin', 'NOK Address', 'NOK Phone']
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    for row_num, member in enumerate(Member.objects.all(), start=1):
        worksheet.write(row_num, 0, member.full_name)
        worksheet.write(row_num, 1, member.sex)
        worksheet.write(row_num, 2, member.age)
        worksheet.write(row_num, 3, str(member.date_of_birth))
        worksheet.write(row_num, 4, member.address)
        worksheet.write(row_num, 5, member.phone_number)
        worksheet.write(row_num, 6, member.email)
        worksheet.write(row_num, 7, member.next_of_kin_name)
        worksheet.write(row_num, 8, member.next_of_kin_address)
        worksheet.write(row_num, 9, member.next_of_kin_phone)

    workbook.close()
    output.seek(0)

    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=members.xlsx'
    return response


def export_members_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    members = Member.objects.all()

    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, 800, "List of Members")
    p.setFont("Helvetica", 10)

    y = 780
    for member in members:
        text = f"{member.full_name} | {member.sex} | {member.age} | {member.phone_number} | {member.email}"
        p.drawString(50, y, text)
        y -= 20
        if y < 50:
            p.showPage()
            y = 800

    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf', headers={'Content-Disposition': 'attachment; filename=members.pdf'})
    
