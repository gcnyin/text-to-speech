import asyncio
from src.main import get_voices

async def test_voices_sorting():
    """测试语音列表排序"""
    voices = await get_voices()
    
    # 打印排序结果
    print("\n=== 语音列表排序测试 ===")
    print("总计语音数量:", len(voices))
    print("\n按 Locale 排序的结果:")
    
    current_locale_prefix = None
    for voice in voices:
        # 获取语言前缀（如 zh-CN 的 zh）
        locale_prefix = voice.locale.split('-')[0]
        
        # 如果是新的语言组，打印分隔线
        if locale_prefix != current_locale_prefix:
            print(f"\n--- {locale_prefix} ---")
            current_locale_prefix = locale_prefix
        
        print(f"Locale: {voice.locale:<8} | Name: {voice.name:<30} | Display: {voice.display_name}")
    
    # 验证排序是否正确
    locales = [voice.locale for voice in voices]
    sorted_locales = sorted(locales)
    
    is_sorted = locales == sorted_locales
    print("\n=== 测试结果 ===")
    print(f"列表是否正确排序: {'✅ 是' if is_sorted else '❌ 否'}")
    
    if not is_sorted:
        print("\n!!! 排序错误 !!!")
        print("第一个不匹配的位置:")
        for i, (current, expected) in enumerate(zip(locales, sorted_locales)):
            if current != expected:
                print(f"位置 {i}:")
                print(f"当前值: {current}")
                print(f"期望值: {expected}")
                break

if __name__ == "__main__":
    asyncio.run(test_voices_sorting())