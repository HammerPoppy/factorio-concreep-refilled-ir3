#! env python3

import json
import os
import os.path
import shutil
import subprocess

os.chdir(os.path.dirname(__file__))

name = "concreep-refilled-ir3"

f = open(f"{name}/info.json")
text = f.read()
data = json.loads(text)
version = data["version"]

os.makedirs("build", exist_ok=True)

outfile = f"build/{name}_{version}.zip"

subprocess.run(["nanazipc", "a", outfile, f"{name}"])

# reading where (factorio mods folder probably) to put archive from settings.json 
f_settings = open(f".vscode/settings.json")
text_settings = f_settings.read()
data_settings = json.loads(text_settings)

shutil.copy2(outfile, data_settings["factorio_mods_dir"][0])
