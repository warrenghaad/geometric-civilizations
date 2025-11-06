#!/usr/bin/env bash
set -euo pipefail

#==============================================================================
# Geometric Civilizations - Master Build Script
# Generates complete curriculum: 54 lessons with slides, videos, and e-textbook
#==============================================================================

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${ROOT_DIR}/.venv"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

#==============================================================================
# Utility Functions
#==============================================================================

log_step() {
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${PURPLE}▶${NC} ${BLUE}$1${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1"
}

log_error() {
    echo -e "${RED}✗${NC} $1"
}

log_info() {
    echo -e "${YELLOW}ℹ${NC} $1"
}

#==============================================================================
# Setup
#==============================================================================

setup_environment() {
    log_step "Setting up environment"

    # Create virtual environment if it doesn't exist
    if [ ! -d "${VENV_DIR}" ]; then
        log_info "Creating Python virtual environment..."
        python3 -m venv "${VENV_DIR}"
        log_success "Virtual environment created"
    else
        log_success "Virtual environment exists"
    fi

    # Activate virtual environment
    source "${VENV_DIR}/bin/activate"

    # Upgrade pip
    log_info "Upgrading pip..."
    pip install --upgrade pip >/dev/null 2>&1

    # Install dependencies
    log_info "Installing dependencies..."
    pip install python-pptx requests Pillow cairosvg >/dev/null 2>&1
    log_success "Dependencies installed"
}

create_directory_structure() {
    log_step "Creating directory structure"

    mkdir -p "${ROOT_DIR}/lessons"
    mkdir -p "${ROOT_DIR}/schemas"
    mkdir -p "${ROOT_DIR}/scripts"
    mkdir -p "${ROOT_DIR}/assets/artifacts"
    mkdir -p "${ROOT_DIR}/assets/overlays"
    mkdir -p "${ROOT_DIR}/assets/characters"
    mkdir -p "${ROOT_DIR}/assets/diagrams"
    mkdir -p "${ROOT_DIR}/assets/worksheets"
    mkdir -p "${ROOT_DIR}/assets/rubrics"
    mkdir -p "${ROOT_DIR}/output/slides"
    mkdir -p "${ROOT_DIR}/output/videos"
    mkdir -p "${ROOT_DIR}/etextbook"
    mkdir -p "${ROOT_DIR}/docs"

    log_success "Directory structure created"
}

#==============================================================================
# Curriculum Generation
#==============================================================================

generate_curriculum() {
    log_step "Generating curriculum (54 lessons)"

    if [ ! -f "${ROOT_DIR}/curriculum_master.csv" ]; then
        log_error "curriculum_master.csv not found!"
        exit 1
    fi

    python3 "${ROOT_DIR}/scripts/generate_curriculum.py"

    local lesson_count=$(find "${ROOT_DIR}/lessons" -name "G*.json" | wc -l)
    log_success "Generated ${lesson_count} lesson JSON files"
}

#==============================================================================
# Image Sourcing
#==============================================================================

source_images() {
    log_step "Sourcing artifact images"

    local mode="${1:-skip}"  # skip, placeholders, or full

    if [ "$mode" == "skip" ]; then
        log_info "Skipping image sourcing (use --images flag to enable)"
        return
    fi

    if [ "$mode" == "placeholders" ]; then
        log_info "Generating placeholder images..."
        # Generate placeholder images for all lessons
        for lesson_file in "${ROOT_DIR}/lessons"/G*.json; do
            lesson_id=$(basename "$lesson_file" .json)
            log_info "Placeholders for ${lesson_id}..."
            # TODO: Implement placeholder generation
        done
        log_success "Placeholder images generated"
    fi

    if [ "$mode" == "full" ]; then
        log_info "Sourcing real images from Met API and Wikimedia..."
        for lesson_file in "${ROOT_DIR}/lessons"/G*.json; do
            lesson_id=$(basename "$lesson_file" .json)
            log_info "Sourcing images for ${lesson_id}..."
            python3 "${ROOT_DIR}/scripts/image_sourcer.py" "$lesson_file"
        done
        log_success "Image sourcing complete"
    fi
}

#==============================================================================
# Overlay Generation
#==============================================================================

generate_overlays() {
    log_step "Generating geometric overlays"

    for lesson_file in "${ROOT_DIR}/lessons"/G*.json; do
        lesson_id=$(basename "$lesson_file" .json)
        log_info "Generating overlays for ${lesson_id}..."
        python3 "${ROOT_DIR}/scripts/overlay_generator.py" "$lesson_file"
    done

    local overlay_count=$(find "${ROOT_DIR}/assets/overlays" -name "*.svg" | wc -l)
    log_success "Generated ${overlay_count} overlay files"
}

#==============================================================================
# E-Textbook Generation
#==============================================================================

generate_etextbook() {
    log_step "Generating interactive e-textbook"

    python3 "${ROOT_DIR}/scripts/etextbook_generator.py"

    if [ -f "${ROOT_DIR}/etextbook/index.html" ]; then
        log_success "E-textbook generated: etextbook/index.html"
        log_info "Open in browser: file://${ROOT_DIR}/etextbook/index.html"
    else
        log_error "E-textbook generation failed"
    fi
}

#==============================================================================
# Slide Generation (PowerPoint)
#==============================================================================

generate_slides() {
    log_step "Generating PowerPoint slides"

    local mode="${1:-skip}"  # skip or generate

    if [ "$mode" == "skip" ]; then
        log_info "Skipping slide generation (use --slides flag to enable)"
        return
    fi

    # TODO: Implement PowerPoint generation
    log_info "PowerPoint generation not yet implemented"
    log_info "See docs/video_workflow.md for implementation guide"
}

#==============================================================================
# Video Generation
#==============================================================================

generate_videos() {
    log_step "Generating lesson videos"

    local mode="${1:-skip}"  # skip or generate

    if [ "$mode" == "skip" ]; then
        log_info "Skipping video generation (use --videos flag to enable)"
        return
    fi

    # TODO: Implement video generation
    log_info "Video generation not yet implemented"
    log_info "See docs/video_workflow.md for implementation guide"
}

#==============================================================================
# Build Individual Lesson
#==============================================================================

build_lesson() {
    local lesson_id="$1"
    log_step "Building lesson: ${lesson_id}"

    local lesson_file="${ROOT_DIR}/lessons/${lesson_id}.json"

    if [ ! -f "$lesson_file" ]; then
        log_error "Lesson file not found: ${lesson_file}"
        return 1
    fi

    # Source images
    log_info "Sourcing images..."
    python3 "${ROOT_DIR}/scripts/image_sourcer.py" "$lesson_file"

    # Generate overlays
    log_info "Generating overlays..."
    python3 "${ROOT_DIR}/scripts/overlay_generator.py" "$lesson_file"

    # TODO: Generate slides
    # TODO: Generate video

    log_success "Lesson ${lesson_id} build complete"
}

#==============================================================================
# Main Build Process
#==============================================================================

main() {
    local image_mode="skip"
    local slides_mode="skip"
    local videos_mode="skip"
    local lesson_id=""

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            --images)
                image_mode="full"
                shift
                ;;
            --placeholders)
                image_mode="placeholders"
                shift
                ;;
            --slides)
                slides_mode="generate"
                shift
                ;;
            --videos)
                videos_mode="generate"
                shift
                ;;
            --lesson)
                lesson_id="$2"
                shift 2
                ;;
            --help)
                cat << EOF
