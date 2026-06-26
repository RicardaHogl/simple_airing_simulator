from dataclasses import dataclass

from psychrolib import *

SetUnitSystem(SI)

PRESSURE = 101325  # Pa


@dataclass
class AirState:
    dry_bulb: float          # °C
    relative_humidity: float # %

    @property
    def humidity_ratio(self):
        return GetHumRatioFromRelHum(
            self.dry_bulb,
            self.relative_humidity / 100,
            PRESSURE,
        )

    @property
    def wet_bulb(self):
        return GetTWetBulbFromHumRatio(
            self.dry_bulb,
            self.humidity_ratio,
            PRESSURE,
        )

    @property
    def dew_point(self):
        return GetTDewPointFromRelHum(
            self.dry_bulb,
            self.relative_humidity / 100,
        )

    @property
    def enthalpy(self):
        return GetMoistAirEnthalpy(
            self.dry_bulb,
            self.humidity_ratio,
        )

    def cooled_to(self, new_temperature):
        """Cool air without changing moisture."""

        rh = GetRelHumFromHumRatio(
            new_temperature,
            self.humidity_ratio,
            PRESSURE,
        )

        return AirState(
            dry_bulb=new_temperature,
            relative_humidity=rh * 100,
        )

    def summary(self):
        return {
            "Dry Bulb": self.dry_bulb,
            "RH": self.relative_humidity,
            "Wet Bulb": self.wet_bulb,
            # "Dew Point": self.dew_point,
            "Humidity Ratio": self.humidity_ratio,
            # "Enthalpy": self.enthalpy,
        }