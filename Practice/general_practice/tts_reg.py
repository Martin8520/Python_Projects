import winreg


def list_available_voices():
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Speech\Voices\Tokens") as key:
            index = 0
            while True:
                try:
                    voice_name = winreg.EnumKey(key, index)
                    if voice_name:
                        print(voice_name)
                    else:
                        break
                    index += 1
                except EnvironmentError:
                    break
                except Exception as e:
                    print("Error occurred while listing voices:", e)
                    break
    except Exception as e:
        print("Error occurred while accessing the registry:", e)


if __name__ == "__main__":
    list_available_voices()
