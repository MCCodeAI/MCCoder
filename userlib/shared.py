class SharedData:
    def __init__(self):
        self._value = None
        self._callbacks = []

    def add_callback(self, callback):
        self._callbacks.append(callback)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self._value != new_value:  # 检查是否真的发生了改变
            old_value = self._value
            self._value = new_value
            for callback in self._callbacks:
                callback(old_value, new_value)  # 触发所有回调

shared_flow_state_str = SharedData()