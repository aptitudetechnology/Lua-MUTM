# Molecular Universal Turing Machine MVP

A prototype implementation of a molecular computing system using Universal Turing Machine principles, built with `pylua_bioxen_vm_lib` and employing a social role personification model for molecular workers.

## Architecture Overview

### Social Role Personification Model

- **Librarian**: Tape/Memory management using Lua tables
- **Inspector**: Head/Reader-Writer operations using Lua closures
- **Foreman**: State Machine/Transition rules using Lua closures
- **Shift Supervisor**: Coroutine scheduler for parallel molecular reactions
- **Diplomatic Corps**: FFI integration with C/C++ libraries

### Key Features

- Chemical Reaction Network (CRN) parsing and execution
- Benchmarking for NP-complete problems (TSP, 3-SAT)
- Synchronous and asynchronous execution modes
- Comprehensive testing with LuaUnit integration
- Debug logging and performance monitoring

## Quick Start

```bash
# Setup environment
pip install -r requirements.txt
luarocks install luasocket

# Run basic example
python examples/basic_turing/simple_utm.py

# Run benchmarks
python benchmarks/run_benchmarks.py
```

## Project Structure

```
molecular_utm_mvp/
├── src/molecular_workers/     # Core molecular worker implementations
├── src/crn_engine/           # Chemical Reaction Network engine
├── benchmarks/               # Performance benchmarks
├── tests/                   # Test suites
├── examples/               # Usage examples
└── docs/                  # Documentation
```

## Development

See [DEVELOPMENT.md](docs/DEVELOPMENT.md) for detailed development guidelines.
