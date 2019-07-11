from PIL import Image
import os
import sys

SCREENSHOTS_FOLDER = "screenshots"

def create_screenshots(path, resolutions):
    color_scheme = {
        "background": Image.open(os.path.join(path, "background.png")).convert("RGBA"),
        "logo": Image.open(os.path.join(path, "logo.png")).convert("RGBA"),
        "progress-bar": Image.open(os.path.join(path, "progress-bar.png")).convert("RGBA"),
        "progress-box": Image.open(os.path.join(path, "progress-box.png")).convert("RGBA"),
        "box": Image.open(os.path.join(path, "box.png")).convert("RGBA"),
        "entry": Image.open(os.path.join(path, "entry.png")).convert("RGBA"),
        "lock": Image.open(os.path.join(path, "lock.png")).convert("RGBA"),
        "bullet": Image.open(os.path.join(path, "bullet.png")).convert("RGBA")
    }

    for r in resolutions:
        x = r["width"]
        y = r["height"]

        background_x = 0
        background_y = 0
        logo_x = (x // 2) - (color_scheme["logo"].size[0] // 2)
        logo_y = (y // 2) - (color_scheme["logo"].size[1] // 2)
        progress_box_x = (x // 2) - (color_scheme["progress-box"].size[0] // 2)
        progress_box_y = int(y * 0.65) - (color_scheme["progress-box"].size[1] // 2)
        progress_bar_x = (x // 2) - (color_scheme["progress-box"].size[0] // 2)
        progress_bar_y = int(y * 0.65) - (color_scheme["progress-box"].size[1] // 2)
        box_x = (x // 2) - (color_scheme["box"].size[0] // 2)
        box_y = int(4 * y / 5) - (color_scheme["box"].size[1] // 2)
        lock_x = box_x + (color_scheme["box"].size[0] // 2) - ((color_scheme["lock"].size[0] + color_scheme["entry"].size[0]) // 2)
        lock_y = box_y + (color_scheme["box"].size[1] // 2) - (color_scheme["lock"].size[0] // 2)
        entry_x = lock_x + color_scheme["lock"].size[0]
        entry_y = box_y + (color_scheme["box"].size[1] // 2) - (color_scheme["entry"].size[1] // 2)
        bullet_y = entry_y + (color_scheme["entry"].size[1] // 2) - (color_scheme["bullet"].size[1] // 2)

        image = Image.new("RGBA", (x, y))
        image.paste(color_scheme["background"].resize((x, y)), (0, 0), color_scheme["background"].resize((x, y)))
        image.paste(color_scheme["logo"], (logo_x, logo_y), color_scheme["logo"])
        image.paste(color_scheme["progress-box"], (progress_box_x, progress_box_y), color_scheme["progress-box"])
        image.paste(color_scheme["progress-bar"].resize((color_scheme["progress-bar"].size[0] // 2, color_scheme["progress-bar"].size[1])), (progress_bar_x, progress_bar_y), color_scheme["progress-bar"].resize((color_scheme["progress-bar"].size[0] // 2, color_scheme["progress-bar"].size[1])))
        image.save(os.path.join(path, SCREENSHOTS_FOLDER, f"{x}x{y}.png"))

        image.paste(color_scheme["box"], (box_x, box_y), color_scheme["box"])
        image.paste(color_scheme["lock"], (lock_x, lock_y), color_scheme["lock"])
        image.paste(color_scheme["entry"], (entry_x, entry_y), color_scheme["entry"])
        for i in range(0, 10):
            image.paste(color_scheme["bullet"], (entry_x + (i * color_scheme["bullet"].size[0]), bullet_y), color_scheme["bullet"])

        image.save(os.path.join(path, SCREENSHOTS_FOLDER, f"{x}x{y}-encrypted.png"))


if __name__ == "__main__":
    path = ""
    resolutions = [
        # {"width": 3840, "height": 2160},
        # {"width": 2560, "height": 1440},
        # {"width": 2560, "height": 1080},
        # {"width": 1920, "height": 1080},
        # {"width": 1600, "height": 900},
        # {"width": 1366, "height": 768},
        # {"width": 1360, "height": 768},
        # {"width": 1280, "height": 720},
        {"width": 1024, "height": 768}
    ]

    # find args
    for arg in sys.argv[1:]:
        if arg.startswith("--path="):
            path = arg.replace("--path=", "")

    # validate args
    if not os.path.isdir(path):
        print(f"Error: {path} is not a valid path")
        exit(0)
    
    print(f"Creating screenshots for {path}")
    create_screenshots(path, resolutions)