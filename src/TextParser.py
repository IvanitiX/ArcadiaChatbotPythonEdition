import os


class TextParser:
    def __init__(self):
        pass

    def parseChannels(self, path):
        canales = []

        with open(path, "r") as archivoCanales:
            lineasArchivo = archivoCanales.readlines()

            for linea in lineasArchivo:
                if linea[0] != "#":
                    if linea[-1] == "\n":
                        linea = linea[0:-1]
                    canales.append(linea)

        return canales

    def parseQuotes(self, path):
        citas = self.parseChannels(path)
        return citas
