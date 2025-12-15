# Installation Guide

## Prerequisites

- Python 3.9+
- FFmpeg
- Git
- curl or wget (for downloading models)

### GPU Acceleration (Recommended)

GPU acceleration significantly speeds up processing:

- **NVIDIA GPU (Linux/Windows)**: CUDA 11.0+ with compatible drivers
- **Apple Silicon Mac (M1/M2/M3)**: MPS (Metal Performance Shaders) - automatically detected, no additional setup required
- **Intel Mac**: CPU-only processing (no GPU acceleration)

> **Note**: GPU acceleration is optional but strongly recommended. CPU processing works but is 10-20x slower.

## Quick Setup (Recommended)

Clone the repository and run the setup script:

```bash
git clone https://github.com/tok/depth-surge-3d.git depth-surge-3d
cd depth-surge-3d
chmod +x setup.sh
./setup.sh
```

The setup script will automatically:
- Install uv package manager (if not present, falls back to pip)
- Create a virtual environment
- Install all Python dependencies
- Download Video-Depth-Anything repository
- Download Video-Depth-Anything-Large model (~1.3GB)
- Verify system requirements

## Model Management

The project includes flexible model management:

```bash
# Download specific models
./download_models.sh large          # Large model (best quality)
./download_models.sh small          # Small model (fastest)
./download_models.sh small base     # Multiple models
./download_models.sh all            # All models

# Check model status
./download_models.sh                # Shows current status

# Models are automatically downloaded if missing
python depth_surge_3d.py input.mp4  # Auto-downloads if needed
```

**Available Models:**
- **Small** (24.8M params) - Fast processing, lower quality
- **Base** (97.5M params) - Balanced performance and quality
- **Large** (335.3M params) - Best quality (default)

## Manual Installation

If you prefer manual setup or if the automatic setup fails:

### Step 1: System Dependencies

**FFmpeg** (required for video processing):
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# macOS (with Homebrew)
brew install ffmpeg

# Windows (with Chocolatey)
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

**Python 3.9+** and **Git**:
```bash
# Ubuntu/Debian
sudo apt install python3 python3-venv git

# macOS (with Homebrew)
brew install python3 git

# Windows: Download from python.org and git-scm.com
```

### Step 2: Python Environment

```bash
# Clone the repository
git clone https://github.com/tok/depth-surge-3d.git depth-surge-3d
cd depth-surge-3d

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### Step 3: Download Video-Depth-Anything

**Option A: Automatic download (recommended)**
```bash
./download_models.sh large
```

**Option B: Manual download**
```bash
# Clone the repository
git clone https://github.com/DepthAnything/Video-Depth-Anything.git video_depth_anything_repo

# Create models directory
mkdir -p models/Video-Depth-Anything-Large

# Download the model (choose one):
# Large model (1.3GB) - best quality
wget https://huggingface.co/depth-anything/Video-Depth-Anything-Large/resolve/main/video_depth_anything_vitl.pth \
     -O models/Video-Depth-Anything-Large/video_depth_anything_vitl.pth

# OR Base model (390MB) - balanced
mkdir -p models/Video-Depth-Anything-Base
wget https://huggingface.co/depth-anything/Video-Depth-Anything-Base/resolve/main/video_depth_anything_vitb.pth \
     -O models/Video-Depth-Anything-Base/video_depth_anything_vitb.pth

# OR Small model (98MB) - fastest
mkdir -p models/Video-Depth-Anything-Small
wget https://huggingface.co/depth-anything/Video-Depth-Anything-Small/resolve/main/video_depth_anything_vits.pth \
     -O models/Video-Depth-Anything-Small/video_depth_anything_vits.pth
```

### Step 4: Verify Installation

```bash
# Test the installation
python depth_surge_3d.py --help

# Check model availability
python depth_surge_3d.py --model-info

# List supported resolutions
python depth_surge_3d.py --list-resolutions
```

**Troubleshooting Manual Setup:**
- If `wget` is not available, use `curl -L -o <output> <url>` instead
- On Windows, use PowerShell or download files manually from the URLs
- Ensure all dependencies are in your PATH before running

## macOS-Specific Notes

### Apple Silicon (M1/M2/M3)

Apple Silicon Macs use Metal Performance Shaders (MPS) for GPU acceleration. This is automatically detected when you use `--device auto` (the default).

```bash
# Verify MPS is available
python -c "import torch; print('MPS available:', torch.backends.mps.is_available())"

# Force MPS device explicitly
python depth_surge_3d.py video.mp4 --device mps
```

**Performance Tips for Apple Silicon:**
- MPS acceleration provides significant speedup over CPU (typically 3-5x faster)
- The Base model (`vitb`) is recommended for Macs with 16GB unified memory
- Use `--vr-resolution 16x9-1080p` for faster processing on lower-end Macs
- Close other memory-intensive applications during processing

### Intel Mac

Intel Macs do not have MPS support. Processing will use CPU only:

```bash
python depth_surge_3d.py video.mp4 --device cpu
```

**Note**: CPU processing is significantly slower. Consider using shorter video clips or lower resolutions.

## Testing Your Installation

Run `./test.sh` to verify your installation:
- ✓ Python dependencies
- ✓ GPU availability (CUDA or MPS)
- ✓ Model files
- ✓ Input video
- ✓ FFmpeg
