# 文本转语音项目

## 项目概述
这是一个文本转语音（Text-to-Speech, TTS）项目，旨在将输入的文本转换为自然语音输出。该项目使用Python编写，并依赖于一些常见的Python库。

## 安装步骤
1. **克隆仓库**
   ```bash
   git clone https://github.com/yourusername/text-to-speech.git
   cd text-to-speech
   ```

2. **设置虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **格式化代码**
   ```bash
   ./format.sh
   ```

5. **运行项目**
   ```bash
   ./run.sh
   ```

## 使用说明
1. **启动服务器**
   ```bash
   ./run.sh
   ```

2. **访问应用**
   打开浏览器并访问 `http://localhost:8000`，你将看到文本转语音的应用界面。

3. **输入文本**
   在输入框中输入你想要转换为语音的文本，然后点击“转换”按钮。

4. **听语音**
   转换完成后，你可以听到生成的语音。

## 许可证
本项目采用 [MIT 许可证](LICENSE)。
