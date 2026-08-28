from __future__ import annotations

from typing import Any
from collections.abc import Mapping

from sjpy.validator import validate_float, validate_int, validate_mapping, validate_str, validate_bool

def require_value(value: Mapping[Any, Any], key: Any) -> Any:
    try:
        return value[key]
    except KeyError as exc:
        raise ValueError(f"Missing key: {key}") from exc

def require_mapping(value: Mapping[Any, Any], key: Any, error_message: str | None = None) -> Mapping[Any, Any]:
    return validate_mapping(require_value(value, key), error_message)

def get_mapping(value: Mapping[Any, Any], key: Any, error_message: str | None = None) -> Mapping[Any, Any] | None:
    val = require_value(value, key)
    if val is None:
        return None
    return validate_mapping(val, error_message)

def require_str(value: Mapping[Any, Any], key: Any, error_message: str | None = None) -> str:
    return validate_str(require_value(value, key), error_message)

def get_str(value: Mapping[Any, Any], key: Any, error_message: str | None = None) -> str | None:
    val = require_value(value, key)
    if val is None:
        return None
    return validate_str(val, error_message)

def require_int(value: Mapping[Any, Any], key: Any, error_message: str | None = None) -> int:
    return validate_int(require_value(value, key), error_message)

def get_int(value: Mapping[Any, Any], key: Any, error_message: str | None = None) -> int | None:
    val = require_value(value, key)
    if val is None:
        return None
    return validate_int(val, error_message)

def require_float(value: Mapping[Any, Any], key: Any, error_message: str | None = None) -> float:
    return validate_float(require_value(value, key), error_message)

def get_float(value: Mapping[Any, Any], key: Any, error_message: str | None = None) -> float | None:
    val = require_value(value, key)
    if val is None:
        return None
    return validate_float(val, error_message)

def get_bool(value: Mapping[Any, Any], key: Any, error_message: str | None = None) -> bool | None:
    val = require_value(value, key)
    if val is None:
        return None
    return validate_bool(val, error_message)

def require_bool(value: Mapping[Any, Any], key: Any, error_message: str | None = None) -> bool:
    val = require_value(value, key)
    return validate_bool(val, error_message)

__all__ = ["require_value", "require_mapping", "require_str", "require_int", "require_float", "require_bool", "get_str", "get_int", "get_float", "get_bool"]
