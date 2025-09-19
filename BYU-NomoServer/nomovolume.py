from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL, CoInitialize, CoUninitialize
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def change_volume(new_volume):
    CoInitialize()
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
    
        # Get current volume level (0.0 to 1.0)
        prev_volume = volume.GetMasterVolumeLevelScalar()
        print(f"Current volume: {prev_volume:.2f}")

        # Lower Volume
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        print(f"New volume: {new_volume:.2f}")
        return prev_volume
    finally:
        CoUninitialize()
