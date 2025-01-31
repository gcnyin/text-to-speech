// 初始化：加载语音模型
window.onload = async function () {
    try {
        const response = await fetch('/voices');
        if (!response.ok) {
            throw new Error('Failed to fetch voices');
        }

        const voices = await response.json();
        const voiceSelect = document.getElementById('voice');

        // 按 locale 排序
        voices.sort((a, b) => a.locale.localeCompare(b.locale));

        voices.forEach(voice => {
            const option = document.createElement('option');
            option.value = voice.name;
            option.textContent = voice.display_name;
            // 添加 data-locale 属性以便于调试
            option.setAttribute('data-locale', voice.locale);
            voiceSelect.appendChild(option);
        });

        // 默认选择中文语音
        const defaultVoice = voices.find(v => v.name.startsWith('zh-'));
        if (defaultVoice) {
            voiceSelect.value = defaultVoice.name;
        }
    } catch (error) {
        console.error('获取语音模型失败:', error);
        alert('获取语音模型失败');
    }
};

// 语音合成函数
async function synthesize(action) {
    const text = document.getElementById('text').value.trim();
    const voice = document.getElementById('voice').value;
    const loading = document.getElementById('loading');
    const previewBtn = document.getElementById('previewBtn');
    const downloadBtn = document.getElementById('downloadBtn');
    const audioPlayer = document.getElementById('audioPlayer');

    if (!text) {
        alert('请输入文本！');
        return;
    }

    // 禁用按钮并显示加载提示
    previewBtn.disabled = true;
    downloadBtn.disabled = true;
    loading.style.display = 'block';

    try {
        console.log(`开始生成语音: ${action}`, { text, voice });

        // 发送请求
        const response = await fetch(`/synthesize?text=${encodeURIComponent(text)}&voice=${encodeURIComponent(voice)}`, {
            method: 'GET'
        });

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`请求失败: ${response.status} ${errorText}`);
        }

        // 检查响应头
        console.log('响应头:', Object.fromEntries(response.headers.entries()));

        const blob = await response.blob();
        console.log('获取到的音频数据:', {
            size: blob.size,
            type: blob.type
        });

        if (blob.size === 0) {
            throw new Error('生成的音频为空');
        }

        // 创建新的音频 URL
        const audioUrl = URL.createObjectURL(blob);

        if (action === 'preview') {
            // 预览模式：播放音频
            audioPlayer.style.display = 'block';

            // 设置音频事件处理器
            audioPlayer.onerror = (e) => {
                console.error('音频错误:', e);
                alert(`音频加载失败: ${e.target.error.message}`);
            };

            audioPlayer.onloadedmetadata = () => {
                console.log('音频元数据已加载');
            };

            // 加载并播放音频
            audioPlayer.src = audioUrl;
            try {
                await audioPlayer.play();
                console.log('音频开始播放');
            } catch (playError) {
                console.error('播放失败:', playError);
                alert(`播放失败: ${playError.message}`);
            }
        } else {
            // 下载模式：触发下载
            const a = document.createElement('a');
            a.href = audioUrl;
            a.download = 'speech.mp3';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }

        // 清理 URL 对象
        setTimeout(() => {
            URL.revokeObjectURL(audioUrl);
        }, 100);

    } catch (error) {
        console.error('错误:', error);
        alert('生成语音失败: ' + error.message);
    } finally {
        // 恢复按钮状态并隐藏加载提示
        previewBtn.disabled = false;
        downloadBtn.disabled = false;
        loading.style.display = 'none';
    }
}