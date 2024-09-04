# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['dice_odds.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['scipy.special._ufuncs', 'scipy.special._ufuncs_cxx', 'scipy.special._cdflib'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='dice_odds',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
