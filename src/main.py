import logging
from typing import List

import edge_tts
from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Text to Speech")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class Voice(BaseModel):
    name: str
    display_name: str
    locale: str  # 添加 locale 字段用于排序


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/voices")
async def get_voices() -> List[Voice]:
    """获取所有可用的语音模型，按照 Locale 排序"""
    voices = await edge_tts.list_voices()
    voice_list = [
        Voice(
            name=voice["ShortName"],
            display_name=f"{voice['FriendlyName']} - {voice['Locale']}",
            locale=voice["Locale"],
        )
        for voice in voices
    ]

    # 按照 Locale 排序
    voice_list.sort(key=lambda x: x.locale)
    return voice_list


@app.get("/synthesize")
async def synthesize_speech(
    text: str = Query(
        ...,  # 表示必需参数
        description="要转换的文本",
        min_length=1,
        max_length=1000,
    ),
    voice: str = Query(
        ...,
        description="语音模型名称",
        min_length=1,
    ),
):
    """生成语音"""
    try:
        logger.info(f"开始生成语音. 文本长度: {len(text)}, 语音模型: {voice}")

        communicate = edge_tts.Communicate(text, voice)

        # 收集音频数据
        audio_stream = []
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_stream.append(chunk["data"])

        # 检查是否有音频数据
        if not audio_stream:
            raise ValueError("生成的音频为空")

        # 计算总大小
        total_size = sum(len(chunk) for chunk in audio_stream)
        logger.info(f"生成的音频大小: {total_size} bytes")

        # 创建生成器函数来流式传输数据
        async def generate():
            for chunk in audio_stream:
                yield chunk

        # 返回音频流
        return StreamingResponse(
            generate(),
            media_type="audio/mp3",
            headers={
                "Content-Type": "audio/mp3",
                "Content-Length": str(total_size),
                "Accept-Ranges": "bytes",
                "Cache-Control": "no-cache",
                "Content-Disposition": 'attachment; filename="speech.mp3"',
            },
        )
    except Exception as e:
        logger.error(f"生成语音时发生错误: {str(e)}", exc_info=True)
        return {"error": str(e)}
