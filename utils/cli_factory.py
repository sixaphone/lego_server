from utils.cli_provider import CLIProvider
from utils.invoke_cli import InvokeCLI
from utils.fabric_cli import FabricCLI


class CLIFactory:
    @staticmethod
    def create_cli(provider: CLIProvider, **kwargs):
        if provider == CLIProvider.INVOKE:
            return InvokeCLI()
        if provider == CLIProvider.FABRIC:
            return FabricCLI(kwargs.get("connection"), kwargs.get("watchers"))
