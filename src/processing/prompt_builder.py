NEGATIVE_PROMPTS = [
    "blurry", "low quality", "distorted", "text overlay", "watermark", "pixelated"
]

class PromptBuilder:
    def __init__(self):
        pass  # no predefined categories needed

    def auto_detect_category(self, product_name: str):
        name = product_name.lower()
        if any(word in name for word in ["tour", "travel", "holiday", "flight", "visa", "package"]):
            return "travel"
        elif any(word in name for word in ["restaurant", "food", "drink", "coffee", "kitchen"]):
            return "food"
        elif any(word in name for word in ["clothing", "fashion", "shoe", "apparel", "style"]):
            return "fashion"
        elif any(word in name for word in ["software", "service", "consulting", "agency", "training"]):
            return "services"
        else:
            return "generic"

    def build_prompt(self, product_name: str):
        category = self.auto_detect_category(product_name)

        if category == "travel":
            prompt = f"Advertisement poster for {product_name}, travel agency style, famous landmarks, vibrant colors, text placeholder for offers, digital artwork"
        elif category == "food":
            prompt = f"Food and beverage promotional ad for {product_name}, modern design, appetizing visuals, marketing poster style, space for slogan"
        elif category == "fashion":
            prompt = f"Fashion advertisement for {product_name}, bold typography, urban background, stylish layout, high quality ad poster"
        elif category == "services":
            prompt = f"Professional services promotional banner for {product_name}, clean corporate style, modern design, marketing flyer layout"
        else:  # generic fallback
            prompt = f"Advertisement poster for {product_name}, modern marketing style, bold design, text space, digital artwork"

        return prompt + ", high resolution, graphic design, sharp focus"


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
