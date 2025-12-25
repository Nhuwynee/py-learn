from starlette.responses import JSONResponse


def response_success(data, message: str = "Success") -> JSONResponse:
    return JSONResponse(
        content={
            "success": True,
            "message": message,
            "data": data
        }
    )

