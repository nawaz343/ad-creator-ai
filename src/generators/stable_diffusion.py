import torch
from diffusers import StableDiffusionPipeline
from .base_generator import BaseGenerator

class AdImageGenerator(BaseGenerator):
    def __init__(self, model_id="runwayml/stable-diffusion-v1-5"):
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            use_safetensors=True
        )
        self.pipe = self.pipe.to("cuda" if torch.cuda.is_available() else "cpu")
        self.pipe.enable_attention_slicing()
        self.pipe.enable_model_cpu_offload()

        self.generation_params = {
            "num_inference_steps": 50,
            "guidance_scale": 7.5,
            "num_images_per_prompt": 4,
            "height": 512,
            "width": 512
        }

    def generate_ad_variants(self, prompt, negative_prompt=None, **kwargs):
        params = {**self.generation_params, **kwargs}
        images = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            **params
        ).images
        return images
