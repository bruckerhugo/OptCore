# OptCore

An independent Python library for combinatorial optimization. Domain models,
constraints, and solvers have not been implemented yet.

## Development environment

Requirements: uv, VS Code, and Python 3.13 (uv can provision
Python if needed). The package uses a `src/` layout and the uv build backend.
`uv sync` installs the package in editable mode and the development dependency
group into `.venv`. Commit `uv.lock`; use `uv sync --locked` to reproduce it.
No global Python package installation is required.

## Work entirely in VS Code

1. Open the repository root with **File > Open Folder**.
2. Open Extensions (`Cmd+Shift+X`), search `@recommended`, and install the workspace
   recommendations: Python, Pylance, Python Debugger, Ruff, and Codex.
3. Select **Terminal > Run Task > OptCore: Sync environment**. Tasks run inside
   VS Code; no external terminal or manually activated environment is needed.
   If `uv` is not found, restart VS Code after installing uv so it inherits PATH.
4. Open the Command Palette (`Cmd+Shift+P`), run **Python: Select Interpreter**,
   and select `.venv/bin/python`. If an interpreter was previously selected,
   select this one explicitly: the default setting does not override that choice.
5. Open a Python file. Saving (`Cmd+S`) formats with Ruff, applies safe fixes,
   and organizes imports. Pylance uses strict type checking; inspect diagnostics
   in **View > Problems**. The CLI Ruff checks do not run Pylance type analysis.
6. Open the Testing view (flask icon), refresh discovery if needed, and use the
   run or debug buttons beside a test. Tests are discovered from `tests/`.
7. Set a breakpoint by clicking the editor gutter. In **Run and Debug**, select
   **Python: Current File**, then press F5 (Fn+F5 on some keyboards).
   **Python: Debug Tests** supplies settings to the Testing view's debug actions;
   start test debugging from that view rather than F5.
8. Run project checks through **Terminal > Run Task**: **Run tests**, **Lint**,
   **Check formatting**, or **Build package**. **Format** edits formatting.
9. Choose **Serve documentation** to preview MkDocs. Open the local address shown
   in the integrated terminal. Stop the server with `Ctrl+C` in that terminal.
   **Build documentation** performs a strict build.

The recommended extensions are declared, not installed automatically.
The Python Debugger extension supplies debugpy; the library does not depend on it.

## Commands

Use these in VS Code's integrated terminal if preferred:

```sh
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv build
uv run mkdocs build --strict
```

Generated benchmark output belongs in `benchmarks/results/`; keep benchmark
scripts and reproducible input data elsewhere under `benchmarks/`.
