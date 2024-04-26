import ctypes

SPI_SETDESKWALLPAPER = 20
WallpaperpathEdu = r"C:\Users\macie\Desktop\duperele\grafiki\tapetaEdu.png" #change path to your own
Wallpaperpath = r"C:\Users\macie\Desktop\duperele\grafiki\tapetav2.png" #change path to your own
SPI_GETDESKWALLPAPER = 115
MAX_PATH = 260


def change_wallpaper_edu():
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, WallpaperpathEdu, 3)

def change_wallpaper_normal():
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, Wallpaperpath, 3)


def get_wallpaper_path():
    wallpaper_path = ctypes.create_unicode_buffer(MAX_PATH)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, MAX_PATH, wallpaper_path, 0)
    return wallpaper_path.value


if __name__ == "__main__":
    current_wallpaper_path = get_wallpaper_path()
    if current_wallpaper_path==Wallpaperpath:
        change_wallpaper_edu()
    else:
        change_wallpaper_normal()
