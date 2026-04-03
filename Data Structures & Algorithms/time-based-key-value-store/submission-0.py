class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        tuple_ = (timestamp, value)
        if key in self.map:
            self.map[key].append(tuple_)
        else:
            self.map[key] = []
            self.map[key].append(tuple_)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        search_space = self.map[key]
        low = 0
        high = len(search_space) - 1
        result = ""
        while low <= high:
            mid = (low + high) // 2
            if search_space[mid][0] <= timestamp:
                result = search_space[mid][1]
                low = mid + 1
            else:
                high = mid - 1

        return result




