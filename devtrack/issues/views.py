import json

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Reporter, Issue, CriticalIssue, LowPriotityIssue

REPORTERS_FILE = settings.BASE_DIR / "reporters.json"
ISSUES_FILE = settings.BASE_DIR / "issues.json"

def read_json_file(file_path):
    if not file_path.exists():
        file_path.write_text("[]")
    
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    
def write_json_file(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def parse_json_body(request):
    try:
        return json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return None
    
@csrf_exempt
def reporters_view(request):
    if request.method == "POST":
        return create_reporter(request)
    
    if request.method == "GET":
        return get_reporters(request)
    
    return JsonResponse({"error": "Method Not Allowed"}, status = 405)

def create_reporter(request):
    data = parse_json_body(request)

    if data is None:
        return JsonResponse({"error": "Invalid JSON body"}, status = 400)
    
    try:
        reporter = Reporter(
            id = data.get("id"),
            name = data.get("name"),
            email= data.get("email"),
            team = data.get("team"),
        )

        reporter.validate()
        reporters = read_json_file(REPORTERS_FILE)

        for existing_reporter in reporters:
            if existing_reporter["id"] == reporter.id:
                return JsonResponse(
                    {"error": "Reporter with this Id already Exists"},
                )
        
        reporters.append(reporter.to_dict())
        write_json_file(REPORTERS_FILE, reporters)

        return JsonResponse(reporter.to_dict(), status = 201)
    except ValueError as error:
        return JsonResponse({"Error" : str(error)}, status = 400)

def get_reporters(request):
    reporters = read_json_file(REPORTERS_FILE)
    reporter_id = request.GET.get("id")

    if reporter_id:
        try:
            reporter_id = int(reporter_id)
        except ValueError:
            return JsonResponse({"error": "Reporter id must be an Integer"}, status = 400)
        
        for reporter in reporters:
            if reporter["id"] == reporter_id:
                return JsonResponse(reporter, status = 200)
        
        return JsonResponse({"error": "Reporter not found"}, status = 400)
    return JsonResponse(reporters, safe=False, status = 200)

# @csrf_exempt
# def issues_view(request):
#     if request.method == "POST":
#         return create_issue(request)
    
#     if request.method == "GET":
#         return get_issue(request)
    
#     return JsonResponse({"error": "Invalid JSON Body"}, status = 405)

# def create_issue(request):
#     data = parse_json_body(request)
    
#     if data is None:
#         return JsonResponse({"error": "Invalid JSON body"}, status = 400)
    

# def get_issue(request):
#     pass
