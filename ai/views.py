from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.llm_utils import LLMHandler
from django.conf import settings
from .models import ResumeAnalysis
class ResumeMatcherView(APIView):
    def post(self, request):
        resume_text = request.data.get("resume_text", "")
        job_description = request.data.get("job_description", "")
        if not resume_text or not job_description:
            return Response({"error": "Texte du CV ou description du poste manquant."}, status=400)

        # Initialiser le LLM
        llm_handler = LLMHandler(settings.OPENAI_API_KEY)
        
        # Prompt pour analyser le CV
        prompt = f"""
        Analysez ce CV : {resume_text}
        En fonction de cette description de poste : {job_description}
        Indiquez les compétences pertinentes et calculez un pourcentage de correspondance.
        """
        analysis = llm_handler.generate_response(prompt=prompt, model="gpt-4", max_tokens=300)

       # Calculer un score fictif (peut être extrait du LLM si nécessaire)
        match_score = 80.0  # Exemple d'un score statique

        # Enregistrer l'analyse
        analysis = ResumeAnalysis.objects.create(
            resume_text=resume_text,
            job_description=job_description,
            match_score=match_score,
            analysis_result= analysis_result
        )

        return Response({
            "analysis_result": analysis.analysis_result,
            "match_score": analysis.match_score
        })
