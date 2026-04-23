# TdR — resumen ejecutivo (M3.1)

Síntesis a partir del extracto del PDF (`incoming/tdr.pdf` → `scripts/extract_tdr_pdf.py`) y el encabezado del tablero. **No** sustituye la revisión legal del documento oficial.

## Identidad del programa (extracto)

| Campo | Valor (del documento) |
|-------|-------------------------|
| Programa | MAP–BID — *Programa de Mejora a la Eficiencia del Servicio Civil de la República Dominicana* |
| Referencia | DR-L1142 (contexto de préstamo / programa en el texto del TdR) |
| Componente | Componente 2 — optimización de infraestructura y soluciones tecnológicas MAP |
| Asunto | **TdR** — *Plataforma IA Jurídica Institucional* |
| Modalidad contractual | **BOT** (Build–Operate–Transfer) |
| Fechas del documento | Marzo / abril de 2026 (las portadas pueden variar) |

## Objetivos (alto nivel)

1. **Base de conocimiento** — Poner a disposición conocimiento jurídico institucional (leyes, reglamentos, manuales, etc.) para el marco de empleo público; periodo inicial citado en el TdR (p. ej. primeros **3 meses** para ciertos hitos).
2. **Asistente con agentes** — Agente experto que investiga, redacta y revisa borradores (trabajo tipo resolución) en una ventana inicial similar.
3. **Cuota de uso** — Al menos **5.000** consultas RAG conversacionales **al mes** durante **18 meses** (12+6) según el extracto.
4. **Operar y mantener** — Ejecutar la plataforma inteligente **18 meses** tras el *go-live*.
5. **Plan de salida** — Plan detallado para que MAP migre a otro proveedor sin pérdida de información ni *vendor lock-in* (plazo ligado al mes **21** en el extracto).

## Contexto de contratación (tablero)

El tablero de brechas (`dashboard.html`) indica (verificar contra vuestra copia oficial):

- **Expediente:** DR-L1142-P00100 · SBC  
- **Sobre:** **USD 200.000** · **24 meses** · modalidad BOT  
- **Umbral pre–prueba técnica:** **63 / 90** puntos (70 %) en experiencia + metodología + personal  
- **Fecha límite EOI (codificada en tablero):** 28 de abril de 2026  

Si algún campo difiere en el pliego final, actualiza **tanto** las constantes del tablero como este resumen.

## Palabras clave de alcance (extracto)

- Plataforma de **IA jurídica** alojada en la nube con **UI web** y **asistente conversacional** usando **RAG**.  
- **Agentes digitales** para flujos investigar → redactar → auditar.  
- Énfasis en **sistematización normativa** del derecho del empleo público.  
- Secciones posteriores del TdR (ver extracto) cubren **DPA**, **versionado de modelos**, **prueba técnica**, **usuarios**, **entregables** y **equipo mínimo**.

## Próximos pasos

1. Regenerar `docs/tor-gap/_extracted/tdr-extract.txt` cuando cambie el PDF.  
2. Rellenar [Cuaderno de análisis de brechas](gap-analysis-workbook.md).  
3. Mantener evidencias de puntuación en la UI del tablero o exportar Markdown/CSV desde sus botones.

## Relacionado

- [Criterios desde el tablero](criteria-from-dashboard.md)  
- [Índice TdR y brechas](index.md)
