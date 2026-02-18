# Common_Resolution_Presets Node for ComfyUI

## Overview
Common_Resolution_Presets is a custom node for [ComfyUI](https://github.com/Comfy-Org/ComfyUI) that provides a dropdown of standard width and height presets, allowing you to select common resolutions instantly without having to manually enter dimensions each time. Custom presets can also be added.

![Example Screenshot 1](/Screenshots/Screenshot1.png)

![Example Screenshot 3](/Screenshots/Screenshot3.png)

![Example Screenshot 2](/Screenshots/Screenshot2.png)

## Installation and Usage
1. Run the following command inside your ComfyUI's custom_nodes folder -

    `git clone `

    > Alternatively, if you don't wish to use git clone, you can download this project as a ZIP file, extract it, and place the folder into your ComfyUI/custom_nodes folder.

2. Start/Restart ComfyUI for the changes to take effect.
3. Add the node by searching "Common Resolution Presets" in your Node Library.

    ![Node Library Screenshot](/Screenshots/Screenshot4.png)

    Alternatively, you can right click in an empty space in your ComfyUI workflow, and select Add Node -> Utils -> Resolution -> Common Resolution Presets.

    ![Add Node Screenshot](/Screenshots/Screenshot5.png)

4. Connect the width and height outputs of this node to the width and height input nodes in your workflow.

    ![Example Screenshot 3](/Screenshots/Screenshot3.png)

## Included Presets
The following resolution presets are included -

Square: 1024x1024, 1280x1280, 1536x1536, 2048x2048

Landscape: 1152x896, 1152x864, 1248x832, 1280x720, 1344x576, 1440x1120, 1472x1104, 1536x1024, 1536x864, 1680x720, 1728x1344, 1728x1296, 1872x1248, 2048x1152, 2016x864

Portrait: 896x1152, 864x1152, 832x1248, 720x1280, 576x1344, 1120x1440, 1104x1472, 1024x1536, 864x1536, 720x1680, 1344x1728, 1296x1728, 1248x1872, 1152x2048, 864x2016

## Adding Custom Resolution Presets
Custom presets can be easily added by editing the `common_resolution_presets.py` file.

1. Open the file in your text editor of choice.
2. Add your custom preset below the line that starts with `#Add custom presets below this line`
3. Save and close the file. Restart ComfyUI for the changes to take effect.

Below is a simple example of how to add 3072 x 3072 custom resolution.
```
    "
    ...
        "Portrait - 1248x1872 (2:3)": (1248, 1872),
        "Portrait - 1152x2048 (9:16)": (1152, 2048),
        "Portrait - 864x2016 (9:21)": (864, 2016),
        #Add custom presets below this line
        "My Custom Resolution - 3072x3072 (1:1)": (3072, 3072),
    }
    ...
```

If you want you can also add the presets under the square, landscape, or portrait groups in the code. You can name them whatever you want, and add as many as you want.

## Issues
For bugs, feature requests, or questions, please open an issue on the project's GitHub with a clear description, steps to reproduce, and any relevant logs or screenshots.