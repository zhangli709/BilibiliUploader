

class Retry:
    def __init__(self, max_retry, success_return_value):
        self.max_retry = max_retry
        self.success_return_value = success_return_value

    def run(self, func, *args, **kwargs):
        status = False
        for i in range(0, self.max_retry):
            return_value = func(*args, **kwargs)
            if return_value == self.success_return_value:
                status = True
                break
        return status


def add_attr(obj):
    obj.added_attr = "new attr"

if __name__ == '__main__':
    a = Retry(1, 2)
    add_attr(a)
    print(a.added_attr)



