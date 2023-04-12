# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['__main__.py'],
    pathex=[],
    binaries=[],
    datas=[('images\\default-job-number.png', 'main\\images'), ('images\\empty-list.png', 'main\\images'), ('images\\win1.png', 'main\\images'), ('images\\win2.png', 'main\\images'), ('images\\win3.png', 'main\\images'), ('images\\win4.png', 'main\\images'), ('images\\win5.png', 'main\\images'), ('images\\win6.png', 'main\\images'), ('images\\pegasus-background.png', 'main\\images'), ('images\\no-windows.png', 'main\\images'), ('images\\view-change.png', 'main\\images'), ('data\\job_details.py', 'main/data')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Auto_Call_Off',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Auto_Call_Off',
)
