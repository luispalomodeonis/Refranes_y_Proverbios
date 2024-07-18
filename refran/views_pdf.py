from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from $HOME/.local/bin/weasyprint import HTML
from weasyprint.fonts import FontConfiguration

def export_pdf(request):

    context = {}
    html = render_to_string("templates/refran/primer-pdf.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)

    return response

