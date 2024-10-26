from blocks.interface_block import IBlock
from blocks.utils import BlockLogType


class BaseBlock():
    """Provide base implementation for blocks."""

    def log(log_message: str, type: BlockLogType):
        log_message_prefix = ''

        match type:
            case BlockLogType.WARNING:
                log_message_prefix = '\033[91mWARNING:\033[0m '

            case BlockLogType.INFO:
                log_message_prefix = '\033[93mINFO: [0m'

        log_message = f"{log_message_prefix}{log_message}"

        print(log_message)
