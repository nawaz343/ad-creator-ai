import gradio as gr
from src.generators.stable_diffusion import AdImageGenerator
from src.processing.prompt_builder import PromptBuilder, NEGATIVE_PROMPTS
from src.processing.post_processor import AdPostProcessor

class AdCreatorInterface:
    def __init__(self):
        self.generator = AdImageGenerator()
        self.processor = AdPostProcessor()
        self.prompt_builder = PromptBuilder()

    def generate_single_ad(self, product_name, category, style, platform):
        prompt = self.prompt_builder.build_product_ad_prompt(product_name, category, style)
        images = self.generator.generate_ad_variants(prompt, negative_prompt=", ".join(NEGATIVE_PROMPTS))
        processed = [self.processor.enhance_image(self.processor.resize_for_platform(img, platform)) for img in images]
        return processed

def main():
    app = AdCreatorInterface()
    with gr.Blocks(title="AI Advertisement Creator") as demo:
        gr.Markdown("# ??? AI-Powered Advertisement Creator")
        with gr.Row():
            product = gr.Textbox(label="Product Name")
            category = gr.Dropdown(["product_showcase", "lifestyle", "emotional"], label="Category")
            style = gr.Dropdown(["professional", "minimalist", "luxury", "vibrant"], label="Style", value="professional")
            platform = gr.Dropdown(["instagram_square","instagram_story","facebook_ad"], label="Platform")
        output = gr.Gallery(label="Generated Ads", columns=2)
        btn = gr.Button("Generate Ad")
        btn.click(app.generate_single_ad, inputs=[product, category, style, platform], outputs=output)
    demo.launch()

if __name__ == "__main__":
    main()
