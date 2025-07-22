import math


def update_mean_std(
    old_mean: float,
    old_std: float,
    old_count: int,
    new_mean: float,
    new_std: float,
    new_count: int,
) -> tuple[float, float]:
    if old_count == 0:
        return new_mean, new_std
    if new_count == 0:
        return old_mean, old_std

    total_count = old_count + new_count
    updated_mean = (old_mean * old_count + new_mean * new_count) / total_count

    updated_std = math.sqrt(
        (
            old_count * (old_std**2 + (old_mean - updated_mean) ** 2)
            + new_count * (new_std**2 + (new_mean - updated_mean) ** 2)
        )
        / total_count
    )

    return updated_mean, updated_std


__all__ = [
    "update_mean_std",
]
