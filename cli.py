from psychrometrics import AirState
from room import Room


def get_inputs():

    area = float(input("Room area (m²) [25]: ").strip() or 25)
    height = float(input("Room height (m) [2.5]: ").strip() or 2.5)
    window_height = float(input("Window height (m) [2.2]: ").strip() or 2.2)
    window_width = float(input("Window width (m) [0.8]: ").strip() or 0.8)
    wind_speed = float(input("Wind speed outside (m/s) [0.5]: ").strip() or 0.5)
    room = Room(area, height)
    num_occupants = int(input("Persons in room [1]:").strip() or 1)

    indoor = AirState(
        float(input("Indoor temperature (°C): ")),
        float(input("Indoor RH (%): ")),
    )

    outdoor = AirState(
        float(input("Outdoor temperature (°C): ")),
        float(input("Outdoor RH (%): ")),
    )
    ventilation_coefficient = 0.6
    sec_to_hours = 3600
    airflow = window_height*window_width*ventilation_coefficient*wind_speed*sec_to_hours

    duration = int(
        input("Ventilation time (minutes): ")
    )

    return (
        room,
        indoor,
        outdoor,
        airflow,
        duration,
        num_occupants
    )