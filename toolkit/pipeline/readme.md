```python
from toolkit.pipeline import PipelineBlock, create_pipeline

# Định nghĩa các block xử lý
@PipelineBlock
def step1(text, num):
    return text.strip(), num

@PipelineBlock
def step2(text, num):
    return text.lower(), num

@PipelineBlock
def step3(text, num):
    for _ in range(num):
        print(text.replace(" ", "_"))

# Kết nối bằng toán tử |
pipeline = create_pipeline(step1 | step2 | step3)

# Chạy thử
pipeline("  Xin Chào GPT  ", 2)

>>> Xin_Chào_GPT
>>> Xin_Chào_GPT
```
