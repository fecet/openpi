# Repository Guidelines

## Project Structure & Module Organization
- `src/openpi/` — core library: `models/`, `models_pytorch/`, `policies/`, `training/`, `serving/`, `shared/`. Tests live next to code as `*_test.py` (see `pyproject.toml:testpaths`).
- `scripts/` — entry points: `compute_norm_stats.py`, `train.py`, `train_pytorch.py`, `serve_policy.py` (+ `docker/`).
- `examples/` — runnable usage and conversion scripts.
- `packages/openpi-client/` — lightweight client (websocket + image utils).
- `docs/`, `third_party/`, `.github/workflows/` — docs, vendored code, CI.

## Build, Test, and Development Commands
- Environment: `GIT_LFS_SKIP_SMUDGE=1 uv sync --all-extras --dev && uv pip install -e .`
- Lint/format: `uv run ruff check . --fix && uv run ruff format .`
- Pre-commit: `uv run pre-commit install && uv run pre-commit run -a`
- Tests (default): `uv run pytest --strict-markers -m "not manual"`
- Example flow: `uv run scripts/compute_norm_stats.py --config-name pi05_libero` then `uv run scripts/train.py pi05_libero --exp-name=exp --overwrite`. Serve: `uv run scripts/serve_policy.py policy:checkpoint --policy.config=pi05_libero --policy.dir=<ckpt_dir>`.

## Coding Style & Naming Conventions
- Python 3.11. Style via Ruff (`line-length=120`, target `py311`); `ruff format` is the formatter; imports are single‑line sorted.
- Naming: files/modules `snake_case.py`; classes `PascalCase`; functions/variables `snake_case`; constants `UPPER_SNAKE`.
- Types: prefer explicit type hints and `dataclasses` for configs. Keep docstrings short and precise.
- Logging: use `logging` inside library code; `print` is acceptable in scripts/tests.

## Testing Guidelines
- Framework: `pytest`. Place tests alongside code as `*_test.py`; keep fast and deterministic (no external network).
- Mark long/integration tests with `@pytest.mark.manual`; CI runs `-m "not manual"`. Run only manual tests with `uv run pytest -m manual`.
- Useful example: `uv run pytest src/openpi/models/model_test.py::test_pi0_model -q`.

## Commit & Pull Request Guidelines
- Commits: imperative, concise subject lines; reference issues when relevant (e.g., `Pi05 + PyTorch support (#634)`, `Fix PyTorch assets save path`).
- PRs: clear description, linked issues, test plan (commands + output), and any perf numbers or screenshots/logs. Include environment/GPU details for training changes.
- Required: pre-commit passes, `ruff` clean, tests green (`pytest --strict-markers -m "not manual"`).

## Security & Configuration Tips
- Use `GIT_LFS_SKIP_SMUDGE=1` during `uv sync` to avoid large LFS pulls.
- If you apply the Transformers patches for PyTorch, note they modify the uv cache; revert with `uv cache clean transformers` if needed.

