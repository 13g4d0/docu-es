# Hooks de Git locales (este repositorio)

`commit-msg` elimina una línea accidental `Made-with: Cursor` del mensaje de commit antes de finalizar el commit, para que no entre en el historial público.

## Configuración única (por clone)

Desde la raíz del repositorio:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/commit-msg
```

## Emergencia: desactivar todos los hooks (raro)

```bash
git -c core.hooksPath=/dev/null commit ...
```
