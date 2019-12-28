from eth_utils import (
    is_binary_address,
    is_checksum_address,
)


def is_valid_address(value):
    return is_binary_address(value) or is_checksum_address(value)
