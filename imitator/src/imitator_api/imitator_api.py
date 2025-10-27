from fastapi import APIRouter

from src.imitator_api.imitator_stryctyre import EMPS_STRYCTYRE

router = APIRouter(
    prefix="/imitator_emps",
    tags=["imitator"]
)

@router.get('/')
def get_info():
    return EMPS_STRYCTYRE
