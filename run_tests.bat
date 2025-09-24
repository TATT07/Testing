@echo off
echo Installing required packages (if missing)...
python -m pip install --user pytest coverage

echo Running pytest...
python -m pytest

echo Running coverage...
python -m coverage run -m pytest
python -m coverage html

echo Copying coverage report to coverage.html...
if exist htmlcov\index.html copy htmlcov\index.html coverage.html

echo Done. coverage.html generated.
pause
