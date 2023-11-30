from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from cursos.models import Cursos 

class Command(BaseCommand):
    help = 'Crea usuarios personalizados'

    def handle(self, *args, **options):
        # Crear superusuario
        User.objects.create_superuser('superadmin', 'admin@example.com', 'password')

        # Crear usuario para editar un modelo específico
        user = User.objects.create_user('edit_user', 'edit_user@example.com', 'password')
        content_type = ContentType.objects.get_for_model(Cursos)
        permissions = Permission.objects.filter(content_type=content_type)
        user.user_permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS('Usuarios creados exitosamente'))

