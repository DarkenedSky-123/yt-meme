import subprocess

def run_command(command):
    """Run a shell command and check for errors."""
    result = subprocess.run(command, shell=True, check=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        raise Exception(f"Command failed with exit code {result.returncode}")

def install_dependencies():
    """Install necessary dependencies for building FFmpeg."""
    dependencies = [
        "build-essential",
        "yasm",
        "nasm",
        "libx264-dev",
        "libx265-dev",
        "libnuma-dev",
        "libvpx-dev",
        "libfdk-aac-dev",
        "libmp3lame-dev",
        "libopus-dev",
        "libass-dev",
        "libfreetype6-dev",
        "libvorbis-dev",
        "libxvidcore-dev"
    ]
    run_command(f"sudo apt update && sudo apt install -y {' '.join(dependencies)}")

def clone_ffmpeg_repo():
    """Clone the FFmpeg repository from GitHub."""
    run_command("git clone https://github.com/FFmpeg/FFmpeg.git")

def build_ffmpeg():
    """Configure, build, and install FFmpeg."""
    configure_command = (
        "./configure --enable-gpl --enable-nonfree --enable-libx264 "
        "--enable-libx265 --enable-libvpx --enable-libfdk-aac --enable-libmp3lame "
        "--enable-libopus --enable-libass --enable-libfreetype --enable-libvorbis --enable-libxvid"
    )
    run_command(configure_command)
    run_command(f"make -j$(nproc)")
    run_command("sudo make install")

def main():
    try:
        install_dependencies()
        clone_ffmpeg_repo()
        run_command("cd FFmpeg")
        build_ffmpeg()
        print("FFmpeg installation completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
