# receipts 🧾

[![Validate skills](https://github.com/effectustasi/agent-receipts/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/effectustasi/agent-receipts/actions/workflows/validate-skills.yml)
[![Latest release](https://img.shields.io/github/v/release/effectustasi/agent-receipts)](https://github.com/effectustasi/agent-receipts/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757)](#instalación)
[![GitHub stars](https://img.shields.io/github/stars/effectustasi/agent-receipts?style=social)](https://github.com/effectustasi/agent-receipts/stargazers)

[English](README.md) · **Español**

**Tu agente de programación dice "Listo ✅". Pero nunca ejecutó el código.**

`receipts` es un conjunto de skills para agentes que obligan a Claude Code, Codex, Cursor y compañía a **mostrar pruebas** antes de afirmar nada.

## Antes / después

**Sin receipts**

> He actualizado el parser de fechas para que admita el formato de semanas ISO. Esto debería funcionar. Listo ✅

**Con receipts**

> Listo. Recibo:
> ```
> $ pytest tests/test_dates.py
> 7 passed in 0.38s
> ```

o, cuando no puede comprobarlo:

> He cambiado `parse_date` para que acepte semanas ISO. **Sin verificar**: aquí no hay ningún test runner configurado.
> Para comprobarlo: `python -c "from app.dates import parse_date; print(parse_date('2026-W40'))"`

## Las skills

| Skill | Evita que tu agente                                                                |
|---|------------------------------------------------------------------------------------|
| [`prove-it`](skills/prove-it/SKILL.md) | Di "listo", "arreglado" o "todos los tests pasan" sin haber ejecutado nada         |
| [`no-guessing`](skills/no-guessing/SKILL.md) | Se invente nombres de funciones, flags de CLI y claves de configuración de memoria |
| [`repro-first`](skills/repro-first/SKILL.md) | "Arregle" bugs que nunca vio fallar                                                |

## Instalación

**Claude Code**

```
/plugin marketplace add effectustasi/agent-receipts
/plugin install receipts@receipts
```

### Codex CLI

Codex CLI lee `AGENTS.md` antes de empezar a trabajar. Desde la raíz de tu proyecto, añade los skills de receipts a ese archivo:

```bash
for skill in prove-it no-guessing repro-first; do
  curl -fsSL "https://raw.githubusercontent.com/effectustasi/agent-receipts/main/skills/$skill/SKILL.md" >> AGENTS.md
done
```

Para aplicar los skills a todos tus proyectos, añádelas a `~/.codex/AGENTS.md`. Inicia una nueva ejecución de Codex después de modificar el archivo y pídele que resuma las instrucciones activas:

```bash
codex --ask-for-approval never "Summarize the current instructions."
```

Consulta la [documentación oficial de instrucciones de Codex](https://developers.openai.com/codex/agent-configuration/agents-md) para conocer el orden de descubrimiento, el alcance global frente al de proyecto y cómo sobrescribirlas.

**Cualquier otro agente** (Cursor, Copilot, Gemini CLI, OpenCode…)

Copia las carpetas de las skills en el directorio de skills de tu agente, o pega el contenido de cada `SKILL.md` en tu `AGENTS.md` o en tu archivo de reglas.
Las guías por agente son bienvenidas: elige tu agente entre los issues de [`agent-support`](https://github.com/effectustasi/agent-receipts/labels/agent-support).

## Benchmark

Las mismas tareas, ejecutadas con y sin `receipts`, midiendo con qué frecuencia el agente afirma un éxito que no es real. Cada ejecución la comprueba un script, no el agente.

Resultados hasta ahora (Claude Code, 300 ejecuciones): Sonnet 5.5 no hizo afirmaciones falsas en ninguna configuración. Haiku 4.5 las hizo en 13 de 30 ejecuciones sin receipts, y receipts todavía no reduce ese total. Sí cambia su comportamiento: cuando un cambio rompe un test existente, Haiku ahora se detiene y pregunta en lugar de editar el test (0 de 10 falsos éxitos en esa tarea). Sigue parcheando una dependencia fijada (pinned) en todas las ocasiones.
Tablas completas, transcripciones y cómo ejecutarlo: [benchmark/](benchmark/README.md). Las nuevas tareas son bienvenidas, consulta la etiqueta [`benchmark`](https://github.com/effectustasi/agent-receipts/labels/benchmark).

## Contribuir

Se agradecen nuevas skills, traducciones, guías de instalación para otros agentes y tareas de benchmark. Empieza por [CONTRIBUTING.md](CONTRIBUTING.md) y la etiqueta [`good first issue`](https://github.com/effectustasi/agent-receipts/labels/good%20first%20issue).

## Licencia

MIT

## Más herramientas de effectustasi

- [blender-dlss5-neural-rendering](https://github.com/effectustasi/blender-dlss5-neural-rendering): viewport y renders de Blender mediante el renderizado neuronal de DLSS 5
- [metahuman-face-capture](https://github.com/effectustasi/metahuman-face-capture): captura facial de MetaHuman desde una webcam en Blender
- [autodesk-inventor-mcp](https://github.com/effectustasi/autodesk-inventor-mcp): conecta agentes de IA a una sesión activa de Autodesk Inventor
- [unreal-groom-alembic-exporter](https://github.com/effectustasi/unreal-groom-alembic-exporter): exporta assets Groom de UE (pelo de MetaHuman) a Alembic
