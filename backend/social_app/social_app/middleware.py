import logging
import uuid

class RequestIDMiddleware:
    #thêm request_id tự động cho log
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = str(uuid.uuid4())
        logging.LoggerAdapter(logging.getLogger(__name__), {'request_id': request_id})
        response = self.get_response(request)
        return response
