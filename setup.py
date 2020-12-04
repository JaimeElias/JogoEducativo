import cx_Freeze

executables = [cx_Freeze.Executable(script="jogo.py")]

cx_Freeze.setup(
    name="Fuga da professora",
    options={"build_exe": {"packages":["pygame"],
            "include_files":["assets"]}},
    executables = executables   
    )
