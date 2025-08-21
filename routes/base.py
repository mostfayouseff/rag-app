from fastapi import APIRouter
import os
from helpers.config import  Setting
base_router = APIRouter()

@base_router.get("/")
async def root():
    app_setting= Setting.get_settings
    app_name=app_setting.App_Name
    app_version=app_setting.App_Version
    return {
        "message": "Hello World",
            "App_Name":app_name,
            "App_Version":app_version
            }
