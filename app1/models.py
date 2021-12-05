from django.db import models



class Audio_store(models.Model):
    record=models.FileField(upload_to='documents/')
    class Meta:
        db_table='Audio_store'

# def filename(self):
#     return os.path.basename(self.file.name)