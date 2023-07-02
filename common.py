def write_file(data: dict, filename: str):
    """Запись данных в файл."""
    with open(filename, 'w') as f:
        for k, v in data.items():
            f.write(f"{k}: {v}\n")