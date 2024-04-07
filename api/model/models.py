from django.db import models
from django.utils.translation import gettext_lazy as _


CASTE_CHOICES = (
    ('Open', 'Open'),
    ('Obc', 'Obc'),
    ('Sbc', 'Sbc'),
    ('SC', 'SC'),
    ('ST', 'ST'),
    ('NT', 'NT'),
    ('VJNT', 'VJNT'),
    ('Navbouddha', 'Navbouddha'),
)

EDUCATION_CHOICES = (
    ('SSC', 'SSC'),
    ('HSC', 'HSC'),
    ('Diploma', 'Diploma'),
    ('Under Graduate', 'Under Graduate'),
    ('Graduate', 'Graduate'),
    ('Post Graduate', 'Post Graduate'),
    ('Doctorate', 'Doctorate'),
)

class Scheme(models.Model):
    scheme_name         = models.TextField(_("Scheme Name"))
    department_name     = models.TextField(_("Department Name"))
    scheme_overview     = models.TextField(_("Scheme Overview"))
    scheme_benefits     = models.TextField(_("Scheme Benefits"))
    scheme_eligibility  = models.TextField(_("Scheme Eligibility"))
    scheme_documents    = models.TextField(_("Scheme Documents"))
    scheme_link         = models.TextField(_("Scheme Link"))
    last_date           = models.DateTimeField()
    created_at          = models.DateTimeField(auto_now_add=True)
    income_criteria     = models.IntegerField()
    caste_criteria      = models.CharField(_("Caste Criteria"), max_length=100, choices=CASTE_CHOICES, default='Open')
    region_criteria     = models.CharField(_("Region Criteria"), max_length=100)
    education_criteria  = models.CharField(_("Education Criteria"), max_length=100, choices=EDUCATION_CHOICES, default='SSC')

    def __str__(self):
        return f"{self.scheme_name}"
    
    class Meta:
        verbose_name = 'Scheme'
        verbose_name_plural = 'Scheme'
