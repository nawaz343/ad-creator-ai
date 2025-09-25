class AdCreatorInterface:
    def __init__(self):
        self.generator = AdImageGenerator()
        self.processor = AdPostProcessor()
        self.prompt_builder = PromptBuilder()

    def generate_single_ad(self, product_name, style, platform):
        prompt = self.prompt_builder.build_prompt(product_name)
        images = self.generator.generate_ad_variants(prompt, negative_prompt=", ".join(NEGATIVE_PROMPTS))
        processed = [self.processor.enhance_image(self.processor.resize_for_platform(img, platform)) for img in images]
        return processed

def main():
    app = AdCreatorInterface()
    with gr.Blocks(title="AI Advertisement Creator") as demo:
        gr.Markdown("# 🖼️ AI-Powered Advertisement Creator")

        with gr.Row():
            product = gr.Textbox(label="Product/Service Name", placeholder="e.g., Qafila Tours Dubai Package")
            style = gr.Dropdown(["professional", "minimalist", "luxury", "vibrant"], label="Style", value="professional")
            platform = gr.Dropdown(["instagram_square","instagram_story","facebook_ad"], label="Platform")

        output = gr.Gallery(label="Generated Ads", columns=2)
        btn = gr.Button("Generate Ad")

        btn.click(app.generate_single_ad, inputs=[product, style, platform], outputs=output)

    demo.launch()
