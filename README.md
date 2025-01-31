# 文本转语音应用程序

## 项目描述
这是一个使用 Python 构建的文本转语音应用程序。它提供了一个简单的 Web 界面，用户可以输入文本并生成相应的语音输出。

### 主要框架和库
- **FastAPI**: 用于构建 Web API 的现代、快速（高性能）的 Web 框架。
- **aiohttp**: 异步 HTTP 客户端/服务器库。
- **Jinja2**: 一个流行的模板引擎，用于生成 HTML。
- **uvicorn**: 一个 ASGI 服务器，用于运行 FastAPI 应用程序。
- **edge-tts**: 用于将文本转换为语音的库。
- **pydantic**: 数据验证和设置管理库。
- **click**: 用于创建命令行界面的库。
- **python-multipart**: 处理多部分表单数据的库。

## 安装
1. 克隆仓库:
   ```bash
   git clone git@github.com:gcnyin/text-to-speech.git
   cd text-to-speech
   ```
2. 创建虚拟环境并安装依赖项:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   # 安装开发环境依赖项
   pip install -r requirements-dev.txt
   ```

## 运行
启动应用程序:
```bash
./run.sh
```
然后在浏览器中访问 `http://localhost:8000` 查看应用。

## 代码格式化
为了确保代码风格一致，可以使用以下命令格式化 Python 代码：
```bash
./format.sh
```
该脚本会使用 `black` 和 `isort` 工具来格式化 `src/` 和 `tests/` 目录下的所有 Python 文件。

## 项目结构
- `src/`: 主要的 Python 代码
- `static/`: 静态资源（CSS 和 JavaScript）
- `templates/`: HTML 模板
- `tests/`: 测试代码
- `pyproject.toml`: 项目配置
- `requirements.txt`: 依赖项列表

## 许可证
本项目采用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。
