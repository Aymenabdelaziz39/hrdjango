from django.db import models

class ChatSession(models.Model):
    """
    Représente une session de chat entre un utilisateur et le bot.
    """
    user_id = models.CharField(max_length=255, blank=True, null=True)  # Identifiant utilisateur (si connecté)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatSession {self.id} - {self.created_at}"


class ChatMessage(models.Model):
    """
    Représente un message dans une session de chat.
    """
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name="messages")
    sender = models.CharField(max_length=50, choices=[('user', 'User'), ('bot', 'Bot')])
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} - {self.timestamp}"
