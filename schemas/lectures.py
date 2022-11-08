from pydantic import BaseModel
from typing import Optional

class Lecture(BaseModel):
    content: str
    bounds: list[tuple[float, float]]

class Results(BaseModel):
    lectures: Optional[list[Lecture]] = None
    shape: Optional[tuple[int, int]] = None
    message: str
    request_id: str
    ip: str
    port: int

    class Config:
        schema_extra = {
            "example": {
                "lectures": [
                    {
                        "content": "33534657-03",
                        "bounds": [
                            (30.0, 10.0), (120.0, 10.0),
                            (120.0, 80.0), (30.0, 80.0)
                        ]
                    }
                ],
                "request_id": "7DJ0PKWPFD979YMZ",
                "message": "Sucesso",
                "shape": (3800, 2100),
                "ip": "192.168.100.21",
                "port": 8000
            }
        }