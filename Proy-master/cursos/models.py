from django.db import models

# Create your models here.
class Cursos(models.Model):
    idC = models.AutoField(primary_key=True, verbose_name="ID curso")
    nomC = models.CharField(max_length=80,verbose_name="Nombre de curso")
    image = models.ImageField(upload_to="projects")
    desC = models.TextField(verbose_name="Descripcion")
    fechaI = models.CharField(max_length=80,verbose_name="Fecha de inicio")
    def formatted_desC(self):
        # Usa linebreaks para que los saltos de línea se reflejen
        return format_html(self.desC.replace('\n', '<br>'))

    formatted_desC.allow_tags = True
    formatted_desC.short_description = 'Descripción con Saltos de Línea'
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('online', 'Online'),
        ('Semipresencial', 'Semipresencial')
    ]

    modC = models.CharField(max_length=15, choices=MODALIDAD_CHOICES, verbose_name="Modalidad de curso")
    fechaT =models.CharField(max_length=80,verbose_name="Fecha de Termino")
    class Meta:
        verbose_name="Curso"
        verbose_name_plural="Cursos"

    def __str__(self):
        return f"Id Curso= {self.idC}-Nombre Curso= {self.nomC}"

class Area(models.Model):
    idA = models.AutoField(primary_key=True, verbose_name="ID Area")
    nomA = models.CharField(max_length=30, verbose_name="Nombre del Área")
    directorD = models.CharField(max_length=150, verbose_name="Director del Área")
    cursos = models.ManyToManyField('Cursos',verbose_name="Cursos en el Área")
    descripcion = models.TextField(verbose_name="Descripción del Área", blank=True, null=True)
    telefono_contacto = models.CharField(max_length=20, verbose_name="Teléfono de Contacto", blank=True, null=True)
    correo_contacto = models.EmailField(verbose_name="Correo de Contacto", blank=True, null=True)

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

    def __str__(self):
        return f"Área: {self.nomA} - Director: {self.directorD}"