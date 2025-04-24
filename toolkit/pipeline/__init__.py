class PipelineBlock:
    def __init__(self, func):
        self.func = func
        self.next = None

    def __or__(self, other):
        if not isinstance(other, PipelineBlock):
            raise TypeError("You can only chain with another PipelineBlock")
        self.next = other
        return self

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        if self.next:
            # Nếu kết quả là tuple, unpack làm args
            if isinstance(result, tuple):
                return self.next(*result)
            else:
                return self.next(result)
        return result


def create_pipeline(block: PipelineBlock):
    def pipeline(*args, **kwargs):
        return block(*args, **kwargs)
    return pipeline

# Định nghĩa các block xử lý
# @PipelineBlock
# def step1(text, num):
#     return text.strip(), num

# @PipelineBlock
# def step2(text, num):
#     return text.lower(), num

# @PipelineBlock
# def step3(text, num):
#     for _ in range(num):
#         print(text.replace(" ", "_"))

# # Kết nối bằng toán tử |
# pipeline = create_pipeline(step1 | step2 | step3)

# # Chạy thử
# pipeline("  Xin Chào GPT  ", 2)