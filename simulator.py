import math

from psychrometrics import AirState


def instant_exchange(outdoor_air):
    """Complete air replacement."""
    return outdoor_air


def cool_after_airing(outdoor_air, final_temperature):
    """Cool outdoor air without removing moisture."""
    return outdoor_air.cooled_to(final_temperature)

def co2_vent_recomm(persons, volume):
    """very rough estimate"""
    volume_ref = 25*2.5
    time_between_ventilations_ref = {1:197, 2:75, 3:47, 4:34, 5:27, 6: 23}
    return time_between_ventilations_ref[persons]*volume/volume_ref
def ventilation_curve(
    indoor,
    outdoor,
    ach,
    duration_minutes,
    timestep=1,
):
    """
    Simulate gradual ventilation.

    Temperature and humidity ratio both approach outdoor
    conditions exponentially.
    """

    results = []

    indoor_w = indoor.humidity_ratio
    outdoor_w = outdoor.humidity_ratio

    for minute in range(duration_minutes + 1):

        t = minute / 60

        factor = math.exp(-ach * t)

        temp = outdoor.dry_bulb + (
            indoor.dry_bulb - outdoor.dry_bulb
        ) * factor

        w = outdoor_w + (
            indoor_w - outdoor_w
        ) * factor

        from psychrolib import GetRelHumFromHumRatio

        rh = (
            GetRelHumFromHumRatio(
                temp,
                w,
                101325,
            )
            * 100
        )

        results.append(AirState(temp, rh))

    return results