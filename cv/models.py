from django.db import models


class Education(models.Model):
    institution_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.institution_name


class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description =  models.TextField(blank=True)

    def __str__(self):
        return self.job_title
    


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    author_name = models.CharField(max_length=100)
    author_company = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.author_name
    