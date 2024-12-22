from django.db import models

# Create your models here.

class ResumeAnalysis(models.Model):
    """
    Stocke les résultats de l'analyse d'un CV par rapport à une description de poste.
    """
    resume_text = models.TextField()
    job_description = models.TextField()
    analyzed_at = models.DateTimeField(auto_now_add=True)
    match_score = models.FloatField(blank=True, null=True)  # Score de correspondance
    analysis_result = models.TextField(blank=True, null=True)  # Résultat détaillé de l'analyse

    def __str__(self):
        return f"ResumeAnalysis - {self.id} - {self.analyzed_at}"
