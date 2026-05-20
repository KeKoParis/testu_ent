import yaml
import pathlib
import subprocess

def get_name(path: str):
    s = path.rfind("/")
    s1 = path.rfind("/", 0, s)
    path = path.replace("/","_")
    return path[s1+1:]


CONF = {}

with open("tests.yaml", "r") as f:
    CONF = yaml.safe_load(f)


keys = CONF.keys()

for i in keys:
    for path in CONF[i]:
        path_u = path[:1].lower() + path[2:]
        p = pathlib.WindowsPath(path_u)
        res = "".join([el for el in p.as_posix() if el.isalpha()])
        run_ent = f"wsl -d Ubuntu-24.04 --exec bash -c \"ent -b /mnt/{p.as_posix()}\" > ./results/ent/{get_name(p.as_posix())}.result.txt"
        run_test_u = f"docker run --rm -i testu01_gw -s < {path} > ./results/testu/{get_name(p.as_posix())}.result.txt"

        print(run_ent)
        print(run_test_u)

        subprocess.Popen(run_ent, shell=True)
        subprocess.Popen(run_test_u, shell=True)