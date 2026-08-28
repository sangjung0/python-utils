from __future__ import annotations

from typing import Any, cast
from collections.abc import Mapping

def validate_mapping(value: Any, error_message: str | None = None) -> Mapping[Any, Any]:
    if not isinstance(value, Mapping):
        raise ValueError("Invalid map" + (f": {error_message}" if error_message else ""))
    return cast(Mapping[Any, Any], value)

def validate_str(value: Any, error_message: str | None = None) -> str:
    if not isinstance(value, str):
        raise ValueError("Invalid string" + (f": {error_message}" if error_message else ""))
    return value

def validate_int(value: Any, error_message: str | None = None) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError("Invalid integer" + (f": {error_message}" if error_message else ""))
    return value

def validate_float(value: Any, error_message: str | None = None) -> float:
    if not isinstance(value, int | float) or isinstance(value, bool):
        raise ValueError("Invalid float" + (f": {error_message}" if error_message else ""))
    return float(value)

def validate_bool(value: Any, error_message: str | None = None) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Invalid boolean" + (f": {error_message}" if error_message else ""))
    return value


__all__ = ["validate_mapping", "validate_str", "validate_int", "validate_float", "validate_bool"]
