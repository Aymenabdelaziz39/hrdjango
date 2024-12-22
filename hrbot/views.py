from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.llm_utils import LLMHandler
from django.conf import settings
from .models import ChatSession, ChatMessage

class ChatBotView(APIView):
    def post(self, request):
        user_message = request.data.get("message", "")
        if not user_message:
            return Response({"error": "Message non fourni."}, status=400)
        
        # Créer une nouvelle session ou utiliser une session existante (par exemple, via user_id)
        session, created = ChatSession.objects.get_or_create(user_id=request.data.get("user_id", None))

        # Ajouter le message utilisateur
        ChatMessage.objects.create(session=session, sender="user", message=user_message)

        # Initialiser le LLM
        llm_handler = LLMHandler(settings.OPENAI_API_KEY)
        bot_response = llm_handler.generate_response(
            prompt=f"Utilisateur : {user_message}\nBot :",
            model="gpt-4",
            max_tokens=100
        )

        return Response({"bot_response": bot_response})