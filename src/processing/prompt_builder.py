PROMPT_TEMPLATES = {
    "product_showcase": {
        "base": "professional product photography of {product}, {style}, {background}",
        "styles": ["minimalist", "luxury", "vibrant", "natural"],
        "backgrounds": ["white background", "lifestyle setting", "gradient backdrop"]
    },
    "lifestyle": {
        "base": "lifestyle photo of {product}, {mood}, {setting}, cinematic lighting",
        "moods": ["happy", "serene", "energetic", "cozy"],
        "settings": ["modern home", "outdoor scene", "office"]
    },
    "emotional": {
        "base": "{emotion} advertisement for {product}, {color_scheme}, {composition}",
        "emotions": ["joy", "comfort", "excitement", "trust"],
        "color_schemes": ["warm tones", "cool palette", "monochrome"],
        "compositions": ["centered", "rule of thirds", "dynamic angle"]
    }
}

NEGATIVE_PROMPTS = [
    "blurry", "low quality", "distorted", "text overlay", "watermark"
]

class PromptBuilder:
    def __init__(self):
        self.templates = PROMPT_TEMPLATES

    def build_product_ad_prompt(self, product_name, category, style="professional", background="clean", mood="appealing"):
        base_template = self.templates[category]["base"]
        prompt = base_template.format(
            product=product_name,
            style=style,
            background=background,
            mood=mood,
            emotion=mood,
            color_scheme="warm tones",
            composition="centered",
            setting="modern home"
        )
        return prompt + ", professional photography, high resolution, sharp focus"