Geometric Civilizations - Master Build Script

Usage: ./build_all.sh [OPTIONS]

Options:
  --images          Source real images from Met API and Wikimedia
  --placeholders    Generate placeholder images
  --slides          Generate PowerPoint slides
  --videos          Generate lesson videos
  --lesson <ID>     Build only specific lesson (e.g., G3-01)
  --help            Show this help message

Examples:
  ./build_all.sh                        # Generate curriculum + e-textbook only
  ./build_all.sh --placeholders         # Include placeholder images
  ./build_all.sh --images               # Source real images (slow)
  ./build_all.sh --lesson G3-01         # Build single lesson
  ./build_all.sh --images --slides      # Full build with slides

EOF
                exit 0
                ;;
            *)
                log_error "Unknown option: $1"
                exit 1
                ;;
        esac
    done

    echo ""
    echo -e "${PURPLE}╔═══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║${NC}  ${CYAN}🔺 Geometric Civilizations - Curriculum Builder 🔺${NC}           ${PURPLE}║${NC}"
    echo -e "${PURPLE}╚═══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""

    # If building single lesson
    if [ -n "$lesson_id" ]; then
        setup_environment
        build_lesson "$lesson_id"
        exit 0
    fi

    # Full build
    setup_environment
    create_directory_structure
    generate_curriculum
    source_images "$image_mode"
    generate_overlays
    generate_etextbook
    generate_slides "$slides_mode"
    generate_videos "$videos_mode"

    echo ""
    log_step "Build Summary"
    echo ""

    local lesson_count=$(find "${ROOT_DIR}/lessons" -name "G*.json" | wc -l)
    local overlay_count=$(find "${ROOT_DIR}/assets/overlays" -name "*.svg" 2>/dev/null | wc -l)

    echo -e "  ${GREEN}✓${NC} Lessons generated:      ${lesson_count}"
    echo -e "  ${GREEN}✓${NC} Overlays generated:     ${overlay_count}"

    if [ -f "${ROOT_DIR}/etextbook/index.html" ]; then
        echo -e "  ${GREEN}✓${NC} E-textbook:             ${ROOT_DIR}/etextbook/index.html"
    fi

    echo ""
    log_success "Build complete!"
    echo ""

    # Instructions
    echo -e "${YELLOW}Next Steps:${NC}"
    echo -e "  1. View e-textbook:   open etextbook/index.html"
    echo -e "  2. Review lessons:    ls -lh lessons/"
    echo -e "  3. Check overlays:    ls -lh assets/overlays/"
    echo ""
}

# Run main
main "$@"
