from typing import Tuple

class CommonResolutionPresets:
    """Select from common resolution presets and output width and height."""

    CATEGORY = "Utils / Resolution"
    NODE_NAME = "Common Resolution Presets"
    DEFAULT_RESOLUTION = (1024, 1024)

    RESOLUTION_MAP = {
        # SQUARE
        "Square - 1024x1024 (1:1)": (1024, 1024),
        "Square - 1280x1280 (1:1)": (1280, 1280),
        "Square - 1536x1536 (1:1)": (1536, 1536),
        "Square - 2048x2048 (1:1)": (2048, 2048),
        # LANDSCAPE
        "Landscape - 1152x896 (9:7)": (1152, 896),
        "Landscape - 1152x864 (4:3)": (1152, 864),
        "Landscape - 1248x832 (3:2)": (1248, 832),
        "Landscape - 1280x720 (16:9)": (1280, 720),
        "Landscape - 1344x576 (21:9)": (1344, 576),
        "Landscape - 1440x1120 (9:7)": (1440, 1120),
        "Landscape - 1472x1104 (4:3)": (1472, 1104),
        "Landscape - 1536x1024 (3:2)": (1536, 1024),
        "Landscape - 1536x864 (16:9)": (1536, 864),
        "Landscape - 1680x720 (21:9)": (1680, 720),
        "Landscape - 1728x1344 (9:7)": (1728, 1344),
        "Landscape - 1728x1296 (4:3)": (1728, 1296),
        "Landscape - 1872x1248 (3:2)": (1872, 1248),
        "Landscape - 2048x1152 (16:9)": (2048, 1152),
        "Landscape - 2016x864 (21:9)": (2016, 864),
        # PORTRAIT
        "Portrait - 896x1152 (7:9)": (896, 1152),
        "Portrait - 864x1152 (3:4)": (864, 1152),
        "Portrait - 832x1248 (2:3)": (832, 1248),
        "Portrait - 720x1280 (9:16)": (720, 1280),
        "Portrait - 576x1344 (9:21)": (576, 1344),
        "Portrait - 1120x1440 (7:9)": (1120, 1440),
        "Portrait - 1104x1472 (3:4)": (1104, 1472),
        "Portrait - 1024x1536 (2:3)": (1024, 1536),
        "Portrait - 864x1536 (9:16)": (864, 1536),
        "Portrait - 720x1680 (9:21)": (720, 1680),
        "Portrait - 1344x1728 (7:9)": (1344, 1728),
        "Portrait - 1296x1728 (3:4)": (1296, 1728),
        "Portrait - 1248x1872 (2:3)": (1248, 1872),
        "Portrait - 1152x2048 (9:16)": (1152, 2048),
        "Portrait - 864x2016 (9:21)": (864, 2016),
    }

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (tuple(cls.RESOLUTION_MAP.keys()),),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "select_resolution"

    def select_resolution(self, preset: str) -> Tuple[int, int]:
        width, height = self.RESOLUTION_MAP.get(preset, self.DEFAULT_RESOLUTION)
        return width, height
