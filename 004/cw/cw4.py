def func(text: str) -> None:
    sort_text = text.split()
    max_len_world = len(max(sort_text, key=len))
    print(max_len_world)


func('Здороваа. Как дела? ))')
