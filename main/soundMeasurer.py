def getSoundTest():
    return 1

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import time


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume.iid, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

master = -volume.GetMasterVolumeLevel()
lowest = -volume.GetVolumeRange()[0]