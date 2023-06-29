from django.db import models

# receiver_id, content, reply, is_view, is_view_num, send_time
class Chatting(models.Model):
    receiver_id = models.CharField(max_length=50)

    content = models.TextField()
    reply = models.TextField()
    
    is_view = models.PositiveBigIntegerField()
    is_view_num = models.PositiveBigIntegerField()
    
    send_time = models.TimeField()