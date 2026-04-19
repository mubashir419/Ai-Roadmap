from pathlib import Path

def count_lines(file_path):
	path =Path(file_path)
	if not path.exists():
		return 0
	return len(path.read_text().splitlines())
