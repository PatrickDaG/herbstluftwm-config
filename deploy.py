#run with fora

from fora.operations import system, git
from fora.host import current_host as host

system.package(["herbstluftwm"])

# clone complete repository to .config
# Once fora supports home directories subject to change
home_directory = host.run(["sh", "-c", "echo", "$HOME"]).stdout
if home_directory == "\\":
    raise ValueError("Home on root not allowed")


git.repo(url = "https://github.com/PatrickDaG/herbstluftwm-config.git",
        path = f"{home_directory}/.config/herbstluftwm",
        depth = 1)
