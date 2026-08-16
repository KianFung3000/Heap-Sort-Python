class DSAHeapEntry:
    def __init__(self, priority: int, value: object):
        self.priority = priority
        self.value = value

    def get_priority(self) -> int:
        return self.priority

    def set_priority(self, priority: int) -> None:
        self.priority = priority

    def get_value(self) -> object:
        return self.value

    def set_value(self, value: object) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"Insert: {self.value} (Priority: {self.priority})"