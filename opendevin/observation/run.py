from dataclasses import dataclass

from .base import Observation


@dataclass
class CmdOutputObservation(Observation):
    """
    This data class represents the output of a command.
    """

    command_id: int
    command: str
    exit_code: int = 0
    observation: str = "run"

    @property
    def error(self) -> bool:
        return self.exit_code != 0

    @property
    def message(self) -> str:
        if self.exit_code == 100:
            print("self.exit_code == 100")
        return f"Command `{self.command}` executed with exit code {self.exit_code}."
