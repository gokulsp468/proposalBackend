# seed_permissions.py
from django.core.management.base import BaseCommand
from django.db import transaction
import json
from ...models import Module, Permission  # Make sure to adjust 'your_app' to the name of your app

class Command(BaseCommand):
    help = "proposal/permissions/management/commands/permission.json"

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help="proposal/permissions/management/commands/permission.json")

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['json_file']
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            with transaction.atomic():
                for module_data in data:
                    self.process_module(None, module_data)

    def process_module(self, parent, module_data):
        module = Module.objects.create(
            parent=parent,
            module=module_data['module'],
            module_label=module_data.get('module_label', ''),
            order=module_data.get('order', 0),
            app_visibility=module_data.get('app_visibility', True),
            web_visibility=module_data.get('web_visibility', True)
        )

        for perm_data in module_data.get('permissions', []):
            self.process_permission(module, None, perm_data)

        for submodule_data in module_data.get('submodules', []):
            self.process_module(module, submodule_data)

    def process_permission(self, module, parent, perm_data):
        permission = Permission.objects.create(
            module=module,
            parent=parent,
            permission=perm_data['permission'],
            permission_label=perm_data['permission_label'],
            pid=perm_data['id'],
            requires=perm_data.get('requires', ''),
            optional_with=perm_data.get('optional_with', '')
        )

        for sub_perm_data in perm_data.get('sub_permissions', []):  
            self.process_permission(module, permission, sub_perm_data)

