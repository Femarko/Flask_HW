import pydantic


class CreateAdv(pydantic.BaseModel):
    title: str
    description: str
    author: str
