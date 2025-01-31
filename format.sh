#!/bin/bash
echo "Formatting Python files..."
black src/ tests/
isort src/ tests/
echo "Done!"
