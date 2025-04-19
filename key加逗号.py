import sys
import pyperclip # 导入 pyperclip 库
import time      # 导入 time 库，可以用于添加短暂延时（有时需要）

def transform_string_split(input_str):
    """
    将形如 sk-100sk-101sk-102 的字符串转换为 sk-100,sk-101,sk-102
    使用 split 和 join 方法。
    如果输入无效，返回 None。
    """
    if not input_str or not isinstance(input_str, str) or not input_str.startswith('sk'):
        # 增加检查，确保是字符串且以 'sk' 开头
        return None
    try:
        parts = input_str.split('sk')
        # 检查分割后是否有内容，避免只有 'sk' 的情况导致 parts[1:] 出错或结果为空
        if len(parts) > 1 and any(parts[1:]):
            processed_parts = ['sk' + part for part in parts[1:]]
            output_str = ','.join(processed_parts)
            return output_str
        elif len(parts) == 2 and parts[1] == '': # 处理输入只有 "sk" 的情况
             return input_str # 或者返回 None，根据需求
        else:
             return None # 其他无效分割情况
    except Exception as e:
        print(f"处理字符串时出错: {e}")
        return None

# --- 主程序 ---
if __name__ == "__main__":
    input_string = None
    output_string = None

    print("正在尝试从剪贴板读取内容...")
    try:
        # 短暂等待，确保剪贴板内容已就绪（有时复制操作需要一点时间）
        # time.sleep(0.1) # 通常不需要，但如果遇到问题可以取消注释试试

        clipboard_content = pyperclip.paste()

        if clipboard_content and isinstance(clipboard_content, str):
            # 打印读取到的内容（为了调试和确认）
            # 如果内容太长，可以只打印一部分
            print(f"从剪贴板读取到内容 (前100字符): {clipboard_content[:100]}{'...' if len(clipboard_content)>100 else ''}")
            input_string = clipboard_content # 使用剪贴板内容作为输入
        else:
            print("剪贴板为空或内容不是文本字符串。")

    except pyperclip.PyperclipException as e:
        print(f"错误：无法访问系统剪贴板。{e}")
        print("请确保 'pyperclip' 库安装正确且环境支持剪贴板操作。")
    except Exception as e: # 捕获其他可能的意外错误
        print(f"读取剪贴板时发生未知错误: {e}")

    # --- 如果成功从剪贴板获取了输入，则进行处理 ---
    if input_string:
        print("\n正在处理读取到的字符串...")
        output_string = transform_string_split(input_string)

        if output_string:
            print("\n处理后的字符串:", output_string)

            # --- 将处理结果复制回剪贴板 ---
            try:
                pyperclip.copy(output_string)
                print(">>> 处理结果已自动复制回剪贴板。 <<<")
            except pyperclip.PyperclipException as e:
                print(f"错误：无法将结果复制到剪贴板。{e}")
            except Exception as e:
                 print(f"复制结果到剪贴板时发生未知错误: {e}")
        else:
            print("从剪贴板读取的内容处理后无有效输出（可能格式不完全符合 sk-...).")
    else:
        # 如果没有从剪贴板获取到有效输入
        print("\n未能从剪贴板获取有效输入，脚本结束。")

