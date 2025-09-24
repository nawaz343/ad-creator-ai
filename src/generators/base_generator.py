from abc import ABC, abstractmethod

class BaseGenerator(ABC):
    @abstractmethod
    def generate_ad_variants(self, prompt, negative_prompt=None, **kwargs):
        pass
