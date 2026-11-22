from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    lower_ing: str = ingredients.lower()
    is_valid: bool = any(item.lower() in lower_ing for item in allowed)
    status: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
