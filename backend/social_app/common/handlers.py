from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    """
    Custom exception handler cho DRF.
    Chuẩn hóa mọi lỗi về JSON trả về
    """
    # Gọi handler mặc định DRF trước
    response = exception_handler(exc, context)

    if response is not None:
        # Nếu DRF đã trả response, chuẩn hóa format
        return Response({
            "success": False,
            "error": {
                "type": exc.__class__.__name__,
                "code": getattr(exc, "default_code", "error"),
                "message": str(exc.detail if hasattr(exc, "detail") else exc)
            }
        }, status=response.status_code)

    # Nếu lỗi ngoài dự kiến (không phải DRF exception)
    return Response({
        "success": False,
        "error": {
            "type": exc.__class__.__name__,
            "code": "server_error",
            "message": str(exc)
        }
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
