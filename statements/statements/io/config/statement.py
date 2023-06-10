from pydantic import BaseModel
from statements.io.config.title_config import TitleConfig


class InputStatementConfig(BaseModel):
    title: TitleConfig
