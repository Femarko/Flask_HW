import pydantic


class CreateAdv(pydantic.BaseModel):
    title: str
    description: str
    author: str


class EditAdv(pydantic.BaseModel):
    title: str | None = None
    description: str | None = None
    author: str | None = None
