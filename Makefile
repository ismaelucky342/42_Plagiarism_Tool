# Variables
PYTHON := python3
PROJECTS_DIR := ./projects
COMPARISON_REPOS_DIR := ./comparison_repos
OUTPUT_DIR := ./output
SRC_DIR := ./src
SCRIPT := plagiarism_checker.py
SH_SCRIPT := scripts/run_checker.sh
REQ_FILE := requirements.txt

# Default target (alias for help)
all: help


# Help target
help:
	@echo "Available targets:"
	@echo "  make install        Install Python dependencies"
	@echo "  make run            Run the plagiarism checker"
	@echo "  make clean          Clean output files (heatmaps, etc.)"
	@echo "  make reset          Clean output and comparison repos"
	@echo "  make help           Show this help message"

# Install Python dependencies
install:
	@echo "Installing Python dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r $(REQ_FILE)

# Run the plagiarism checker script (using the shell script)
run:
	@echo "Running the plagiarism checker..."
	bash $(SH_SCRIPT)

# Clean output files (heatmaps, etc.)
clean:
	@echo "Cleaning output directory..."
	rm -f $(OUTPUT_DIR)/*

# Clean output and reset repos
reset: clean
	@echo "Cleaning comparison repositories and resetting..."
	rm -rf $(COMPARISON_REPOS_DIR)/*
	@echo "Comparison repos cleaned."

