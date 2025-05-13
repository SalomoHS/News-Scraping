import winreg

def enable_proxy():
    proxy_server = 'IP_PROXY'
    key_path = r'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings'
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxy_server)
    winreg.CloseKey(key)

def disable_proxy():
    key_path = r'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings'
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
    winreg.CloseKey(key)