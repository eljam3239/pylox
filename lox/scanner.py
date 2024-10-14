from .token import *
from .tokentype import *


class Scanner:
    source = ""
    tokens = []

    def __init__(self, source):
        self.source = source
        self.tokens = []

    def scan_tokens(self):
        while