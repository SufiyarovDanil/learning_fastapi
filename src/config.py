from pydantic_settings import BaseSettings, SettingsConfigDict


class __Config(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SECRET_KEY: str
    
    @property
    def database_uri_asyncpg(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


config: __Config = __Config()
