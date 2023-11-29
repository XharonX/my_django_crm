from .forms import ServiceForm, TechFindingForm
from django.http.response import JsonResponse
from .models import Servicing, ErrorResult, ErrorReturn
from productions.models import Product
from django.views.generic import CreateView, UpdateView, ListView
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


class CreateServiceFrom(CreateView):
    form_class = ServiceForm
    template_name = 'services-dept/error_received_forms.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Error Service has been created {request.user}')
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            return redirect(request.META.get("HTTP_REFERER"))


class ReturnErrorsView(ListView):
    model = ErrorReturn
    template_name = 'services-dept/return_error_list.html'


class FindingResultView(UpdateView):
    form_class = TechFindingForm
    model = Servicing
    template_name = 'services-dept/finding_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['received_form'] = self.object.form
        return context


class ErrorTechnicianView():
    ...

def get_product_info(request, product_code):
    try:
        product = Product.objects.get(product_code=product_code)
        data = {
            'name': product.product_name,
            'code': product.product_code,
                }
        return JsonResponse(data)

    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product Not Found'}, status=404)



