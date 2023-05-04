from pydantic import BaseModel


class CocktailParams(BaseModel):
    liquor: str
    cocktail_type: str
    cuisine: str
    theme: str


class MenuCocktailParams(BaseModel):
    liquor: str
    cocktail_type: str
    menu_text: str
