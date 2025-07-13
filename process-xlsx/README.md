# XLSX to Parquet Bulk Converter

## Overview

A simple, efficient tool to convert multiple XLSX files to Parquet format using DuckDB. This script ingests all sheets from all input files without additional transformation.

## Features

- Bulk convert XLSX files to Parquet
- Process entire directories of Excel files
- Preserve original sheet and file structure
- Low memory footprint
- Fast conversion using DuckDB

## Prerequisites

- Python 3.8+
- uv (Python package manager)

## Installation

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Usage

```bash
uv run convert.py /path/to/input/xlsx/files /path/to/output/parquet/directory
```

## How It Works

1. Scans input directory for XLSX files
2. Converts all sheets from each file to Parquet
3. Preserves original sheet names in output files
4. Generates one Parquet file per sheet
