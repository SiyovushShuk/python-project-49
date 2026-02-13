FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# Настраиваем переменные окружения
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    # Добавляем путь к бинарникам виртуального окружения в PATH
    PATH="/app/.venv/bin:$PATH"

# 1. Устанавливаем зависимости (слой будет кэшироваться)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# 2. Копируем исходный код
COPY . .

# 3. Устанавливаем сам проект. 
# Это автоматически создаст команды brain-games, brain-even и т.д.
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# По умолчанию запускаем одну из игр
CMD ["brain-games"]

