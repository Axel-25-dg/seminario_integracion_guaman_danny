from abc import ABC, abstractmethod


class SolicitudConsular(ABC):
    @abstractmethod
    def procesar(self):
        pass


class SolicitudVisa(SolicitudConsular):
    def procesar(self):
        return "Solicitud de visa procesada."


class SolicitudPasaporte(SolicitudConsular):
    def procesar(self):
        return "Solicitud de pasaporte procesada."


visa = SolicitudVisa()
pasaporte = SolicitudPasaporte()

print(visa.procesar())
print(pasaporte.procesar())
