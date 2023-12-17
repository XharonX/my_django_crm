from .forms import ServiceForm, TechFindingForm
from django.http.response import JsonResponse, HttpResponse, HttpResponseNotAllowed
from .models import Servicing, ErrorReturn
from productions.models import Product
from django.views.generic import CreateView, UpdateView, ListView
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from employees.models import Employee

# Create your views here.


class CreateServiceFrom(CreateView):
    form_class = ServiceForm
    template_name = 'services-dept/error_received_forms.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            if request.user.is_authenticated and request.user.dept_id == 3:
                received_by = Employee.objects.get(username=user.username)
                instance = form.save(commit=False)
                instance.received_by = received_by
                instance.save()
                messages.success(request, _(f'Error Service has been created {request.user}'))
            return redirect('error_list')
        else:
            print(form)
            messages.error(request, form.errors)
            return redirect(request.META.get("HTTP_REFERER"))


class EditServiceForm(UpdateView):
    model = ErrorReturn
    template_name = 'services-dept/edit_service_form.html'
    form_class = ServiceForm
    success_url = 'error_list'

    def get_object(self, queryset=None):
        return ErrorReturn.objects.get(pk=self.kwargs['pk'])


class ReturnErrorsView(ListView):
    model = ErrorReturn
    template_name = 'services-dept/return_error_list.html'
    ordering = ['received_date']


class FindingResultView(UpdateView):
    form_class = TechFindingForm
    model = Servicing
    template_name = 'services-dept/finding_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['received_form'] = self.object.form
        return context

    def post(self, request, *args, **kwargs):
        tech_form = self.form_class(request.POST)
        instance = self.get_object().form
        if tech_form.is_valid():
            try:
                servicing_instance = instance.servicing
                servicing_instance.technician_finding = tech_form.cleaned_data['technician_finding']
                servicing_instance.final_result = tech_form.cleaned_data['final_result']
                servicing_instance.fees = tech_form.cleaned_data['fees']
                servicing_instance.fees_by = tech_form.cleaned_data['fees_by']
                servicing_instance.save()
            except ErrorReturn.DoesNotExist or Servicing.DoesNotExist:
                return HttpResponse('Invalid Service finding for service form.')
            messages.success(request, _("Finished finding. Ready to return back to customer or shop/wholesale. "))
            return redirect('error_list')
        else:
            messages.error(request, tech_form.errors)
        return redirect(request.META.get("HTTP_REFERER"))


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



