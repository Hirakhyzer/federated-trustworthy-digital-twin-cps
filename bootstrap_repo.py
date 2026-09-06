import base64
import json
import pathlib
import shutil
import subprocess
import zlib

EXPECTED_PARTS = 7
EXPECTED_PAYLOAD_LENGTH = 26620


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def main() -> None:
    root = pathlib.Path('.').resolve()
    part_dir = root / '.bootstrap_payload'
    parts = sorted(part_dir.glob('part_*.txt'))
    if len(parts) != EXPECTED_PARTS:
        raise RuntimeError(f'Expected {EXPECTED_PARTS} payload parts, found {len(parts)}')

    payload = ''.join(part.read_text(encoding='utf-8').strip() for part in parts)
    if len(payload) != EXPECTED_PAYLOAD_LENGTH:
        raise RuntimeError(
            f'Expected payload length {EXPECTED_PAYLOAD_LENGTH}, found {len(payload)}'
        )

    compressed = base64.b64decode(payload, validate=True)
    files = json.loads(zlib.decompress(compressed).decode('utf-8'))

    for rel_path, content in files.items():
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')

    shutil.rmtree(part_dir)
    (root / 'bootstrap_repo.py').unlink(missing_ok=True)

    run('git', 'config', 'user.name', 'github-actions[bot]')
    run('git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
    run('git', 'add', '-A')

    status = subprocess.run(
        ['git', 'status', '--porcelain'],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if status:
        run('git', 'commit', '-m', 'Add federated trustworthy digital-twin CPS research framework')
        run('git', 'push', 'origin', 'HEAD:main')


if __name__ == '__main__':
    main()
