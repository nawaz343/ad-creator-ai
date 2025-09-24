# Advertisement Creator - AI Image Generation

Capstone project demonstrating how open-source AI models can automate ad creation.

## Features
- Stable Diffusion text-to-image generation.
- Modular pipeline (prompt builder, generator, post-processor).
- Gradio interface for single ads and campaigns.
- Evaluation framework (quality metrics + A/B testing).
- Extensible for new models (FLUX, Hydream).

## Run
```bash
pip install -r requirements.txt
python src/interface/gradio_app.py
```