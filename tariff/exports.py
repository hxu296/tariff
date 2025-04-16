import builtins
import inspect
import random
import sys
import time
from functools import wraps
from typing import Union

# cached lookup table on modules with tariff
_tariff_lookup = {}


_pooh_phrases = [
    "YY将坚决反制。",
    "XX挑起YX贸易战，符合不了任何一方的利益。",
    "保护主义没有出路，贸易战和关税战没有赢家。",
    "单方面加征关税严重违反世界贸易组织规则。",
    "现在是XX停止错误做法的时候，通过平等协商解决与贸易伙伴的分歧。",
]
_original_sleep = time.sleep


def _test_for_tariff(module_name: str):
    global _tariff_lookup

    if module_name in _tariff_lookup:
        return _tariff_lookup[module_name]

    # check if sleep is called when importing a module
    # but do not actually impose the tariff
    def _trace_sleep_once(seconds: float):
        global _tariff_lookup

        _tariff_lookup[module_name] = True

    # trap stdout while testing
    sys.stdout = None
    time.sleep = _trace_sleep_once
    builtins.__import__(module_name)
    time.sleep = _original_sleep
    sys.stdout = sys.__stdout__

    if _tariff_lookup[module_name]:
        print(f"[{module_name}]: A tariff has been imposed on our module!")
    return _tariff_lookup[module_name]


def set_tariff(tariff_rates: Union[float, dict], retaliatory_only: bool = False):
    """
    Decorator to set an export tariff on a function - i.e. this function will be slower.

    `tariff_rates` can be a flat number or a variable rate based on user (caller package name).

    If `retaliatory_only` flag is set, tariff is imposed only when user of the function
    is unfriendly, and imposed a tariff on your package.

    Args:
        tariff_rates (float | dict):
            tariff rate to apply in percent. Either a flat value, or a dict[caller -> rate in percent].
        retaliatory_only (bool):
            set to only impose tariff when there is a tariff on function's parent module.
        export_only (bool):
            set to impose tariff when exporting 
    """
    module_name = inspect.stack()[1].frame.f_globals["__name__"].split(".")[0]
    impose_tariff = _test_for_tariff(module_name) if retaliatory_only else True

    def _trace_sleep_once(seconds: float):
        global _tariff_lookup

        _tariff_lookup[module_name] = True
        _original_sleep(seconds)
        time.sleep = _original_sleep

    time.sleep = _trace_sleep_once

    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            global _tariff_lookup

            start_time = time.time()
            output = func(*args, **kwargs)
            timetaken = time.time() - start_time
            caller = inspect.stack()[1].frame.f_globals["__name__"]
            if isinstance(tariff_rates, dict):
                tariff_rate = tariff_rates.get(caller, None)
            elif isinstance(tariff_rates, (int, float)):
                tariff_rate = tariff_rates
            else:
                raise TypeError(
                    "`tariff_rates` for {func.__name__} should be a number or dict: package_name -> rate in percent"
                )

            if impose_tariff and tariff_rate is not None:
                sleep_time = timetaken * (tariff_rate / 100.0)
                time.sleep(sleep_time)

                extras = (
                    f" because `{caller}` imposed a TARIFF on `{module_name}`"
                    if retaliatory_only
                    else ""
                )
                print(
                    f"[{module_name}] JUST IMPOSED a {tariff_rate}% TARIFF on `{func.__name__}`{extras}! "
                    f"Original response took {round(timetaken, 2)} sec, "
                    f"now takes {round(timetaken + sleep_time, 2)} sec. "
                    f"{_get_pooh_phrase() if _tariff_lookup.get(module_name) else ''}",
                )
            return output

        return decorated

    return decorator


def _get_pooh_phrase():
    return random.choice(_pooh_phrases)
