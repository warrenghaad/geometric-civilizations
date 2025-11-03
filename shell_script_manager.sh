#!/usr/bin/env bash
set -euo pipefail

# SHELL SCRIPT CROSS-REFERENCE AND EXECUTION SYSTEM
# =================================================
# This script manages all shell scripts and integrates with Python system

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="${SCRIPT_DIR}"
PYTHON_CROSS_REF="${ROOT_DIR}/script_cross_reference.py"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${BLUE}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

success() {
    echo -e "${GREEN}✅ $1${NC}"
}

warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

error() {
    echo -e "${RED}❌ $1${NC}"
}

# SHELL SCRIPT DEPENDENCIES MAP
declare -A SHELL_DEPENDENCIES=(
    # Main lesson setup scripts
    ["setup-G3-Lesson-A.sh"]=""
    ["setup-G3-Lesson-B.sh"]=""
    ["setup-G3-Lesson-C.sh"]=""
    ["setup-G3-Lesson-D.sh"]=""
    ["setup-G3-Lesson-E.sh"]=""
    ["setup-G3-Lesson-F.sh"]=""
    ["setup-G3-Lesson-G.sh"]=""
    ["setup-G3-Lesson-H.sh"]=""
    ["setup-G4-Lesson-A.sh"]=""
    ["setup-G4-Lesson-C.sh"]=""
    
    # Batch creation scripts
    ["create_all_grade4_lessons.sh"]="setup-G4-Lesson-A.sh setup-G4-Lesson-B.sh setup-G4-Lesson-D.sh setup-G4-Lesson-E.sh setup-G4-Lesson-F.sh setup-G4-Lesson-G.sh setup-G4-Lesson-H.sh"
    
    # Test and utility scripts
    ["test_script_structure.sh"]=""
)

# SHELL SCRIPT DESCRIPTIONS
declare -A SHELL_DESCRIPTIONS=(
    ["setup-G3-Lesson-A.sh"]="Creates Grade 3 Lesson A: Place Value & Rounding with 36 slides"
    ["setup-G3-Lesson-B.sh"]="Creates Grade 3 Lesson B: Addition & Subtraction"
    ["setup-G3-Lesson-C.sh"]="Creates Grade 3 Lesson C: Multiplication Basics"
    ["setup-G3-Lesson-D.sh"]="Creates Grade 3 Lesson D: Division Introduction"
    ["setup-G3-Lesson-E.sh"]="Creates Grade 3 Lesson E: Fractions Basics"
    ["setup-G3-Lesson-F.sh"]="Creates Grade 3 Lesson F: Measurement & Time"
    ["setup-G3-Lesson-G.sh"]="Creates Grade 3 Lesson G: Geometry Shapes"
    ["setup-G3-Lesson-H.sh"]="Creates Grade 3 Lesson H: Data & Graphs"
    ["setup-G4-Lesson-A.sh"]="Creates Grade 4 Lesson A: Advanced Place Value"
    ["setup-G4-Lesson-C.sh"]="Creates Grade 4 Lesson C: Multi-digit Operations"
    ["create_all_grade4_lessons.sh"]="Batch creates all Grade 4 lessons (A,B,D-H)"
    ["test_script_structure.sh"]="Tests directory structure and organization"
)

# EXECUTION PHASES FOR SHELL SCRIPTS
declare -a SHELL_EXECUTION_ORDER=(
    # Phase 1: Individual Grade 3 lessons
    "setup-G3-Lesson-A.sh"
    "setup-G3-Lesson-B.sh" 
    "setup-G3-Lesson-C.sh"
    "setup-G3-Lesson-D.sh"
    "setup-G3-Lesson-E.sh"
    "setup-G3-Lesson-F.sh"
    "setup-G3-Lesson-G.sh"
    "setup-G3-Lesson-H.sh"
    
    # Phase 2: Grade 4 batch creation
    "create_all_grade4_lessons.sh"
    
    # Phase 3: Structure validation
    "test_script_structure.sh"
)

# Function to check if script exists
script_exists() {
    local script_name="$1"
    [ -f "${ROOT_DIR}/${script_name}" ]
}

# Function to make script executable
make_executable() {
    local script_name="$1"
    if script_exists "$script_name"; then
        chmod +x "${ROOT_DIR}/${script_name}"
        return 0
    else
        return 1
    fi
}

