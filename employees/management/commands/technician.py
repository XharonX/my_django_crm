from django.core.management.base import BaseCommand
from employees.models import Department, Position, Employee
from django.contrib.auth.models import Permission, Group


class Command(BaseCommand):
    help = "Create a sale manager user with specific permission"

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The username for the sale manager')

    def handle(self, *args, **options):
        username = options['username']
        DEPARTMENT = 'Technology'
        dept, created = Department.objects.get_or_create(name=DEPARTMENT)
        position, created = Position.objects.get_or_create(name='Technician')
        permission, created = Permission.objects.get_or_create(codename='can_perform_technical_task')
        sales_manager = Employee.objects.create(username=username, dept=dept, position=position)

        sale_group, created = Group.objects.get_or_create(name=DEPARTMENT)
        sale_group.user_set.add(sales_manager)
        sales_manager.user_permissions.add(permission)
        self.stdout.write(self.style.SUCCESS(f" {username} Technician was added SUCCESSFULLY."))

