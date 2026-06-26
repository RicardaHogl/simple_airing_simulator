from dataclasses import dataclass


@dataclass
class Room:
    area: float      # m²
    height: float    # m

    @property
    def volume(self):
        return self.area * self.height

    def air_changes_per_hour(self, airflow_m3h):
        return airflow_m3h / self.volume