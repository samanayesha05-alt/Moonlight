from pydantic_settings import SettingsConfigDict,BaseSettings

class Settings(BaseSettings):
    DATABASE_URL : str
    SECRET_KEY : str
    ACCESS_TOKEN_EXPIRY_MINUTES : int
    ALGORITHM : str
    
    model_config = SettingsConfigDict(
        env_file= '.env',
        env_file_encoding='utf-8'
    )
    
settings = Settings()