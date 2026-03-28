from time import sleep

from tqdm import tqdm


def core_fun() -> None:
    for i in tqdm(range(5), desc="core_fun"):
        sleep(0.25)
