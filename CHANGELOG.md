# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.1.0] - 2025-03-22

### Added
- Full ETL pipeline for teams
...

## [Unreleased]
## [0.3.0] - 2025-03-22

### Added
- _Describe new features here_

### Changed
- _Describe changes here_

### Fixed
- _Describe fixes here_


### Added
- Full ETL pipeline for teams (extract, transform, load)
- Modular Python architecture with `etl/` submodules
- Logging system with timestamped `.log` files
- Execution summary and success messages in terminal
- Interactive CLI via `make menu`
- Makefile commands: `setup`, `run`, `teams`, `test`, `clean`, `freeze`
- Environment test script for DB connection and API key
- `.env` support with `python-dotenv`

### Changed
- Refactored imports to support `python -m` execution
- Improved console output for better traceability

### Removed
- All print/debug lines in French
