# main.py

import argparse
from task_processor import process_task

def main():
    parser = argparse.ArgumentParser(description="使用 GLM-4V-Flash 执行多模态图像理解任务")
    parser.add_argument("image", type=str, help="输入图像路径（如：photo.jpg）")
    parser.add_argument("prompt", type=str, nargs="?", default="", help="用户提示（对于 visual-question 必填）")
    parser.add_argument("type", type=str, choices=[
        "image-class",
        "visual-question",
        "count-target",
        "caption",
        "caption-detailed",
        "region-caption"
    ], help="任务类型")

    args = parser.parse_args()

    try:
        result = process_task(args.image, args.prompt.strip(), args.type)
        print(result)
    except Exception as e:
        print(f"❌ 调用失败: {e}")

if __name__ == "__main__":
    main()