from .http_error import HTTPError


def check_index(index: int, target_list: list) -> int:
    return (
        index
        if 0 <= index < len(target_list)
        else HTTPError.not_found(f"Post with id {index} not found")
    )


def check_list(target_list: list) -> dict:
    return (
        {"detail": f"{len(target_list)} Posts found", "posts": target_list}
        if len(target_list) > 0
        else {"detail": "No posts founded"}
    )
