# AGENTS.md - Airtest Automation Project Guidelines

## Project Overview

This is an **Airtest** Android automation testing project for testing the "中原安全" (Zhongyuan Security) Android application. Airtest is a cross-platform UI automation framework for Android, iOS, and Windows.

## Project Structure

```
zhongyuan/
├── hq/                      # Test case: hq (probably "行情" - market data)
│   ├── hq.py               # Main test script
│   ├── function.py         # Helper functions
│   └── *.png               # Template images for image recognition
└── untitled.air/           # Default test case directory
    ├── untitled.py         # Main test script
    └── *.png               # Template images
```

## Build & Test Commands

### Running Airtest Scripts

**Using Airtest IDE (GUI):**
- Open `hq/hq.py` or `untitled.air/untitled.py` in Airtest IDE
- Click "Run" button or press F5

**Using Command Line:**
```bash
# Run a single .py script
airtest run "D:\Airtest\zhongyuan\hq\hq.py"

# Run with device specified
airtest run "D:\Airtest\zhongyuan\hq\hq.py" --device Android:///

# Generate HTML report after run
airtest report "D:\Airtest\zhongyuan\hq\hq.py" --logroot log/
```

**Using pytest (if pytest-airtest is installed):**
```bash
# Run all test cases
pytest

# Run specific test file
pytest hq/hq.py

# Run with verbose output
pytest -v hq/hq.py

# Run specific test function
pytest hq/function.py::test_function_name -v
```

### Key CLI Options
- `--device`: Specify target device (e.g., `Android:///`, `Android:///serialno`)
- `--logdir`: Specify log directory path
- `--recording`: Record device screen during test execution
- `-s`: Show print output (stdout/stderr)

## Code Style Guidelines

### File Headers
```python
# -*- encoding=utf8 -*-
__author__ = "Your Name"
```

### Imports (Order)
1. Python standard library (`import time`, `import os`)
2. Airtest core modules (`from airtest.core.api import *`)
3. Airtest CLI/parser (`from airtest.cli.parser import cli_setup`)
4. Poco framework (`from poco.drivers.android.uiautomation import AndroidUiautomationPoco`)
5. Third-party libraries

### Naming Conventions
- **Files**: snake_case (e.g., `hq.py`, `function.py`, `untitled.py`)
- **Functions**: snake_case (e.g., `check_refresh()`, `login()`)
- **Variables**: snake_case (e.g., `price_old`, `poco`)
- **Constants**: UPPER_SNAKE_CASE
- **Classes**: PascalCase (rarely used in Airtest scripts)

### Airtest-Specific Patterns

**Setup:**
```python
# For standalone scripts
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///",])

# Or simply
auto_setup(__file__)
```

**Poco Initialization:**
```python
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
```

**Template Usage:**
```python
# Always use raw string (r"...")
touch(Template(r"tpl1772729181893.png", record_pos=(-0.195, 0.979), resolution=(1080, 2376)))
```

**Poco Element Access:**
```python
# Use resourceId for reliable element selection
poco("com.hexin.plat.android.ZhongyuanSecurity:id/backButton").click()

# Or chain descendant access
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("...")
```

### Error Handling
- Use `exists()` before `touch()` for elements that may not always appear
- Add `sleep()` or `wait()` for timing issues
- Wrap complex operations in try-except when needed

### Prohibited Patterns
- **Never** use hardcoded sleep (`time.sleep()`) excessively - prefer Airtest's `wait()` or `sleep()` with small values
- **Never** use `as any` or type suppression
- **Avoid** absolute x/y coordinates - use Templates and Poco selectors
- **Avoid** hardcoding device serial numbers in shared scripts

## Testing Best Practices

### Template Images
- Keep template images in the same directory as the test script
- Use descriptive filenames if possible
- Template resolution should match target device (e.g., 1080x2376)

### Device Configuration
- Use `Android:///` for automatic device detection
- Specify serial number only when targeting specific device: `Android:///serialno`

### Logging
- Use `print()` for debugging (visible in Airtest IDE console)
- Use `log()` for test step logging in reports

### Report Generation
```python
from airtest.report.report import simple_report
simple_report(__file__, logpath=True)
```

## Additional Notes

- This project uses **Airtest** framework (not pytest-based unit tests)
- Target app: `com.hexin.plat.android.ZhongyuanSecurity`
- Device resolution: 1080x2376
- Scripts are designed to run on Android devices/emulators
