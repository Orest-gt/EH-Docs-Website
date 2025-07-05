function toggleAudio() {
    if (document.getElementById('back-audio').paused) {
        document.getElementById('back-audio').play();
    } else {
        document.getElementById('back-audio').pause();
    }
}