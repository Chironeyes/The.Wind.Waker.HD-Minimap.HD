"""Create and verify the installation ZIP from the existing Cemu pack.

Uses only Python 3's standard library. This is a packaging tool, not an
assembler, SVG compiler, or replacement for the internal layout builder.
"""
import hashlib
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
PACK_NAME = 'WindWakerHD_MinimapHD'
PACK = ROOT / 'graphicPacks' / PACK_NAME


def digest(data):
    return hashlib.sha256(data).hexdigest()


def build():
    version_text = (PACK / 'VERSION.txt').read_text(encoding='utf-8')
    match = re.match(r'Minimap HD (\d+\.\d+\.\d+)\n', version_text)
    assert match, 'Invalid VERSION.txt'
    version = match.group(1)
    rules = (PACK / 'rules.txt').read_text(encoding='utf-8')
    assert f'name = Minimap HD {version} - EU v0' in rules
    assert re.search(r'^version = 6$', rules, re.M)
    assert re.search(r'^titleIds = 0005000010143600$', rules, re.M)
    patch = (PACK / 'patch_map.asm').read_bytes()
    assert b'moduleMatches = 0xB7E748DE' in patch
    assert b'_qa' not in patch, 'QA instrumentation must not be distributed'
    assert {p.name for p in PACK.iterdir()} == {'rules.txt', 'patch_map.asm', 'VERSION.txt'}

    entries = {
        f'{PACK_NAME}/rules.txt': (PACK / 'rules.txt').read_bytes(),
        f'{PACK_NAME}/patch_map.asm': patch,
        f'{PACK_NAME}/VERSION.txt': (PACK / 'VERSION.txt').read_bytes(),
        f'{PACK_NAME}/INSTALLATION.md': (ROOT / 'docs/installation.md').read_bytes(),
        f'{PACK_NAME}/CONFIGURATION.md': (ROOT / 'docs/configuration.md').read_bytes(),
        f'{PACK_NAME}/ASSET_PROVENANCE.md': (ROOT / 'docs/asset-provenance.md').read_bytes(),
        f'{PACK_NAME}/LICENSE': (ROOT / 'LICENSE').read_bytes(),
        f'{PACK_NAME}/NOTICE.md': (ROOT / 'NOTICE.md').read_bytes(),
        'CHANGELOG.md': (ROOT / 'CHANGELOG.md').read_bytes(),
    }
    manifest = ''.join(f'{digest(data)}  {name}\n' for name, data in sorted(entries.items()))
    entries['SHA256SUMS.txt'] = manifest.encode('utf-8')
    output = ROOT / 'dist'
    output.mkdir(exist_ok=True)
    target = output / f'{PACK_NAME}-{version}.zip'
    temporary = target.with_suffix('.zip.tmp')
    with ZipFile(temporary, 'w', ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(entries.items()):
            item = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            item.compress_type = ZIP_DEFLATED
            item.create_system = 3
            item.external_attr = 0o100644 << 16
            archive.writestr(item, data, compresslevel=9)
    with ZipFile(temporary) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(entries)
        assert len(archive.namelist()) == len(entries)
        for name, data in entries.items():
            assert archive.read(name) == data, name
        for line in archive.read('SHA256SUMS.txt').decode('utf-8').splitlines():
            checksum, name = line.split('  ', 1)
            assert digest(archive.read(name)) == checksum, name
    temporary.replace(target)
    checksum = digest(target.read_bytes())
    target.with_suffix('.zip.sha256').write_text(
        f'{checksum}  {target.name}\n', encoding='ascii', newline='\n')
    print(f'{target.name}: {target.stat().st_size} bytes; {len(entries)} entries')
    print(f'SHA-256: {checksum}')


if __name__ == '__main__':
    build()
