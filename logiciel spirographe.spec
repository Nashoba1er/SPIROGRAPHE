# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['logiciel spirographe.py'],
    pathex=[],
    binaries=[],
    datas=[('ressources/github.png', 'ressources'), ('ressources/sphere.png', 'ressources'), ('ressources/project_tech__spirographe-4.pdf', 'ressources')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='logiciel spirographe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
