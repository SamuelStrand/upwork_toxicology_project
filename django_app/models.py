from django.db import models


class Question(models.Model):
    AGE_CATEGORIES = (
        ('Infants', 'Infants (1 month to 1 year)'),
        ('Children', 'Children (1 year through 12 years)'),
        ('Adolescents', 'Adolescents (13 years through 17 years)'),
        ('Adults', 'Adults (18 - 65 years)'),
        ('Elderly', 'Elderly > 65'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Pregnant', 'Pregnant'),
        ('Unknown', 'Unknown'),
    )

    UNIT_CHOICES = (
        ('ng', 'ng'),
        ('mcg', 'mcg'),
        ('mg', 'mg'),
        ('g', 'g'),
        ('ml', 'ml'),
        ('oz', 'oz'),
        ('IU', 'IU'),
    )

    SALICYLATE_CHOICES = (
        ('Acetaminosalol', 'Acetaminosalol'),
        ('Aloxiprin', 'Aloxiprin'),
        ('Aluminum aspirin', 'Aluminum aspirin'),
        # Add other salicylate types as needed...
    )

    AGE_UNIT_CHOICES = (
        ('year', 'year(s)'),
        ('month', 'month(s)'),
    )

    SERUM_LEVEL_UNIT_CHOICES = (
        ('mcg/dL', 'mcg/dL'),
        ('mg/L', 'mg/L'),
    )

    TIME_UNIT_CHOICES = (
        ('h', 'h'),
        ('unknown', 'unknown'),
    )

    chronicity = models.CharField(max_length=20, choices=(
        ('Acute', 'Acute'),
        ('Acute on chronic', 'Acute on chronic'),
        ('Chronic use', 'Chronic use'),
    ))

    age = models.DecimalField(max_digits=5, decimal_places=2)
    age_unit = models.CharField(max_length=5, choices=AGE_UNIT_CHOICES)
    age_category = models.CharField(max_length=15, choices=AGE_CATEGORIES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    weight_unit = models.CharField(max_length=5, choices=UNIT_CHOICES)

    dose = models.DecimalField(max_digits=10, decimal_places=2)
    dose_unit = models.CharField(max_length=5, choices=UNIT_CHOICES)
    concentration = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mdd_dose = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mdd_dose_unit = models.CharField(max_length=5, choices=UNIT_CHOICES)
    salicylate_type = models.CharField(max_length=50, choices=SALICYLATE_CHOICES, null=True, blank=True)

    apap_serum_level = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    apap_serum_level_unit = models.CharField(max_length=10, choices=SERUM_LEVEL_UNIT_CHOICES, null=True, blank=True)
    apap_serum_level_time = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    apap_serum_level_time_unit = models.CharField(max_length=10, choices=TIME_UNIT_CHOICES, null=True, blank=True)

    # Add other serum levels as needed...

    def __str__(self):
        return f"Question {self.id}"