# Function to run a specific shell script
run_shell_script() {
    local script_name="$1"
    local script_path="${ROOT_DIR}/${script_name}"
    
    if ! script_exists "$script_name"; then
        error "Script not found: $script_name"
        return 1
    fi
    
    log "Running shell script: $script_name"
    log "Description: ${SHELL_DESCRIPTIONS[$script_name]:-No description}"
    
    # Make executable
    if ! make_executable "$script_name"; then
        error "Could not make script executable: $script_name"
        return 1
    fi
    
    # Check dependencies
    local deps="${SHELL_DEPENDENCIES[$script_name]:-}"
    if [ -n "$deps" ]; then
        log "Dependencies: $deps"
        for dep in $deps; do
            if ! script_exists "$dep"; then
                error "Missing dependency: $dep"
                return 1
            fi
        done
    fi
    
    # Run the script
    cd "${ROOT_DIR}"
    if bash "$script_path"; then
        success "Completed: $script_name"
        return 0
    else
        error "Failed: $script_name"
        return 1
    fi
}

# Function to validate all shell scripts
validate_shell_scripts() {
    log "Validating all shell scripts..."
    
    local missing_scripts=()
    local total_scripts=0
    local found_scripts=0
    
    # Check main scripts
    for script_name in "${!SHELL_DEPENDENCIES[@]}"; do
        total_scripts=$((total_scripts + 1))
        if script_exists "$script_name"; then
            found_scripts=$((found_scripts + 1))
            success "Found: $script_name"
        else
            missing_scripts+=("$script_name")
            error "Missing: $script_name"
        fi
    done
    
    # Check dependencies
    for script_name in "${!SHELL_DEPENDENCIES[@]}"; do
        local deps="${SHELL_DEPENDENCIES[$script_name]}"
        if [ -n "$deps" ]; then
            for dep in $deps; do
                if ! script_exists "$dep"; then
                    missing_scripts+=("$dep")
                    error "Missing dependency: $dep (required by $script_name)"
                fi
            done
        fi
    done
    
    if [ ${#missing_scripts[@]} -eq 0 ]; then
        success "All shell scripts validated successfully ($found_scripts/$total_scripts found)"
        return 0
    else
        error "Missing ${#missing_scripts[@]} shell scripts: ${missing_scripts[*]}"
        return 1
    fi
}

# Function to run all shell scripts in order
run_all_shell_scripts() {
    log "Running all shell scripts in execution order..."
    
    local total=${#SHELL_EXECUTION_ORDER[@]}
    local completed=0
    
    for i in "${!SHELL_EXECUTION_ORDER[@]}"; do
        local script_name="${SHELL_EXECUTION_ORDER[$i]}"
        local step=$((i + 1))
        
        log "Step $step/$total: $script_name"
        
        if run_shell_script "$script_name"; then
            completed=$((completed + 1))
        else
            error "Pipeline failed at step $step: $script_name"
            return 1
        fi
    done
    
    success "All shell scripts completed successfully ($completed/$total)"
}

# Function to run complete system (Python + Shell)
run_complete_system() {
    log "Running COMPLETE SYSTEM: Shell scripts + Python pipeline"
    echo "=========================================================="
    
    # Step 1: Validate everything
    log "Phase 1: Validation"
    if ! validate_shell_scripts; then
        error "Shell script validation failed"
        return 1
    fi
    
    if [ -f "$PYTHON_CROSS_REF" ]; then
        if ! python3 "$PYTHON_CROSS_REF" validate; then
            error "Python script validation failed"
            return 1
        fi
    else
        warning "Python cross-reference not found: $PYTHON_CROSS_REF"
    fi
    
    # Step 2: Run shell scripts (creates lessons)
    log "Phase 2: Shell Script Execution"
    if ! run_all_shell_scripts; then
        error "Shell script execution failed"
        return 1
    fi
    
    # Step 3: Run Python pipeline (processes lessons)
    log "Phase 3: Python Pipeline Execution"
    if [ -f "$PYTHON_CROSS_REF" ]; then
        if ! python3 "$PYTHON_CROSS_REF" run-all; then
            error "Python pipeline failed"
            return 1
        fi
    else
        warning "Skipping Python pipeline - cross-reference not found"
    fi
    
    success "COMPLETE SYSTEM executed successfully!"
    log "All lessons created, images downloaded, presentations processed, and e-textbooks generated"
}

# Function to create missing shell scripts
create_missing_scripts() {
    log "Creating missing shell scripts..."
    
    # Create setup-G3-Lesson-B.sh if missing
    if ! script_exists "setup-G3-Lesson-B.sh"; then
        log "Creating setup-G3-Lesson-B.sh..."
        
        # Use G3-Lesson-A as template but change content
        sed 's/G3-Lesson-A/G3-Lesson-B/g; s/Place Value & Rounding/Addition & Subtraction/g' "${ROOT_DIR}/setup-G3-Lesson-A.sh" > "${ROOT_DIR}/setup-G3-Lesson-B.sh"
        make_executable "setup-G3-Lesson-B.sh"
        success "Created setup-G3-Lesson-B.sh"
    fi
    
    # Create other missing Grade 3 lessons
    local grade3_lessons=("C" "D" "E" "F" "G" "H")
    local grade3_topics=("Multiplication Basics" "Division Introduction" "Fractions Basics" "Measurement & Time" "Geometry Shapes" "Data & Graphs")
    
    for i in "${!grade3_lessons[@]}"; do
        local lesson_code="${grade3_lessons[$i]}"
        local topic="${grade3_topics[$i]}"
        local script_name="setup-G3-Lesson-${lesson_code}.sh"
        
        if ! script_exists "$script_name"; then
            log "Creating $script_name..."
            sed "s/G3-Lesson-A/G3-Lesson-${lesson_code}/g; s/Place Value & Rounding/${topic}/g" "${ROOT_DIR}/setup-G3-Lesson-A.sh" > "${ROOT_DIR}/${script_name}"
            make_executable "$script_name"
            success "Created $script_name"
        fi
    done
    
    # Create setup-G4-Lesson-A.sh if missing
    if ! script_exists "setup-G4-Lesson-A.sh"; then
        log "Creating setup-G4-Lesson-A.sh..."
        sed 's/G3-Lesson-A/G4-Lesson-A/g; s/Place Value & Rounding/Advanced Place Value/g; s/Grade3/Grade4/g' "${ROOT_DIR}/setup-G3-Lesson-A.sh" > "${ROOT_DIR}/setup-G4-Lesson-A.sh"
        make_executable "setup-G4-Lesson-A.sh"
        success "Created setup-G4-Lesson-A.sh"
    fi
}

# Function to show system status
show_system_status() {
    echo "GEOMETRIC CIVILIZATIONS AUTOMATION SYSTEM STATUS"
    echo "==============================================="
    
    # Shell script status
    echo ""
    echo "Shell Scripts:"
    local shell_found=0
    local shell_total=0
    for script_name in "${!SHELL_DEPENDENCIES[@]}"; do
        shell_total=$((shell_total + 1))
        if script_exists "$script_name"; then
            shell_found=$((shell_found + 1))
            echo "  ✅ $script_name"
        else
            echo "  ❌ $script_name"
        fi
    done
    echo "  Shell Scripts: $shell_found/$shell_total found"
    
    # Python script status
    echo ""
    echo "Python Integration:"
    if [ -f "$PYTHON_CROSS_REF" ]; then
        echo "  ✅ script_cross_reference.py"
        if python3 "$PYTHON_CROSS_REF" validate >/dev/null 2>&1; then
            echo "  ✅ Python scripts validated"
        else
            echo "  ❌ Python script validation failed"
        fi
    else
        echo "  ❌ script_cross_reference.py"
    fi
    
    # Environment status
    echo ""
    echo "Environment:"
    if command -v python3 >/dev/null 2>&1; then
        echo "  ✅ Python 3 available"
    else
        echo "  ❌ Python 3 missing"
    fi
    
    if [ -d "${ROOT_DIR}/.venv" ]; then
        echo "  ✅ Virtual environment exists"
    else
        echo "  ❌ Virtual environment missing"
    fi
    
    echo ""
}

# Main function
main() {
    case "${1:-status}" in
        "validate")
            validate_shell_scripts
            ;;
        "run-all")
            run_all_shell_scripts
            ;;
        "run")
            if [ $# -lt 2 ]; then
                error "Usage: $0 run <script_name>"
                exit 1
            fi
            run_shell_script "$2"
            ;;
        "create-missing")
            create_missing_scripts
            ;;
        "complete-system")
            run_complete_system
            ;;
        "status")
            show_system_status
            ;;
        *)
            echo "Shell Script Manager for Geometric Civilizations"
            echo ""
            echo "Usage:"
            echo "  $0 status           - Show system status"
            echo "  $0 validate         - Validate all shell scripts"
            echo "  $0 create-missing   - Create any missing scripts"
            echo "  $0 run-all          - Run all shell scripts in order"
            echo "  $0 run <script>     - Run specific shell script"
            echo "  $0 complete-system  - Run EVERYTHING (shell + python)"
            echo ""
            echo "Available Scripts:"
            for script_name in "${!SHELL_DESCRIPTIONS[@]}"; do
                printf "  %-25s - %s\n" "$script_name" "${SHELL_DESCRIPTIONS[$script_name]}"
            done
            ;;
    esac
}

# Run main function
main "$@"