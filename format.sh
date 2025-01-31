#!/bin/bash
echo "Formatting Python files..."
black src/
isort src/
echo "Done!"
