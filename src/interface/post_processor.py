from PIL import Image, ImageEnhance, ImageFilter

class AdPostProcessor:
    def __init__(self):
        self.sizes = {
            "instagram_square": (1080, 1080),
            "instagram_story": (1080, 1920),
            "facebook_ad": (1200, 628),
            "banner_large": (728, 90),
            "banner_medium": (300, 250)
        }

    def resize_for_platform(self, image, platform="instagram_square"):
        target_size = self.sizes[platform]
        return image.resize(target_size, Image.Resampling.LANCZOS)

    def enhance_image(self, image, brightness=1.1, contrast=1.2, saturation=1.1):
        image = ImageEnhance.Brightness(image).enhance(brightness)
        image = ImageEnhance.Contrast(image).enhance(contrast)
        image = ImageEnhance.Color(image).enhance(saturation)
        return image.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))
