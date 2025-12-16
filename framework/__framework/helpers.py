from typing import Any, Callable
import inspect


def generate_function(
    name: str = "dynamically_generated_function",
    parameters: list[inspect.Parameter] | None = None,
    body_lines: list[str] | None = None,
    namespace: dict[str, Any] | None = None,
) -> Callable[..., Any]:
    
    parameters = parameters or []
    body_lines = body_lines or ["pass"]
    namespace = dict(namespace or {})

    signature = inspect.Signature(parameters)
    indented_body = "    " + "\n    ".join(body_lines)
    source = f"def {name}{signature}:\n{indented_body}"
    
    exec(source, namespace)
    func = namespace[name]
    func.__signature__ = signature
    return func
