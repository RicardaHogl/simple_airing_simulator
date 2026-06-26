from cli import get_inputs
from simulator import (
    ventilation_curve,
    cool_after_airing,
    co2_vent_recomm,
)
from plots import plot


def print_state(title, state):

    print(f"\n{title}")

    for k, v in state.summary().items():
        if k=="Humidity Ratio":
            format = f"{v:.5f}"
        else:
            format = f"{v:.2f}"
        if isinstance(v, float):
            print(f"{k:20}: ",format)
        else:
            print(f"{k:20}: {v}")


def main():

    (
        room,
        indoor,
        outdoor,
        airflow,
        duration,
        num_occupants,
    ) = get_inputs()

    ach = room.air_changes_per_hour(airflow)

    print(f"\nRoom volume: {room.volume:.1f} m³")
    print(f"Air changes/hour: {ach:.2f}")

    print_state("Indoor", indoor)
    print_state("Outdoor", outdoor)

    cooled = cool_after_airing(
        outdoor,
        indoor.dry_bulb,
    )

    print_state(
        "Outdoor Air Cooled Indoors",
        cooled,
    )
    print("Based on occupancy, air room at least every ",co2_vent_recomm(num_occupants, room.volume)," minutes to avoid CO2 buildup"
)
    curve = ventilation_curve(
        indoor,
        outdoor,
        ach,
        duration,
    )

    plot(curve)


if __name__ == "__main__":
    main()