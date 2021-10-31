from Arcadia import Arcadia
from Colores import bcolors

if __name__ == "__main__":
    print(
        f"{bcolors.OKGREEN}   _                     _ _       {bcolors.OKBLUE}    ___ _           _   _           _   {bcolors.ENDC}"
    )
    print(
        f"{bcolors.OKGREEN}  /_\  _ __ ___ __ _  __| (_) __ _ {bcolors.OKBLUE}   / __\ |__   __ _| |_| |__   ___ | |_ {bcolors.ENDC}"
    )
    print(
        f"{bcolors.OKGREEN} //_\\\\| '__/ __/ _` |/ _` | |/ _` |{bcolors.OKBLUE}  / /  | '_ \ / _` | __| '_ \ / _ \| __| {bcolors.ENDC}"
    )
    print(
        f"{bcolors.OKGREEN}/  _  \ | | (_| (_| | (_| | | (_| |{bcolors.OKBLUE} / /___| | | | (_| | |_| |_) | (_) | |_  {bcolors.ENDC}"
    )
    print(
        f"{bcolors.OKGREEN}\_/ \_/_|  \___\__,_|\__,_|_|\__,_|{bcolors.OKBLUE} \____/|_| |_|\__,_|\__|_.__/ \___/ \__| {bcolors.ENDC}"
    )
    print("\n\n")

    print(
        f"{bcolors.BOLD}Bot para {bcolors.UNDERLINE}Twitch{bcolors.ENDC}{bcolors.BOLD} creado por {bcolors.WARNING}IvanitiX{bcolors.ENDC}{bcolors.BOLD} basado en {bcolors.WARNING}Pyt{bcolors.OKBLUE}hon{bcolors.ENDC}{bcolors.BOLD} y TwitchIO{bcolors.ENDC}\n\n"
    )

    bot = Arcadia()
    bot.run()
