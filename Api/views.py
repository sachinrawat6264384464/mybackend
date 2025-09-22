from django.http import JsonResponse
import json

def receive_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message = data.get("message", "")
            return JsonResponse({"status": "success", "message": f"Received: {message}"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    else:
        # GET ya koi aur method aayi to
        return JsonResponse({"status": "error", "message": "Only POST allowed"})
