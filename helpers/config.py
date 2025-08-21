from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    App_Name:str
    App_Version:str

def get_setting():
    return Setting


